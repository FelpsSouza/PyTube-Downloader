import yt_dlp
from tqdm import tqdm
import msvcrt

# Função de progresso para o yt-dlp
def progress_hook(d):
    if d['status'] == 'downloading':
        if 'total_bytes' in d:
            total = d['total_bytes']
        elif 'total_bytes_estimate' in d:
            total = d['total_bytes_estimate']
        else:
            total = None

        if total and not hasattr(progress_hook, 'bar'):
            progress_hook.bar = tqdm(total=total, unit='B', unit_scale=True, desc="Baixando")

        if total:
            progress_hook.bar.n = d['downloaded_bytes']
            progress_hook.bar.refresh()

    elif d['status'] == 'finished':
        if hasattr(progress_hook, 'bar'):
            progress_hook.bar.close()
        print("\n✅ Download complete! Converting if needed...")

# Entrada do usuário
url = input("Paste YouTube video link: ")
download_location = "C:\Downloads\PyTube Downloader"

# Configurações do yt-dlp
ydl_opts = {
    'outtmpl': f'{download_location}/%(title)s.%(ext)s',
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
    'merge_output_format': 'mp4',
    'progress_hooks': [progress_hook],
    'quiet': True,
    'no_warnings': False,
    'cookiefile': 'cookies.txt',  # usa cookies exportados
    'noplaylist': False,          # permite baixar playlists completas
    'ignoreerrors': True,         # se um vídeo da playlist falhar, continua
}


# Executa o download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    print(f"\n🎬 Vídeo baixado: {info.get('title')} ({info.get('ext')})")


print("\n✅ Press any key to continue...")
print("Project made by Felipe de Souza\nSee more projects in:")
print("GitHub: https://github.com/FelpsSouza")
print("Linkedin: https://www.linkedin.com/in/felipe-de-souza-silva/")
msvcrt.getch()