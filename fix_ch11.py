filepath = "chapters/11-conclusion-call-to-action-v8.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace mentions of Mediocrity Principle with Biophysical Realism in text
content = content.replace(
    "embracing cosmic humility under the Mediocrity Principle",
    "embracing ecological humility under biophysical realism"
)
content = content.replace(
    "cosmic humility, intrinsic motivation, and the Mediocrity Principle",
    "systems alignment, intrinsic motivation, and biophysical realism"
)

with open("chapters/11-conclusion-call-to-action-v9.md", "w", encoding="utf-8") as f:
    f.write(content)
