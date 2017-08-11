from PIL import Image
from PIL import ImageDraw


SIZE_W = 120
SIZE_H = 200


def create_image():
    img = Image.new("RGBA", (SIZE_W, SIZE_H), (0, 0, 0))

    draw = ImageDraw.Draw(img)
    for i in range(4):
        draw.rectangle([(i * 30 + 5, 10), (i * 30 + 25, 190)], fill=(80, 80, 80))

    draw.line([(5, 100), (25, 100)], fill=(255, 255, 255), width=2)
    draw.line([(35, 130), (55, 130)], fill=(255, 255, 255), width=2)

    return img


img = create_image()


img.save("teste.png")
