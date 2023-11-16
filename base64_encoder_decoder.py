import base64

def base64_decode(encoded_data):
    decoded_bytes = base64.b64decode(encoded_data.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

if __name__ == "__main__":
    user_input = input("Enter text to decode: ")
    
    decoded_result = base64_decode(user_input)
    print(f"Decoded: {decoded_result}")
