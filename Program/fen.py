import tkinter, re
from tkinter import *
from collections import Counter

# --------------------------------------------------------------------------------------------------------------------------------------------

boardImg = 'board.png'
pieces = dict()
pieces['p'] = 'bp.png'
pieces['P'] = 'wp.png'
pieces['b'] = 'bb.png'
pieces['B'] = 'wb.png'
pieces['n'] = 'bn.png'
pieces['N'] = 'wn.png'
pieces['r'] = 'br.png'
pieces['R'] = 'wr.png'
pieces['q'] = 'bq.png'
pieces['Q'] = 'wq.png'
pieces['k'] = 'bk.png'
pieces['K'] = 'wk.png'
wrong = 'wrong.png'
checkImg = 'check.png'
correct = TRUE
correctCastling = TRUE
validChars = ['p', 'P', 'b', 'B', 'n', 'N', 'r', 'R', 'q', 'Q', 'k', 'K']
checked = [0, 0]
fullPiecesCount = 0

board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]

startBoard = [
    ['r','n','b','q','k','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ['P','P','P','P','P','P','P','P'],
    ['R','N','B','Q','K','B','N','R']
    ]

boardErr = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]

boardCh = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]

# --------------------------------------------------------------------------------------------------------------------------------------------

def countPieces():
    vcs = ['p', 'P', 'bb', 'bw', 'Bb', 'Bw', 'n', 'N', 'r', 'R', 'q', 'Q', 'k', 'K']
    countAll = 0
    count = dict()
    count['p'] = 0
    count['P'] = 0
    count['bb'] = 0
    count['bw'] = 0
    count['Bb'] = 0
    count['Bw'] = 0
    count['n'] = 0
    count['N'] = 0
    count['r'] = 0
    count['R'] = 0
    count['q'] = 0
    count['Q'] = 0
    count['k'] = 0
    count['K'] = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[j][i] in validChars):
                if board[j][i] in ['b', 'B']:
                    if (j + i) % 2 == 0:
                        count[board[j][i] + 'w'] += 1
                    else:
                        count[board[j][i] + 'b'] += 1
                else:
                    count[board[j][i]] += 1
                countAll += 1
    for vc in vcs:
        #print(vc + ' -> ' + str(count[vc]))
        if(vc in ['p', 'P'] and count[vc] > 8):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[j][i] == vc):
                        boardErr[j][i] = 1
        if(vc in ['k', 'K'] and count[vc] != 1):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[j][i] == vc):
                        boardErr[j][i] = 1
        if(vc in ['n', 'r'] and count[vc] > 2 and count['p'] > 10 - count[vc]):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[j][i] == vc):
                        boardErr[j][i] = 1
        if(vc in ['N', 'R'] and count[vc] > 2 and count['P'] > 10 - count[vc]):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[j][i] == vc):
                        boardErr[j][i] = 1
        if(vc in ['q', 'bb', 'bw'] and count[vc] > 1 and count['p'] > 9 - count[vc]):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if len(vc) == 1 and board[j][i] == vc:
                        boardErr[j][i] = 1
                    elif board[j][i] == vc[0] and ((vc[1] == 'w' and (j + i) % 2 == 0) or (vc[1] == 'b' and (j + i) % 2 == 1)):
                        boardErr[j][i] = 1
        if(vc in ['Q', 'Bb', 'Bw'] and count[vc] > 1 and count['P'] > 9 - count[vc]):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if len(vc) == 1 and board[j][i] == vc:
                        boardErr[j][i] = 1
                    elif board[j][i] == vc[0] and ((vc[1] == 'w' and (j + i) % 2 == 0) or (vc[1] == 'b' and (j + i) % 2 == 1)):
                        boardErr[j][i] = 1
        if vc in ['k', 'K']:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[j][i] == vc:
                        for k in range(i - 1, i + 2):
                            for l in range(j - 1, j + 2):
                                if k in range(0, 7) and l in range(0, 7):
                                    if (vc == 'k' and board[l][k] == 'K') or (vc == 'K' and board[l][k] == 'k'):
                                        boardErr[l][k] = 1
    for i in range(len(board[0])):
        for j in [0, 7]:
            if board[j][i] in ['p', 'P']:
                boardErr[j][i] = 1
    return countAll

def checkIfChecking(fig, y, x, chk):
    checkedFig = chk.copy()
    if fig in ['p', 'n', 'b', 'r', 'q']:
        target = 'K'
    elif fig in ['P', 'N', 'B', 'R', 'Q']:
        target = 'k'
    if fig in ['p', 'P']:
        if fig == 'p':
            xy = [
                [x - 1, y + 1],
                [x + 1, y + 1]
                ]
        else:
            xy = [
                [x - 1, y - 1],
                [x + 1, y - 1]
                ]
        for ij in xy:
            j = ij[1]
            i = ij[0]
            if(i >= 0 and i <= 7 and j >= 0 and j <= 7):
                #boardCh[j][i] = 1
                if board[j][i] == target:
                    boardCh[j][i] = 1
                    if target == 'k':
                        checkedFig[1] = 1
                    else:
                        checkedFig[0] = 1
    elif fig in ['n', 'N']:
        xy = [
            [x + 1, y + 2],
            [x + 2, y + 1],
            [x + 2, y - 1],
            [x + 1, y - 2],
            [x - 1, y - 2],
            [x - 2, y - 1],
            [x - 2, y + 1],
            [x - 1, y + 2]
            ]
        for ij in xy:
            j = ij[1]
            i = ij[0]
            if(i >= 0 and i <= 7 and j >= 0 and j <= 7):
                #boardCh[j][i] = 1
                if board[j][i] == target:
                    boardCh[j][i] = 1
                    if target == 'k':
                        checkedFig[1] = 1
                    else:
                        checkedFig[0] = 1
    elif fig in ['r', 'R']:
        xy = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
            ]
        for move in xy:
            j = y + move[1]
            i = x + move[0]
            if j in range(8) and i in range(8):
                while board[j][i] == 0:
                    j += move[1]
                    i += move[0]
                    if j not in range(8) or i not in range(8):
                        break
            if j in range(8) and i in range(8):
                if board[j][i] == target:
                    boardCh[j][i] = 1
                    if target == 'k':
                        checkedFig[1] = 1
                    else:
                        checkedFig[0] = 1
    elif fig in ['b', 'B']:
        xy = [
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1]
            ]
        for move in xy:
            j = y + move[1]
            i = x + move[0]
            if j in range(8) and i in range(8):
                while board[j][i] == 0:
                    j += move[1]
                    i += move[0]
                    if j not in range(8) or i not in range(8):
                        break
            if j in range(8) and i in range(8):
                if board[j][i] == target:
                    boardCh[j][i] = 1
                    if target == 'k':
                        checkedFig[1] = 1
                    else:
                        checkedFig[0] = 1
    elif fig in ['q', 'Q']:
        xy = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1]
            ]
        for move in xy:
            j = y + move[1]
            i = x + move[0]
            if j in range(8) and i in range(8):
                while board[j][i] == 0:
                    j += move[1]
                    i += move[0]
                    if j not in range(8) or i not in range(8):
                        break
            if j in range(8) and i in range(8):
                if board[j][i] == target:
                    boardCh[j][i] = 1
                    if target == 'k':
                        checkedFig[1] = 1
                    else:
                        checkedFig[0] = 1
    return checkedFig

# --------------------------------------------------------------------------------------------------------------------------------------------

fen = input('Podaj zapis w notacji FEN: ').split(' ')
if(len(fen) != 6):
    correct = FALSE
    print('Błąd w zapisie')

# Ustawienie bierków

if(correct):
    row = fen[0].split('/')
    if(len(row) != 8):
        correct = FALSE
        print('Błąd w zapisie - niewłaciwy rozmiar planszy')
    else:
        kcnt = 0
        Kcnt = 0
        for r in row:
            if 'k' in r:
                kcnt += 1
            if 'K' in r:
                Kcnt += 1
        if kcnt == 0:
            correct = FALSE
            print('Błąd w zapisie - brak czarnego króla')
        if Kcnt == 0:
            correct = FALSE
            print('Błąd w zapisie - brak białego króla')
        if(correct):
            for r in range(len(row)):
                rowLen = 0
                for i in range(len(row[r])):
                    if(row[r][i] in validChars):
                        rowLen += 1
                        board[r][rowLen - 1] = row[r][i]
                    elif(int(row[r][i]) in [1,2,3,4,5,6,7,8]):
                        rowLen += int(row[r][i])
                if(rowLen != 8):
                    correct = FALSE
                    print('Błąd w zapisie - niewłaciwy rozmiar planszy')
                    break
                
if correct:
    whitePawns = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
    blackPawns = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
    for i in range(8):
        for j in range(1, 7):
            if board[j][i] == 'P':
                whitePawns[6 - j][i] = 1
    for i in range(8):
        for j in range(1, 7):
            if board[j][i] == 'p':
                blackPawns[j - 1][i] = 1
    
    for i in range(8):
        for j in range(1, 6):
            if whitePawns[j][i] == 1:
                start = i - j
                if start < 0:
                    start = 0
                stop = j + i
                if stop > 7:
                    stop = 7
                test = TRUE
                for k in range(start, stop + 1):
                    if whitePawns[0][k] == 0:
                        whitePawns[0][k] = str(j) + str(i)
                        test = FALSE
                        break
                if test:
                    boardErr[6 - j][i] = 1
    
    for i in range(8):
        for j in range(1, 6):
            if blackPawns[j][i] == 1:
                start = i - j
                if start < 0:
                    start = 0
                stop = j + i
                if stop > 7:
                    stop = 7
                test = TRUE
                for k in range(start, stop + 1):
                    if blackPawns[0][k] == 0:
                        blackPawns[0][k] = str(j) + str(i)
                        test = FALSE
                        break
                if test:
                    boardErr[1 + j][i] = 1

# Ruch

if(correct):
    fullPiecesCount = countPieces()
    for i in range(len(board)):
        for j in range(len(board[i])):
            checked = checkIfChecking(board[j][i], j, i, checked)
    if checked[0] == checked[1] == 1:
        print('Błąd w zapisie - obaj króle szachowani')
    elif (fen[1] == 'w' and checked[1] == 1) or (fen[1] == 'b' and checked[0] == 1):
        print('Błąd w zapisie - niewłaciwe oznaczenie kolejności ruchu')
    elif(fen[1] == 'w'):
        print('Białe są na ruchu')
    elif(fen[1] == 'b'):
        print('Czarne są na ruchu')
    else:
        print('Błąd w zapisie - niewłaciwe oznaczenie kolejności ruchu')

# Roszady
        
if(correct):
    castling = fen[2]
    if(len(castling) > 4 or (len(castling) > 1 and '-' in castling)):
        print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
        correctCastling = FALSE
    elif(castling == '-'):
        print('Roszady nie są możliwe')
    else:
        c = Counter(castling)
        if(re.match('^[kKqQ]*$', castling) and c[max(c)] == 1):
            if((board[0][4] != 'k' and ('k' in castling or 'q' in castling)) or (board[7][4] != 'K' and ('K' in castling or 'Q' in castling))):
                print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
                correctCastling = FALSE
            else:
                if('K' in castling):
                    if board[7][7] == 'R':
                        print('Biały król może wykonać roszadę po swojej stronie')
                    else:
                        print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
                        correctCastling = FALSE
                        boardErr[7][7] = 1
                if('Q' in castling):
                    if board[7][0] == 'R':
                        print('Biały król może wykonać roszadę po stronie hetmana')
                    else:
                        print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
                        correctCastling = FALSE
                        boardErr[7][0] = 1
                if('k' in castling):
                    if board[0][7] == 'r':
                        print('Czarny król może wykonać roszadę po swojej stronie')
                    else:
                        print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
                        correctCastling = FALSE
                        boardErr[0][7] = 1
                if('q' in castling):
                    if board[0][0] == 'r':
                        print('Czarny król może wykonać roszadę po stronie hetmana')
                    else:
                        print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
                        correctCastling = FALSE
                        boardErr[0][0] = 1
        else:
            print('Błąd w zapisie - niewłaciwe oznaczenie roszad')
            correctCastling = FALSE

# Bicie w przelocie

def colNum(col):
    return {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
        }[col]

if(correct):
    enPasTar = fen[3]
    if(enPasTar in ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']):
        if(enPasTar[1] == '6'):
            eptStart = 1
            eptItr = 1
            eptFig = 'p'
        else:
            eptStart = 6
            eptItr = -1
            eptFig = 'P'
        if (fen[1] == 'w' and enPasTar[1] == '6') or (fen[1] == 'b' and enPasTar[1] == '3'):
            if(board[eptStart][colNum(enPasTar[0])] == board[eptStart + eptItr][colNum(enPasTar[0])] == 0 and board[eptStart + eptItr * 2][colNum(enPasTar[0])] == eptFig):
                print('Możliwe bicie w przelocie na ' + enPasTar)
            else:
                print('Błąd w zapisie - bicie w przelocie niemożliwe')
                boardErr[eptStart + eptItr][colNum(enPasTar[0])] = 1
        else:
            print('Błąd w zapisie - bicie w przelocie niemożliwe, złe bierki na ruchu')
            boardErr[eptStart + eptItr][colNum(enPasTar[0])] = 1
    elif(enPasTar == '-'):
        print('Brak możliwoci bicia w przelocie')
    else:
        print('Błąd w zapisie - niewłaciwe oznaczenie bicia w przelocie')
        
# Półtury i tury

if correct:
    halfMoves = fen[4]
    fullMoves = fen[5]
    
    if halfMoves.isnumeric() and fullMoves.isnumeric():
        if int(fullMoves) == 1:
            if fen[1] == 'b' and board == startBoard:
                print('Błąd w zapisie - partię powinny zaczynać białe')
            if correctCastling:
                test = ['K', 'Q', 'k', 'q']
                for m in range(4):
                    if test[m] not in castling:
                        print('Błąd w zapisie - na początku partii wszystkie opcje roszad powinny być dostępne')
                        break
        else:
            if int(halfMoves) > 100:
                print('Błąd w zapisie - gra już dawno powinna zakończyć się remisem')
            if int(fullMoves) < 1:
                print('Błąd w zapisie - iloć pełnych ruchów powinna wynosić minimum 1')
            if fullPiecesCount == 32 and int(halfMoves) != 0:
                print('Błąd w zapisie - brak bicia, liczba półruchów powinna wynosić 0')
            elif int(int(halfMoves) / 2) + 1 > int(fullMoves):
                print('Błąd w zapisie - za dużo półruchów')
            if fullPiecesCount != 32 and (int(halfMoves) / 2) + 1 == int(fullMoves):
                print('Błąd w zapisie - za dużo półruchów')
    else:
        correct = FALSE
        print('Błąd w zapisie - zły zapis iloci ruchów')

# --------------------------------------------------------------------------------------------------------------------------------------------

if(correct):
    root = tkinter.Tk()
    root.geometry("840x840")
    root.title('Notacja FEN')
    root.lift()
    root.wm_attributes("-topmost", True)
    
    canvas = Canvas(root, width = 840, height = 840)
    canvas.pack()
    bg = PhotoImage(file = boardImg)
    canvas.create_image(420, 420, image = bg)
    img = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[j][i] != 0):
                img.append(PhotoImage(file = pieces[board[j][i]]))
                canvas.create_image(100 * i + 90, 100 * j + 50, image = img[-1])
    
    for i in range(len(boardErr)):
        for j in range(len(boardErr[i])):
            if(boardErr[j][i] == 1):
                img.append(PhotoImage(file = wrong))
                canvas.create_image(100 * i + 90, 100 * j + 50, image = img[-1])
    for i in range(len(boardCh)):
        for j in range(len(boardCh[i])):
            if(boardCh[j][i] == 1):
                img.append(PhotoImage(file = checkImg))
                canvas.create_image(100 * i + 90, 100 * j + 50, image = img[-1])
    
    root.mainloop()