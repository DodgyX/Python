from PIL import Image

# Your original binary data
binary_data = "0101010101100010..."

# Make the length a perfect square (assuming the binary data is too short)
perfect_square_length = int(len(binary_data) ** 0.5)
new_length = perfect_square_length ** 2
padding_bits = "1" * (new_length - len(binary_data))  # Using '1' for red padding

# Add padding to the binary data
padded_binary_data = binary_data + padding_bits

# Assume a square image, calculate the side length
side_length = int(len(padded_binary_data) ** 0.5)

# Convert binary string to a list of pixel values (0 or 1)
pixels = [int(bit) for bit in padded_binary_data]

# Reshape the 1D array to a 2D array (image)
image = [[pixels[i * side_length + j] for j in range(side_length)] for i in range(side_length)]

# Create an image from the array
img = Image.new('1', (side_length, side_length), color=1)  # Initialize with white pixels
img.putdata(pixels)

# Save or display the image
img.save('output_image.png')
img.show()
