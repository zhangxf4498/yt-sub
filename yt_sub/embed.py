import subprocess

def embed_soft_subtitles(video_path, srt_path, output_path, language="chi"):
    """嵌入可开关的字幕流"""
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-i", srt_path,
        "-map", "0",
        "-map", "1",
        "-c:v", "copy",
        "-c:a", "copy",
        "-c:s", "mov_text",
        "-metadata:s:s:0", f"language={language}",
        output_path
    ]
    subprocess.run(cmd, check=True)

def embed_hard_subtitles(video_path, srt_path, output_path):
    """嵌入硬字幕到视频（永久烧录）"""
    video_path = str(video_path)
    srt_path = str(srt_path)
    output_path = str(output_path)

    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"subtitles='{srt_path.replace("'", "'\\''")}'",
        "-c:a", "copy",
        output_path
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"硬字幕烧录成功: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"硬字幕烧录失败: {e}")
        raise