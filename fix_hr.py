import os, glob, re

for f in glob.glob("chapters/*.md"):
    if os.path.basename(f) == "00-Book-Map-of-Content.md" or os.path.basename(f) == "SUMMARY.md":
        continue
    
    with open(f, "r") as file:
        content = file.read()
    
    # Replace multiple occurrences of horizontal rules (at least 3 hyphens) separated by whitespace
    # with a single horizontal rule '---'
    # Wait, the regex `(?m)^---$(?:\s*^---$)+` matches multiple horizontal rules.
    new_content = re.sub(r'(?m)^---$(?:\s*^---$)+', '---', content)
    
    # Also replace cases where we have `--\n` or `----` if any exist, but let's just stick to `---`
    # Let's also look for `---` followed by a bunch of newlines and then another `---`
    new_content = re.sub(r'(---\s*){2,}', '---\n\n', new_content)
    
    if new_content != content:
        print(f"Fixed double HR in {f}")
        with open(f, "w") as file:
            file.write(new_content)
