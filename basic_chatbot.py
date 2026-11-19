def chatbot():
    print("🤖 Chatbot: Hello! Welcome to my chatbot.")
    print("Type 'bye' to exit the chat.")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user == "what can you do":
            print("Bot: I can chat with you!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


if __name__ == "__main__":
    chatbot()
