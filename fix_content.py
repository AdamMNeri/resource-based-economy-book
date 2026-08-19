import os
import re

def update_file(filepath, replacements):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes in {filepath}")

# 1. Fix Introduction
intro_replacements = [
    (
        "The crises confronting 21st-century civilization—climate instability, biodiversity loss, mental health epidemics, sovereign debt crises, and the existential risk of exponential technology coupled with competitive market incentives—are not evidence of human wickedness. They are the predictable operational outputs of a legacy economic operating system (MV = PY driven by D(t) = P₀e^(rt)) running on modern high-leverage hardware.",
        "The crises confronting 21st-century civilization are not evidence of human wickedness. Climate instability, biodiversity loss, mental health epidemics, and sovereign debt crises are structural. They are the predictable operational outputs of a legacy economic operating system running on modern high-leverage hardware. This system operates on rigid mathematical formulas—such as compounding debt mandates ($D(t) = P_0 e^{rt}$) and traditional price/velocity metrics ($MV=PY$)—which inherently force continuous consumption and extraction regardless of physical limits."
    )
]
update_file("chapters/00-introduction-v3.md", intro_replacements)

# 2. Fix Chapter 2
ch2_replacements = [
    (
        "To operate the high-powered 5-axis CNC router and heavy woodworking lathes, you scan your digital profile badge",
        "To operate the high-powered 5-axis CNC router, biomaterial extruders, and advanced hydroponic sequencers, you scan your digital profile badge"
    ),
    (
        "Within seconds, the bench unlocks its precision woodworking tools, CNC router, and electronic soldering stations, while a veteran craftsperson nearby offers guidance on grain finishing.",
        "Within seconds, the bench unlocks its precision tools, biomaterial extruders, and electronic soldering stations, while a veteran engineer nearby offers guidance on deploying software for your agtech automation."
    ),
    (
        "woodworking, robotics, topiary, welding, clay throwing, or software development",
        "robotics, regenerative agtech, bio-fabrication, digital media arts, or software development"
    ),
    (
        "industrial multi-axis precision router, bio-fabrication printer, or spatial audio workstation.",
        "industrial multi-axis CNC machine, bio-fabrication printer, agricultural robotics array, or spatial audio workstation."
    ),
    (
        "sustainable timber, clay, electronic components, metals",
        "sustainable bioplastics, agricultural sensors, electronic components, advanced composite metals"
    ),
    (
        "high-voltage welding equipment, or heavy woodworking routers",
        "high-voltage welding equipment, or advanced chemical and bio-fabrication suites"
    )
]
update_file("chapters/02-introducing-resourceism-v15.md", ch2_replacements)

# 3. Fix Chapter 9
ch9_replacements = [
    (
        "**The Precision Acoustic Luthier**: An elder master craftsman collaborates with teenagers in the community woodworking lab, crafting specialized acoustic guitars and stringed instruments. Without the need to mass-produce cheap instruments for a consumer market, they spend months carefully tuning resonant soundboards, selecting ethically sourced timber, and teaching the deep patience required for world-class sonic mastery.",
        "**The Digital-Biological Innovator**: An elder software engineer collaborates with teenagers in the community agtech lab, crafting specialized sensor arrays for vertical hydroponic farms. Without the need to rush cheap consumer products to market, they spend months carefully tuning the machine learning algorithms, selecting ethically sourced bio-polymers for the 3D-printed housing, and teaching the deep patience required for world-class ecological stewardship."
    )
]
update_file("chapters/09-human-flourishing-dividend-v8.md", ch9_replacements)

# 4. Fix Chapter 10
ch10_replacements = [
    (
        "transition into furniture craftsmanship and woodworking at a community Resource Hub",
        "transition into open-source software engineering or biomaterials research at a community Resource Hub"
    )
]
update_file("chapters/10-behavioral-architecture-and-identity-v12.md", ch10_replacements)
