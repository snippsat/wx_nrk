# WX NRK

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/) [![wxPython](https://img.shields.io/badge/wxPython-GUI-green.svg)](https://www.wxpython.org/) [![Windows](https://img.shields.io/badge/Windows-10%2B-0078D6.svg)](https://www.microsoft.com/windows) [![FFmpeg](https://img.shields.io/badge/FFmpeg-included-orange.svg)](https://ffmpeg.org/) [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Version](https://img.shields.io/badge/Version-2.7-red.svg)](https://github.com/snippsat/wx_nrk/releases)

Downloading video content and subtitles from **NRK TV**, **NRK Radio**, and **NRK Super**.  
Drag a URL onto the window to start a download.

![Application screenshot](http://imageshack.com/a/img853/8555/pfwy.jpg)

## Requirements

- Windows (32-bit or 64-bit)
- Internet connection
- No separate install needed,all bundle in $\color{Green}{\textsf{nrk.exe}}$ 

## Download

Download from [GitHub Releases](https://github.com/snippsat/wx_nrk/releases) — not from the repo source tree:

| File | Platform |
|------|----------|
| `wx_nrk_32_2.7.zip` | 32-bit Windows |
| `wx_nrk_64_2.7.zip` | 64-bit Windows |

Extract the zip and run `Nrk.exe`.

## Usage

1. Start the application.
2. Choose video quality: low, medium, or high (default: high).
3. Drag a URL from NRK TV, NRK Radio, or NRK Super into the window.
4. Downloads are saved in the application directory as $\color{Green}{\textsf{.mkv}}$ (video) or $\color{Green}{\textsf{.mp3}}$  (radio podcasts), with subtitles as $\color{Green}{\textsf{.srt}}$ when available.

Multiple URLs can be dropped in sequence; each download runs in its own thread. Use **Close all downloads** to stop active FFmpeg processes.

## Supported sources

| Source | Output |
|--------|--------|
| NRK TV | MKV + SRT subtitles |
| NRK Super | MKV + SRT subtitles |
| NRK Radio (stream) | MKV |
| NRK Radio (podcast) | MP3 |

## Changelog

**2.7** (2024-01-14) — Fixed media naming for older NRK content.

**2.6** — NRK Radio dual-system support (MP3 and MKV streaming); NRK TV unchanged.

**2.4** — Stable NRK TV downloads.

**2.3** — Fixes for specific NRK Radio programs.

**2.2** — NRK Radio and NRK Super support; improved program title handling.

## Development

Source: `drag_drop_2_7.py`

| Component | Tool |
|-----------|------|
| GUI | wxPython |
| HTTP / parsing | requests, BeautifulSoup4 |
| Transcoding | FFmpeg (video copy, AAC → AC3; VTT → SRT) |

Requires Python 3.11+, wxPython, requests, beautifulsoup4, and unidecode. FFmpeg must be on `PATH` when running from source.

## License

MIT — see [LICENSE](LICENSE).

Copyright © 2021–2024 Tom (Snippsat)

## Disclaimer

For personal use only. Respect NRK's terms of service and download only content you are entitled to access.
