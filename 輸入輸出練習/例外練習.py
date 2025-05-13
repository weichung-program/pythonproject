
filename = input("輸入檔名: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print("An error occurred:", e)
finally:
    file.close()