
mr_miyagi = ''
while mr_miyagi != 'Sensei, I am at peace':
    mr_miyagi = str(input('whatcha wanna ask your personal assistant? '.lower()))
# every time you ask a question --> Mr. Miyagi responde with
    if '?' in mr_miyagi:
        print('questions are wise, but for now. Wax on, and Wax off!')
    elif 'Sensei' not in mr_miyagi:
        print('You are smart, but not wise - address me as Sensei please')
    elif 'block' or 'blocking' in mr_miyagi:
        print('Remember, best block, not to be there..')
    else:
        print('do not lose focus. Wax on. Wax off.')
    break




# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')