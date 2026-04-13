import subprocess
from pathlib import Path

WIDTH = 1080
HEIGHT = 1920

def process_video(file_path: Path):
    output = file_path.with_name(file_path.stem + "_🎉Finished.mp4")

    if "_tiktok" in file_path.stem:
        return

    print(f"📹 Processing: {file_path.name}")

    cmd = [
        "ffmpeg", "-y",
        "-i", str(file_path),
        "-vf",
        (
            f"split[v1][v2];"
            f"[v1]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
            f"boxblur=20:10,crop={WIDTH}:{HEIGHT}[bg];"
            f"[v2]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease[fg];"
            f"[bg][fg]overlay=(W-w)/2:(H-h)/2"
        ),
        "-c:v", "libx264",
        "-crf", "20",
        "-preset", "medium",
        "-c:a", "copy",
        str(output)
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Done: {output.name}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed: {file_path.name}")


def main():
    video_files = Path(".").glob("*.mp4")

    for file in video_files:
        process_video(file)

    print("🎉 Finished processing all files!")


if __name__ == "__main__":
    main()
