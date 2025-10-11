import argparse

parser = argparse.ArgumentParser(description="Calculator")
parser.add_argument("--x", type=float, required=True, help="number1")
parser.add_argument("--y", type=float, required=True, help="number2")
parser.add_argument("--operation", choices=['add', 'subtract', 'multiply', 'divide'],
                    required=True, help="Operations")
parser.add_argument("--verbose", action="store_true",
                    help="Show more details")

args = parser.parse_args()
if args.operation == "add":
    result = args.x + args.y
elif args.operation == "subtract":
    result = args.x - args.y
elif args.operation == "multiply":
    result = args.x * args.y
elif args.operation == "divide":
    if args.y != 0:
        result = args.x / args.y
    else:
        result = "Zero Division"

if args.verbose:
    print(
        f"Operation:{args.operation}, X:{args.x}, Y: {args.y}, Result:{result}")
else:
    print(result)
