# Write your code here :-)
a = 10
b =16

if a > b:
    print("Ogo!")
    print(a - b)
else:
    print("Danuna!")
    print(b - a)

print("THE END")

def open_file(filename):
    print("File reading", filename)
    with open(filename) as f:
        return f.read()
        print("Done!")
