#read in a book from the specificed path
def readbook(path):
    with open(path) as f:
        file_contents = f.read()         
        return file_contents



# countwords in a string
def countwords(txt):
    words = txt.split()
    wordcount = len(words)
    return wordcount

# create a dictionary of character counts...
def countchars(txt):
    chardict = {}

    txt = txt.lower()
    for ch in txt:
        if ch not in chardict: 
            chardict[ch]=0   
        chardict[ch] +=1

    return chardict

def sort_on(dict):
    return dict["num"]


def generatereport(path,words,chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")

    wordlist = list(words)
    print(wordlist)







    for k in chars:
        if k.isalpha():
            print(f"The \'{k}\' characeter was found {chars[k]} times")


# read in a book, then count words..
def main(): 
    bookpath = "books/frankenstein.txt"
    booktext = readbook(bookpath)
    wordcount = countwords(booktext)
    charcount = countchars(booktext)
    print(charcount)
    generatereport(bookpath,wordcount,charcount)

main()






