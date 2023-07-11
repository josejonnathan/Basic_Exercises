bear = '''
     (()__(()
     /       \ 
    ( /    \  \\
     \ o o    /
     (_()_)__/ \             
    / _,==.____ \\
   (   |--|      )
   /\_.|__|'-.__/\_
  / (        /     \ 
  \  \      (      /
   )  '._____)    /    
(((____.--(((____/'''

bat = '''
   /\                 /\\
  / \'._   (\_/)   _.'/  \\
 /_.''._'--('.')--'_.''._\\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
   `      \(/|\)/       `
           " ` "'''

aardvark = '''
                    _,,......_
                 ,-'          `'--.
              ,-'  _              '-.
     (`.    ,'   ,  `-.              `.
      \ \  -    / )    \               \\
       `\`-^^^, )/      |     /         :
         )^ ^ ^V/            /          '.
         |      )            |           `.
         9   9 /,--,\    |._:`         .._`.
         |    /   /  `.  \    `.      (   `.`.
         |   / \  \    \  \     `--\   )    `.`.___
        .;;./  '   )   '   )       ///'       `-"'
        `--'   7//\    ///\\
            '''

camel = '''
                  ,,__
        ..  ..   / o._)            
       /--'/--\  \-'||       
      /        \_/ / |     
    .'\  \__\  __.'.'     
      )\ |  )\ |      
     // \\ // \\\\
    ||_  \\|_  \\\\_
    '--' '--'' '--'
'''

print("*** WELCOME ***")
print()


election = (": ")

while election:
    print("choose something to print or quit")
    print('''
1 - Bear
2 - Bat
3 - Aardvark
4 - Camel
5 - Quit''')
    print()
    election = input(" ").lower()
    if election == "bear" or election == "1":
        print(bear)
        print()
    elif election == "bat" or election == "2":
        print(bat)
        print()
    elif election == "aardvark" or election == "3":
        print(aardvark)
        print()
    elif election == "camel" or election == "4":
        print(camel)
        print()
    elif election == "quit" or election == "5":
        print("Bye, Bye!!!")
        break
    else:
        print("choose an option from the list")
        print()
