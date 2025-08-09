#!/usr/bin/env python3

import argparse
import sys
from PIL import Image
from pathlib import Path

def parse_color(color_str):
    """Parse color string to RGBA tuple"""
    if not color_str:
        return None
    
    # Handle common color names
    color_map = {
        'black': (0, 0, 0, 255),
        'white': (255, 255, 255, 255),
        'red': (255, 0, 0, 255),
        'green': (0, 255, 0, 255),
        'blue': (0, 0, 255, 255),
        'yellow': (255, 255, 0, 255),
        'cyan': (0, 255, 255, 255),
        'magenta': (255, 0, 255, 255),
        'gray': (128, 128, 128, 255),
        'lightgray': (211, 211, 211, 255),
        'darkgray': (64, 64, 64, 255),
        'transparent': (0, 0, 0, 0),
        'clear': (0, 0, 0, 0)
    }
    
    color_lower = color_str.lower()
    if color_lower in color_map:
        return color_map[color_lower]
    
    # Handle hex colors
    if color_str.startswith('#'):
        hex_color = color_str[1:]
        if len(hex_color) == 6:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return (r, g, b, 255)
        elif len(hex_color) == 8:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            a = int(hex_color[6:8], 16)
            return (r, g, b, a)
    
    # Handle RGB tuples like "255,0,0" or "255,0,0,128"
    if ',' in color_str:
        try:
            parts = [int(x.strip()) for x in color_str.split(',')]
            if len(parts) == 3:
                return (parts[0], parts[1], parts[2], 255)
            elif len(parts) == 4:
                return (parts[0], parts[1], parts[2], parts[3])
        except ValueError:
            pass
    
    raise ValueError(f"Invalid color format: {color_str}. Use color names, hex (#FF0000), or RGB (255,0,0)")

def generate_output_filename(input_path, padding, color_rgba):
    """Generate output filename based on input and settings"""
    path = Path(input_path)
    
    # Create descriptive suffix
    if color_rgba == (0, 0, 0, 0):  # Transparent
        color_desc = "clear"
    elif color_rgba == (255, 255, 255, 255):  # White
        color_desc = "white"
    else:
        color_desc = f"{color_rgba[0]}-{color_rgba[1]}-{color_rgba[2]}"
        if color_rgba[3] != 255:
            color_desc += f"-{color_rgba[3]}"
    
    suffix = f"_padded_{padding}px_{color_desc}"
    return str(path.parent / f"{path.stem}{suffix}{path.suffix}")

def main():
    parser = argparse.ArgumentParser(description="PNG Expand - Add padding around PNG images with customizable background color")
    
    # Required input
    parser.add_argument("input", help="Input PNG file path")
    
    # Optional output
    parser.add_argument("output", nargs='?', help="Output PNG file path (auto-generated if not provided)")
    
    # Padding options
    parser.add_argument("-p", "--padding", type=int, default=50, 
                       help="Padding in pixels for all sides (default: 50)")
    
    # Color options
    parser.add_argument("-c", "--color", default="clear", 
                       help="Background color: clear/transparent (default), white, black, red, etc., hex (#FF0000), or RGB (255,0,0)")
    
    args = parser.parse_args()
    
    try:
        # Parse color
        try:
            background_color = parse_color(args.color)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        
        # Generate output filename if not provided
        output_path = args.output
        if not output_path:
            output_path = generate_output_filename(args.input, args.padding, background_color)
        
        # Process the image
        expand_png(args.input, output_path, args.padding, background_color)
        
        print(f"✓ Successfully expanded {args.input}")
        print(f"✓ Saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def expand_png(input_path, output_path, padding, background_color):
    """
    Expand a PNG image by adding uniform padding around all edges with specified background color.
    """
    # Open the input image
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_path}' not found")
    except Exception as e:
        raise Exception(f"Failed to open input file: {e}")
    
    # Convert to RGBA if not already (to handle transparency properly)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Calculate new dimensions with uniform padding
    original_width, original_height = img.size
    new_width = original_width + (padding * 2)
    new_height = original_height + (padding * 2)
    
    # Create new image with specified background color
    new_img = Image.new('RGBA', (new_width, new_height), background_color)
    
    # Paste the original image in the center
    paste_x = padding
    paste_y = padding
    new_img.paste(img, (paste_x, paste_y), img if img.mode == 'RGBA' else None)
    
    # Convert back to RGB if original was RGB and background is opaque
    if img.mode == 'RGB' and background_color[3] == 255:
        new_img = new_img.convert('RGB')
    
    # Save the result
    try:
        new_img.save(output_path, 'PNG')
    except Exception as e:
        raise Exception(f"Failed to save output file: {e}")

if __name__ == "__main__":
    main()