from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

KV = """
MyBL
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x":0.5, "center_y":0.5}
        
        Label:
                frontsize: "50sp"
                text: root.data_label0
        Label:
                frontsize: "50sp"
                text: root.data_label01        
        TextInput:
                id: Inp1
                multiline: False
                padding_y: (5,5)
                size_hint: (1, 0.4)
                on_text: app.zalupa()        
        Label:
                frontsize: "50sp"
                text: root.data_label1
        Label:
                frontsize: "50sp"
                text: root.data_label12 
                
        TextInput:
                id: Inp2
                multiline: False
                padding_y: (5,5)
                size_hint: (1, 0.4)
                on_text: app.opentxt()    
                      
        Label:
                frontsize: "50sp"
                text: root.data_label2
                
        Label:        
                frontsize: "50sp"
                text: root.data_label21
          
                
        TextInput:
                id: Inp3
                multiline: False
                padding_y: (5,5)
                size_hint: (1, 0.4)
                on_text: app.closetxt()  
        
                                             
        Button:
                text: "Ввод ключа"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.key()
        Button:
                text: "Зашифррование"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.cripto()
        Button:
                text: "Расшифование"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.anticripto()
                
"""
key = 0
opentxt = 0
keystr0 = [0]
closetxt = 0
class MyBL(BoxLayout):
    data_label0 = StringProperty("Введите 64 значный ключ шифрования")
    data_label1 = StringProperty("Введите текст для зашифррования размером не более 64")
    data_label2 = StringProperty("Введите текст для расшифрования")
    data_label21 = StringProperty(" ")
    data_label12 = StringProperty(" ")
    data_label01 = StringProperty(" ")

    indexw = 0
    def key(self):
        global key
        vsesimv = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u",
                   "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                   "P",
                   "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "А",
                   "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
                   "Х",
                   "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и",
                   "й",
                   "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э",
                   "ю",
                   "я", " ", ".", ",", "?", "!", '"', ":", "-", "(", ")", ]
        keystr1 = []
        global keystr0
        keystr0.remove(0)
        keystr1 = key
        b = len(keystr1)
        print(b)
        for i in range(b):
            keystr0.append(vsesimv.index(keystr1[i]))
        if len(keystr1) == 64:
            self.data_label01 = "ключ успешно введен"
            indexw = 1
        else:
            self.data_label01 = "введен не корректный ключ"


    def cripto(self):
        global keystr0
        vsesimv = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u",
                   "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                   "P",
                   "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "А",
                   "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
                   "Х",
                   "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и",
                   "й",
                   "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э",
                   "ю",
                   "я", " ", ".", ",", "?", "!", '"', ":", "-", "(", ")", ]
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
            self.data_label12 = ("Зашифрованный текст:")+(''.join(closetxtstr0))
            print (''.join(closetxtstr0))


    def anticripto(self):
        global keystr0
        vsesimv = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u",
                   "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                   "P",
                   "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "А",
                   "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
                   "Х",
                   "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и",
                   "й",
                   "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э",
                   "ю",
                   "я", " ", ".", ",", "?", "!", '"', ":", "-", "(", ")", ]
        global closetxt
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
        self.data_label21 = ("Открытый текст:") + (''.join(opentxtstr))

class MyApp(App):
    runningg = True

    def zalupa(self):
        global key
        key = self.root.ids.Inp1.text
        print(key)
    def opentxt(self):
        global opentxt
        opentxt = self.root.ids.Inp2.text

    def closetxt(self):
        global closetxt
        closetxt = self.root.ids.Inp3.text
    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.runningg = False

MyApp().run()
