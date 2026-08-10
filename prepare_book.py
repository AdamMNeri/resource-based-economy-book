import os
import re
import shutil
from datetime import datetime
from generate_epub import build_epub

chapters_dir = "chapters"
src_dir = "src"
images_dir = "images"
src_images_dir = os.path.join(src_dir, "images")

os.makedirs(src_dir, exist_ok=True)

# Copy images directory to src/images if it exists
if os.path.exists(images_dir):
    os.makedirs(src_images_dir, exist_ok=True)
    for fn in os.listdir(images_dir):
        src_file = os.path.join(images_dir, fn)
        dst_file = os.path.join(src_images_dir, fn)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)

# Generate current formatted timestamp
now_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " EDT"

# Read README.md
with open("README.md", "r") as f:
    readme_content = f.read()

# Automatically ensure **Last Revised:** line exists/is updated in README.md
if "**Last Revised:**" in readme_content:
    readme_content = re.sub(r"\*\*Last Revised:\*\*.*", f"**Last Revised:** {now_timestamp}", readme_content)
else:
    readme_content = readme_content.replace(
        "**Project Lead & Concept:** Adam Neri",
        f"**Project Lead & Concept:** Adam Neri  \n**Last Revised:** {now_timestamp}"
    )

# Write updated README.md
with open("README.md", "w") as f:
    f.write(readme_content)

# Write to src/index.md
with open(os.path.join(src_dir, "index.md"), "w") as f:
    f.write(readme_content)

# Process root SUMMARY.md and write normalized version to src/SUMMARY.md
with open("SUMMARY.md", "r") as f:
    summary_content = f.read()
summary_src_content = summary_content.replace("chapters/", "").replace("README.md", "index.md")
summary_src_content = re.sub(r"^\[summary\]\s*\n", "", summary_src_content, flags=re.IGNORECASE)

with open(os.path.join(src_dir, "SUMMARY.md"), "w") as f:
    f.write(summary_src_content)

# Process chapter files, stripping agent validation notes
chapter_files = sorted([fn for fn in os.listdir(chapters_dir) if fn.endswith(".md") and not fn.startswith(".")])

for filename in chapter_files:
    with open(os.path.join(chapters_dir, filename), "r") as f:
        content = f.read()
    
    patterns = [
        r"\n##\s+Agent First-Pass Validation.*",
        r"\n#\s+Agent First-Pass Validation.*",
        r"\n##\s+Agent Validation.*"
    ]
    
    stripped = content
    for p in patterns:
        match = re.search(p, stripped, re.IGNORECASE | re.DOTALL)
        if match:
            stripped = stripped[:match.start()]
            break
            
    with open(os.path.join(src_dir, filename), "w") as f:
        f.write(stripped.strip() + "\n")

print(f"Book chapters prepared successfully for clean publishing (Revision: {now_timestamp}).")

# Automatically generate EPUB export
try:
    build_epub()
except Exception as e:
    print(f"Warning: EPUB generation encountered an error: {e}")
