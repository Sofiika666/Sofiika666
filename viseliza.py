words =open(r"/Users/sofia/Desktop/бутер/project/russian_nouns.txt", "r",  encoding="utf-8").read().split("\n")
import random
word = random.choice(words)  
death = [ "      ______",                                       
     "      |     |",
     "      0     |",
     "     /|\    |",
     "     / \    | ",
      "тупой ишак" ]
victory = [" ну я не ожидала что ты выиграешь)",
           "ну так уж и быть",
           "　　　　　　　　 　　　　　　   ／ ¯¯｀フ",
           "　　　　　　　　　,　'' ｀ ｀ / 　 　 　 !　 　",
           "　　　　　　　 , ' 　　　　 レ　 _,　 -' ミ",
           "　　　　　　　 ; 　 　 　 　 　`ミ __,xノﾞ､",
           "　　　 　　 　 i　 　　　ﾐ　　　; ,､､､、　ヽ ¸",
           "　　　 　　,.-‐! 　 　 　 ﾐ　　i　　　｀ヽ.._,,))",
           "　　 　　//´｀｀､　　　　 ミ　ヽ　　　　　(¯`v´¯)",
           "　　　　| l　　 　｀ ｰｰ -‐''ゝ､,,)).    ..`·.¸.·´",
           "　　　 　ヽ.ー─'´)　",
           "Ты такой же сладкий как этот котик)"]
print('Привет! Ты находишься в игре "Виселица"')
print('У тебя 5 попыток угадать слово')
print('Если введеной тобой буквы нет в словe, у тебя - попытка')
print('Если же тебе повезло, продолжай угадывать')
let = []
count = 10
find = ['*'] * len(word)
print("Введите букву")
letter = input()
while '*' in find and count > 0:
    while letter in let:
        letter = input()
        print('Прости, эта буква уже была( Попробуй еще раз.')
    if letter in word:
        print('Молодец) Это буква есть в загаданном слове.')
        let.append(letter)
        for i in range(len(word)):
            if word[i] == letter:
                find[i] = letter
        print(*find)
        if '*' not in find:
            for i in victory:
                print(i)
            break
    else:
        print('Тебе не повезло, этой буквы нет в загаданном слове, у тебя минус попытка.')
        count -= 1
        print("Осталось попыток", count)
        print(*find)
        print('Гадай дальше)')
        let.append(letter)
        if count == 0:
            print('Прости, но не в этот раз!')
            for i in death:
                print(i)
            break



