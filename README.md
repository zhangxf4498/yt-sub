# yt-sub

`yt-sub` 是一个用于自动化下载 YouTube 视频、生成英文字幕、翻译成中文，并最终将中英双语字幕嵌入到视频中的工具。

## 功能特性

- **视频下载**: 使用 `yt-dlp` 从 `videoID` 文件中下载指定视频。
- **字幕生成**: 使用 `OpenAI Whisper` 自动从视频中生成英文字幕（`*.srt`）。
- **字幕翻译**: 使用 `googletrans` 将生成的英文字幕翻译成中文。
- **字幕合并**: 将中英文字幕合并为一个双语字幕文件。
- **字幕嵌入**:
  - 支持**软字幕**嵌入：将字幕作为可开关的流嵌入到视频中，视频画质无损。
  - 支持**硬字幕**嵌入：将字幕永久烧录到视频画面上。

## 依赖

您需要确保系统已安装以下工具：

- **yt-dlp**: 用于下载 YouTube 视频。
- **ffmpeg**: 用于视频格式转换和字幕嵌入。

## 安装

1.  克隆项目仓库：
    ```bash
    git clone [https://github.com/your-username/yt-sub.git](https://github.com/your-username/yt-sub.git)
    cd yt-sub
    ```

2.  安装 Python 依赖：
    ```bash
    pip install -e .
    ```
    `-e` 参数表示以可编辑模式安装，方便开发。

## 使用方法

1.  **准备视频ID**：
    在项目根目录下创建一个名为 `videoID` 的文件。在文件中，每行输入一个您想要下载和处理的 YouTube 视频的 URL 或 ID。

    例如：
    ```
    [https://www.youtube.com/watch?v=xxxxxxxxxxx](https://www.youtube.com/watch?v=xxxxxxxxxxx)
    [https://www.youtube.com/watch?v=yyyyyyyyyyy](https://www.youtube.com/watch?v=yyyyyyyyyyy)
    ```

2.  **运行脚本**：
    在项目根目录下，运行主脚本来执行整个工作流程。

    ```bash
    python main.py
    ```

    脚本将依次执行以下操作：
    -   从 `videoID` 文件下载所有视频。
    -   为每个视频生成英文字幕。
    -   将英文字幕翻译为中文。
    -   合并中英字幕。
    -   生成带有硬字幕（永久烧录）的视频。

## 项目结构