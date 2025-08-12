from pathlib import Path
from yt_sub.download import download_videos
from yt_sub.subtitle import generate_subtitles, translate_srt, merge_bilingual_srt
from yt_sub.embed import embed_hard_subtitles, embed_soft_subtitles

def main_workflow():
    # 1. 下载视频
    download_videos()

    # 获取当前目录下所有mp4文件
    path = Path.cwd()
    filenames = [file.stem for file in path.glob("*.mp4")]

    if not filenames:
        print("未找到任何 .mp4 文件，请确保视频已下载。")
        return

    for filename in filenames:
        video_path = f"{filename}.mp4"
        english_srt_path = f"{filename}_en.srt"
        chinese_srt_path = f"{filename}_zh.srt"
        bilingual_srt_path = f"{filename}_bilingual.srt"
        hard_sub_video_path = f"{filename}_hard_subs.mp4"
        soft_sub_video_path = f"{filename}_soft_subs.mp4"

        # 2. 生成英文字幕
        print(f"\n正在为 {video_path} 生成英文字幕...")
        generate_subtitles(video_path, english_srt_path)

        # 3. 翻译字幕
        print(f"正在翻译英文字幕到中文...")
        translate_srt(english_srt_path, chinese_srt_path)

        # 4. 合并为双语字幕
        print(f"正在合并中英双语字幕...")
        merge_bilingual_srt(chinese_srt_path, english_srt_path, bilingual_srt_path)

        # 5. 嵌入硬字幕
        print(f"正在嵌入硬字幕...")
        embed_hard_subtitles(video_path, bilingual_srt_path, hard_sub_video_path)

        # 6. 嵌入软字幕 (可选)
        # print(f"正在嵌入软字幕...")
        # embed_soft_subtitles(video_path, bilingual_srt_path, soft_sub_video_path)

if __name__ == "__main__":
    main_workflow()