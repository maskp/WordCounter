import csv
def main():
    Wordlist = []
    abbreviation = ["blvd.","Ave.","N.","Mr.", "Ms.", "Mrs.", "Sr.", "St.", "Rd."]
    sentence = 0
    validWord = 0
    lines = 0
    check = True
    while check:
        try:
            userInput = input('Enter a filename: ')
            userInput2 = int(input('How many characters can be a word: '))
            if userInput.endswith('.txt'):

                openFile = open(userInput, 'r')
                contents = openFile.readlines()

                for i in range(len(contents)):
                    Wordlist.extend(contents[i].split())
                    lines += 1

                if lines <= 1000:
                    for j in Wordlist:
                        if j.endswith(('.', '?', '!', ';', ':', ',')):
                            sentence = sentence + 1
                        if len(j) >= userInput2 and j.endswith(('.', '?', '!', ',', ':', ';')):
                            WordLen = len(j) - 1
                            if WordLen >= userInput2:
                                validWord = validWord + 1
                        elif len(j) >= userInput2 and j.endswith(('.', '?', '!', ',', ':', ';')) == False:
                            validWord = validWord+ 1

                if not set(abbreviation).isdisjoint(Wordlist):
                    sentence = sentence - 1
                Average = validWord/ sentence

                print('lines', lines,'sentence: ', sentence,'Average: ', Average,'validWord',validWord)
                print('WordList: \n', Wordlist)
                with open('output.txt', 'w') as fname:
                    fnameWriter = csv.writer(fname)
                    fnameWriter.writerow([userInput, userInput2, validWord, sentence, Average])

                check = False
                break
            else:
                raise IOError
                break
        except IOError:
            print('Please enter .txt file')
        except ValueError:
            print('Please Enter input in correct format')
        except ZeroDivisionError:
            print('Please do not input an empty file')



main()
while True:
    try:
        userInput3 = input('Do you want to enter another file? Y/N: ')
        if userInput3 == 'Y' or userInput3 =='y':
            main()
        elif userInput3 == 'N' or userInput3 == 'n':
            break
        else:
            raise IOError
    except IOError:
        print('Please Enter \'Y\' or \'y\' to continue or \'N\' or \'n\' to discontinue')

