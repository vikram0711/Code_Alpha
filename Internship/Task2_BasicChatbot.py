def chatbot():
    print("Chatbot: Hi! How can I assist you today?")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hello', 'hi', 'hey']:
            print("Chatbot: Hi there!")
        elif user_input == 'how are you':
            print("Chatbot: I'm doing well, thank you!")
        elif user_input in ['bye', 'goodbye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")


if __name__ == "__main__":
    chatbot()
