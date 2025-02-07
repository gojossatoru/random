lang=input('ru/en:  ')
code=input('шифр/дешифр:  ')
num=int(input('шаг:  '))
text=input('текст:  ')
text1=''
enalp='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy'
enalp2='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY'
rualp='абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэю'
rualp2='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ'
if lang == 'en':
    if code == 'шифр':
        for i in range(len(text)):
            if text[i] in enalp:
                letter=enalp[enalp.find(text[i]) + num]
                text1 += letter
                continue
            if text[i] in enalp2:
                letter=enalp2[enalp2.find(text[i]) + num]
                text1 += letter
                continue
            else:
                letter=text[i]
                text1 += letter
    if code == 'дешифр':
        for i in range(len(text)):
            if text[i] in enalp:
                letter=enalp[enalp.rfind(text[i]) - num]
                text1 += letter
                continue
            if text[i] in enalp2:
                letter=enalp2[enalp2.rfind(text[i]) - num]
                text1 += letter
                continue
            else:
                letter=text[i]
                text1 += letter

if lang == 'ru':
    if code == 'шифр':
        for i in range(len(text)):
            if text[i] in rualp:
                letter=rualp[rualp.find(text[i]) + num]
                text1 += letter
                continue
            if text[i] in rualp2:
                letter=rualp2[rualp2.find(text[i]) + num]
                text1 += letter
                continue
            else:
                letter=text[i]
                text1 += letter
    if code == 'дешифр':
        for i in range(len(text)):
            if text[i] in rualp:
                letter=rualp[rualp.rfind(text[i]) - num]
                text1 += letter
                continue
            if text[i] in rualp2:
                letter=rualp2[rualp2.rfind(text[i]) - num]
                text1 += letter
                continue
            else:
                letter=text[i]
                text1 += letter
        
print(text1)
            