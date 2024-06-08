# ASCII Art Generator

This Python script uses the `ascii_magic` library to convert an image file into ASCII art and saves the result as an HTML file.

## Prerequisites

Before running the script, make sure you have the `ascii_magic` library installed. You can install it using pip:

```
pip install ascii-magic
```

## Usage

1. Replace the file path `'C:/Parth gohil/Picture/.thumbnails/1000009455.jpg'` with the actual path to your desired image file.

2. Run the script.

3. The script will generate an HTML file named `ascii_art.html` in the same directory as the script.

4. Open the `ascii_art.html` file in a web browser to view the ASCII art representation of your image.

## How it Works

1. The script imports the `AsciiArt` class from the `ascii_magic` library.

2. It creates an instance of the `AsciiArt` class by calling the `from_image` method and passing the file path of the image you want to convert to ASCII art.

3. The `to_html_file` method is called on the `AsciiArt` instance with the following arguments:
   - `'ascii_art.html'`: The file name for the HTML file that will be generated.
   - `columns=200`: The number of columns (character width) for the ASCII art representation.
   - `width_ratio=2`: The width ratio for the ASCII art characters.

4. The script generates an HTML file containing the ASCII art representation of the specified image, with the specified width and character ratio.

5. You can open the generated `ascii_art.html` file in a web browser to view the ASCII art.

Note: Make sure to replace the file path with the correct path to your desired image file. The script assumes that the provided file path is valid and accessible.
