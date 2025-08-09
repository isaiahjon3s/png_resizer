A simple program to resize .png images via the command line. 

*For full disclosure I am sure that there are possibly simpler ways and tools to resize pngs, but I created this because there was not a way of resizing the boarder of a png that I liked.*

## Purpose
* Resize any png by increasing the blank space of the png 
    * This is especially useful for creating profile pictures from pngs as an image with more blank space is often desireable to create a correctly sized profile picture

* Change the color of a png's background
    * Either to common color, or a custom hex or rgb color code

## Requirements

- Python 3.12 or higher
- Pillow (PIL) library

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/png_expand.git
   cd png_expand
   ```

2. **Install the required dependency:**
   ```bash
   pip install Pillow
   ```

## Usage

```bash
# Basic usage - auto-generated filename with 50px transparent padding
python png_expand.py image.png
# Creates: image_padded_50px_clear.png

# Custom output filename
python png_expand.py image.png my_new_image.png
# Creates: my_new_image.png

# Custom padding amount with auto-generated name
python png_expand.py image.png -p 100
# Creates: image_padded_100px_clear.png

# Custom output name with specific settings
python png_expand.py image.png final_image.png -p 75 -c white
# Creates: final_image.png

# Different colors (auto-generated names show the color)
python png_expand.py image.png -c red
# Creates: image_padded_50px_255-0-0.png

python png_expand.py image.png -c "#FF0000"
# Creates: image_padded_50px_255-0-0.png

python png_expand.py image.png -c "255,0,0"
# Creates: image_padded_50px_255-0-0.png
```

## Command Format

```bash
python png_expand.py INPUT_FILE [OUTPUT_FILE] [OPTIONS]
```

- `INPUT_FILE` - Path to your PNG file
- `OUTPUT_FILE` - Optional custom output filename (auto-generated if not provided)
- `-p PADDING` - Padding in pixels for all sides (default: 50)
- `-c COLOR` - Background color (default: clear/transparent)

## Output Filename Options

**Custom filename:** Specify exactly what you want
```bash
python png_expand.py image.png my_picture.png
```

**Auto-generated filename:** Descriptive name showing your settings
```bash
python png_expand.py image.png -p 100 -c white
# Creates: image_padded_100px_white.png
```

## Supported Colors

**Color Names:** `clear`, `white`, `black`, `red`, `green`, `blue`, `yellow`, `cyan`, `magenta`, `gray`

**Hex Colors:** `#FF0000`, `#00FF0080` (with transparency)

**RGB Colors:** `255,0,0`, `255,0,0,128` (with transparency)

## Examples

```bash
# Profile picture with white background
python png_expand.py avatar.png -p 100 -c white

# Logo with transparent padding
python png_expand.py logo.png -p 50

# Custom colored border
python png_expand.py image.png -p 25 -c "#FFD700"
```

## License

MIT



Good luck, I hope this can be of help to someone!