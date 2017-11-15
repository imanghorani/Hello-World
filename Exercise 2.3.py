x = 5
print('Hello')

def print_lyrics():
    print("I'am a lumberjack, and I'am okay.")
    print('I sleep all night and I work all day.')
    
print('Yo')
print_lyrics()
x = x + 2
print(x)



def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    else:
        print('Hello')
        
greet('en')
greet('es')
greet('fr')

def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    else:
        return 'Hello'
        
print(greet('en'), 'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')

