story = ''
while True:
    new_text = input('Add to the story:\n')
    split = new_text.split()
    if new_text.lower() == 'the end':
        print(story)
        break
    elif len(split) == 2:
        story = story + ' ' + new_text