from PIL import Image
import pytesseract

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_to_binary(input_image_path, output_image_path):
    # Define the target gray color
    target_color = (128, 128, 128)
    tolerance = 30  # Tolerance for color matching

    # Open the image
    image = Image.open(input_image_path)

    # Convert the image to RGB mode
    rgb_image = image.convert("RGB")
    
    # Get the image dimensions
    width, height = image.size
    
    # Create a new image with the same dimensions
    result_image = Image.new("L", (width, height))  # L mode for grayscale image

    # Iterate over each pixel and convert to black and white
    for x in range(width):
        for y in range(height):
            # Get the pixel color
            pixel_color = rgb_image.getpixel((x, y))

            # Check if the pixel color is within the tolerance range of the target gray color
            if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                # Pixel color is within tolerance, set it to black
                result_image.putpixel((x, y), 0)  # 0 for black
            else:
                # Pixel color is not within tolerance, set it to white
                result_image.putpixel((x, y), 255)  # 255 for white

    # Save the modified image
    result_image.save(output_image_path)

def recognize_text(image_path):
    # Use pytesseract to perform OCR
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

if __name__ == "__main__":
    input_image_path = "test/captcha.jpeg"
    output_image_path = "result/captcha_processed.jpeg"
    
    convert_to_binary(input_image_path, output_image_path)
    print("Image processing complete.")
    
    recognized_text = recognize_text(output_image_path)
    print("Recognized Text:")
    print(recognized_text)
