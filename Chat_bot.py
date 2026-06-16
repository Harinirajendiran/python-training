print("welcome to the chat bot")
while True:#infinite while loop
    user=input("you:")
    if user.lower() in ["quit","bye","exit"]:#is the if condition where user input is quit,bye,exit output is goodbye
        print("Bot:Good bye")
        break
    if user.lower() in ["hello"]:
        print("Bot:Hii GOOD MORNING")
    if user.lower() in ["how are you?"]:
        print("Bot:I am fine ,how you now?")
    if user in ["how i learn python?"]:
        print("Bot:going with course")
    if user.lower() in ("need course","suggest me one"):
        print("Bot:sure ,i will give a suggetion")
    if user.lower() in ("is this usefull for my career"):
        print("Bot:yeah,many python developer have various role in developing field")
    if user.lower() in ["i need to loss a weight"]:
        user=input("you:")
        if user.lower() in ("need suggestion"):
            print("Bot:i give the great diet and exercise chat") 
        else:
            print("Bot:welcome")
    else:#else execute only when the user input is not  in the defined process
        print("Bot:not valid info to BOT sorry for the interrupt")
    
        
    
        