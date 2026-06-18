print("🤖 Welcome to AI Chatbot")
print("Type 'exit' to quit")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who created you":
        print("Bot: Siddartha created me.")

    elif user == "ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "python":
        print("Bot: Python is a programming language.")

    elif user == "internship":
        print("Bot: This project is part of the DecodeLabs Internship.")

    elif user == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user == "good evening":
        print("Bot: Good evening!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("Bot: I can answer basic questions. Try asking my name or about AI.")

    elif user == "what can you do":
        print("Bot: I can chat and answer predefined questions.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")