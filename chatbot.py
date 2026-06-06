print("Welcome to DecodeBot!")

while True:

    user_input = input("You: ").strip().lower()

    if user_input in ("exit", "bye", "quit"):
        print("Bot: Goodbye!")
        break

    elif user_input in ("hello", "hi", "hey"):
        print("Bot: Hi there!")

    elif user_input == "how are you":
        print("Bot: I am doing great!")

    elif user_input == "what is your name":
        print("Bot: I am DecodeBot!")

    else:
        print("Bot: I don't understand.")