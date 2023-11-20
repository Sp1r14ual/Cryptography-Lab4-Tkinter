from re import findall

MATRIX_SIZE = 2

ALPHA = tuple("abcdefgh")


def check_errors(cryptMode, MATRIX_KEY):
    det = MATRIX_KEY[0][0] * MATRIX_KEY[1][1] - \
        MATRIX_KEY[0][1] * MATRIX_KEY[1][0]
    if det != 1:
        print("Error: determinant != 1")
        raise SystemExit


def regular(text):
    template = r"[a-h]{"+str(MATRIX_SIZE)+"}"
    return findall(template, text)


def encryptDecrypt(message, matrix, summ=0, final=""):
    for double in range(len(message)):
        for string in range(MATRIX_SIZE):
            for column in range(MATRIX_SIZE):
                summ += matrix[string][column] * \
                    ALPHA.index(message[double][column])
            final += ALPHA[(summ) % 8]
            summ = 0
    return final


def start(startMessage, MATRIX_KEY, cryptMode):

    check_errors(cryptMode, MATRIX_KEY)

    iMATRIX_KEY = [[MATRIX_KEY[1][1], -MATRIX_KEY[0][1]],
                   [-MATRIX_KEY[1][0], MATRIX_KEY[0][0]]]

    for symbol in startMessage:
        if symbol not in ALPHA:
            startMessage = startMessage.replace(symbol, '')

    while len(startMessage) % MATRIX_SIZE != 0:
        startMessage += 'h'

    if cryptMode == 'E':
        finalMessage = encryptDecrypt(regular(startMessage), MATRIX_KEY)
    else:
        finalMessage = encryptDecrypt(regular(startMessage), iMATRIX_KEY)

    print("Final message:", finalMessage)

    return finalMessage
