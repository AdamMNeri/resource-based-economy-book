import os
import re
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont

def generate_composite_cover(output_path="images/cover_full_title.jpeg"):
    canvas_w, canvas_h = 1200, 1600
    bg_color = (11, 17, 30) # #0B111E dark navy/slate
    
    cover = Image.new("RGB", (canvas_w, canvas_h), bg_color)
    draw = ImageDraw.Draw(cover)
    
    logo_path = "images/Minimalist_vector_logo_symbol.jpeg"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        logo_size = 680
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        logo_x = (canvas_w - logo_size) // 2
        logo_y = 100
        cover.paste(logo, (logo_x, logo_y))
    
    # Fonts
    font_bold_path = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_reg_path = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    
    if not os.path.exists(font_bold_path):
        font_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    if not os.path.exists(font_reg_path):
        font_reg_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    title_font = ImageFont.truetype(font_bold_path, 72)
    subtitle_font = ImageFont.truetype(font_reg_path, 34)
    author_font = ImageFont.truetype(font_bold_path, 40)
    
    # Colors
    gold_color = (229, 193, 88)   # #E5C158
    cyan_color = (78, 205, 196)   # #4ECDC4
    white_color = (240, 244, 248) # #F0F4F8
    
    # Draw Title
    title_text = "BEYOND MONEY"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((canvas_w - title_w) // 2, 830), title_text, font=title_font, fill=gold_color)
    
    # Draw Subtitle (wrapped)
    sub_line1 = "A Systems Architecture for Human Flourishing"
    sub_line2 = "and Planetary Stewardship"
    
    sub1_bbox = draw.textbbox((0, 0), sub_line1, font=subtitle_font)
    sub2_bbox = draw.textbbox((0, 0), sub_line2, font=subtitle_font)
    
    draw.text(((canvas_w - (sub1_bbox[2] - sub1_bbox[0])) // 2, 940), sub_line1, font=subtitle_font, fill=white_color)
    draw.text(((canvas_w - (sub2_bbox[2] - sub2_bbox[0])) // 2, 995), sub_line2, font=subtitle_font, fill=white_color)
    
    # Decorative Gold/Cyan Divider Line
    line_x1 = (canvas_w - 300) // 2
    line_x2 = line_x1 + 300
    draw.line([(line_x1, 1340), (line_x2, 1340)], fill=cyan_color, width=3)
    
    # Draw Author
    author_text = "ADAM NERI"
    author_bbox = draw.textbbox((0, 0), author_text, font=author_font)
    draw.text(((canvas_w - (author_bbox[2] - author_bbox[0])) // 2, 1375), author_text, font=author_font, fill=gold_color)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cover.save(output_path, "JPEG", quality=95)
    print(f"Generated 3:4 composite cover: {output_path} ({os.path.getsize(output_path)} bytes)")
    return output_path

def build_epub():
    summary_path = 'SUMMARY.md'
    src_dir = 'src'
    chapters_dir = 'chapters'
    exports_dir = 'exports'
    images_dir = 'images'
    os.makedirs(exports_dir, exist_ok=True)

    # 1. Generate 3:4 composite cover
    cover_image_path = generate_composite_cover(os.path.join(images_dir, 'cover_full_title.jpeg'))

    if not os.path.exists(summary_path):
        print("SUMMARY.md not found, skipping EPUB build.")
        return

    with open(summary_path, 'r') as f:
        lines = f.readlines()

    chapter_files = []
    for line in lines:
        match = re.search(r'\((chapters/[^)]+)\)', line)
        if match:
            chapter_files.append(os.path.basename(match.group(1)))

    if not chapter_files:
        print("No chapter files found in SUMMARY.md for EPUB build.")
        return

    epub_paths = []
    patterns = [
        r'\n##\s+Agent First-Pass Validation.*',
        r'\n#\s+Agent First-Pass Validation.*',
        r'\n##\s+Agent Validation.*'
    ]

    for filename in chapter_files:
        chapter_path = os.path.join(chapters_dir, filename)
        if not os.path.exists(chapter_path):
            continue
        with open(chapter_path, 'r') as f:
            content = f.read()
        stripped = content
        for p in patterns:
            m = re.search(p, stripped, re.IGNORECASE | re.DOTALL)
            if m:
                stripped = stripped[:m.start()]
                break
        stripped = stripped.replace("../images/", "images/")
        temp_path = os.path.join(src_dir, f'temp_epub_{filename}')
        with open(temp_path, 'w') as f:
            f.write(stripped.strip() + '\n\n')
        epub_paths.append(temp_path)

    css_file = os.path.join(exports_dir, 'epub-fix.css')
    with open(css_file, 'w') as f:
        f.write('''@page { margin: 0; padding: 0; }
body { font-family: sans-serif; line-height: 1.5; margin: 5%; color: #111111; background-color: #ffffff; }
div.cover, figure.cover { text-align: center; margin: 0; padding: 0; width: 100vw; height: 100vh; page-break-after: always; }
img.cover, img { max-width: 100%; height: auto; object-fit: contain; display: block; margin: 0 auto; }
pre, code { font-family: monospace; font-size: 65%; page-break-inside: avoid; break-inside: avoid; white-space: pre-wrap; }
ul { display: block; list-style-type: disc; margin-top: 0.5em; margin-bottom: 0.8em; padding-left: 2em; }
ol { display: block; list-style-type: decimal; margin-top: 0.5em; margin-bottom: 0.8em; padding-left: 2em; }
li { display: list-item; margin-bottom: 0.5em; line-height: 1.4; }
ol ol, ul ol { list-style-type: lower-alpha; margin-top: 0.3em; margin-bottom: 0.3em; }
ul ul, ol ul { list-style-type: circle; margin-top: 0.3em; margin-bottom: 0.3em; }
h1, h2, h3 { page-break-after: avoid; break-after: avoid; }''')

    # Primary release EPUB filename (fresh name forces Kobo database to re-parse title & sleep cover)
    epub_release = os.path.join(exports_dir, 'Beyond-Money-Adam-Neri.epub')
    epub_draft = os.path.join(exports_dir, 'rbe-book-draft.epub')

    cmd = ['pandoc'] + epub_paths + [
        '-o', epub_release,
        '--toc',
        '--toc-depth=2',
        '--metadata', 'title=Beyond Money: A Systems Architecture for Human Flourishing and Planetary Stewardship',
        '--metadata', 'author=Adam Neri',
        '--metadata', 'identifier=urn:uuid:beyond-money-adam-neri-2026-v1',
        '--css', css_file,
        '--split-level=1',
        '--standalone'
    ]

    if os.path.exists(cover_image_path):
        cmd.extend(['--epub-cover-image', cover_image_path])

    print(f"Building Release EPUB: {epub_release} ...")
    subprocess.run(cmd, check=True)

    # Also save as rbe-book-draft.epub for backwards compatibility
    shutil.copy2(epub_release, epub_draft)

    for p in epub_paths:
        if os.path.exists(p):
            os.remove(p)

    print(f"EPUB generation complete: {epub_release} ({os.path.getsize(epub_release)} bytes)")
    print(f"Draft copy updated: {epub_draft} ({os.path.getsize(epub_draft)} bytes)")

if __name__ == '__main__':
    build_epub()
