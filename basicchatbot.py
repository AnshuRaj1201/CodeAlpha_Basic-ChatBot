def get_reply(user_input):
    """Returns a bot reply based on user input."""
    user_input = user_input.lower().strip()  # handle uppercase & spaces

    if user_input == "hello":
        return "Hi there! 👋"
    elif user_input == "how are you":
        return "I'm just a bot, but I'm doing great! 😄"
    elif user_input == "what is your name":
        return "I'm ChatBot 3000! 🤖"
    elif user_input == "bye":
        return "Goodbye! See you soon! 👋"
    else:
        return "Hmm, I don't understand that. Try: hello, how are you, bye"


def run_chatbot():
    """Main function to run the chatbot."""
    print("=" * 35)
    print("   Welcome to ChatBot 3000! 🤖")
    print("   Type 'bye' to exit.")
    print("=" * 35)

    while True:
        user_input = input("\nYou: ")

        if not user_input:          # if user pressed Enter without typing
            print("Bot: Please say something!")
            continue

        reply = get_reply(user_input)
        print(f"Bot: {reply}")

        if user_input.lower().strip() == "bye":
            break


# Start the chatbot
run_chatbot()