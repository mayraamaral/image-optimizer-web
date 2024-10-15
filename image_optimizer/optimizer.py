import argparse, sys, os
from PIL import Image, UnidentifiedImageError

class ImageOptimizerError(Exception):
    pass

def image_optimizer(input_file, output_file, quality=85, scale=0.8, verbose=True):
    """
    Compress and resize an image.

    :param input_file: Path to the original image
    :param output_file: Path to save the output file
    :param quality: Compression quality (0-100 | default: 85)
    :param scale: Scale of resizing (default: 80%)
    :param verbose: Whether to print messages (default: True)
    """

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext != output_ext:
        raise ImageOptimizerError(f"Input file type '{input_ext}' does not match output file type '{output_ext}'.")

    try:
        imagem = Image.open(input_file)
    except FileNotFoundError:
        raise ImageOptimizerError(f"File '{input_file}' was not found.")
    except UnidentifiedImageError:
        raise ImageOptimizerError(f"File '{input_file}' is not a valid image.")

    width, height = imagem.size
    new_width = int(width * scale)
    new_height = int(height * scale)
    imagem = imagem.resize((new_width, new_height), Image.Resampling.LANCZOS)
    imagem.save(output_file, optimize=True, quality=quality)
    
    if verbose:
        print(f"Image successfully optimized and save as '{output_file}'.")

def main():
    parser = argparse.ArgumentParser(description="Compress and resize images.")
    parser.add_argument("input_file", type=str, help="Path to the original image")
    parser.add_argument("output_file", type=str, help="Path to save the output file")
    parser.add_argument("--quality", type=int, default=85, help="Compression quality (0-100)")
    parser.add_argument("--scale", type=float, default=0.8, help="Scale of resizing (0.1 a 1.0)")
    parser.add_argument("--verbose", action=argparse.BooleanOptionalAction, default=True, help="Whether to print messages (--verbose / --no-verbose)")
    
    args = parser.parse_args()
    
    try:
        image_optimizer(args.input_file, args.output_file, args.quality, args.scale, args.verbose)
    except ImageOptimizerError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
