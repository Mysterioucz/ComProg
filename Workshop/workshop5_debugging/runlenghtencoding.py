# Run length encoding
# จงเขียนฟังก์ชั่นบีบอัดข้อความสาย DNA ที่มีแค่ ATCG (ตัวใหญ่หรือตัวเล็กก็ได้) เท่านั้น

def encode(inputstring):
# encode จะบีบอัดข้อความ (string) โดยนับจำนวนตัวอักษรที่ติดกันและแทนด้วยตัวเลข
# รับข้อมูลเป็น string ที่ประกอบด้วย ATCG (ตัวใหญ่หรือตัวเล็กก็ได้)
# และคืนค่าเป็น string ที่เป็นตัวใหญ่และตัวเลขเท่านั้น
# ถ้าข้อมูล inputstring ไม่ถูกต้องให้คืนว่า "ERROR"
# ตัวอย่าง
# "AAAA" -> "A4"
# "aAAACTGG" -> "A4CTG2"
# "CATS" -> "ERROR"
  outputstring = ""
  dna = inputstring.upper()
  c = 1
  for i in range(len(dna)):
    if dna[i] in "ATCG":
      if i != len(dna)-1:
          if dna[i] == dna[i+1]:
            c += 1
          else:
            if c != 1:
              outputstring += dna[i] + str(c)
              c = 1
            else:
              outputstring += dna[i]
            
      else:
        if dna[i] != dna[i-1]:
           outputstring += dna[i]
        else:
          if c!=1:
            outputstring += dna[i] + str(c)
          else:
            outputstring += dna[i]
    else:
      return "ERROR"
  return outputstring
      
  # for ch in inputstring.upper():
  #   if ch not in char:
  #     if ch in "ATCG":
  #       char += ch
  #     else:
  #       return "ERROR"
  # for ch in char:
  #   outputstring += ch + str(inputstring.upper().count(ch))
  # return outputstring.replace("1","")


def decode(inputstring):
# decode จะย้อนกลับกระบวนการของ encode
# รับข้อมูลเป็น string ที่ประกอบด้วย ATCG และตัวเลข (ตัวใหญ่หรือตัวเล็กก็ได้)
# และคืนค่าเป็น string ที่เป็นตัวใหญ่ ATCG เท่านั้น
# ถ้าข้อมูล inputstring ไม่ถูกต้องให้คืนว่า "ERROR"
# ตัวอย่าง
# "A4" -> "AAAA"
# "AAC4G" -> "ERROR" (ไม่ควรมี AA ติดกันจากกระบวนการ encode)
# "a4CtG2" -> "AAAACTGG"
# "ERROR" -> "ERROR"
  outputstring = " "
  for i in range(len(inputstring)):
    if inputstring[i].isalpha():
      if inputstring[i].upper() in "ATCG":
        if i != len(inputstring)-1 :
          if inputstring[i+1].isnumeric():
            if inputstring[i] != outputstring[-1]:
              try:
                outputstring += inputstring[i].upper()*int(inputstring[i+1:i+3])
              except:
                outputstring += inputstring[i].upper()*int(inputstring[i+1])
            else:
              return "ERROR"
          elif inputstring[i].upper() != inputstring[i+1].upper():
            if inputstring[i] != outputstring[-1]:
              outputstring += inputstring[i].upper()
            else:
              return "ERROR"
          else:
            return "ERROR"
        else:
          if inputstring[i] != outputstring[-1]:
              outputstring += inputstring[i].upper()
          else:
              return "ERROR"
      else:
        return "ERROR"
    elif not inputstring[max(i-1,0)].isalpha() and not inputstring[max(i-2,0)].isalpha():
      return "ERROR"

  return outputstring.strip()

#ให้เขียน test case สำหรับทดสอบคำสั่ง encode และ decode อย่างละ 10 test case
# เราจะใช้คำสั่ง assert https://www.w3schools.com/python/ref_keyword_assert.asp
#ตัวอย่างการใช้งาน
# assert encode("ASDF") == "" #ตอน function เปล่าๆ บรรทัดนี้จะไม่เกิดอะไรขึ้น
# assert decode("") == "asdf" #เมื่อปรับ function แล้ว บรรทัดนี้จะเกิด AssertionError

# เขียน test case encode สิบอันด้านล่าง
assert encode("aaaaa") == "A5"
assert encode("AACCGGTT") == "A2C2G2T2"
assert encode("ATTCG") == "AT2CG"
assert encode("ATCG") == "ATCG"
assert encode("AATCG") == "A2TCG"
assert encode("ATCCG") == "ATC2G"
assert encode("ATCGG") == "ATCG2"
assert encode("") == ""
assert encode("ASDF") == "ERROR"
assert encode("AAATTTGGGFFF") == "ERROR"

# เขียน test case decode สิบอันด้านล่าง
assert decode("A5") == "AAAAA"
assert decode("A2C2G2T2") == "AACCGGTT"
assert decode("AT2CG") == "ATTCG"
assert decode("A2TCG") == "AATCG"
assert decode("ATC2G") == "ATCCG"
assert decode("ATCG2") == "ATCGG"
assert decode("") == ""
assert decode("AAAAA") == "ERROR"
assert decode("ARCGGG") == "ERROR"
assert decode("FF") == "ERROR"
assert decode("A2A3") == "ERROR"
assert decode("A10") == "AAAAAAAAAA"
assert decode("1A") == "ERROR"
assert decode("A0") == ""
assert decode("TC2A20") == "TCC"+"A"*20
# assert decode("T1010C123") == "T"*1010 + "C"*123
# exec(input().strip())