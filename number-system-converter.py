
print("=== Number System Converter ===")

decimal = int(input("Enter a decimal number: "))

print("\nDecimal:", decimal)
print("Binary:", bin(decimal)[2:])
print("Octal:", oct(decimal)[2:])
print("Hexadecimal:", hex(decimal)[2:].upper())
