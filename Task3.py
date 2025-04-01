import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello! How can I help you?", "Hey!"],
        "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!"],
        "what is your name": ["I'm ChatBot!", "You can call me ChatBot."],
        "bye": ["Goodbye! Have a great day!", "See you soon!"],
        "default": ["I'm not sure how to respond to that.", "Can you rephrase that?", "Interesting! Tell me more."]
    }
    
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
