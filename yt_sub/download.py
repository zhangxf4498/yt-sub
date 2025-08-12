import subprocess
import sys

def download_videos(video_ids_file="videoID"):
    """
    Downloads videos from a list of video IDs using yt-dlp.

    Args:
        video_ids_file (str): Path to the file containing video IDs.
    """
    try:
        with open(video_ids_file, 'r') as f:
            video_ids = [line.strip() for line in f if line.strip()]

        if not video_ids:
            raise ValueError("videoID文件为空")

    except FileNotFoundError:
        print(f"错误：找不到文件 {video_ids_file}")
        return

    for video_id in video_ids:
        cmd = [
            "yt-dlp",
            "--cookies-from-browser", "chrome",
            "-f", "bestvideo[height<=4320]+bestaudio",
            "--merge-output-format", "mp4",
            "--recode-video", "mp4",
            "--postprocessor-args", "ffmpeg:-c:v libx264 -c:a aac",
            video_id
        ]

        print(f"\n正在下载视频: {video_id}")
        print("执行命令:", " ".join(cmd))

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                print(line, end='')

            return_code = process.wait()

            if return_code == 0:
                print(f"成功下载: {video_id}")
            else:
                print(f"下载失败: {video_id} (返回码: {return_code})")

        except Exception as e:
            print(f"执行过程中出错: {str(e)}")
            continue

if __name__ == "__main__":
    if len(sys.argv) > 1:
        download_videos(sys.argv[1])
    else:
        download_videos()