from openai import OpenAI

# key = "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"

key = ''
messages = []

client = OpenAI(
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )

    # Only print the assistant's response
    assistant_reply = chat_completion.choices[0].message.content
    message = {
        "role": "assistant",
        "content": assistant_reply
    }
    messages.append(message)
    print(f"Jarvis: {assistant_reply}")

if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis, How may I help you?\n")
    while True:
        user_question = input("Users: ")
        print(f"User: {user_question}")
        completion(user_question)
