input = input("This is the text which is decrypted!")
output = []
length = 8
for i in range(len(input))[::length]:
    output.append(input[i:i+length])
    
for i in range(len(output)):
    print(output[i])
for i in range(len(output)):
    print(output[i],end="")
