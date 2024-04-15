import tkinter as tk
import random

# Define pairs of patterns and responses for the chatbot
pairs = {
    "hi|hello|hey": ["Hello!", "Hi there!", "Hey!"],
    "how are you ?": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "what is your name ?": ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"],
    "exit|bye|quit": ["Goodbye!", "See you later!", "Take care!"]
}

# Function to generate response based on user input
def generate_response(user_input):
    for pattern, responses in pairs.items():
        if user_input.lower() in pattern:
            return random.choice(responses)
    return "I'm sorry, I don't understand."

# Function to handle user input and display chatbot responses
def send():
    user_input = entry.get()
    response = generate_response(user_input)
    text_box.config(state=tk.NORMAL)
    text_box.insert(tk.END, "You: {}\n".format(user_input))
    text_box.insert(tk.END, "ChatBot: {}\n\n".format(response))
    text_box.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("ChatBot")

# Create a text box to display the conversation
text_box = tk.Text(root, height=20, width=50)
text_box.pack(padx=10, pady=10)
text_box.insert(tk.END, "ChatBot: Hello! How can I help you today?\n\n")
text_box.config(state=tk.DISABLED)

# Create an entry widget for user input
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Create a button to send user input
send_button = tk.Button(root, text="Send", command=send)
send_button.pack(padx=10, pady=5)

# Function to handle pressing Enter key to send user input
def on_enter(event):
    send()

root.bind('<Return>', on_enter)

root.mainloop()