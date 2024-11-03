import random

Size_MATRICE = 11
EMPTY = 0 # 0 - nu există nici o bomboană în acel element
CANDY_TYPES = [1, 2, 3, 4]
# 1- bomboană de culoare roșie
# 2 - bomboană de culoare galbenă
# 3 - bomboană de culoare verde
# 4 - bomboană de culoare albastră

TARGET_SCORE = 10000 # pt fiecare joc

POINTS_LINE_3 = 5
POINTS_LINE_4 = 10
POINTS_LINE_5 = 50
POINTS_L_SHAPE = 20
POINTS_T_SHAPE = 30

# 5 pct - linie de 3
# 10 pct - linie de 4
# 50 pct - linie de 5
# 20 - L cu laturile de 3
# 30 - T cu laturile de 3

def initializare_matrice():
    return [[random.choice(CANDY_TYPES) for _ in range(Size_MATRICE)] for _ in range(Size_MATRICE)]
    # initializam matricea (11x11) random cu bomboane(1,2,3,4)

def find_formations(matrice):
    to_remove = set()
    global score

    # Cautare linii de 5 pe orizontala
    for i in range(Size_MATRICE):
        for j in range(Size_MATRICE - 4):
            if matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] == matrice[i][j + 3] == matrice[i][j + 4] != EMPTY:
                to_remove.update([(i, j + k) for k in range(5)])
                score += POINTS_LINE_5

    # Cautare linii de 5 pe verticala
    for i in range(Size_MATRICE - 4):
        for j in range(Size_MATRICE):
            if matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] == matrice[i + 3][j] == matrice[i + 4][j] != EMPTY:
                to_remove.update([(i + k, j) for k in range(5)])
                score += POINTS_LINE_5


    for i in range(Size_MATRICE - 2):
        for j in range(Size_MATRICE - 2):
            # Cautare formatiuni L (orizontala sau verticala)
            if (matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] == matrice[i + 2][j + 1] == matrice[i + 2][j + 2] != EMPTY):
                to_remove.update([(i, j), (i + 1, j), (i + 2, j), (i + 2, j + 1), (i + 2, j + 2)])
                score += POINTS_L_SHAPE
            if (matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] == matrice[i + 1][j + 2] == matrice[i + 2][j + 2] != EMPTY):
                to_remove.update([(i, j), (i, j + 1), (i, j + 2), (i + 1, j + 2), (i + 2, j + 2)])
                score += POINTS_L_SHAPE

            # Cautare formatiuni T
            if (matrice[i][j + 1] == matrice[i + 1][j + 1] == matrice[i + 2][j + 1] == matrice[i + 1][j] == matrice[i + 1][
                j + 2] != EMPTY):
                to_remove.update([(i, j + 1), (i + 1, j + 1), (i + 2, j + 1), (i + 1, j), (i + 1, j + 2)])
                score += POINTS_T_SHAPE

    # Cautare linii de 4 orizontala
    for i in range(Size_MATRICE):
        for j in range(Size_MATRICE - 3):
            if matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] == matrice[i][j + 3] != EMPTY:
                to_remove.update([(i, j + k) for k in range(4)])
                score += POINTS_LINE_4

    # Cautare linii de 4 verticala
    for i in range(Size_MATRICE - 3):
        for j in range(Size_MATRICE):
            if matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] == matrice[i + 3][j] != EMPTY:
                to_remove.update([(i + k, j) for k in range(4)])
                score += POINTS_LINE_4

    # Cautare linii de 3 orizontala
    for i in range(Size_MATRICE):
        for j in range(Size_MATRICE - 2):
            if matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2] != EMPTY:
                to_remove.update([(i, j + k) for k in range(3)])
                score += POINTS_LINE_3

    # Cautare linii de 3 verticala
    for i in range(Size_MATRICE - 2):
        for j in range(Size_MATRICE):
            if matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j] != EMPTY:
                to_remove.update([(i + k, j) for k in range(3)])
                score += POINTS_LINE_3

    return to_remove


def remove_candies(matrice, to_remove):
    for (i, j) in to_remove:
        matrice[i][j] = EMPTY


def drop_and_fill_candies(matrice):
    for j in range(Size_MATRICE):
        column = [matrice[i][j] for i in range(Size_MATRICE) if matrice[i][j] != EMPTY]

        # Completeaza spatiile lasate goale cu bomboane noi
        new_candies = [random.choice(CANDY_TYPES) for _ in range(Size_MATRICE - len(column))]
        new_column = new_candies + column

        # Actualizeaza matricea
        for i in range(Size_MATRICE):
            matrice[i][j] = new_column[i]


def find_possible_move(matrice):
    for i in range(Size_MATRICE):
        for j in range(Size_MATRICE):
            if j < Size_MATRICE - 1:  # Mutare pe orizontala
                matrice[i][j], matrice[i][j + 1] = matrice[i][j + 1], matrice[i][j]
                if find_formations(matrice):
                    matrice[i][j], matrice[i][j + 1] = matrice[i][j + 1], matrice[i][j]
                    return (i, j), (i, j + 1)
                matrice[i][j], matrice[i][j + 1] = matrice[i][j + 1], matrice[i][j]
            if i < Size_MATRICE - 1:  # Mutare pe verticala
                matrice[i][j], matrice[i + 1][j] = matrice[i + 1][j], matrice[i][j]
                if find_formations(matrice):
                    matrice[i][j], matrice[i + 1][j] = matrice[i + 1][j], matrice[i][j]
                    return (i, j), (i + 1, j)
                matrice[i][j], matrice[i + 1][j] = matrice[i + 1][j], matrice[i][j]
    return None

def print_matrice(matrice):
    for row in matrice:
        print(" ".join(str(candy) for candy in row))
    print()

def candy_crush():
    global score, operations_count
    matrice = initializare_matrice()
    score = 0
    operations_count = 0
    game_over = False

    while not game_over and score < TARGET_SCORE:
        to_remove = find_formations(matrice)
        if to_remove:
            remove_candies(matrice, to_remove)
            drop_and_fill_candies(matrice)
        else:
            move = find_possible_move(matrice)
            if move:
                (x1, y1), (x2, y2) = move
                matrice[x1][y1], matrice[x2][y2] = matrice[x2][y2], matrice[x1][y1]
                operations_count += 1
                #print("Matricea dupa interschimbare:")
                #print_matrice(matrice)
            else:
                game_over = True

    return score, operations_count


scor_total = 0
nr_total_interschimbari = 0
nr_jocuri = 100

for _ in range(nr_jocuri):
    scor_final, operations = candy_crush()
    scor_total += scor_final
    nr_total_interschimbari += operations
    print(f"Numarul de operatiuni jocul cu nr {_} este: {operations}, iar scorul: {scor_final}")


average_score = scor_total / nr_jocuri
average_operations = nr_total_interschimbari / nr_jocuri
print(f"\nScorul mediu obtinut in 100 de jocuri este: {average_score}")
print(f"\nNumarul mediu de operatiuni pentru a obtine {TARGET_SCORE} de puncte este: {average_operations}")
