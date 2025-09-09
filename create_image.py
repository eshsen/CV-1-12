from PIL import Image
import random

N = 189
M = 761

img = Image.new('RGB', (N, M))

for x in range(N):
    for y in range(M):
        r = random.randint(200, 255)
        g = random.randint(0, 50)
        b = random.randint(0, 50)
        img.putpixel((x, y), (r, g, b))

img.save('img.png')
