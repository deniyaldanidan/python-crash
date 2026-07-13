import argparse

parser = argparse.ArgumentParser(description="String Formatter")
# Positional Arguments
parser.add_argument("echo", help="Echo this argument in command line", type=str)

# Optional Flags
parser.add_argument("-j", "--join", type=str, help="Join element", default=" ")

# Optional Flags
parser.add_argument(
    "-r", "--r", help="How many times it needs to be repeated?", default=1, type=int
)

# Optional Flags - With 1 or more inputs
parser.add_argument(
    "-st", "--start", nargs="+", help="Additional strings in the start", default=[]
)
# Optional Flags - With 0 or more inputs
parser.add_argument(
    "-e", "--end", nargs="*", help="Additional strings in the end", default=[]
)


# Mutually Exclusive Arguments - If user provided both, script will fail
group = parser.add_mutually_exclusive_group()

# Mutually Exclusive Optional Flags - Switches (Boolean)
group.add_argument(
    "-up",
    "--upper",
    help="Turn the string into UPPERCASE",
    default=False,
    action="store_true",
)
# Mutually Exclusive Optional Flags - Restricted Choices
group.add_argument(
    "-op",
    "--operation",
    help="What operation needed?",
    choices=["upper", "lower", "capitalize", "none"],
    default="none",
)


args = parser.parse_args()

# print(args)

# python argparse_mod_trials/trial_1.py "Hello" -j "-" -r 2 -op "upper" -st "world" "." -e ". " "Hello Everyone"

# Formatting Strings

echo_string: str = args.echo

if len(args.start):
    echo_string = f"{" ".join(args.start)} {echo_string}"

if len(args.end):
    echo_string = f"{echo_string} {" ".join(args.end)}"

echo_string = f"{args.join}".join([echo_string for _ in range(args.r)])

if args.upper:
    echo_string = echo_string.upper()

match args.operation:
    case "upper":
        echo_string = echo_string.upper()
    case "lower":
        echo_string = echo_string.lower()
    case "capitalize":
        echo_string = echo_string.capitalize()


print(echo_string)

# python argparse_mod_trials/trial_1.py World -r 2 -j "-" -st "Hey," "Hello" -e "Hello" "Everyone" -op "capitalize"
# Hey, hello world hello everyone-hey, hello world hello everyone

# print(
#     f"Echo: {" ".join([args.echo.upper() if args.upper else args.echo for _ in range(args.r)])}"
# )


# type=int    --retries 3 args.retries = 3 (Integer)
# action="store_true" --force args.force = True (Boolean)
# action="store_false"--no-cacheargs.cache = False (Boolean)
# default="main" (Flag left out) args.value = "main"
# required=True  --key 123   Forces an optional flag to become mandatory
# nargs="+"  --items a b   cargs.items = ['a', 'b', 'c'] (List)
