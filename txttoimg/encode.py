from PIL import Image

def encode_text(image_path, text_path, output_path):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = list(image.getdata())
    
    # Read the text to hide
    with open(text_path, 'r') as file:
        text = file.read()
    
    # Append a delimiter to indicate the end of the text
    text += "%%EOF"

    # Convert text to binary
    binary_text = ''.join([format(ord(char), '08b') for char in text])
    binary_index = 0

    # Create a new list for modified pixels
    new_pixels = []
    
    for pixel in pixels:
        if binary_index < len(binary_text):
            r, g, b = pixel
            new_r = r & ~1 | int(binary_text[binary_index])  # Modify LSB of red
            binary_index += 1
            if binary_index < len(binary_text):
                new_g = g & ~1 | int(binary_text[binary_index])  # Modify LSB of green
                binary_index += 1
            else:
                new_g = g
            if binary_index < len(binary_text):
                new_b = b & ~1 | int(binary_text[binary_index])  # Modify LSB of blue
                binary_index += 1
            else:
                new_b = b
            new_pixels.append((new_r, new_g, new_b))
        else:
            new_pixels.append(pixel)
    
    # Create a new image and save it
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path)
    print("Text successfully hidden in the image!")

# Usage
encode_text('random.png', 'random.txt', 'output_image.png')