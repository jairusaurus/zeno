from ollama import chat


#main function
def main():
    question = input("Ask anything. ")
    generate_response(question)

#generates response in chunks
def generate_response(question):
    # variable for 'messages' for chat function
    messages = [
       {
        'role': 'user',
        'content': question,
       },
    ]
    
    #response variable is assigned to chat function of ollama
    response = chat(model='zeno', messages=messages, stream = True)
    
    #using loop to print chunks of 
    for part in response:
        print (part.message.content, end='', flush=True)

if __name__ == "__main__":
    main ()