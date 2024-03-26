# HW4_Social_Media_Data

# ให้ลบบรรทัด pass แล้วแทนด้วยโค้ดของนิสิต

def social_media_data(file_in):
    file = open("/Users/chatrinyoonchalard/Documents/CU/Year 1/Com Prog/ComProg/HW/"+file_in,"r",encoding="utf8")
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
    file = open("/Users/chatrinyoonchalard/Documents/CU/Year 1/Com Prog/ComProg/HW/"+"stopwords.txt","r")
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
            for punc in '''!"$%&'()*,-./:;<=>?@[\]^_`{|}~''':
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
    return word_count_dict


def count_words_from_data_dict(data_dict, year, country, platform):
    bool_year,bool_coun,bool_plat = [year=="all",country=="all",platform=="all"]
    count_word_dict = {}
    for value in data_dict.values():
        year_data,coun,plat = value[5],value[4],value[1]
        cond = (year_data == year or bool_year) and (coun == country or bool_coun) and (plat == platform or bool_plat)
        if cond:
            count_words_from_text(count_word_dict,value[0])
    return count_word_dict
       
def top_k_words(word_count_dict, k):
    list_word = sorted(word_count_dict.items(),key=lambda x:(-x[1],x[0]))
    res,c,pre_value = [],1,list_word[0][1]
    for word,count in list_word:
        if count == pre_value:
            c += 1
            res.append(word)
        elif c <= k:
            c += 1
            pre_value = count
            res.append(word)
        else:
            break
    return res
            
def count_word_summary(file_in, file_out, k, year, country, platform):
    sum_data = top_k_words_count(count_words_from_data_dict(social_media_data(file_in),year,country,platform),k)
    filename = open(file_out,"w")
    if len(sum_data) == 0:
        filename.write("No data")
        return None
    for line in sum_data:
        filename.write(line+"\n")

# Write your functions here ONLY (If any)
def top_k_words_count(word_count_dict, k):
    list_word = sorted(word_count_dict.items(),key=lambda x:(-x[1],x[0]))
    if len(list_word)==0:
        return []
    res,c,pre_value = [],1,list_word[0][1]
    for word,count in list_word:
        if count == pre_value:
            c += 1
            res.append(word+":"+str(count))
        elif c <= k:
            c += 1
            pre_value = count
            res.append(word+":"+str(count))
        else:
            break
    return res

exec(input())


