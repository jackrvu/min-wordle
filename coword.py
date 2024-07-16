# 43 seed words tested / minute
import pyautogui
import time
import subprocess
import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION
def findResult(x, y): # difference in y is 70, so is diff in x
    # y, w, w, g (177, 161,
    #

    # 76, 255) (58, 59, 60, 255) (58, 59, 60, 255) (97, 141, 85, 255)
    global count
    y = y + 90
    x = x + 20
    line = 0
    image = pyautogui.screenshot()
    pixels = []

    for num in range(5):
        pixels.append(image.getpixel((((x + num * 60) * 2), (y + count * 65) * 2)))
    '''
    one = image.getpixel((x, y))
    two = image.getpixel((x + 160, y + count * 145))
    three = image.getpixel((x + 320, y + count * 145))
    four = image.getpixel((x + 480, y + count * 145))
    five = image.getpixel((x + 540, y + count * 145))
    '''
    result = ""
    for pixel in pixels:
        print(pixel)
        if pixel[0] < 150:
            result += "g"
        elif pixel[0] < 200:
            result += "w"
        else:
            result += "y"
    return result
def legalWords():
    words = []
    file = open("/Users/jackvu/Desktop/cowordle/venv/gist.githubusercontent.com_scholtes_94f3c0303ba6a7768b47583aff36654d_raw_d9cddf5e16140df9e14f19c2de76a0ef36fd2748_wordle-La.txt", "r")
    word = file.readline()[:-1]
    while len(word) == 5:
        words.append(word)
        word = file.readline()[:-1]
    return words
words = legalWords()
'''
letters = "gyw"
combinations = []
for num in letters:
    for num1 in letters:
        for num2 in letters:
            for num3 in letters:
                for num4 in letters:
                    combinations.append((str(num) + str(num1)+ str(num2)+ str(num3)+ str(num4)))
print(combinations)
'''

def results(word, words):
    results = []
    for legalWord in words:
        result = ""
        for num in range(5):
            if word[num] == legalWord[num]:
                result = "".join([result, "g"])
            elif word[num] in legalWord:
                result = "".join([result, "y"])
            else:
                result = "".join([result, "w"])
        results.append(result)
    return results
def adjustFrequencies(word): # try to use list comprehension to change the frequencies
    combinations = ['ggggg', 'ggggy', 'ggggw', 'gggyg', 'gggyy', 'gggyw', 'gggwg', 'gggwy', 'gggww', 'ggygg', 'ggygy', 'ggygw', 'ggyyg', 'ggyyy', 'ggyyw', 'ggywg', 'ggywy', 'ggyww', 'ggwgg', 'ggwgy', 'ggwgw', 'ggwyg', 'ggwyy', 'ggwyw', 'ggwwg', 'ggwwy', 'ggwww', 'gyggg', 'gyggy', 'gyggw', 'gygyg', 'gygyy', 'gygyw', 'gygwg', 'gygwy', 'gygww', 'gyygg', 'gyygy', 'gyygw', 'gyyyg', 'gyyyy', 'gyyyw', 'gyywg', 'gyywy', 'gyyww', 'gywgg', 'gywgy', 'gywgw', 'gywyg', 'gywyy', 'gywyw', 'gywwg', 'gywwy', 'gywww', 'gwggg', 'gwggy', 'gwggw', 'gwgyg', 'gwgyy', 'gwgyw', 'gwgwg', 'gwgwy', 'gwgww', 'gwygg', 'gwygy', 'gwygw', 'gwyyg', 'gwyyy', 'gwyyw', 'gwywg', 'gwywy', 'gwyww', 'gwwgg', 'gwwgy', 'gwwgw', 'gwwyg', 'gwwyy', 'gwwyw', 'gwwwg', 'gwwwy', 'gwwww', 'ygggg', 'ygggy', 'ygggw', 'yggyg', 'yggyy', 'yggyw', 'yggwg', 'yggwy', 'yggww', 'ygygg', 'ygygy', 'ygygw', 'ygyyg', 'ygyyy', 'ygyyw', 'ygywg', 'ygywy', 'ygyww', 'ygwgg', 'ygwgy', 'ygwgw', 'ygwyg', 'ygwyy', 'ygwyw', 'ygwwg', 'ygwwy', 'ygwww', 'yyggg', 'yyggy', 'yyggw', 'yygyg', 'yygyy', 'yygyw', 'yygwg', 'yygwy', 'yygww', 'yyygg', 'yyygy', 'yyygw', 'yyyyg', 'yyyyy', 'yyyyw', 'yyywg', 'yyywy', 'yyyww', 'yywgg', 'yywgy', 'yywgw', 'yywyg', 'yywyy', 'yywyw', 'yywwg', 'yywwy', 'yywww', 'ywggg', 'ywggy', 'ywggw', 'ywgyg', 'ywgyy', 'ywgyw', 'ywgwg', 'ywgwy', 'ywgww', 'ywygg', 'ywygy', 'ywygw', 'ywyyg', 'ywyyy', 'ywyyw', 'ywywg', 'ywywy', 'ywyww', 'ywwgg', 'ywwgy', 'ywwgw', 'ywwyg', 'ywwyy', 'ywwyw', 'ywwwg', 'ywwwy', 'ywwww', 'wgggg', 'wgggy', 'wgggw', 'wggyg', 'wggyy', 'wggyw', 'wggwg', 'wggwy', 'wggww', 'wgygg', 'wgygy', 'wgygw', 'wgyyg', 'wgyyy', 'wgyyw', 'wgywg', 'wgywy', 'wgyww', 'wgwgg', 'wgwgy', 'wgwgw', 'wgwyg', 'wgwyy', 'wgwyw', 'wgwwg', 'wgwwy', 'wgwww', 'wyggg', 'wyggy', 'wyggw', 'wygyg', 'wygyy', 'wygyw', 'wygwg', 'wygwy', 'wygww', 'wyygg', 'wyygy', 'wyygw', 'wyyyg', 'wyyyy', 'wyyyw', 'wyywg', 'wyywy', 'wyyww', 'wywgg', 'wywgy', 'wywgw', 'wywyg', 'wywyy', 'wywyw', 'wywwg', 'wywwy', 'wywww', 'wwggg', 'wwggy', 'wwggw', 'wwgyg', 'wwgyy', 'wwgyw', 'wwgwg', 'wwgwy', 'wwgww', 'wwygg', 'wwygy', 'wwygw', 'wwyyg', 'wwyyy', 'wwyyw', 'wwywg', 'wwywy', 'wwyww', 'wwwgg', 'wwwgy', 'wwwgw', 'wwwyg', 'wwwyy', 'wwwyw', 'wwwwg', 'wwwwy', 'wwwww']
    frequencies = [0 for number in range(243)]
    answers = results(word, words)
    for answer in answers:
        for num in range(243):
            if combinations[num] == answer:
                frequencies[num] += 1
    return frequencies
def numPossibilitiesForResultWord(result, word): # theoretically easy to improve upon
    count = 0
    for answerWord in words:
        for num in range(5):
            if result[num] == "g":
                if word[num] != answerWord[num]:
                    break
            elif result[num] == "y":
                if word[num] not in answerWord: # yellow
                    break
            else:
                totalReal = 0
                totalWord = 0
                for number in range(5): # inputWord[number] is the
                    if word[num] == word[number] and result[number] != "w": # if it's in it and not white
                        totalReal += 1
                    if word[number] == answerWord[num]:
                        totalWord += 1 # the word guessed has to have the same number since one is gray
                if totalReal != totalWord:
                    isLegal = False
                    break
            if num == 4:
                count += 1
    return count

def averageRemaining(word):
    combinations = ['ggggg', 'ggggy', 'ggggw', 'gggyg', 'gggyy', 'gggyw', 'gggwg', 'gggwy', 'gggww', 'ggygg', 'ggygy', 'ggygw', 'ggyyg', 'ggyyy', 'ggyyw', 'ggywg', 'ggywy', 'ggyww', 'ggwgg', 'ggwgy', 'ggwgw', 'ggwyg', 'ggwyy', 'ggwyw', 'ggwwg', 'ggwwy', 'ggwww', 'gyggg', 'gyggy', 'gyggw', 'gygyg', 'gygyy', 'gygyw', 'gygwg', 'gygwy', 'gygww', 'gyygg', 'gyygy', 'gyygw', 'gyyyg', 'gyyyy', 'gyyyw', 'gyywg', 'gyywy', 'gyyww', 'gywgg', 'gywgy', 'gywgw', 'gywyg', 'gywyy', 'gywyw', 'gywwg', 'gywwy', 'gywww', 'gwggg', 'gwggy', 'gwggw', 'gwgyg', 'gwgyy', 'gwgyw', 'gwgwg', 'gwgwy', 'gwgww', 'gwygg', 'gwygy', 'gwygw', 'gwyyg', 'gwyyy', 'gwyyw', 'gwywg', 'gwywy', 'gwyww', 'gwwgg', 'gwwgy', 'gwwgw', 'gwwyg', 'gwwyy', 'gwwyw', 'gwwwg', 'gwwwy', 'gwwww', 'ygggg', 'ygggy', 'ygggw', 'yggyg', 'yggyy', 'yggyw', 'yggwg', 'yggwy', 'yggww', 'ygygg', 'ygygy', 'ygygw', 'ygyyg', 'ygyyy', 'ygyyw', 'ygywg', 'ygywy', 'ygyww', 'ygwgg', 'ygwgy', 'ygwgw', 'ygwyg', 'ygwyy', 'ygwyw', 'ygwwg', 'ygwwy', 'ygwww', 'yyggg', 'yyggy', 'yyggw', 'yygyg', 'yygyy', 'yygyw', 'yygwg', 'yygwy', 'yygww', 'yyygg', 'yyygy', 'yyygw', 'yyyyg', 'yyyyy', 'yyyyw', 'yyywg', 'yyywy', 'yyyww', 'yywgg', 'yywgy', 'yywgw', 'yywyg', 'yywyy', 'yywyw', 'yywwg', 'yywwy', 'yywww', 'ywggg', 'ywggy', 'ywggw', 'ywgyg', 'ywgyy', 'ywgyw', 'ywgwg', 'ywgwy', 'ywgww', 'ywygg', 'ywygy', 'ywygw', 'ywyyg', 'ywyyy', 'ywyyw', 'ywywg', 'ywywy', 'ywyww', 'ywwgg', 'ywwgy', 'ywwgw', 'ywwyg', 'ywwyy', 'ywwyw', 'ywwwg', 'ywwwy', 'ywwww', 'wgggg', 'wgggy', 'wgggw', 'wggyg', 'wggyy', 'wggyw', 'wggwg', 'wggwy', 'wggww', 'wgygg', 'wgygy', 'wgygw', 'wgyyg', 'wgyyy', 'wgyyw', 'wgywg', 'wgywy', 'wgyww', 'wgwgg', 'wgwgy', 'wgwgw', 'wgwyg', 'wgwyy', 'wgwyw', 'wgwwg', 'wgwwy', 'wgwww', 'wyggg', 'wyggy', 'wyggw', 'wygyg', 'wygyy', 'wygyw', 'wygwg', 'wygwy', 'wygww', 'wyygg', 'wyygy', 'wyygw', 'wyyyg', 'wyyyy', 'wyyyw', 'wyywg', 'wyywy', 'wyyww', 'wywgg', 'wywgy', 'wywgw', 'wywyg', 'wywyy', 'wywyw', 'wywwg', 'wywwy', 'wywww', 'wwggg', 'wwggy', 'wwggw', 'wwgyg', 'wwgyy', 'wwgyw', 'wwgwg', 'wwgwy', 'wwgww', 'wwygg', 'wwygy', 'wwygw', 'wwyyg', 'wwyyy', 'wwyyw', 'wwywg', 'wwywy', 'wwyww', 'wwwgg', 'wwwgy', 'wwwgw', 'wwwyg', 'wwwyy', 'wwwyw', 'wwwwg', 'wwwwy', 'wwwww']
    frequencies = adjustFrequencies(word)
    count = 0
    for num in range(243):
        count += frequencies[num] * numPossibilitiesForResultWord(combinations[num], word)
    return count
def mostComm():
    global frequencies
    combinations = ['ggggg', 'ggggy', 'ggggw', 'gggyg', 'gggyy', 'gggyw', 'gggwg', 'gggwy', 'gggww', 'ggygg', 'ggygy', 'ggygw', 'ggyyg', 'ggyyy', 'ggyyw', 'ggywg', 'ggywy', 'ggyww', 'ggwgg', 'ggwgy', 'ggwgw', 'ggwyg', 'ggwyy', 'ggwyw', 'ggwwg', 'ggwwy', 'ggwww', 'gyggg', 'gyggy', 'gyggw', 'gygyg', 'gygyy', 'gygyw', 'gygwg', 'gygwy', 'gygww', 'gyygg', 'gyygy', 'gyygw', 'gyyyg', 'gyyyy', 'gyyyw', 'gyywg', 'gyywy', 'gyyww', 'gywgg', 'gywgy', 'gywgw', 'gywyg', 'gywyy', 'gywyw', 'gywwg', 'gywwy', 'gywww', 'gwggg', 'gwggy', 'gwggw', 'gwgyg', 'gwgyy', 'gwgyw', 'gwgwg', 'gwgwy', 'gwgww', 'gwygg', 'gwygy', 'gwygw', 'gwyyg', 'gwyyy', 'gwyyw', 'gwywg', 'gwywy', 'gwyww', 'gwwgg', 'gwwgy', 'gwwgw', 'gwwyg', 'gwwyy', 'gwwyw', 'gwwwg', 'gwwwy', 'gwwww', 'ygggg', 'ygggy', 'ygggw', 'yggyg', 'yggyy', 'yggyw', 'yggwg', 'yggwy', 'yggww', 'ygygg', 'ygygy', 'ygygw', 'ygyyg', 'ygyyy', 'ygyyw', 'ygywg', 'ygywy', 'ygyww', 'ygwgg', 'ygwgy', 'ygwgw', 'ygwyg', 'ygwyy', 'ygwyw', 'ygwwg', 'ygwwy', 'ygwww', 'yyggg', 'yyggy', 'yyggw', 'yygyg', 'yygyy', 'yygyw', 'yygwg', 'yygwy', 'yygww', 'yyygg', 'yyygy', 'yyygw', 'yyyyg', 'yyyyy', 'yyyyw', 'yyywg', 'yyywy', 'yyyww', 'yywgg', 'yywgy', 'yywgw', 'yywyg', 'yywyy', 'yywyw', 'yywwg', 'yywwy', 'yywww', 'ywggg', 'ywggy', 'ywggw', 'ywgyg', 'ywgyy', 'ywgyw', 'ywgwg', 'ywgwy', 'ywgww', 'ywygg', 'ywygy', 'ywygw', 'ywyyg', 'ywyyy', 'ywyyw', 'ywywg', 'ywywy', 'ywyww', 'ywwgg', 'ywwgy', 'ywwgw', 'ywwyg', 'ywwyy', 'ywwyw', 'ywwwg', 'ywwwy', 'ywwww', 'wgggg', 'wgggy', 'wgggw', 'wggyg', 'wggyy', 'wggyw', 'wggwg', 'wggwy', 'wggww', 'wgygg', 'wgygy', 'wgygw', 'wgyyg', 'wgyyy', 'wgyyw', 'wgywg', 'wgywy', 'wgyww', 'wgwgg', 'wgwgy', 'wgwgw', 'wgwyg', 'wgwyy', 'wgwyw', 'wgwwg', 'wgwwy', 'wgwww', 'wyggg', 'wyggy', 'wyggw', 'wygyg', 'wygyy', 'wygyw', 'wygwg', 'wygwy', 'wygww', 'wyygg', 'wyygy', 'wyygw', 'wyyyg', 'wyyyy', 'wyyyw', 'wyywg', 'wyywy', 'wyyww', 'wywgg', 'wywgy', 'wywgw', 'wywyg', 'wywyy', 'wywyw', 'wywwg', 'wywwy', 'wywww', 'wwggg', 'wwggy', 'wwggw', 'wwgyg', 'wwgyy', 'wwgyw', 'wwgwg', 'wwgwy', 'wwgww', 'wwygg', 'wwygy', 'wwygw', 'wwyyg', 'wwyyy', 'wwyyw', 'wwywg', 'wwywy', 'wwyww', 'wwwgg', 'wwwgy', 'wwwgw', 'wwwyg', 'wwwyy', 'wwwyw', 'wwwwg', 'wwwwy', 'wwwww']
    biggest = 0
    indexBiggest = 0
    stringBiggest = combinations[0]
    for num in range(243):
        if frequencies[num] > biggest:
            biggest = frequencies[num]
            indexBiggest = num
            stringBiggest = combinations[num]
    print(biggest, indexBiggest, stringBiggest)


def narrow(inputWord, result):
    newLegalWords = [] # if it's white and it's in, it may be more complicated - multiple yellows, barely matters
    for word in words:
        isLegal = True
        for num in range(5):
            if result[num] == "g":
                if word[num] != inputWord[num]: # if exact letter not equal
                    isLegal = False
                    break
            elif result[num] == "y":
                if inputWord[num] not in word or inputWord[num] == word[num]: # yellow
                    isLegal = False
                    break
            else:
                totalReal = 0
                totalWord = 0
                for number in range(5): # inputWord[number] is the
                    if inputWord[num] == inputWord[number] and result[number] != "w": # if it's in it and not white
                        totalReal += 1
                    if word[number] == inputWord[num]:
                        totalWord += 1 # the word guessed has to have the same number since one is gray
                if totalReal != totalWord:
                    isLegal = False
                    break

        if isLegal:

            newLegalWords.append(word)
    return newLegalWords
def findSeedWord():
    fewestLeft = 15000
    wordFewest = ""
    for word in words:
        remaining = averageRemaining(word)
        print(word, remaining)
        if remaining < fewestLeft:
            fewestLeft = remaining
            wordFewest = word
            print("New lowest: " + wordFewest, averageRemaining(word))
    print(f"Best word: {wordFewest}")
def findWord(seedWord, x, y):
    global words
    global count
    result = findResult(x, y)
    print(result)
    words = narrow(seedWord, result)
    print(words)
    fewestLeft = 15000
    wordFewest = ""
    for word in words:
        remaining = averageRemaining(word)
        if remaining < fewestLeft:
            fewestLeft = remaining
            wordFewest = word
            print("New lowest: " + wordFewest, averageRemaining(word))
    print(f"Best word: {wordFewest}")
    return wordFewest
def locateAnchorPoint():
    anchorPoint = pyautogui.locateOnScreen("/Users/jackvu/Desktop/cowordle/venv/Screen Shot 2023-09-23 at 12.20.20 PM.png", confidence=.8)
    return anchorPoint
def typeResponse(word):
    pyautogui.write(word, interval = .01)
    pyautogui.press("enter")
window_name = "Google Chrome"
def switch_to_window(window_name):
    try:
        # Move the mouse to the top-left corner to prevent any interference.
        #pyautogui.moveTo(0, 0, duration=0.1)

        # Use AppleScript to switch to the desired window by name.
        applescript = f'tell application "{window_name}" to activate'
        subprocess.run(['osascript', '-e', applescript])

        time.sleep(0.5)  # Add a short delay to allow the window to switch.
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


count = 0
'''
def main():
    global words
    global count
    word = "raise"
    switch_to_window("Google Chrome")
    time.sleep(1)
    x = 1142
    y = 459
    typeResponse(word)
    time.sleep(4)
    while True:
        lastword = word
        word = findWord(word, x, y)
        count += 1
        if lastword == word:
            print("you won")
            break
        switch_to_window("Google Chrome")
        typeResponse(word)
        print(word)
'''
def main():
    global words
    global count
    words = legalWords()
    count = 0
    word = "raise"
    switch_to_window("Google Chrome")
    loc = locateAnchorPoint()
    x = loc[0] // 2
    y = loc[1] // 2
    print(x, y)
    while pyautogui.locateOnScreen("/Users/jackvu/Desktop/cowordle/venv/Screen Shot 2023-09-23 at 11.15.14 PM.png", confidence=.8) == None:
        time.sleep(.1)
    time.sleep(4.5)
    while True:
        typeResponse(word)
        time.sleep(.5)
        result = findResult(x, y)
        print(count)
        print(result)
        words = narrow(word, result)
        print(words)
        fewestLeft = 15000
        wordFewest = ""
        for word in words:
            remaining = averageRemaining(word)
            if remaining < fewestLeft:
                fewestLeft = remaining
                wordFewest = word
                print("New lowest: " + wordFewest, averageRemaining(word))
        print(f"Best word: {wordFewest}")
        word = wordFewest
        if len(word) == 0:
            break
        count += 1
while True:
    switch_to_window("Google Chrome")
    while True:
        location = pyautogui.locateOnScreen("/Users/jackvu/Desktop/cowordle/venv/Screen Shot 2023-09-23 at 11.24.19 PM.png", confidence=.8)
        if location != None:
            pyautogui.click(location[0] // 2, location[1] // 2)
            break
        location2 = pyautogui.locateOnScreen("/Users/jackvu/Desktop/cowordle/venv/Screen Shot 2023-09-23 at 11.27.56 PM.png", confidence=.8)
        if location2 != None:
            pyautogui.click(location2[0] // 2, location2[1] // 2)
            break
    main()



