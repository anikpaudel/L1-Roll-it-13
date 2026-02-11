
while True:

    want_instruction =input(" do you need help: ").lower()

    #yes or nah
    if want_instruction == "yes" or want_instruction == "y":
        print("Ok")
        break
    elif want_instruction == "no" or want_instruction == "n":
        print("Ok Then Lets start The Best Game Ever")
        break
    else:
        print("yes or no?") 
        continue

print("Ok we are done")