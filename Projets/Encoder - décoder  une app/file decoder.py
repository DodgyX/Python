import base64
from base2048 import base2048
import base65536

with open(r"C:\Users\yoann.wiss\Desktop\python\Python\Encoder - décoder  une app\test\AutoClicker-3.0.exe", 'rb') as file:
    binary_data = file.read()
print(binary_data)
# Convert binary data to binary string
binary_string = ''.join(format(byte, '08b') for byte in binary_data)

# Convert binary data

decimal_value = int(binary_string, 2)
hex_representation = format(decimal_value, 'X')
base64_data = base64.b64encode(binary_data).decode('utf-8')
base2048_data = base2048.encode(binary_data)
base65536_data = base65536.encode(binary_data)

chunk_size = 10000

# Split the encoded data into chunks
chunks = [base65536_data[i:i + chunk_size] for i in range(0, len(base65536_data), chunk_size)]

# Ask the user for the chunk number
while True:
    try:
        user_choice = int(input(f"Enter the chunk number (1-{len(chunks)}): "))
        if 1 <= user_choice <= len(chunks):
            break
        else:
            print("Invalid choice. Please enter a valid chunk number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Get the user-selected chunk
selected_chunk = chunks[user_choice - 1]

# Print or process the selected chunk
print(f"Selected Chunk {user_choice}: {selected_chunk}")

# Save base65536 data to text file
with open(r"C:\Users\hp\Desktop\Code\Python\Encoder - décoder  une app\text5.txt", 'w', encoding='utf-8') as base65536_file:
    base65536_file.write(base65536_data)
print(len(base65536_data))
# Save base2048 data to text file
with open(r'C:\Users\hp\Desktop\Code\Python\Encoder - décoder  une app\text4.txt', 'w', encoding='utf-8') as base2048_file:
    base2048_file.write(base2048_data)

# Save base64 data to text file
with open(r'C:\Users\hp\Desktop\Code\Python\Encoder - décoder  une app\text3.txt', 'w') as base64_file:
    base64_file.write(base64_data)

# Print or use the hexadecimal representation
with open(r'C:\Users\hp\Desktop\Code\Python\Encoder - décoder  une app\text2.txt', 'w') as lol2:
    lol2.write(hex_representation)

# Save binary string to text file
with open(r'C:\Users\hp\Desktop\Code\Python\Encoder - décoder  une app\text.txt', 'w') as lol:
    lol.write(decimal_value)