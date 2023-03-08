# a dictionary of pre-defined responses
responses = {
    "hi": "Hello!",
    "how are you?": "I'm doing well, thank you. How about you?",
    "what's your name?": "My name is Slickbot. What's yours?",
    "Who created you?": "My creators name is Ernest",
    "What can you do?": "For now, I can only answer to your questions with pre-defined responses",
    "goodbye": "Goodbye!",
    "what's the weather like today": "I'm sorry, I don't have that information.",
    "what's the meaning of life": "I'm sorry, I don't know the answer to that.",
    "what do you like to do for fun": "I like to chat with people like you!",
    "how old are you": "I don't have an age. I'm a bot!",
    "what's the capital of France": "The capital of France is Paris.",
    "what's your favorite food": "I don't eat food. I'm a bot!",
    "where do you live": "I don't live anywhere. I exist in the digital world!",
    "what's your favorite movie": "I don't watch movies. I'm a bot!",
    "do you have any siblings": "No, I don't have any siblings. I'm an only child!",
    "what's your favorite animal": "I don't have a favorite animal. I'm a bot!",
    "how tall are you": "I don't have a height. I'm a bot!",
    "what's the meaning of the universe": "I'm sorry, I don't know the answer to that.",
    "what's your favorite book": "I don't read books. I'm a bot!",
    "what's the capital of Japan": "The capital of Japan is Tokyo.",
    "what's your favorite sport": "I don't play sports. I'm a bot!, basketball is interesting tho",
    "how do you spend your free time": "I don't have free time. I'm always available to chat!",
    "what's your favorite song": "I don't listen to music. I'm a bot!",
    "what's your favorite hobby": "I don't have hobbies. I'm a bot!",
    "what's your favorite TV show": "I don't watch TV shows. But breaking bad seems cool",
    "what's the capital of China": "The capital of China is Beijing.",
    "what's your favorite subject": "I don't have a favorite subject. I'm a bot!",
    "what's your favorite place to visit": "I don't travel. I exist in the digital world!",
    "what's your favorite thing to do": "I like to chat with people like you!",
    "what's your favorite game": "I don't play games. I'm a bot!",
    "what's the capital of Canada": "The capital of Canada is Ottawa.",
    "what's your favorite restaurant": "I don't eat at restaurants. I'm a bot!",
    "what's your favorite holiday": "I don't celebrate holidays. I'm a bot!",
    "what's your favorite city": "I don't have a favorite city. I'm a bot!, Norway does have a nice scenery tho"
}

# a function to accept user input
def respond_to_input(input_text):
    # Convert the input text to lowercase for case-insensitivity
    input_text = input_text.lower()
    # Check if the input matches any of the pre-defined responses
    if input_text in responses:
        return responses[input_text]
    else:
        return "I'm sorry, I don't understand. Could you please rephrase your question?"

# Main loop of the chatbot
while True:
    # Get user input
    user_input = input("You: ")
    # Respond to user input
    bot_response = respond_to_input(user_input)
    # bot's response
    print("Slickbot:", bot_response)


