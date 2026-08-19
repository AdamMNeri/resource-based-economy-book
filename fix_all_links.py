import os
import glob
import re

chapters_dir = "chapters"

# Get current active chapters
active_chapters = {}
for file_path in glob.glob(os.path.join(chapters_dir, "*.md")):
    base_name = os.path.basename(file_path)
    # The correct regex to extract prefix without -vX
    match = re.match(r'^(.+?)(?:-v\d+)?\.md$', base_name)
    if match:
        prefix = match.group(1)
        active_chapters[prefix] = base_name

# Fix SUMMARY.md
summary_path = "SUMMARY.md"
if os.path.exists(summary_path):
    with open(summary_path, "r", encoding="utf-8") as f:
        content = f.read()
    for prefix, current_name in active_chapters.items():
        pattern = re.compile(rf'{prefix}(?:-v\d+)?\.md')
        content = pattern.sub(current_name, content)
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(content)

# Fix links in all chapters
for file_path in glob.glob(os.path.join(chapters_dir, "*.md")):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for prefix, current_name in active_chapters.items():
        # Replace links like [[chapters/11-conclusion-call-to-action-v8|
        # or [[11-conclusion-call-to-action-v8]]
        
        # We want to replace prefix-vX without the .md extension inside wiki links
        current_name_no_ext = current_name.replace(".md", "")
        
        pattern = re.compile(rf'{prefix}(?:-v\d+)?(?=\|\])')
        # Actually it's better to just replace prefix-vX with current_name_no_ext
        # We need a regex that matches prefix optionally followed by -v\d+
        # But we must be careful not to match prefix-v10 if prefix is prefix-v1.
        # But prefix does not have -v in it.
        pattern = re.compile(rf'\b{re.escape(prefix)}(?:-v\d+)?\b')
        
        # Replace but we have to ensure it's not replacing the .md if it's there
        # Let's do it simpler:
        # replace prefix-vX.md with current_name
        pattern_md = re.compile(rf'{re.escape(prefix)}(?:-v\d+)?\.md')
        new_content = pattern_md.sub(current_name, new_content)
        
        # replace prefix-vX with current_name_no_ext for wiki links
        pattern_wiki = re.compile(rf'{re.escape(prefix)}(?:-v\d+)?(?=[|\]])')
        new_content = pattern_wiki.sub(current_name_no_ext, new_content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated links in {file_path}")
