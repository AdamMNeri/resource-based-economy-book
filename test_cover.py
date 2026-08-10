import os
from PIL import Image, ImageDraw, FontFile, ImageFont

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
    
    # Decorative Gold Divider Line
    line_x1 = (canvas_w - 300) // 2
    line_x2 = line_x1 + 300
    draw.line([(line_x1, 1340), (line_x2, 1340)], fill=cyan_color, width=3)
    
    # Draw Author
    author_text = "ADAM NERI"
    author_bbox = draw.textbbox((0, 0), author_text, font=author_font)
    draw.text(((canvas_w - (author_bbox[2] - author_bbox[0])) // 2, 1375), author_text, font=author_font, fill=gold_color)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cover.save(output_path, "JPEG", quality=95)
    print(f"Generated composite cover: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    generate_composite_cover()
