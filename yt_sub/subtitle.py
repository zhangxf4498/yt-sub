import whisper
from googletrans import Translator
import re

def generate_subtitles(video_path, output_srt_path):
    """使用 Whisper 生成英文字幕文件"""
    model = whisper.load_model("tiny")
    result = model.transcribe(video_path)

    with open(output_srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"]):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            f.write(f"{i+1}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(f"{text}\n\n")

def format_time(seconds):
    """将秒数转换为 SRT 时间格式 (HH:MM:SS,mmm)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}".replace(".", ",")

def translate_srt(input_file, output_file, src_lang='en', dest_lang='zh-cn'):
    """将 SRT 英文字幕文件翻译为中文"""
    translator = Translator()
    with open(input_file, 'r', encoding='utf-8') as f_in:
        srt_content = f_in.read()

    blocks = re.split(r'\n\s*\n', srt_content.strip())
    translated_blocks = []

    for block in blocks:
        if not block.strip():
            continue

        lines = block.split('\n')
        header = lines[:2]
        text = ' '.join(lines[2:])

        if text.strip() and not '-->' in text:
            try:
                translated = translator.translate(text, src=src_lang, dest=dest_lang).text
                translated_block = '\n'.join(header + [translated])
            except Exception as e:
                print(f"翻译失败: {e}")
                translated_block = block
        else:
            translated_block = block

        translated_blocks.append(translated_block)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write('\n\n'.join(translated_blocks))

def merge_bilingual_srt(srt_zh_path, srt_en_path, output_srt_path):
    """合并中英字幕为一个双语 SRT 文件"""
    with open(srt_zh_path, 'r', encoding='utf-8') as f_zh, \
         open(srt_en_path, 'r', encoding='utf-8') as f_en:
        zh_blocks = f_zh.read().split('\n\n')
        en_blocks = f_en.read().split('\n\n')

    with open(output_srt_path, 'w', encoding='utf-8') as f_out:
        for zh_block, en_block in zip(zh_blocks, en_blocks):
            zh_lines = zh_block.strip().split('\n')
            en_lines = en_block.strip().split('\n')
            if len(zh_lines) >= 3 and len(en_lines) >= 3:
                merged_block = (
                    f"{zh_lines[0]}\n{zh_lines[1]}\n"
                    f"{zh_lines[2]}\n{en_lines[2]}\n"
                )
                f_out.write(merged_block + "\n")