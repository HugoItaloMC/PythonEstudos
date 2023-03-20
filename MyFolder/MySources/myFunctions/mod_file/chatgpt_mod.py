import openai

openai.api_key = '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'

def gerar_texto(prompt):
    completions = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = completions.choices[0].text
    return message.strip()
def main():
    while (prompt := input(':: You  = ')) != 'sair':
        print('R:  ', gerar_texto(prompt))
if __name__ == '__main__':
    main()