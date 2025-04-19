words =open(r"/Users/sofia/Desktop/бутер/project/russian_nouns.txt", "r",  encoding="utf-8").read().split("\n")
import random
word = random.choice(words)  
death = [ "      ______",                                       
     "      |     |",
     "      0     |",
     "     /|\    |",
     "     / \    | ",
      "тупой ишак" ]
victory = [" ну я не ожидала что ты выиграешь, ты все равно маймун",
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

print('Салам Алейкум брат, деньги переводи по номеру ...')
print('крч у тебя 5 попыток угадать слово')
print('если введеной тобой буквы нет в словe, у тебя - попытка')
print('если же тебе повезло, продолжай угадывать')
print('Автор заранее приносит извинения за оскарбления или же если вы фанат русского языка примите мои извинения за грамматику')
let = []
count = 10
find = ['*'] * len(word)
print("Введите букву")
letter = input()
while '*' in find and count > 0:
    while letter in let:
        letter = input()
        print('Леее не мороси по-братски! эта буква уже была маймун')
    if letter in word:
        print('Ай тигр, правильная буква')
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
        print('Э-э хайван, ослеп что ли, не понимаешь, что в этом слове нет такой буквы?!')
        count -= 1
        print("Осталось попыток", count)
        print(*find)
        print('Ищи дальше, манг авалия')
        let.append(letter)
        if count == 0:
            print('Аста аста брат, къалкай, просто мзгов пока не хватает')
            for i in death:
                print(i)
            break

#осталось пихнкуть все в тг бота а мне в час ночи это делать лень)



