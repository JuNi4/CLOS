usdt = ['ɐ', 'q', 'ɔ', 'p', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ᴉ', 'ɾ', 'ʞ', 'l', 'ɯ', 'u', 'p', 'o', 'd', 'b', 'ɹ', 's', 'ʇ', 'n', 'ʌ', 'ʍ', 'x', 'ʎ', 'z', '∀', 'q', 'Ɔ', 'p', 'Ǝ', 'Ⅎ', 'פ', 'H', 'I', 'ſ', 'ʞ', '˥', 'W', 'N', 'O', 'Ԁ', 'Ò', 'ɹ', 'S', '┴', '∩', 'Λ', 'M', 'X', '⅄', 'Z', 'Ɩ', 'ᄅ', 'Ɛ', 'ㄣ', 'ϛ', '9', 'ㄥ', '8', '6', '0', "'", '؛', '˙', '‾', '¡', '¿', ',']
txt  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'd', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', ';', '.', '_', '!', '?', "'"]
print('Please input your Text to be turned upside down:')
x = input()
inp2 = list(x)
inp1 = []
inp = []
for o in range(0,len(inp2)):
    inp1.append(inp2[(len(inp2)-1)-o])

for o in inp1:
    try:
        inp.append(usdt[txt.index(o)])
    except:
        inp.append(o)

x = ''
for o in inp:
    x = x + o

print('Output: '+x)