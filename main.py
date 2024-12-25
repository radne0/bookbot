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



# read in a book, then count words..
def main(): 
    bookpath = "books/frankenstein.txt"
    booktext = readbook(bookpath)
    wordcount = countwords(booktext)
    print(wordcount)    

main()






