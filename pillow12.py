from PIL import Image # Import Image class from the library.
#Some of the file formats supported are PPM, PNG, JPEG, GIF, TIFF, and BMP. It is also possible to create new file decoders to expand the library of file formats accessible
image = Image.open("templetes/image/albert.jpg") # Load the image.
rotated_image = image.rotate(90) # Rotate the image by 180 degrees.
rotated_image.save("file_rotated.jpg") # Save the rotated image.