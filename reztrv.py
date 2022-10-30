vsesimv = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I","J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7","8", "9", "А","Б","В","Г","Д","Е","Ё","Ж","З","И","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я", "а", "б", "в", "г", "д", "е","ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " ", ".", ",", "?", "!", '"', ":", "-", "(", ")", ]
indexw = 0
while indexw == 0:
    print("Введите 64 значный буквенно цифрровой ключ")
    key = input()
    keystr1 = []
    keystr0 = [0]
    keystr0.remove(0)
    keystr1 = key
    b = len(keystr1)
    for i in range(b):
        keystr0.append(vsesimv.index(keystr1[i]))

    if len(keystr1) == 64:
        print ("ключ успешно введен")
        indexw = 1
    else:
        print ("введен не корректный ключ")

indexw = "0"
while indexw == "0":
    print("Если вы желаете зашифрровать сообщение нажмите 1, если расшифрровать полученное сообщение нажмите 0")
    index = input()
    if index == "1":
        print("Введите буквенно-цифровое сообщение не длинее 64 знаков без специальных знаков")
        opentxt = input()
        opentxtstr0 = [0]
        opentxtstr0.remove(0)
        opentxtstr1 = opentxt
        j = len(opentxtstr1)
        if j > 64:
            print("Введённое сообщение слишком длинное")
        else:
            for i in range(j):
                opentxtstr0.append(vsesimv.index(opentxtstr1[i]))
            print(opentxtstr0)
            closetxtstr0 = [0]
            closetxtstr0.remove(0)
            for i in range(j):
                closetxt = opentxtstr0[i] + keystr0[i]
                if closetxt > 136:
                    closetxt = closetxt - 137
                closetxtstr0.append(closetxt)
            for i in range(j):
                closetxtstr0[i] = vsesimv[closetxtstr0[i]]
            print("Зашифрованный текст:")
            print(''.join(closetxtstr0))

    if index == "0":
        print("Введите зашифрованное сообщение")
        closetxt = input()
        closetxtstr0 = [0]
        closetxtstr0.remove(0)
        closetxtstr1 = closetxt
        j = len(closetxtstr1)
        for i in range(j):
            closetxtstr0.append(vsesimv.index(closetxtstr1[i]))
        opentxtstr = [0]
        opentxtstr.remove(0)
        opentxt = 0
        for i in range(j):
            opentxt = closetxtstr0[i] - keystr0[i]
            if opentxt < 0:
                opentxt = opentxt + 137
            opentxtstr.append(opentxt)
        for i in range(j):
            opentxtstr[i] = vsesimv[opentxtstr[i]]
        print("Открытый текст:")
        print(''.join(opentxtstr))


    if index != "1" and index != "0":
        print("вы ввели не корректное значение")
