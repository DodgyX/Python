from PIL import Image, ImageDraw

def create_image_with_number(output_file=r"C:\Users\hp\Desktop\Code\Python\image creator\Sanstitre.png"):
    # Set image properties
    width, height = 200, 200

    # Get user input for the number
    try:
        number_to_display = int(input("Enter a number between 0 and 16777215: "))
        if not (0 <= number_to_display <= 16777215):
            raise ValueError("Number must be between 0 and 16777215.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Invert RGB values from the input number
    blue = int(number_to_display / 65536)
    green = int((number_to_display % 65536) / 256)
    red = number_to_display % 256

    # Create a new image with the specified color
    image = Image.new("RGB", (width, height), (red, green, blue))

    # Save the image to a file
    image.save(output_file)
    print(blue)
    print(green)
    print(red)

if __name__ == "__main__":
    create_image_with_number()
