import ollama
import os

# Ollama chat in console mode
def ask(query):
    query = f'{query}'
    response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])
    response = response['message']['content']
    return response

os.system('cls')
while True:
    query = input('how can i help you?  ')
    os.system('cls')
    answer = ask(query)
    print(f'Question: {query}')
    print(answer)