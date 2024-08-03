import pyjokes # import external library for Jokes

prompt='' # variable initialization

prompt += '\nDo you want a new Jokes y(or anything)/n :'

while (response := input(prompt).lower()) != 'n':
    print('response is ',response)
    if response=='y':
        print(pyjokes.get_joke(language= "en",category= "neutral"))
    else :
        print('Please enter correct response')
