import Image

img = Image.open("ex.jpg")

tile_size = (128, 64)
img_p = img.crop((0, 0, 128, 128))
img_p = img_p.rotate(45, expand=1).resize(tile_size)
img_p.save('test.png', 'PNG', transparency=0)

print img_p.size
