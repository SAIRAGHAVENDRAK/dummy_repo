import os

key = "sbdkakkakdbasdbas"
password = "dsbkjdafhdskfksd"

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)

token = "ajskdhaskjdhka"

def main():
    filename = 'test.txt'
    if os.path.exists(filename):
        read_file(filename)
    else:
        print(f"File '{filename}' does not exist.")

if __name__ == '__main__':
    main()
