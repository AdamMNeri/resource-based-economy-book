import os
import glob
import re

chapters_dir = "chapters"

# Get current active chapters
active_chapters = {}
for file_path in glob.glob(os.path.join(chapters_dir, "*.md")):
    base_name = os.path.basename(file_path)
    # Extract the base prefix (e.g., "01-the-case-for-change")
    match = re.match(r'(\d+-[a-zA-Z0-9-]+?)(?:-v\d+)?\.md$', base_name)
    if match:
        prefix = match.group(1)
        active_chapters[prefix] = base_name
    elif base_name.startswith("00-introduction"):
        active_chapters["00-introduction"] = base_name
    elif base_name.startswith("references"):
        active_chapters["references"] = base_name

# Now update SUMMARY.md
summary_path = "SUMMARY.md"
if os.path.exists(summary_path):
    with open(summary_path, "r", encoding="utf-8") as f:
        summary_content = f.read()
    
    for prefix, current_name in active_chapters.items():
        # Replace instances of prefix-vX.md with current_name
        pattern = re.compile(rf'{prefix}(?:-v\d+)?\.md')
        summary_content = pattern.sub(current_name, summary_content)
    
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary_content)

# Update 00-Book-Map-of-Content.md if it exists
moc_path = os.path.join(chapters_dir, "00-Book-Map-of-Content.md")
if os.path.exists(moc_path):
    with open(moc_path, "r", encoding="utf-8") as f:
        moc_content = f.read()
    
    for prefix, current_name in active_chapters.items():
        pattern = re.compile(rf'{prefix}(?:-v\d+)?\.md')
        moc_content = pattern.sub(current_name, moc_content)
    
    with open(moc_path, "w", encoding="utf-8") as f:
        f.write(moc_content)
    print("Updated MOC")

# Update README.md
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
    
    for prefix, current_name in active_chapters.items():
        pattern = re.compile(rf'{prefix}(?:-v\d+)?\.md')
        readme_content = pattern.sub(current_name, readme_content)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

print("Updated links in SUMMARY, MOC, and README")
