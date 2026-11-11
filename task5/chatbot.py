print("Welcome to Simple AI Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Welcome.")

    elif user == "how are you":
        print("Bot: I'm fine. How can I help you?")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "help":
        print("Bot: Sure! Ask me something.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")