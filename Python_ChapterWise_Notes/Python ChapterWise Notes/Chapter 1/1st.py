import pyjokes

prompt=''

prompt += '\nDo you want a new Jokes y(or anything)/n :'

while (response := input(prompt).lower()) != 'n':
    print('response is ',response)
    if response=='y':
        print(pyjokes.get_joke())
    else :
        print('Please enter correct response')
