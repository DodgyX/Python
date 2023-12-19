from PIL import Image

def get_image_rgb_values(input_file):
    try:
        # Open the image
        image = Image.open(input_file)

        # Get the size of the image
        width, height = image.size

        # Get RGB values for a sample pixel (e.g., the top-left corner)
        red, green, blue = image.getpixel((0, 0))

        print(f"Image size: {width}x{height}")
        print(f"RGB values at (0, 0): Red={red}, Green={green}, Blue={blue}")

    except Exception as e:
        print(f"Error: {e}")
    
    number = red + (green)*256 + (blue)*65536
    print(number)

if __name__ == "__main__":
    input_file = r"C:\Users\hp\Desktop\Code\Python\image creator\Sanstitre.png"
    get_image_rgb_values(input_file)

