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
#     This code is a Python script for creating a chatbot using the AIML (Artificial Intelligence Markup Language) library. AIML is a markup
    
#        language used for creating chatbots and natural language processing applications. Here's an explanation of how the code works:

# 1. Import AIML Library:
#    - The code begins by importing the `aiml` library, which provides tools for creating chatbots based on AIML files.

# 2. Create an AIML Kernel:
#    - An AIML kernel is created using the `aiml.Kernel()` constructor. The kernel serves as the core of the chatbot and handles interactions 
# with the user based on predefined AIML rules.

# 3. Load AIML Files:
#    - AIML files are used to define the chatbot's responses and behavior. The code loads AIML files using the `learn()` method of the kernel.
# You need to specify the path to the directory containing AIML files as an argument to the `learn()` method. Replace `'bot.aiml'` with 
# the actual path to your AIML files. The AIML files contain patterns and responses that the chatbot uses to engage in conversations.

# 4. User Interaction Loop:
#    - The code enters a loop that allows for user interactions. It continues to interact with the user until the user enters "exit."
#    - Within the loop, the following actions occur:
#      - The user is prompted to input a message with the `input()` function. The user's input is stored in the `user_input` variable.
#      - If the user's input is "exit" (case-insensitive), the code prints a farewell message and exits the loop, ending the 
# chatbot session.
#      - If the user's input is not "exit," the code uses the `respond()` method of the AIML kernel to obtain a response from 
# the chatbot based
# on the user's input.
#      - The response is then printed to the console, with the user's input followed by the chatbot's response.

# This code sets up a simple conversational interface with the chatbot, where the bot responds to user input based on the 
# AIML files it has loaded. It can be extended and customized by creating or modifying AIML files to define the chatbot's responses 
# to specific user queries and interactions. The chatbot continues to respond until the user chooses to exit the conversation.