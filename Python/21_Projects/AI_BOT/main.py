from openai import OpenAI

key = "give the api key from openapi"

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
