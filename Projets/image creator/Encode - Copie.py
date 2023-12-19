from PIL import Image, ImageDraw

def create_image_with_number(output_file=r"C:\Users\hp\Desktop\Code\Python\image creator\Sanstitre.png"):
    # Set image properties
    width, height = 1, 1

    # Get user input for the number
    try:
        number_to_display = int(input("Enter a number: "))
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Calculate the number of cycles and the remainder for both pixels
    cycles_first_pixel = number_to_display // (255 * 3)
    remainder_first_pixel = number_to_display % (255 * 3)

    cycles_second_pixel = (number_to_display + 1) // (255 * 3)
    remainder_second_pixel = (number_to_display + 1) % (255 * 3)

    # Calculate RGB values for the first pixel
    first_pixel_red = remainder_first_pixel % 256
    first_pixel_green = (remainder_first_pixel // 256) % 256
    first_pixel_blue = (remainder_first_pixel // (256 * 256)) % 256

    # Calculate RGB values for the second pixel
    second_pixel_red = remainder_second_pixel % 256
    second_pixel_green = (remainder_second_pixel // 256) % 256
    second_pixel_blue = (remainder_second_pixel // (256 * 256)) % 256

    # Create a new image with the specified color for the first pixel
    image = Image.new("RGB", (width, height), (first_pixel_red, first_pixel_green, first_pixel_blue))

    # Save the image to a file
    image.save(output_file)

    print(f"First pixel RGB: ({first_pixel_red}, {first_pixel_green}, {first_pixel_blue})")

    # Create a new image with the specified color for the second pixel
    image = Image.new("RGB", (width, height), (second_pixel_red, second_pixel_green, second_pixel_blue))

    # Save the image to a file
    image.save(r"C:\Users\hp\Desktop\Code\Python\image creator\Sanstitre_second_pixel.png")

    print(f"Second pixel RGB: ({second_pixel_red}, {second_pixel_green}, {second_pixel_blue})")

if __name__ == "__main__":
    create_image_with_number()
