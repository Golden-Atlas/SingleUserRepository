import random
import os

def dealCards(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck

def show_cards(cards, hidden, cardScore):
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card in ['J', 'Q', 'K', 'A']:
            s = s + '\t|  {}             |'.format(card)
        elif card == 'Ace':
            s = s + '\t|  {}             |'.format('A')
        elif card == '10':
            s = s + '\t|  {}            |'.format(card)
        else:
            s = s + '\t|  {}             |'.format(card)

    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|      * *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|    *     *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        if card == 'Ace':
            s = s + '\t|       {}        |'.format('A')
        elif card == '10':
            s = s + '\t|       {}       |'.format(card)
        else:
            s = s + '\t|       {}        |'.format(card)
    if hidden:
        s += '\t|          *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|         *      |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card in ['J', 'Q', 'K', 'A']:
            s = s + '\t|            {}   |'.format(card)
        elif card == 'Ace':
            s = s + '\t|  {}             |'.format('A')
        elif card == '10':
            s = s + '\t|  {}            |'.format(card)
        else:
            s = s + '\t|            {}   |'.format(card)
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|________________|'
    if hidden:
        s += '\t|________________|'
    print(s)
    print()

def playBlackjack(deck, cardScore):
    playerCards = []
    dealerCards = []
    playerScore = 0
    dealerScore = 0

    while len(playerCards) <= 2:
        playerCard, deck = dealCards(deck)
        playerCards.append(playerCard)
        playerScore += cardScore[playerCard]

        while playerScore > 21:
            if 'A' in playerCards:
                playerScore -= 10

        print('---------------------------------------------------')
        print('Player Cards: ')
        show_cards(playerCards, False, cardScore)
        print(f'Player Score: {playerScore}')
        print('---------------------------------------------------')

        input('Click "enter" to continue...')
        os.system('cls')

        '''----------------------------------------------------------'''

        dealerCard, deck = dealCards(deck)
        dealerCards.append(dealerCard)
        dealerScore += cardScore[dealerCard]
        print('---------------------------------------------------')

        while dealerScore > 21:
            if 'A' in dealerCards:
                dealerScore -= 10

        print('Dealer Cards: ')
        if len(dealerCards) == 1:
            show_cards(dealerCards, False, cardScore)
            print(f'Dealer Score: {dealerScore}')
            print('---------------------------------------------------')
        else:
            show_cards(dealerCards[0], True, cardScore)
            print(f'Known Dealer Score: {dealerScore - cardScore[dealerCards[-1]]}')
            print('---------------------------------------------------')

        input('Click "enter" to continue...')

        if len(playerCards) == 2:
            break

        '''----------------------------------------------------------'''

    if playerScore == 21:
        if dealerScore == 21:
            print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nTie Game!')
        else:
            print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nPlayer Wins!')

    while playerScore < 21:
        try:
            user = input('Do you want to hit or stand? Enter "H" or "s": ').upper()
            if user != 'S' and user != 'H':
                raise ValueError
        except ValueError:
            print('Please enter a valid choice.')
            continue

        if user == 'S':
            break
        elif user == 'H':
            playerCard, deck = dealCards(deck)
            playerCards.append(playerCard)
            playerScore += cardScore[playerCard]

            while playerScore > 21:
                if 'A' in playerCards:
                    playerScore -= 10
                    playerCards[playerCards.index('A')] = 'Ace'
                if 'A' not in playerCards and playerScore > 21:
                    print('Player Cards: ')
                    show_cards(playerCards, False, cardScore)
                    print('---------------------------------------------------')
                    print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nPlayer Busts! Dealer Wins!')
                    return



            print('Player Cards: ')
            show_cards(playerCards, False, cardScore)
            print(f'Player Score: {playerScore}')
            print('---------------------------------------------------')


        input('Click "enter" to continue... ')

    x = random.randint(13,20)
    while dealerScore < x:
        print('Dealer decides to hit!')
        dealerCard, deck = dealCards(deck)
        dealerCards.append(dealerCard)
        dealerScore += cardScore[dealerCard]
        print('Dealer Cards: ')
        show_cards(dealerCards[:-1], True, cardScore)
        print(f'Known Dealer Score: {dealerScore - cardScore[dealerCards[-1]]}')
        print('---------------------------------------------------')
    else:
        print('Dealer decides to stand.')
        x = 99999



    print('Player Cards: ')
    show_cards(playerCards, False, cardScore)
    print(f'Player Score: {playerScore}')
    print('---------------------------------------------------')
    print()
    print('Dealer is revealing their cards!')
    print('Dealer Cards: ')
    show_cards(dealerCards, False, cardScore)
    print('DEALER SCORE = ', dealerScore)
    print('---------------------------------------------------')

    input('Click "enter" to continue... ')

    '''------------------------------------------------------------'''

    print('---------------------------------------------------')

    if playerScore == dealerScore:
        print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nTie Game!')
    elif dealerScore > 21:
        print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nDealer Busted! Player Wins!')
    elif playerScore > 21:
        print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nPlayer Busted! Dealer Wins!')
    elif dealerScore > playerScore:
        print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nDealer Wins!')
    elif playerScore > dealerScore:
        print(f'Player Score: {playerScore} \nDealer Score: {dealerScore}  \nPlayer Wins!')
    else:
        print('What did you even do...?')



deck = ['2']*4 + ['3']*4 + ['4']*4 + ['5']*4 + ['6']*4 + ['7']*4 + ['8']*4 + ['9']*4 + ['10']*4 + ['J']*4 + ['Q']*4 + ['K']*4 + ['A']*4
cardScore = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Q':10, 'K':10, 'J':10, 'A':11}


while True:
    try:
        user = input('Play? Y/N: ')
        if user.lower() == 'y':
            print(playBlackjack(deck, cardScore))
        elif user.lower() == 'n':
            print('Game functionality halted.')
            quit()
        else:
            raise ValueError
    except ValueError:
        print('Invalid Input \nPlease Try Again. ')
