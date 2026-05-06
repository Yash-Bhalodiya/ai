def chatbot():
    print("Welcome to Customer Support Chatbot!")
    print("Type 'exit' to end chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Thank you! Have a great day.")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you?")

        elif "price" in user_input:
            print("Bot: Our product prices start from ₹499.")

        elif "hours" in user_input or "timing" in user_input:
            print("Bot: We are open from 9 AM to 6 PM.")

        elif "location" in user_input:
            print("Bot: We are located in Pune, Maharashtra.")

        elif "contact" in user_input:
            print("Bot: You can contact us at support@example.com.")

        else:
            print("Bot: Sorry, I didn't understand. Please try again.")

# -------- MAIN --------
chatbot()