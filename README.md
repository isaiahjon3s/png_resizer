# PNG Expand

Add padding around PNG images with customizable background colors.

## Usage

```bash
# Basic usage - 50px transparent padding
python png_expand.py image.png

# Custom padding and color
python png_expand.py image.png -p 100 -c white

# Hex colors
python png_expand.py image.png -c "#FF0000"

# RGB colors  
python png_expand.py image.png -c "255,0,0"
```

## Installation

```bash
pip install Pillow
```

## Colors

- `clear` (default), `white`, `black`, `red`, `green`, `blue`
- Hex: `#FF0000` 
- RGB: `255,0,0`

## License

MIT