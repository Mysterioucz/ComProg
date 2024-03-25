# HW4_Social_Media_Data

# ให้ลบบรรทัด pass แล้วแทนด้วยโค้ดของนิสิต

def social_media_data(file_in):
    file = open(file_in,"r",encoding="utf8")
    data = {}
    lines = [e.strip().split(',') for e in file.readlines()][1:]
    if len(lines) <= 1:
        file.close()
        return data
    for line in lines:
        data[line[0]] = [e.strip() for e in [line[1],line[5]]]+[int(num) for num in line[6:8]]+[e.strip() for e in line[8:10]]
    file.close()
    return data

def is_stopword(word):
    if not word.isalpha():
        for punc in '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''':
            word.replace(punc,"")
    else:
        word = word.lower()
    file = open("stopwords.txt","r")
    lines = []
    for e in file.readlines():
        lines += e.strip().split(", ")
    lines = [e.strip() for e in lines]
    return word in lines

def count_words_from_text(word_count_dict, text):
    list_text = text.split()
    for word in list_text:
        if word.isalpha() :
            word = word.lower()
            if not is_stopword(word) :
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
        else:
            for punc in '''!"$%&'()*+,-./:;<=>?@[\]^_`{|}~''':
                if punc in word:
                    word = word.replace(punc,"")
            if "#" in word:
                word = word[0]+word[1:].lower()
            else:
                word = word.lower()
            if not is_stopword(word) :
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
    print(word_count_dict)
    return word_count_dict


def count_words_from_data_dict(data_dict, year, country, platform):
    pass


def top_k_words(word_count_dict, k):
    pass


def count_word_summary(file_in, file_out, k, year, country, platform):
    pass

# Write your functions here ONLY (If any)
exec(input())


