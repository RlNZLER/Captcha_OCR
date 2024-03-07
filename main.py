from PIL import Image

def remove_colors_except_gray(input_image_path, output_image_path):
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
    result_image = Image.new("RGB", (width, height))

    # Iterate over each pixel and retain only the ones with similar color to the target gray
    for x in range(width):
        for y in range(height):
            # Get the pixel color
            pixel_color = rgb_image.getpixel((x, y))

            # Check if the pixel color is within the tolerance range of the target gray color
            if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                # Pixel color is within tolerance, retain it
                result_image.putpixel((x, y), pixel_color)
            else:
                # Pixel color is not within tolerance, set it to white
                result_image.putpixel((x, y), (255, 255, 255))

    # Save the modified image
    result_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "test/captcha.jpeg"
    output_image_path = "result/captcha_processed.jpeg"
    
    remove_colors_except_gray(input_image_path, output_image_path)
    print("Image processing complete.")
