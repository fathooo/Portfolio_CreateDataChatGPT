from app.config.openAI import OPENAI

def getResponseAI(conversation):
    conversation += "\nYOU: " + conversation + "\nIA:"
    response = OPENAI.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["\n", " YOU:", " IA:"]
    )
    answer = response.choices[0].text.strip()
    return answer



