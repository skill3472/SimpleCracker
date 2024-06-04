import hashlib
import argparse
import re

parser = argparse.ArgumentParser(
    prog='numcracker',
    description='Crack simple number hashes. Made by skill347'
)

parser.add_argument("range", type=str, help="Range of numbers to crack. Example: 100-250")
parser.add_argument("expression", type=str, help="RegEx expression to match.")
parser.add_argument("--mode", "-m", type=str, help="Select the hashing algorithm. Default is SHA512.",
                    default="sha512", choices=["sha512", "sha256", "sha1", "md5"])
parser.add_argument("--out", "-o", type=str, help="Output filename.")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose mode.")
parser.add_argument("--leading", "-l", type=int, help="Target number length (will add leading zeros).")

args = parser.parse_args()
startPos = int(args.range.split('-')[0])
endPos = int(args.range.split('-')[1])
exp = re.compile(args.expression)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def HashNumber(number, mode="sha512") -> str:
    mode = mode.lower()
    if mode not in hashlib.algorithms_available:
        raise ValueError("Hashing algorithm not supported on this version of the Python interpreter.")

    if args.leading is not None:
        zerosToAdd = args.leading - len(str(number))
        if zerosToAdd > 0:
            numberStr = zerosToAdd*"0" + str(number)
        else:
            numberStr = str(number)
    else:
        numberStr = str(number)

    match mode:
        case "sha512":
            return hashlib.sha512(numberStr.encode()).hexdigest()
        case "sha256":
            return hashlib.sha256(numberStr.encode()).hexdigest()
        case "sha1":
            return hashlib.sha1(numberStr.encode()).hexdigest()
        case "md5":
            return hashlib.md5(numberStr.encode()).hexdigest()
        case _:
            raise ValueError("Hashing mode does not exist, or is not supported.")


found = []
for i in range(startPos, endPos + 1):
    if args.verbose:
        print(f"Cracking number {i}/{endPos}...")
    res = HashNumber(i, args.mode)
    if re.match(exp, res):
        if args.out:
            with open(args.out, 'w') as f:
                f.write(str(i))
                f.write("\n")
                f.close()
        found.append(str(i))

if found:
    print(f"{bcolors.OKGREEN}Numbers that match the provided expression: {found}{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}No numbers that match the provided expression have been found.{bcolors.ENDC}")
