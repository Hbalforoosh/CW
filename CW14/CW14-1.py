import argparse
"""Create Parser"""
parser = argparse.ArgumentParser(
    description="---Calculator---",
    epilog="CLI execution example:\n python file_name.py --value 1 2 3")
# subparser = parser.add_subparsers(dest="command")
# add_parser = subparser.add_parser(
#     "calc", help="Calculate the sum, average, and maximum value")
parser.add_argument("--value", nargs='+', type=float,
                    required=True, help=" enter your numbers")
args = parser.parse_args()
# if args.command == "calc":
#     list_value = args.value
#     total = sum(list_value)
#     avg = total / len(list_value)
#     maximum = max(list_value)
#     print(f"Sum: {total}")
#     print(f"Average: {avg}")
#     print(f"Maximum: {maximum}")
# else:
#     parser.print_help()

if args.value:
    list_value = args.value
    total = sum(list_value)
    avg = total / len(list_value)
    maximum = max(list_value)
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {maximum}")
else:
    parser.print_help()
