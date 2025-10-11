import argparse


def text_analyzor(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return len(text), upper_count, lower_count


parser = argparse.ArgumentParser(
    description="Text analyzer system",
    epilog="CLI execution example:\n python file_name.py --text your text --verbose")
parser.add_argument("--verbose", action="store_true",
                    help="Show detailed text [e.g: len, upper, lower , ...]")
parser.add_argument("--text", type=str, required=True,
                    help="please input text")

args = parser.parse_args()

if args.verbose:
    length, upper, lower = text_analyzor(args.text)
    print(f"Text: {args.text}")
    print(f"Length: {length}")
    print(f"Upper: {upper}")
    print(f"Lower: {lower}")
else:
    print(args.text)
