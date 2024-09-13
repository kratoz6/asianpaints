import openai

# Replace with your OpenAI API key
api_key = "your-api-key"

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = input("You: ")
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)