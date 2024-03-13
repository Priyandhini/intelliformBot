import openai


openai.api_key = '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'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response['choices'][0]['message']['content']

def form_bot():
    print("Welcome! I'm here to help you complete your form.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the form bot. Goodbye!")
            break

        # Add user input to the conversation history
        prompt = f"User: {user_input}"
        bot_response = generate_response(prompt)

        # Extract and print the bot's response
        print("Bot:", bot_response)

        # Check if the form is completed
        if "Thank you for completing the form!" in bot_response:
            print("Form completed successfully. Exiting the form bot. Goodbye!")
            break

if __name__ == "__main__":
    form_bot()
