# Convert Decimal to Hexadecimal and vice versa
import os
import sys
import json

hexchars = ["a","b","c","d","e","f"]

# Hex to Base 10
def from_hex(hex):
    # Convert Hex string to list
    hex = list(hex)
    base10 = 0
    # For each letter in hex list
    for i in range(len(hex)):
        # If letter is a charactar
        if hex[i].lower() in hexchars:
            # Convert it to number
            hex[i]=10+hexchars.index(hex[i].lower())
        i = i+1
        # Get the position of the digit
        pos = len(hex)-i
        # Get the exponent
        hexm = 16**pos
        i = i-1
        #Pultiply the digit by 16 to the exponent
        base10 += int(hex[i])*hexm
    # return base10
    return base10

# To Hex
def to_hex(b10):
    b102= int(b10)
    # Hex String
    hex = ""
    # Base 10 to Number
    b10 = int(b10)
    x = True
    # While b10 is greater than 0
    while x:
        # Get Remainder & Quotient
        quotient = b10//16
        remainder = b10%16
        # If remainder is less than 10
        if remainder < 10:
            # Add remainder to hex
            hex = str(remainder) + hex
        # If remainder is greater than 10
        else:
            # Add remainder as Letter to hex
            hex = hexchars[remainder-10] + hex
        # Set b10 to quotient
        b10 = quotient
        # If b10 is 0
        if quotient == 0 and b102 > 0:
            # Exit Loop
            x = False
        elif b102 <= 0:
          return '0'
    # Return Hex
    return hex.upper()

# add ../libs to path
f = open(os.path.dirname(os.path.relpath(__file__))+'/dirs.json', 'r')
dirs = json.loads(f.read())
f.close()

sys.path.append(dirs['LIB_DIR'])

# Import ARGS
import args

args.add_arg('-d', args.ARG_OPTIONAL, None, True, '--decimal', 'Decimal to Hex')
args.add_arg('-h', args.ARG_OPTIONAL, None, True, '--hex', 'Hex to Decimal')

if args.get_arg('-d', sys.argv)!=None:
    print('0x'+str(to_hex(args.get_arg('-d', sys.argv))).lower())
elif args.get_arg('-h', sys.argv)!=None:
    if args.get_arg('-h', sys.argv).startswith('0x'):
        print(from_hex(args.get_arg('-h', sys.argv)[2:]))
    else:
        print(from_hex(args.get_arg('-h', sys.argv)))
else:
    print("No Argument Given")
