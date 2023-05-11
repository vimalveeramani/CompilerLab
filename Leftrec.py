gram = {}

def add(str):                               

    str = str.replace(" ", "").replace("    ", "").replace("\n", "")

    x = str.split("->")

    y = x[1]

    x.pop()

    z = y.split("|")

    x.append(z)

    gram[x[0]]=x[1]

remgram= {'E': [['T', "E'"]], 

          'T': [['F', "T'"]],

          'F': [['(', 'E', ')'], ['i', 'd']],

          "E'": [['+', 'T', "E'"], ['e']],

          "T'": [['*', 'F', "T'"], ['e']]

         }

for x,y in remgram.items():

    print(f'{x} -> ', end="")

    for index, i in enumerate(y):

        for j in i:

            print(j, end="")

            if (index != len(y) - 1):

                print(" | ", end="")

    print()
