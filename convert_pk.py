import base58

print("Enter your private key:\n")
string_private_key = input()
secret_key_binary = base58.b58decode(string_private_key)
private_key_byte_array = [int(c) for c in secret_key_binary]
print(private_key_byte_array)