#!/bin/bash
set -euo pipefail

echo "🎬 Converting to 9:16 with blurred background..."

# Check dependencies
command -v ffmpeg >/dev/null 2>&1 || { echo "❌ FFmpeg not installed"; exit 1; }

WIDTH=1080
HEIGHT=1920

find . -maxdepth 1 -type f -name "*.mp4" ! -name "*_tiktok.mp4" -print0 | while IFS= read -r -d '' file; do
  echo "📹 Processing: $file"

  output="${file%.*}_🎉Finished.mp4"

  if ffmpeg -i "$file" -vf \
  "split[v1][v2];
   [v1]scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=increase,boxblur=20:10,crop=${WIDTH}:${HEIGHT}[bg];
   [v2]scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=decrease[fg];
   [bg][fg]overlay=(W-w)/2:(H-h)/2" \
  -c:v libx264 -crf 20 -preset medium -c:a copy "$output"; then

    echo "✅ Done: $output"
  else
    echo "❌ Failed: $file"
  fi

done

echo "🎉 Finished processing all files!"
