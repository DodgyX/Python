import time

start = time.time()

mylist = []
nbr = 0
def contains_zero(number):
    return '0' in str(number)
def contains_5_and_even(number):
    str_num = str(number)
    return '5' in str_num and any(int(digit) % 2 == 0 for digit in str_num)

def calculate_multiplicative_persistence(number):
    global nbr
    persistence = 0

    while number >= 10:
        product = 1
        for digit_char in str(number):
            digit = int(digit_char)
            product *= digit

        number = product
        persistence += 1
    
    nbr += 1
    mylist.append(persistence)
    return persistence

start_range = 100000
end_range = 1000000

for num in range(start_range, end_range + 1):
    if contains_zero(num) or contains_5_and_even(num):
        continue  # Skip numbers with the digit 0
    persistence = calculate_multiplicative_persistence(num)
    print(f"Number: {num}, Persistence: {persistence}")

print(nbr)
print(max(mylist))

end = time.time()

print(end - start)

# normal                                        : 21.31656503677368
# skip the 0's                                  : 10.424999237060547
# skip the 0 and the 2/5                        : 9.579432964324951
# skip the 0 and the even numbers/5             : 7.234774112701416


