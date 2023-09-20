
import serial
import time
import speechprocessing 
ser = serial.Serial('COM6', 9600)

# Define a dictionary for Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Use slash to represent space in Morse code
}

# Function to encode text to Morse code
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)  # Keep non-alphanumeric characters as they are
    return ' '.join(morse_code)

# Function to decode Morse code to text
def morse_to_text(morse_code):
    text = []
    morse_code = morse_code.split(' ')
    for code in morse_code:
        if code in morse_code_dict.values():
            text.append([char for char, value in morse_code_dict.items() if value == code][0])
        elif code == '/':
            text.append(' ')  # Space
        else:
            text.append(code)  # Keep unknown Morse code sequences as they are
    return ''.join(text)


while True:
    command = int(input("1.Listen\n2.Quit\nEnter Here:"))
    if command == 1:
        try:
            text = speechprocessing.audio_input()
            
            if text.startswith("dot") or text.startswith("dash"):
                    text = text.replace(" ", "")
                    text = text.replace("and", " ")
                    text = text.replace("dot", ".")
                    text = text.replace("dash", "-")
                    text = morse_to_text(text)
                    print("Your Message:", text)
                    input_text = text
                    ser.write(input_text.encode())
                    
            else:
                print("Your Message:", text)
                input_text = text_to_morse(text)
                ser.write(input_text.encode())
        except:
            print("Rerun the program")
    elif command == 2:
        break
    else:
        continue
    # text = "Hello World"
    
    # print("sent to receiver")
    # if ser.read().decode().strip() == "transfered":
    #     print("transfered")



# Test the functions
# input_text = "Sazz Sharma!"
# encoded_text = text_to_morse(input_text)
# decoded_text = morse_to_text(encoded_text)

# print(f"Original Text: {input_text}")
# print(f"Encoded Morse Code: {encoded_text}")
# print(f"Decoded Text: {decoded_text}")
