import re
import os
import shutil

# Read the old chapter 10 to extract the text
ch10_path = "chapters/.archive/10-behavioral-architecture-and-identity-v13.md"
with open(ch10_path, "r", encoding="utf-8") as f:
    ch10_content = f.read()

# Extract Transactional Marriage text
marriage_match = re.search(r'(\d\.\s+\*\*The Transactional Nature of Marriage and Family:\*\*.+?)---\n', ch10_content, re.DOTALL)
if marriage_match:
    marriage_text = marriage_match.group(1).strip()
    # Remove the list number prefix to make it a clean heading or text
    marriage_text = re.sub(r'^\d\.\s+', '### ', marriage_text)
else:
    print("Could not find marriage text!")
    exit(1)

# Extract Perpetual Youth text
youth_match = re.search(r'(## 10\.2 The Perpetual Youth Engine: Manufactured Insecurity & Cosmetic Predation.+?)---\n', ch10_content, re.DOTALL)
if youth_match:
    youth_text = youth_match.group(1).strip()
    # Demote headings
    youth_text = youth_text.replace("## 10.2", "###")
    youth_text = youth_text.replace("### The Business", "#### The Business")
    youth_text = youth_text.replace("### Reclaiming Youth", "#### Reclaiming Youth")
else:
    print("Could not find youth text!")
    exit(1)

# Now inject into Chapter 9
ch9_path = "chapters/09-human-flourishing-dividend-v9.md"
with open(ch9_path, "r", encoding="utf-8") as f:
    ch9_content = f.read()

# Inject Marriage into 9.5
ch9_content = ch9_content.replace(
    "## 9.5 Reimagining Childhood and Family Cohesion\n",
    f"## 9.5 Reimagining Childhood and Family Cohesion\n\n{marriage_text}\n\n"
)

# Inject Youth into 9.3
# We will insert it just before the `---` that follows section 9.3
ch9_content = ch9_content.replace(
    "community stewardship*.\n\n---",
    f"community stewardship*.\n\n{youth_text}\n\n---"
)

new_ch9_path = "chapters/09-human-flourishing-dividend-v10.md"
with open(new_ch9_path, "w", encoding="utf-8") as f:
    f.write(ch9_content)
print(f"Created {new_ch9_path}")
if os.path.exists(ch9_path):
    shutil.move(ch9_path, os.path.join("chapters/.archive", os.path.basename(ch9_path)))
    print(f"Archived {ch9_path}")
