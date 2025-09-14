#-------------------------------
# Name:        drag_drop.py
# Author:      Tom
# Created:     07.09.2021
# Copyright:   (c) Snippsat 2021
# Python 3.11
#-------------------------------
import wx
from bs4 import BeautifulSoup
import requests
import re, sys, os
import subprocess
import threading
from unidecode import unidecode

VERSION = "2.7"

def nrk_super(url):
    '''Parse/API get content'''
    try:
        if 'nrksuper' in url:
            # Super
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            data_id = soup.select_one('#content > div.pending-reskin-container > div')
            media_id = data_id.get('data-episode-id')
        elif re.search(r'[A-Z]+\d+', url):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Kodi
            media_id = soup.find('meta', property="og:url")
            media_id = media_id.get('content').split('/')[-1]
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Avspiller
            media_id = soup.select_one('#series-program-id-container')
            media_id = media_id.get('data-program-id')
        #--| Stream url
        stream = requests.get(f'https://psapi.nrk.no/playback/manifest/program/{media_id}')
        stream_url = stream.json()
        stream_url = stream_url['playable']['assets'][0]['url']
        stream_url = stream_url.split('?')[0]
        print(stream_url)
        #--| Sub title
        sub_text = requests.get(f'https://psapi.nrk.no/playback/manifest/program/{media_id}')
        sub_text = sub_text.json()
        try:
            sub_text = sub_text['playable']['subtitles'][0]['webVtt']
        except IndexError:
            sub_text = 'No sub'

        #--| Program Title
        resp = requests.get(f'https://psapi.nrk.no/playback/metadata/program/{media_id}')
        resp_json = resp.json()
        if len(resp_json['preplay']['titles']['subtitle']) < 90:
            resp_json = resp_json['preplay']['titles']
            prog_title = f"{resp_json['title']} {' '.join(resp_json['subtitle'].split())}"
            prog_title = re.sub('[/\\\?%\*:|"<>]', '_', prog_title)
        else:
            resp_json = resp_json['preplay']['titles']
            prog_title = resp_json['title']
            prog_title = re.sub('[/\\\?%\*:|"<>]', '_', prog_title)
        return stream_url, prog_title, sub_text
    except Exception as error:
        return error

def radio(url, vid_quality):
    if 'l_' in url:
        media_id = url.split('/')[-1]
        base_url = f"https://psapi.nrk.no/playback/manifest/podcast/{media_id}"
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            mp3_url = data["playable"]["assets"][0]["url"]
            temp_name = data["statistics"]["ga"]["dimension2"]
            basename = re.sub('[/\\\?%\*:|"<>]', '_', temp_name)
            filename = basename + '.mp3'
            resp = requests.get(mp3_url)
            with open(filename, 'wb') as file:
                file.write(resp.content)
    else:
        media_id = url.split('/')[-1]
        base_url = f"https://psapi.nrk.no/playback/manifest/program/{media_id}"
        response = requests.get(base_url)
        data = response.json()
        #--- Get and fix
        dimension2 = data.get("statistics", {}).get("ga", {}).get("dimension2")
        url = data.get("playable", {}).get("assets", [])[0].get("url")
        stream_url = url.split('?')
        dimension2 = data["statistics"]["ga"]["dimension2"]
        base_name = re.sub('[/\\\?%\*:|"<>]', '_', dimension2)
        quality = {
                "low": "?bw_high=32",
                "high":"?bw_high=194",
            }

        # vid_quality = self.vid_choice
        url_adress = f'{stream_url[0]}{quality[vid_quality]}'
        file_name = f'{base_name}.mkv'
        file_name = unidecode(file_name)
        #---| Stream
        process = subprocess.Popen('cmd.exe /k ',\
            shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
        arg_command =  f'ffmpeg -y -i {url_adress} -c:a copy "{file_name}"\n'
        process.stdin.write(arg_command.encode())
        o, e = process.communicate()
        process.stdin.close()

def vtt_srt(sub_title, program_title):
    try:
        response = requests.get(sub_title)
        if response.status_code == 200:
            with open(f"{program_title}.srt", 'wb') as f:
                f.write(response.content)
    except requests.exceptions.MissingSchema:
        return False

def nrk(stream_url, program_title, vid_quality):
    """Parse data for nrk-tv website"""
    quality = {
        "low": "?bw_high=1000",
        "med": "?bw_high=2000",
        "high":"?bw_high=3500",
    }
    #--| Commands parameters
    url_adress = f'{stream_url}{quality[vid_quality]}'
    print(url_adress)
    #--| cmd commands
    if 'podkast.nrk' in url_adress:
        pass
    else:
        file_name = f'{program_title}.mkv'
        process = subprocess.Popen('cmd.exe /k ',\
            shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
        arg_command =  f'ffmpeg -y -i "{url_adress}" -vcodec copy -acodec ac3 "{file_name}"\n'
        process.stdin.write(arg_command.encode())
        o, e = process.communicate()
        process.stdin.close()


class MyURLDropTarget(wx.DropTarget):
    '''Drag and drop'''
    def __init__(self, window,radio_choice):
        wx.DropTarget.__init__(self)
        self.window = window
        self.vid_choice = radio_choice
        self.data = wx.URLDataObject();
        self.SetDataObject(self.data)

    def OnDragOver(self, x, y, d):
        return wx.DragLink

    def OnData(self, x, y, d):
        if not self.GetData():
            return wx.DragNone
        url = self.data.GetURL()
        # High med low
        vid_quality = self.vid_choice
        if 'radio.nrk' in url:
            thread = threading.Thread(target=radio, args=(url, vid_quality))
            thread.start()
            self.window.AppendText(url + "\n")
        else:
            nrk_info = nrk_super(url)
            try:
                stream_url = nrk_info[0]
            except(TypeError,AttributeError):
                # Wrong url not from nrk
                return False
            program_title = nrk_info[1]
            # Unidecode beacuse of cmd encoding
            program_title = unidecode(program_title)
            #--| Get nrk_super func info
            sub_title = nrk_info[2]
            vtt_srt(sub_title, program_title)
            nrk_run = threading.Thread(target=nrk, args=(stream_url, program_title, vid_quality,))
            nrk_run.start()
            self.window.AppendText(url + "\n")
        return d

class MyFrame(wx.Frame):
    '''Gui frontend'''
    def __init__(self, parent, mytitle, mysize):
        wx.Frame.__init__(self, parent, wx.ID_ANY, mytitle,\
        size=mysize,style=wx.DEFAULT_DIALOG_STYLE | wx.MINIMIZE_BOX)
        #--| Setup
        self.SetBackgroundColour('#bcb998')
        self.panel = wx.Panel(self)
        ico = wx.Icon('tv_green.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        #--| Picture
        wx.StaticBitmap(self.panel,-1,wx.Bitmap("nrk_pic.png",
              wx.BITMAP_TYPE_ANY),pos=(200,13), size=(200,24))
        #--| Button
        close = wx.Button(self.panel, -1, "Close all downloads",(440,23), (115,26))
        self.Bind(wx.EVT_BUTTON, self.EvtChoice, close)
        #--| Textbox
        self.dropText = wx.TextCtrl(self.panel, pos=(0,55), size=(574,210),
            style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
        #--| Radiobuttons
        quality = ['low', 'med', 'high']
        rb = wx.RadioBox(self.panel,-1,"Video quality",(10,3),wx.DefaultSize,quality,3,wx.RA_SPECIFY_COLS)
        rb.SetSelection(2)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)
        self.radio_choice = rb.GetStringSelection()
        #-- | Call dropText and set "high" vid_quality
        dt = MyURLDropTarget(self.dropText, self.radio_choice)
        self.dropText.SetDropTarget(dt)

    def EvtRadioBox(self, event):
        self.radio_choice = event.GetString()
        dt = MyURLDropTarget(self.dropText, self.radio_choice)
        self.dropText.SetDropTarget(dt)

    def EvtChoice(self, event):
        '''Shutdown ffmpeg process'''
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.call('taskkill /F /IM ffmpeg.exe', startupinfo=startupinfo)

    def OnStartDrag(self, evt):
        if evt.Dragging():
            url = self.draggableURLText.GetValue()
            data = wx.URLDataObject()
            data.SetURL(url)
            dropSource = wx.DropSource(self.draggableURLText)
            dropSource.SetData(data)
            result = dropSource.DoDragDrop()

if __name__ == "__main__":
    app = wx.App(redirect=False, filename='info.txt') #redirect=False
    mytitle = 'Wx_nrk'
    width = 580
    height = 294
    MyFrame(None, mytitle, (width, height)).Show()
    app.MainLoop()



