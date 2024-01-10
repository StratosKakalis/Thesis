# after
from openai import OpenAI

def GPT_Inference(question, learning_type):
    # Replace with your OpenAI API key
    openai_api_key = "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"

    client = OpenAI(
        api_key=openai_api_key
    )

    # One-shot learning.
    one_conversation = [
        {"role": "system", "content": "You only perform toponym recognition. You answer like this: 'Location Name': 'wikipedia link' | 'Another location name': 'another wikipedia link'. Like this example: Prompt: Athens is the capitol of Greece. Answer: Athens: https://en.wikipedia.org/wiki/Athens | Greece: https://en.wikipedia.org/wiki/Greece"},
        {"role": "user", "content": question},
    ]

    # Few-shot learning.
    few_conversation = [
        {"role": "system", "content": "You only perform toponym recognition, you don't answer any questions. Some questions dont include toponyms. You answer exactly like this depending on the number of toponyms: 'Location Name' | 'wikipedia link'. Follow these examples:"
         "Q: 'Which 5 municipalities east of Athens have the most residents?' A: 'Athens:  https://en.wikipedia.org/wiki/Athens'"
         "Q: 'Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland?' A: 'Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland'"
         "Q: 'Which is the largest rural area?' A: 'No toponym found in the question.'"
         "Q: 'Is Dublin the capital of Ireland?' A: 'Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: 'https://en.wikipedia.org/wiki/Ireland'"
         "Q: 'Which state in the US has the most neighboring states?' A: 'United States: https://en.wikipedia.org/wiki/United_States'"},
        {"role": "user", "content": question},
    ]

    # Few-shot learning version 2.
    few2_conversation = [
        {"role": "system", "content": "You only perform toponym recognition, you don't answer any questions. Some questions dont include toponyms. Your answers depend on the amount of toponyms (if there are any) and you answer exactly like this: 'Location Name' | 'wikipedia link'. Follow these examples:"
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens"
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland"
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland"
         "Q: Which state in the US has the most neighboring states? A: United States: https://en.wikipedia.org/wiki/United_States"},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    # Few-shot learning version 3.      Tried to follow basic prompt engineering principles.
    few3_conversation = [
        {"role": "system", "content": "I am a developer trying to use this conversation as an automated tool for toponym recognition. Can you identify the toponyms in the given questions?"
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples:"
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens"
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland"
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland"
         "Q: Which state in the US has the most neighboring states? A: United States: https://en.wikipedia.org/wiki/United_States"},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    # Few-shot learning version 4.      Same prompt but shifted the examples to the user content.
    few4_conversation = [
        {"role": "system", "content": "I am a developer trying to use this conversation as an automated tool for toponym recognition. Can you identify the toponyms in the given questions?"
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow the given examples:"},
        {"role": "user", "content": "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens"
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland"
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland"
         "Q: Which state in the US has the most neighboring states? A: United States: https://en.wikipedia.org/wiki/United_States"
         "Q: " + question + " A: "},
    ]

    if (learning_type == "one"):
        conversation = one_conversation
    elif (learning_type == "few"):
        conversation = few_conversation
    elif (learning_type == "few2"):
        conversation = few2_conversation
    elif (learning_type == "few3"):
        conversation = few3_conversation
    elif (learning_type == "few4"):
        conversation = few4_conversation


    # Make a chat completion request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=conversation,
        max_tokens=70,
        temperature=0.2
    )

    # Extract and print the assistant's reply
    assistant_reply = response.choices[0].message.content
    return assistant_reply