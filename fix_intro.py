import re

filepath = "chapters/00-introduction-v3.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

old_text = "The crises confronting 21st-century civilization—climate instability, biodiversity loss, mental health epidemics, sovereign debt crises, and the existential risk of exponential technology coupled with competitive market incentives—are not evidence of human wickedness. They are the predictable operational outputs of a legacy economic operating system ($MV=PY$ driven by $D(t) = P_0 e^{rt}$) running on modern high-leverage hardware."
new_text = "The crises confronting 21st-century civilization are not evidence of human wickedness. Climate instability, biodiversity loss, mental health epidemics, and sovereign debt crises are structural. They are the predictable operational outputs of a legacy economic operating system running on modern high-leverage hardware. This system operates on rigid mathematical formulas—such as compounding debt mandates ($D(t) = P_0 e^{rt}$) and traditional price/velocity metrics ($MV=PY$)—which inherently force continuous consumption and extraction regardless of physical limits."

if old_text in content:
    content = content.replace(old_text, new_text)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed intro")
else:
    print("Could not find exact match in intro")
