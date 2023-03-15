hello_world = "Hello, World!"

ascii_values = list(map(lambda x: ord(x), hello_world))

for value in ascii_values:
    print("The ASCII value of", chr(value), "is", value)


# print("Hello, World!") was too easy !
# Execute with 'python hello.py'