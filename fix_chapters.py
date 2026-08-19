import os
import re
import glob
import shutil

chapters_dir = "chapters"
archive_dir = os.path.join(chapters_dir, ".archive")
os.makedirs(archive_dir, exist_ok=True)

# 1. Remove Guided Visualizations from all files
for file_path in glob.glob(os.path.join(chapters_dir, "*.md")):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to match Guided Visualization sections
    # It matches "### Guided Visualization" and everything up to the next "---" or "## "
    new_content = re.sub(
        r'### Guided Visualization.*?(?=\n---|\n## )',
        '',
        content,
        flags=re.DOTALL
    )
    # Remove any extra newlines that might have been left
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)

    if content != new_content:
        # Versioning: move original to archive, save new version
        base_name = os.path.basename(file_path)
        
        # Determine new version number
        match = re.search(r'-v(\d+)\.md$', base_name)
        if match:
            old_v = int(match.group(1))
            new_v = old_v + 1
            new_name = base_name.replace(f"-v{old_v}.md", f"-v{new_v}.md")
        else:
            new_name = base_name.replace(".md", "-v2.md")
        
        new_path = os.path.join(chapters_dir, new_name)
        
        # Save new file
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        # Archive old file
        shutil.move(file_path, os.path.join(archive_dir, base_name))
        print(f"Updated {base_name} -> {new_name}")

# 2. Fix the specific sentences in Introduction
intro_files = glob.glob(os.path.join(chapters_dir, "00-introduction*.md"))
if intro_files:
    intro_file = intro_files[0]
    with open(intro_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_text = "The crises confronting 21st-century civilization—climate instability, biodiversity loss, mental health epidemics, sovereign debt crises, and the existential risk of exponential technology coupled with competitive market incentives—are not evidence of human wickedness. They are the predictable operational outputs of a legacy economic operating system (MV = PY driven by D(t) = P₀e^(rt)) running on modern high-leverage hardware."
    
    new_text = "The crises confronting 21st-century civilization are not evidence of human wickedness. Climate instability, biodiversity loss, mental health epidemics, and sovereign debt crises are structural. They are the predictable operational outputs of a legacy economic operating system running on modern high-leverage hardware. This system operates on rigid mathematical formulas—such as compounding debt mandates ($D(t) = P_0 e^{rt}$) and traditional price/velocity metrics ($MV=PY$)—which inherently force continuous consumption and extraction regardless of physical limits."
    
    # We must match exactly, but there might be slight whitespace differences
    if old_text in content:
        new_content = content.replace(old_text, new_text)
        
        base_name = os.path.basename(intro_file)
        match = re.search(r'-v(\d+)\.md$', base_name)
        if match:
            old_v = int(match.group(1))
            new_v = old_v + 1
            new_name = base_name.replace(f"-v{old_v}.md", f"-v{new_v}.md")
        else:
            new_name = base_name.replace(".md", "-v2.md")
            
        new_path = os.path.join(chapters_dir, new_name)
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        shutil.move(intro_file, os.path.join(archive_dir, base_name))
        print(f"Fixed sentences in {base_name} -> {new_name}")
    else:
        print("Sentence not found exactly. Trying regex.")
        # Sometimes there's smart quotes or different spaces
        pattern = re.compile(r"The crises confronting 21st-century civilization.*?running on modern high-leverage hardware\.", re.DOTALL)
        if pattern.search(content):
            new_content = pattern.sub(new_text, content)
            
            base_name = os.path.basename(intro_file)
            match = re.search(r'-v(\d+)\.md$', base_name)
            if match:
                old_v = int(match.group(1))
                new_v = old_v + 1
                new_name = base_name.replace(f"-v{old_v}.md", f"-v{new_v}.md")
            else:
                new_name = base_name.replace(".md", "-v2.md")
                
            new_path = os.path.join(chapters_dir, new_name)
            with open(new_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            shutil.move(intro_file, os.path.join(archive_dir, base_name))
            print(f"Fixed sentences (via regex) in {base_name} -> {new_name}")
        else:
            print("Failed to find the sentence.")
