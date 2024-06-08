from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('C:/Parth gohil/Picture/.thumbnails/1000009455.jpg')
my_art.to_html_file('ascii_art.html',columns=200, width_ratio=2)