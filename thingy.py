import sys

def main(args):
    numbers = []
    for arg in args:
        numbers += [int(c) for c in iter(arg) if c in '1234567890']
    return 1.0*sum(numbers)/len(numbers)

print main(sys.argv[1:])
