from PIL import Image;

def decode_text(image_path):
    # Open the image
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_text = ""
    for pixel in pixels:
        for color_value in pixel[:3]:  # Only check RGB channels
            binary_text += str(color_value & 1)

    # Split the binary string into 8-bit chunks and convert to characters
    hidden_text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        char = chr(int(byte, 2))
        hidden_text += char
        # Stop when the delimiter is found
        if hidden_text.endswith("%%EOF"):
            hidden_text = hidden_text[:-5]  # Remove delimiter
            break
    
    print("Hidden text found:")
    print(hidden_text)

# Usage
decode_text('output_image.png')
