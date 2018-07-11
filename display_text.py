
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--text", help = "enter some text here in quotes ")
parser.add_argument("--verbose",action = "store_true", help = "enter verbose to set to true")

args = parser.parse_args()


if args.verbose == True: 
    print("args.text = ", args.text, " args.verbose = ", args.verbose)
if args.text != None:
    print(args.text)
else:
    print("No text provided")



### END CODE