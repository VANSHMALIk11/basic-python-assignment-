# assignment - 4
# task -1
try:
    with open('sample.txt', 'r') as file:
        print("reading file contents  :")
        for index, line in enumerate(file , start=1):
             print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print(" ERROR : The file 'sample.txt' was not found")

# task - 2
txt= input("Enter text to write to the file  : ")
with open("output.txt","w") as file:
    file.write(txt+"\n")
print("Data successfully written to 'output.txt'")

additional_text = input("Enter additional text to write to the file  : ")
with open("output.txt","a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended")


with open("output.txt","r") as file:
    content = file.read()
print("\n Final contents of 'output.txt':")
print(content)









