import sys

text = ''
if len(sys.argv) > 1:
    for word in range(1, len(sys.argv)):
        if word != len(sys.argv)-1:
            text += f'{sys.argv[word]} '
        else:
            text += sys.argv[word]
else:
    print("please enter a word or sentence to reverse")

text = list(text)

result = []
while len(text) > 0:
    result.append(text[len(text)-1])
    text.pop(len(text)-1)

display = ''.join(result)

print(display)