from PIL import Image, ImageDraw

# The webpage details
url = "http://www.pythonchallenge.com/pc/return/5808.html"
username = "huge"
password = "file"

# Title is called odd even. Can the image be segregated by odd and even pixels?

# # Open image and get its data
im = Image.open('cave.jpg')
pixels = list(im.getdata()) # Get Pixel Data
width, height = im.size
# Initialize odd and even images
odd = Image.new("RGB", (width // 2, height // 2))
even = Image.new("RGB", (width // 2, height // 2))
# Put appropriate pixels in place
for w in range(width):
    for h in range(height):
        if (w + h) % 2 == 0:
            even.putpixel( (w // 2, h // 2), pixels[ h * width + w] )
        else:
            odd.putpixel( (w // 2, h // 2), pixels[ h * width + w] )
# Show the images
odd.show()
even.show()
