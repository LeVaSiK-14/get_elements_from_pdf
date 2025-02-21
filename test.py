from PIL import Image, ImageDraw

def draw_line_on_image(image_path, output_path, lines, color=(255, 0,0), width=4):

    image = Image.open(image_path)
    
    draw = ImageDraw.Draw(image)
    

    for line in lines:
        draw.line(line, fill=color, width=width)
    

    image.save(output_path)

draw_line_on_image("image.jpg", "output.jpg", [[(160, 100), (100, 300)], [(160, 100), (220, 300)], [(220, 300), (50, 180)], [(50, 180), (270, 180)], [(100, 300), (270, 180)]])
