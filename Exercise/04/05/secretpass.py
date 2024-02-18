ch_dict = {}
file = open('data.txt','r')
for line in file:
    for ch in line.strip():
        if ch not in ch_dict:
            ch_dict[ch] = 1
        else:
            ch_dict[ch] += 1
def char_amount(x):
    return ch_dict[x]
text = []
for i in range(3):
    text.append(input().strip())
text.sort(key=char_amount,reverse=True)
print("".join(text))