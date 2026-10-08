#mini-project:
dictionary={}
while True:
    print("<----Welcome to Dictionary management system---->")
    print("1.Add a word")
    print("2.Search for meaning")
    print("3.Display all words")
    print("4.update meaning")
    print("5.Delete word")
    print("6.exit")
    choice=input("enter your choice:")
    if choice=="1":
        word=input("enter the word:")
        meaning=input("enter a meaning:")
        dictionary[word]=meaning
        print("word added sucessfully!")
    elif choice=="2":
        word=input("enter a word :")
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("word not found in the dictionary!")
    elif choice=="3": 
        if dictionary:
            print("words and their meanings:")
            for word,meaning in dictionary.items():
                print(f"{word}:{meaning}")
        else:
            print("dictionary is empty!")
    elif choice=="4":
        word=input("enter a word to update meaning:")
        if word in dictionary:
            new_meaning=input("enter the new meaning:")
            dictionary[word]=meaning
            print("meaning updated sucessfully!")
            print("updated maning:",dictionary[word])
        else:
            print("word not found in the dictionary")
    elif choice=="5":
        word=input("enter the word to delete:")
        if word in dictionary:
            del dictionary[word]
            print("word deleted successfully!")
        else:
            print("word not found in the dictionary!")
    elif choice=="6":
        print("existing program !..")
        break
    else:
        print("invalid choice!please enter a valid option")
            






