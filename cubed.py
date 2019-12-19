def hangman(word):
    wrong = 0                   #間違えた回数
    stages = ["",               #ハングマン
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)       #wordの文字を1文字ずつの要素に分解してリスト
    board = ["_"] * len(word)  #どの文字が正解しているか
    win = False                 #
    print("ハングマンへようこそ!") #

    while wrong < len(stages) - 1: #ループ、間違えた回数がstagesの行数を超えたら終了
        print("\n")                #見やすくするため改行
        msg = "1文字を予想してね"     #
        char = input(msg)          #答えをcharに保存
        if char in rletters:       #rlettersにcharsの文字がある場合は実行(True・正解)
            cind = rletters.index(char) #cindに正解した文字のリスト値を保存
            board[cind] = char        #boardの指定リスト(cind)に正解した文字を入れる
            rletters[cind] = '$'   #答えに複数同じ文字が含まれている場合の為"$"に置き換え
        else:
            wrong += 1             #間違えたらwrongに1加算
        print((" ".join(board)))   #
        e = wrong + 1              #
        print("\n".join(stages[0: e])) #
        if "_" not in board:      #
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:                    #TrueかFalseかで返している普通なら演算子?使うけど変な感じ
        print("\n".join(stages[0: wrong+1]))
        print("あなたの負け!正解は{}.".format(word))


import random

Word_List = ["Python", "Java", "C+", "Rsta"] #アルファベットのリスト
letters = random.choice(Word_List) #指定された文字数を選ぶ

hangman(letters)  #hangman関数の実行
