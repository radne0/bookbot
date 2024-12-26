###################################################################################################
# BookBot
# Guided project boot.dev
# Reads in a text file counts the number of words and the count for each letter in the document.
###################################################################################################

## readbook(path)
# read in a book from the specificed string path
def readbook(path):
    with open(path) as f:
        file_contents = f.read()         
        return file_contents

## countwords(txt)
# return the number of words in the string txt.   
def countwords(txt):
    words = txt.split()
    wordcount = len(words)
    return wordcount

## countchars(txt)
# return a list that countains the number of time each alphanumerical character appears in txt.
def countchars(txt):
    chardict = {}

    # create a dictionary from all characters and their count.
    txt = txt.lower()
    for ch in txt:
        if ch not in chardict: 
            chardict[ch]=0   
        chardict[ch] +=1

    # create a list of dictionaries from this so that it can be sorted...
    charlist = []
    for ch in chardict:
        if ch.isalpha():
            charlist.append( {"character": ch, "count":chardict[ch]  }           )

    # sort
    charlist.sort(reverse=True,key=sort_on)
    return charlist



## sort_on()
#  helper function for sorting the list of dictionaries.
def sort_on(lst):
    return lst["count"]


def generatereport(path,words,chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")

    for d in chars:
        ch = d["character"]
        charcount = d["count"]
        print(f"The \'{ch}\' characeter was found {charcount} times")


# read in a book, then count words..
def main(): 
    bookpath = "books/frankenstein.txt"
    booktext = readbook(bookpath)
    wordcount = countwords(booktext)
    charcount = countchars(booktext)
    generatereport(bookpath,wordcount,charcount)

main()






