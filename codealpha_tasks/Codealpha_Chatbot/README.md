import datetime

def chatbot():
    print("Chatbot: Hello! I am your simple chatbot.")
    print("Type 'help' to see commands or 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi there!")

        elif user == "how are you":
            print("Chatbot: I'm doing great, thanks!")

        elif user == "what is your name":
            print("Chatbot: My name is SimpleBot.")

        elif user == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print("Chatbot: Current time is", now)

        elif user == "date":
            today = datetime.date.today()
            print("Chatbot: Today's date is", today)

        elif user == "help":
            print("Chatbot commands you can use:")
            print("hello")
            print("how are you")
            print("what is your name")
            print("time")
            print("date")
            print("bye")

        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
