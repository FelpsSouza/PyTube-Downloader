# PyTube Downloader

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Status](https://img.shields.io/badge/status-active-success)]()

---

## 🇧🇷 Descrição (PT-BR)

O **PyTube Downloader** é um script em Python criado para baixar vídeos e playlists completas do YouTube com segurança, rapidez e praticidade.  
Inspirado na dificuldade de encontrar ferramentas confiáveis para esse tipo de tarefa, o projeto oferece uma alternativa livre de anúncios invasivos, sites suspeitos e riscos de malware.

### Recursos principais
- Download de vídeos em alta qualidade (áudio + vídeo)
- Barra de progresso interativa em tempo real
- Merge automático em MP4 via FFmpeg
- Suporte a playlists completas

### Tecnologias utilizadas
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [tqdm](https://github.com/tqdm/tqdm)
- [FFmpeg](https://ffmpeg.org/)

### Objetivos futuros
- Seleção de qualidade de saída (720p, 1080p, 4K...)
- Suporte a diferentes formatos (MP4, MKV, MP3)
- Menu interativo para facilitar a experiência
- Otimização para grandes playlists

---

## 🇺🇸 Description (EN)

**PyTube Downloader** is a Python script designed to download YouTube videos and full playlists safely, quickly, and efficiently.  
Born from the difficulty of finding trustworthy tools for this task, it provides an alternative free of intrusive ads, shady websites, or hidden malware risks.

### Key Features
- High-quality video downloads (audio + video)
- Real-time interactive progress bar
- Automatic MP4 merging via FFmpeg
- Full playlist support

### Technologies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [tqdm](https://github.com/tqdm/tqdm)
- [FFmpeg](https://ffmpeg.org/)

### Future Plans
- Output quality selection (720p, 1080p, 4K...)
- Support for multiple formats (MP4, MKV, MP3)
- Interactive menu for better user experience
- Optimization for large playlists

---

## 🚀 Instalação

Clone este repositório e instale as dependências necessárias:

```bash
git clone https://github.com/FelpsSouza/PyTube-Downloader.git
cd PyTube-Downloader
pip install -r requirements.txt
```

Certifique-se de ter o **FFmpeg** instalado e configurado no PATH do sistema.

---

## ▶️ Uso básico

### Baixar um vídeo
```bash
python downloader.py https://www.youtube.com/watch?v=VIDEO_ID
```

### Baixar uma playlist
```bash
python downloader.py https://www.youtube.com/playlist?list=PLAYLIST_ID
```

O script exibirá uma barra de progresso interativa e fará o merge automático do áudio + vídeo.

---

## 📌 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📄 Licença
Este projeto está sob a lic
