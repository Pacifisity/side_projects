ingrediant_list = []
ingrediant = input("What ingredient is needed first? (Enter nothing to save recipe) ")

while ingrediant != '':
    ingrediant_list += [ingrediant]
    ingrediant = input(f"What's the {str(len(ingrediant_list) + 1)} ingrediant needed? (Enter nothing to save recipe) ")

print('The ingrediants needed are: ')
for ingrediant in ingrediant_list:
    print('   ' + ingrediant)
print(ingrediant_list)