# 🎥 WX NRK - Video Downloader

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![wxPython](https://img.shields.io/badge/wxPython-GUI-green.svg)](https://www.wxpython.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.7-red.svg)](https://github.com/snippsat/wx_nrk/releases)

A powerful **drag & drop GUI application** built with Python and wxPython for downloading video content and subtitles from **NRK TV**, **NRK Radio**, and **NRK Super**.

![Application Screenshot](http://imageshack.com/a/img853/8555/pfwy.jpg)

## ✨ Features

- 🖱️ **Drag & Drop Interface** - Simply drag URLs or video thumbnails to the application window
- 🎬 **Multi-Platform Support** - Works with NRK TV, NRK Radio, and NRK Super
- 📺 **Quality Selection** - Choose from low, medium, or high quality (high is default)
- 📝 **Automatic Subtitles** - Downloads and converts subtitles to SRT format
- 🧵 **Multi-threading** - Download multiple videos simultaneously with bandwidth sharing
- 🎵 **Audio Support** - Download radio content in MP3 or MKV format
- 📦 **Portable** - No additional installation required, includes Python and FFmpeg

## 🚀 Quick Start

### Installation

1. **Download** the latest release from the [Downloads](https://github.com/snippsat/wx_nrk/releases) section
2. **Extract** the zip file to your preferred location
3. **Run** `Nrk.exe` to start the application

### Usage

1. **Open** the WX NRK application
2. **Select** your preferred video quality (low/medium/high)
3. **Drag** a URL from NRK TV/Radio/Super into the application window
4. **Wait** for the download to complete
5. **Find** your downloaded video (MKV) and subtitle (SRT) files in the application directory

## 📋 Supported Platforms

| Platform | Status | File Format | Notes |
|----------|--------|-------------|-------|
| **NRK TV** | ✅ Full Support | MKV + SRT | Video with subtitles |
| **NRK Radio** | ✅ Full Support | MP3/MKV | Dual format system |
| **NRK Super** | ✅ Full Support | MKV + SRT | Kids content |

## 🔧 System Requirements

- **Operating System**: Windows (32-bit or 64-bit)
- **Dependencies**: Included (Python 3.11+ and FFmpeg bundled)
- **Internet**: Required for downloading content

## 📖 Version History

### Version 2.7 (Latest) - *January 14, 2024*
- 🔧 **Fixed** media naming for older content
- 🎯 **Improved** compatibility with legacy NRK content

### Version 2.6
- 🔧 **Fixed** NRK Radio dual-system support (MP3 + MKV streaming)
- ✅ **Maintained** full NRK TV compatibility

### Version 2.4
- ✅ **Stable** performance for NRK TV content

### Version 2.3
- 🔧 **Fixed** issues with specific NRK Radio programs

### Version 2.2
- ➕ **Added** NRK Radio and NRK Super support
- 🎯 **Improved** program title generation
- 📺 **Demo** available [here](https://www.dropbox.com/sh/wackcyek8nzziaf/wJ1hAkF49U)

## 🎮 How It Works

The application utilizes the NRK streaming infrastructure:

- **CDN**: Akamai Cloud solution
- **Streaming**: Fragment-based (Adobe HDS) streaming
- **Quality Range**: 
  - On-demand: 0.2 kbps to 2.5 Mbps
  - Live TV: 0.2 Mbps to 3.7 Mbps
- **Video Compression**: MPEG4, H.264 (AAC audio codec)
- **Resolution Range**: 320×180 to 1280×720 pixels
- **Subtitle Format**: Converted from NRK's .str format to standard .srt

## 🛠️ Technical Details

- **Language**: Python 3.11+
- **GUI Framework**: wxPython
- **Video Processing**: FFmpeg
- **Audio Conversion**: AAC to AC3 codec
- **Subtitle Processing**: VTT to SRT conversion
- **Web Scraping**: BeautifulSoup4
- **HTTP Requests**: requests library

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Tom (Snippsat)**
- Copyright © 2021-2024

## ⚠️ Disclaimer

This tool is for personal use only. Please respect NRK's terms of service and only download content you have the right to access.

---

> 🎯 **Pro Tip**: For best results, use the "high" quality setting and ensure you have a stable internet connection for large downloads.