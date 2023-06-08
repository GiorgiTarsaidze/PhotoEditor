from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import sys
import os

def main():
    path = input("Enter the image path: ")
    if not os.path.isfile(path):
        print("Invalid image path. Please try again.")
        return

    original_image = Image.open(path)
    modified_image = original_image.copy()
    history = [original_image]
    redo_history = []

    while True:
        options()
        option = get_option()

        if option == "U":
            modified_image = undo(modified_image,history,redo_history)
        elif option == "R":
            modified_image = redo(modified_image, history, redo_history)
        else:
            modified_image = choose_option(option,modified_image)
            history.append(modified_image.copy())
            redo_history.clear()

        choice = input("Save file or Continue? (S/C) ")
        if choice.upper() == "S":
            save_file(modified_image)
            sys.exit("File has been successfully saved!")
        elif choice.upper() == "C":
            continue
        else:
            print("Invalid choice. Please enter 'S' to save or 'C' to continue.")
            break

def options():
    options = [
        "1. Flip X",
        "2. Flip Y",
        "3. Contrast",
        "4. Blur",
        "5. Contour",
        "6. Emboss",
        "7. Brightness",
        "8. Saturation",
        "9. Greyscale"
    ]
    for option in options:
        print(option)
    print("U. Undo")
    print("R. Redo")


def get_option():
    while True:
        option = input("Please choose an option: ")
        if option.isdigit() and 1 <= int(option) <= 9:
            return option
        elif option.upper() == "U":
            return "U"
        elif option.upper() == "R":
            return "R"
        else:
            print("Invalid option. Please choose a number between 1 and 9.")

def choose_option(option, image):
    options = {
        "1": flipx,
        "2": flipy,
        "3": contrast,
        "4": blur,
        "5": contour,
        "6": emboss,
        "7": brightness,
        "8": saturation,
        "9": greyscale
    }
    return options[option](image)

def flipx(image):
    return ImageOps.mirror(image)

def flipy(image):
    return ImageOps.flip(image)

def blur(image):
    while True:
        blur_level = int(input("Please choose the level of BLUR: (1-10) "))
        if blur_level < 1 or blur_level > 10:
            print("Please choose the blur level between 1 and 10 ")
        else:
            return image.filter(ImageFilter.GaussianBlur(blur_level))

def contrast(image):
    while True:
        contrast_level = int(input("Please choose the level of CONTRAST: (1-10) "))
        if contrast_level not in range(1,11):
            print("Please choose the contrast level between 1 and 10 ")
        else:
            return image.filter(ImageFilter.UnsharpMask(contrast_level))

def contour(image):
    return image.filter(ImageFilter.CONTOUR)

def emboss(image):
    return image.filter(ImageFilter.EMBOSS)

def brightness(image):
    while True:
        brightness_level = float(input("Please choose the level of BRIGHTNESS: (0.0-2.0): "))
        if brightness_level >= 0.0 and brightness_level <= 2.0:
            enhancer = ImageEnhance.Brightness(image)
            return enhancer.enhance(brightness_level)
        else:
            print("BRIGHTNESS level must between 0.0 and 2.0")

def saturation(image):
    while True:
        saturation_level = float(input("Please choose the level of SATURATION: (0.0-2.0): "))
        if saturation_level >= 0.0 and saturation_level <= 2.0:
            enhancer = ImageEnhance.Color(image)
            return enhancer.enhance(saturation_level)
        else:
            print("SATURATION level must between 0.0 and 2.0")

def greyscale(image):
    return image.convert("L")

def undo(modified_image, history, redo_history):
    if len(history) > 1:
        redo_history.append(modified_image)
        history.pop()
        modified_image = history[-1]
        modified_image.show()
    else:
        print("No more undo steps available.")
    return modified_image

def redo(modified_image, history, redo_history):
    if redo_history:
        history.append(redo_history[-1])
        modified_image = redo_history.pop()
        modified_image.show()
    else:
        print("No redo steps available.")
    return modified_image

def save_file(modified_file):
    print("Please note, that if format is not specified, '.jpg' file will be created")
    new_file = input("Name of the new file?")
    if not new_file.lower().endswith(('.jpg','.jpeg','.png')):
        new_file += '.jpg'
    modified_file.save(new_file, format="JPEG")

if __name__ == "__main__":
    main()