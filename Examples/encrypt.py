plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance to shift characters: "))
code = ""

for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)

    code += chr(cipherValue)
print("The encrypted message is", code)
