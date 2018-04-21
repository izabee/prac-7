#politely tells you whether an input sentence is a palindrome or not

def main():
    s = input("Enter a word/phrase to check for palindrome: ")
    sent = s.lower()
    cleansent = cleaner(sent)

    reverse = cleansent[::-1]     #checks whether the reverse is the same as the cleaned sentence
    if (reverse == cleansent):
        print("This is indeed a palindrome.")
    else:
        print("Sorry, it's not a palindrome.")

def cleaner(s):    #removes all punctuation from the string, and returns a string
    slist = list(s)
    print(slist)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    for item in slist:
        if item not in alphabet:
            slist.remove(item)
    print(slist)
    cleansent = "".join(slist)
    return cleansent

if __name__ == "__main__":
    main()
