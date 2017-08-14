import base64

for x in range(1, 600):
    pad = 16 - len(str(x))
    line = ""
    for y in range(0, pad):
        line += str(0)
    line += str(x)
    print(line)
    # print(base64.b64encode(base64.b64encode(line)))
