# PhotoEditor

This is a simple **command-line** image editing tool implemented in Python using the PIL (Python Imaging Library) library.
It provides options such as flipping, blurring, enhancing contrast, applying filters, adjusting brightness and saturation, and converting to grayscale. 
The program supports undo and redo functionality, allowing users to revert and reapply modifications. Additionally, users can save the modified image to a file.

## Features

- Flip the image horizontally or vertically.
- Adjust the contrast level of the image.
- Apply blur effect to the image.
- Apply a contour filter to the image.
- Apply an emboss filter to the image.
- Adjust the brightness level of the image.
- Adjust the saturation level of the image.
- Convert the image to grayscale.
- Undo and redo previous image modifications.
- Save the modified image to a file.

## Getting Started

### Requirements

- Python 3
- PIL (Python Imaging Library)

### Installation

1. Clone the repository or download the source code files.
2. Install the required dependencies

### Usage

1. Open a terminal or command prompt and navigate to the directory where the code is located.
2. Move the image or photo you want to modify into the same directory as the code. (You can use `dog_test.jpg` for testing, It comes with the source code)
3. Run the following command to start the image editing tool: `python editor.py`
4. Follow the on-screen instructions to provide the image path, choose editing options, and save the modified image.

### Examples

1. Chosing editing options:
```
1. Flip X
2. Flip Y
3. Contrast
4. Blur
5. Contour
6. Emboss
7. Brightness
8. Saturation
9. Greyscale
U. Undo
R. Redo
Please choose an option:
```
2. Flipping the image horizontally:
```
Please choose an option: 1
Save file or Continue? (S/C) S
Name of the new file? modified_image.jpg
```
3. Adjusting the contrast level:
```
Please choose an option: 3
Please choose the level of CONTRAST: (1-10) 7
Save file or Continue? (S/C) S
Name of the new file? modified_image.jpg
```
3. Applying a blur effect:
```
Please choose an option: 4
Please choose the level of BLUR: (1-10) 5
Save file or Continue? (S/C) S
Name of the new file? modified_image.jpg
```
## Video Tutorial
- You can additionaly watch [this VIDEO DEMO](https://www.youtube.com/watch?v=eZsM-Hxa_Ts), that I created for Harvard CS50P: 

## Acknowledgments

- The image editing tool is based on the Python Imaging Library (PIL).
- This project was created as a learning exercise and for educational purposes.
- This is my final project for Harvard CS50P course https://cs50.harvard.edu/python/2022/project/
- This script was written by Giorgi Tarsaidze
