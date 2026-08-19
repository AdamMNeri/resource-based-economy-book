filepath = "ACKs from HERMES.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the text of the recent action
old_action = "1. **Guided Visualizations Eradicated:** A script was executed to find and strip every single instance of \"Guided Visualization\" out of all chapters. This removes the amateur pop-psychology tone completely from the book."
new_action = "1. **Manufacturing Examples Diversified:** Preserved the highly effective 'Guided Visualizations', but replaced the repetitive niche examples (CNC, clay, woodworking) with a broader array of future-focused applications (biomaterials, agtech automation, open-source software, spatial audio) to maximize relatability for a wider target audience."

if old_action in content:
    content = content.replace(old_action, new_action)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed ACKs")
else:
    print("Could not find old_action in ACKs")
