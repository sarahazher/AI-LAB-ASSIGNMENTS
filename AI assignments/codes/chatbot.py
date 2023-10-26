import aiml
# Create an AIML kernel
kernel = aiml.Kernel()
# Load the combined AIML file (replace 'path_to_aiml_directory' with your directory containing AIML files)
kernel.learn("bot.aiml")
# Use a loop for user interactions
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    bot_response = kernel.respond(user_input)
    print("Bot:", bot_response)
    bot_response = kernel.respond(user_input)
    print("Chatbot:", bot_response)