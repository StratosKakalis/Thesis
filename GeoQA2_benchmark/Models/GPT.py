import openai

def GPT_Inference(question):
    # Replace with your OpenAI API key
    api_key = "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"

    # Define the chat conversation
    conversation = [
        {"role": "system", "content": "You only perform toponym recognition. You answer like this: 'Location Name': 'wikipedia link'. Like this example: Prompt: Athens is the capitol of Greece. Answer: Athens: https://en.wikipedia.org/wiki/Athens , Greece: https://en.wikipedia.org/wiki/Greece"},
        {"role": "user", "content": question},
    ]

    # Make a chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=conversation,
        max_tokens=30,  # Adjust the maximum number of tokens in the response as needed
        api_key=api_key
    )

    # Extract and print the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply