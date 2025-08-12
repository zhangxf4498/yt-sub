from setuptools import setup, find_packages

setup(
    name='yt-sub',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'yt-dlp',
        'openai-whisper',
        'googletrans==4.0.0-rc1',
    ],
    entry_points={
        'console_scripts': [
            # 可以在这里添加命令行入口点
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to download YouTube videos and generate bilingual subtitles.',
    long_description='A tool to download YouTube videos and generate bilingual subtitles.',
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/yt-sub',
)