travel_log = ['Delhi' , 'Jaipur' , 'Ajmer']

# we can have list under list , or dictionary under dictionary  or dictionary under list, list under dictionay 
toDo =  { 
    'cooking' : {
        'morning': 'Grilled Sandwich',
        'afternoon' : 'Pulses',
        'night' : 'soup'
    },

    'playing' : {
        'cricket': 'with few of my friend',
        'football' : 'just for change'

    }
}
print(toDo['cooking']['morning'])