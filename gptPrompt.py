import openai

def gpt3_5(prompt):
    model = 'gpt-3.5-turbo'
    return openai.ChatCompletion.create(
        model=model,
        messages=[  # 2. Change the prompt parameter to the messages parameter
            {'role': 'user', 'content': prompt}
        ]
    ).choices[0].message.content


def gpt3(prompt):
    model = 'text-davinci-003'
    return openai.Completion.create(
        model=model,
        prompt=prompt
    ).choices[0].text
