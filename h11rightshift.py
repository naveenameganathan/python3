def reverseWordSentence(): 
    words = input().split(" ") 
    newWords = [word[::-1] for word in words]  
    newSentence = " ".join(newWords) 
    return newSentence 
print(reverseWordSentence()) 
