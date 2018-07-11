
import helper
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--num1", help = "Enter num1: ")
parser.add_argument("--num2", help = "Enter num2: ")

args = parser.parse_args()

print(helper.add(int(args.num1),int(args.num2)))




### END CODE