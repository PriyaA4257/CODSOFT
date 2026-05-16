import datetime
import random

# Dictionary for meanings & opposites
word_dict = {
    "happy": ("feeling joy or pleasure", "sad"),
    "big": ("large in size", "small"),
    "fast": ("moving quickly", "slow"),
    "easy": ("not difficult", "hard"),
    "good": ("something positive", "bad")
}

# Store current question & answer
current_question = None
current_answer = None


def get_time_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night & Sweet Dreams!"


def get_response(user):
    global current_question, current_answer
    user = user.lower().strip()

    # Check answer if a question was asked
    if current_question:
        if user == current_answer:
            current_question = None
            return "Correct! Great job!"
        else:
            current_question = None
            return f"Not quite. The correct answer is {current_answer}."

    # Greetings + time-based
    if any(word in user for word in ["hello", "hi", "hey"]):
        return f"{get_time_greeting()}! How can I help you?"

    # Health check
    elif "sick" in user or "not feeling well" in user:
        return "Ohh no! Take care and get well soon!"

    # About chatbot
    elif "your name" in user:
        return "I'm RuleBot, your AI chatbot."

    elif "who made you" in user:
        return "I was created using Python."

    elif "help" in user:
        return ("I can answer questions about time, date, weather, programming, "
                "jokes, aptitude, meanings, opposites and more!")

    # Time & Date
    elif "time" in user:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "Today's date is " + datetime.datetime.now().strftime("%Y-%m-%d")

    # Weather
    elif "weather" in user:
        return "I can't check live weather, but I hope it's a great day!"

    # Music
    elif "music" in user:
        return "I love music! 🎶 What kind do you like?"

    elif "song" in user or "sing" in user:
        return "La la la... hope you liked it!"

    # Programming
    elif "python" in user:
        return "Python is a programming language and great for AI, web, and automation."

    elif "java" in user:
        return "Java is a widely-used object-oriented programming language."

    elif "sql" in user:
        return "SQL is used to manage databases."

    # Jokes
    elif "joke" in user:
        jokes = [
            "Why do programmers hate nature? Too many bugs!",
            "Why did the computer go to the doctor? It caught a virus!",
            "Why do Java developers wear glasses? Because they don’t C#!"
        ]
        return random.choice(jokes)

    # Logical Question
    elif "logical" in user:
        current_question = "logical"
        current_answer = "m"
        return "What comes once in a minute, twice in a moment, but never in a thousand years?"

    # Aptitude Question
    elif "aptitude" in user:
        current_question = "aptitude"
        current_answer = "300"
        return "If a train travels 60 km in 1 hour, how far will it travel in 5 hours?"

    # Meaning
    elif "meaning of" in user:
        word = user.replace("meaning of", "").strip()
        if word in word_dict:
            return f"Meaning of '{word}': {word_dict[word][0]}"
        else:
            return "Sorry, I don't have meaning for that word."

    # Opposite
    elif "opposite of" in user:
        word = user.replace("opposite of", "").strip()
        if word in word_dict:
            return f"Opposite of '{word}': {word_dict[word][1]}"
        else:
            return "Sorry, I don't know the opposite of that word."

    # Requests
    elif "can you" in user or "please" in user:
        return "Sure! I'll try to help you."

    # Thanks
    elif "thank" in user:
        return "You're welcome!"

    # Exit
    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    # Default
    else:
        return random.choice([
            "Sorry, I didn't understand that.",
            "Can you rephrase?",
            "I'm still learning!"
        ])


def main():
    print("Chatbot: Hello! I am RuleBot.")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()