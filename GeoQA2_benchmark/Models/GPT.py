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

    # Few-shot learning version 5.      Simplified version of prompt 3.
    few5_conversation = [
        {"role": "system", "content": "I want to identify toponyms from sentences. Can you identify the toponyms in the given questions? The number of"
         "toponyms in each question varies from 0 to 3 and you have to answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples:"
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens"
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland"
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland"
         "Q: Which state in the US has the most neighboring states? A: United States: https://en.wikipedia.org/wiki/United_States"},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    # Few-shot learning version 6.      Simplified version of prompt 4, trying to see if placing more meaning on the user content and less on the system content affects the predictions. 
    few6_conversation = [
        {"role": "system", "content": "You are a toponym recognition model. Only respond with: toponym: wiki link"},
        {"role": "user", "content": "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens"
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland"
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland"
         "Q: Which state in the US has the most neighboring states? A: United States: https://en.wikipedia.org/wiki/United_States"
         "Q: " + question + " A: "},
    ]

    # Few-shot learning version 7.      Different variation of 6, with more info for both user and system.
    few7_conversation = [
        {"role": "system", "content": "You are a toponym recognition model. Only respond with: toponym: wiki link"},
        {"role": "user", "content": "I want to identify toponyms from sentences. Can you identify the toponyms in the given questions? The number of"
         "toponyms in each question varies from 0 to 3 and you have to answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples:"
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens"
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland"
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland"
         "Q: Which state in the US has the most neighboring states? A: United States: https://en.wikipedia.org/wiki/United_States"
         "Q: " + question + " A: "},
    ]

    # Few-shot learning version 8.      Another clone of experiment 3, it's the best performing experiment so far.
    few8_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    # Few-shot learning version 9.      Deviation from 8 with more questions and unavailable instead of blank answers.
    few9_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom1_conversation = [
        {"role": "system", "content": "You are an expert SPARQL query generator."
         """For each question that the user supplies, the generator will convert it into a valid SPARQL query that can be used to answer the question."""},
        {"role": "user", "content": """Human: "Where is the Dorset county located?"
Generator:"""},
    ]

    custom2_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom3_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom4_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom5_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom6_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom7_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom8_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom9_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom10_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom11_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom12_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom13_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
    ]

    custom14_conversation = [
        {"role": "system", "content": "Can you identify the toponyms in the given questions? "
         "Your answers depend on the amount of toponyms in each sentence (if there are any) and you answer strictly like this: 'Location Name' | 'wikipedia link'. Follow these examples: "
         "Q: Which 5 municipalities east of Athens have the most residents? A: Athens:  https://en.wikipedia.org/wiki/Athens "
         "Q: Is Belfast closer to the capital of the Republic of Ireland or the capital of Scotland? A: Belfast: https://en.wikipedia.org/wiki/Belfast | Republic of Ireland: https://en.wikipedia.org/wiki/Republic_of_Ireland | Scotland: https://en.wikipedia.org/wiki/Scotland "
         "Q: Which is the largest rural area? A: "
         "Q: Is Dublin the capital of Ireland? A: Dublin: https://en.wikipedia.org/wiki/Dublin | Ireland: https://en.wikipedia.org/wiki/Ireland "
         "Q: Which state in the US has the most neighboring states? A: US: https://en.wikipedia.org/wiki/United_States"
         "Q: Is Kalamata north of Tripoli? A: Kalamata: https://en.wikipedia.org/wiki/Kalamata | Tripoli: https://en.wikipedia.org/wiki/Tripoli"
         "Q: Which municipalities contain at least one beach and one village? A: "},
        {"role": "user", "content": "Q: " + question + " A: "},
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
    elif (learning_type == "few5"):
        conversation = few5_conversation
    elif (learning_type == "few6"):
        conversation = few6_conversation
    elif (learning_type == "few7"):
        conversation = few7_conversation
    elif (learning_type == "few8"):
        conversation = few8_conversation
    elif (learning_type == "few9"):
        conversation = few9_conversation
    elif (learning_type == "custom1"):
        conversation = custom1_conversation
    elif (learning_type == "custom2"):
        conversation = custom2_conversation
    elif (learning_type == "custom3"):
        conversation = custom3_conversation
    elif (learning_type == "custom4"):
        conversation = custom4_conversation
    elif (learning_type == "custom5"):
        conversation = custom5_conversation
    elif (learning_type == "custom6"):
        conversation = custom6_conversation
    elif (learning_type == "custom7"):
        conversation = custom7_conversation
    elif (learning_type == "custom8"):
        conversation = custom8_conversation
    elif (learning_type == "custom9"):
        conversation = custom9_conversation
    elif (learning_type == "custom10"):
        conversation = custom10_conversation
    elif (learning_type == "custom11"):
        conversation = custom11_conversation
    elif (learning_type == "custom12"):
        conversation = custom12_conversation
    elif (learning_type == "custom13"):
        conversation = custom13_conversation
    elif (learning_type == "custom14"):
        conversation = custom14_conversation


    # Make a chat completion request
    response = client.chat.completions.create(
        #model="gpt-3.5-turbo-0613",
        model="gpt-4-turbo-2024-04-09",
        messages=conversation,
        max_tokens=70,
        temperature=0.2
    )

    # Extract and print the assistant's reply
    assistant_reply = response.choices[0].message.content
    return assistant_reply