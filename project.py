from ollama import chat
from ollama import ChatResponse


def main():
    question = input("Ask anything. ")
    print (generate_response(question))

def generate_response(question):
    response: ChatResponse = chat(model='llama3.1', messages=[
    {
        'role': 'user',
        'content': question,
    },
    ])
    return (response['message']['content'])
# or access fields directly from the response object
#print(response.message.content)

if __name__ == "__main__":
    main ()