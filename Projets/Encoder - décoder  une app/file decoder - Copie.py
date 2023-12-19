import base64
import sys
sys.set_int_max_str_digits(10000000)

with open(r"C:\Users\yoann.wiss\Desktop\python\Python\Encoder - décoder  une app\test\AutoClicker-3.0.exe", 'rb') as file:
    binary_data = file.read()
print(binary_data)
# Convert binary data to binary string
binary_string = ''.join(format(byte, '08b') for byte in binary_data)

# Convert binary data

decimal_value = int(binary_string, 2)
hex_representation = format(decimal_value, 'X')
base64_data = base64.b64encode(binary_data).decode('utf-8')



# Print or use the hexadecimal representation
with open(r'C:\Users\yoann.wiss\Desktop\python\Python\Encoder - décoder  une app\text.txt', 'w') as lol2:
    lol2.write(hex_representation)

# Save binary string to text file
with open(r'C:\Users\yoann.wiss\Desktop\python\Python\Encoder - décoder  une app\tex2.txt', 'w') as lol:
    lol.write(str(decimal_value))