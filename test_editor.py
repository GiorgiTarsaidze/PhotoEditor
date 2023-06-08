from editor import undo, flipx, flipy, redo, greyscale
from PIL import Image

def test_flipx():
    image_path = "dog_test.jpg"
    image = Image.open(image_path)
    flipped_image = flipx(image)
    assert flipped_image != image
    assert flipped_image.size == image.size

def test_flipy():
    image_path = "dog_test.jpg"
    image = Image.open(image_path)
    flipped_image = flipy(image)
    assert flipped_image != image
    assert flipped_image.size == image.size

def test_greyscale():
    image_path = "dog_test.jpg"
    image = Image.open(image_path)
    grayscale_image = greyscale(image)

    assert grayscale_image.mode == "L"
    assert grayscale_image.size == image.size


def test_redo():
    image_path = "dog_test.jpg"
    original_image = Image.open(image_path)
    modified_image = original_image.copy()
    history = [original_image, modified_image.copy()]
    redo_image = Image.new("RGB", (100, 100))
    redo_history = [redo_image]
    result = redo(modified_image, history, redo_history)

    assert result == redo_image
    assert len(history) == 3
    assert len(redo_history) == 0

def test_undo():
    image_path = "dog_test.jpg"
    original_image = Image.open(image_path)
    modified_image = original_image.copy()
    history = [original_image, modified_image.copy()]
    redo_history = [Image.new("RGB", (100, 100))]
    result = undo(modified_image, history, redo_history)

    assert result == history[-1]
    assert len(history) == 1
    assert len(redo_history) == 2
