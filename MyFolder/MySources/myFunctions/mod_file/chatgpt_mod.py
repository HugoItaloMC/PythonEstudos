import openai
from datetime import datetime


openai.api_key = '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'
CHAT_WRITES_READ: list = []


def gerar_texto(prompt):
    completions = openai.Completion.create(
        engine='text-ada-001',
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
        CHAT_WRITES_READ.append(prompt)
        CHAT_WRITES_READ.append(gerar_texto(prompt))
        with open('arq.txt', '+a') as arq:
            arq.write(f'\n{datetime.now()}\n:: YOU\t=\n{CHAT_WRITES_READ[0]}\n:: R\t=\n{CHAT_WRITES_READ[1]}\n')
if __name__ == '__main__':
    main()












