#chatgpt ai
from PIL import Image, ImageDraw, ImageFont

def create_app_icon(output_path="app_icon.png", size=(512, 512), text="AI"):
    # Create an image with a gradient background
    img = Image.new("RGB", size, "#FF5733")  # Base color
    draw = ImageDraw.Draw(img)
    
    # Draw a simple gradient
    for i in range(size[1]):
        color = (255, 87, 51 - int((i / size[1]) * 50))  # Slight gradient effect
        draw.line([(0, i), (size[0], i)], fill=color)
    
    # Add text in the center
    try:
        font = ImageFont.truetype("arial.ttf", 150)
    except:
        font = ImageFont.load_default()
    
    text_size = draw.textsize(text, font=font)
    text_x = (size[0] - text_size[0]) // 2
    text_y = (size[1] - text_size[1]) // 2
    draw.text((text_x, text_y), text, font=font, fill="white")
    
    # Save the icon
    img.save(output_path)
    print(f"Icon saved as {output_path}")

# Generate an icon
create_app_icon()
