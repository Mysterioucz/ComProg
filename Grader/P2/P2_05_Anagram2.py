word1 = input().strip()
word2 = input().strip()
def wcd(word):
    res = {}
    for ch in word.lower():
        if (ch not in res)and(ch.isalpha()):
            res[ch] = word.lower().count(ch)
    return res
def anagram(d_word1,d_word2):
    remove = []
    for k in d_word1:
        if k not in d_word2:
            remove.append([k,d_word1[k]])
        elif d_word1[k]>d_word2[k]:
            remove.append([k,d_word1[k]-d_word2[k]])
    return remove
def output(rem,word):
    print(word)
    if len(rem) == 0:
        print(' - None')
    else:
        for e in rem:
            if e[1] > 1:
                print(" - remove",e[1],e[0]+"'s")
            else:
                print(" - remove",e[1],e[0])
wc1 = wcd(word1)
wc2 = wcd(word2)
rem1 = anagram(wc1,wc2)
rem2 = anagram(wc2,wc1)
rem1.sort()
rem2.sort()
output(rem1,word1)
output(rem2,word2)
# print(rem1,rem2)
