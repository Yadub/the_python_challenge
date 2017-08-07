from PIL import Image

im = Image.open('oxygen.png') # Load Image
pixels = list(im.getdata()) # Get Pixel Data
width, height = im.size

middle_pixels =  pixels[ width * (height / 2): (width) * (1 + height / 2)]
unique_RGB = [r for r, g, b, a in middle_pixels[::7] if r == g == b]
solution = "".join(map(chr, map(int, unique_RGB)))
print solution

# Solution states:
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
new_letters = [chr(i) for i in next_level]
final_solution = "".join(map(chr, map(int, next_level)))
print final_solution
