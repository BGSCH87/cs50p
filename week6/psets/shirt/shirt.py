import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. Validate number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # 2. Extract extensions and validate them
    # splitext returns a tuple like ('filename', '.jpg')
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    
    valid_extensions = [".jpg", ".jpeg", ".png"]

    if ext2 not in valid_extensions:
        sys.exit("Invalid output")
    
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    # 3. Process the images
    try:
        # Open the overlay shirt
        shirt = Image.open("shirt.png")
        size = shirt.size

        # Open the input photo
        with Image.open(sys.argv[1]) as photo:
            # Use ImageOps.fit to resize and crop the photo to match the shirt
            photo_fitted = ImageOps.fit(photo, size)
            
            # Paste the shirt on top of the fitted photo
            # The second 'shirt' argument is the 'mask' for transparency
            photo_fitted.paste(shirt, shirt)
            
            # Save the result
            photo_fitted.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()