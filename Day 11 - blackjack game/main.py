import art
import deck
import random
import time
from replit import clear

# Shuffle function
def shuffle(num_decks):
    shuffled_deck = deck.single_deck * num_decks
    random.shuffle(shuffled_deck)
    return shuffled_deck

# Hit function
def hit(hand, card_deck):
    card_drawn = random.randint(0, len(card_deck) - 1)
    hand.append(card_deck[card_drawn])
    card_deck.pop(card_drawn)
    return hand

# Deal function
def deal(card_deck):
    '''
    deal(list)\n
    \nCards are dealt alternatingly starting with the player.  As cards are dealt, they are removed from the game deck.\n
    \nlist: list type whose elements are strings representing all cards in a multiple deck stack of cards defined by shuffle()
    \noutput: tuple type two lists the first of which is the player's hand and the second is the dealer's
    '''
    user_hand = []
    cpu_hand = []
    for i in range(2):
        user_hand = hit(user_hand, card_deck)
        cpu_hand = hit(cpu_hand, card_deck)
    return (user_hand, cpu_hand)

# Dealer hit function
def dealer_hit(dealer, card_deck):
    total = 0
    print(f'Dealer hand: {dealer}')
    for card in dealer:
        total += deck.card_values[card]
    while total < 17:
        time.sleep(1)
        dealer = hit(dealer, card_deck)
        print(f'Dealer hand: {dealer}')
        total += deck.card_values[dealer[-1]]
        if total > 21:
            for card in dealer:
                if card == 'A':
                    total -= 10
    return total

# Player hit function
def player_hit(player, card_deck):
    '''
    player_hit(list1, list2)

    Deals an additional card to the player using hit(). Checks if player's hand is a bust. If so, all aces are converted to 1's.\n
    list1: list containing player's cards whose elements are strings\n
    list2: list containing the current cards in the deck.\n
    ouput: total value of player's cards
    '''
    total = 0
    player = hit(player, card_deck)
    print(f'Player hand: {player}')
    for card in player:
        total += deck.card_values[card]
    if total > 21:
        for card in player:
            if card == 'A':
                total -= 10
    return total
    
# Blackjack game function
def blackjack():
    '''
    blackjack()

    Plays 1 hand of traditional blackjack against a dealer.
    '''
    print(art.logo)
    player_total = 0
    dealer_total = 0
    # Ask how many decks to play with and shuffle cards
    decks = int(input('How many decks of cards do you want to play with?: '))
    game_deck = shuffle(decks)
    # Deal cards
    hands = deal(game_deck)
    print('Dealing cards...')
    time.sleep(3)
    # Print player and dealer hands to the screen masking the first dealer card
    print(f'Player hand: [{hands[0][0]}, {hands[0][1]}]')
    print(f'Dealer hand: [X, {hands[1][1]}]')
    for card in hands[0]:
        player_total += deck.card_values[card]
    for card in hands[1]:
        dealer_total += deck.card_values[card]
    
    # Once cards are dealt, the player is asked whether to hit or stay 
    action = input('\nWould you like to HIT or STAY? (h/s): ').lower()

    # Input error checking loop
    while action != 'h' and action != 's':
        print('Invalid input. Please try again.')
        action = input('Would you like to HIT or STAY? (h/s): ').lower()

    # Loop logic for player's turn
    while action != 's':
        # Deal player a card and print their hand to the screen
        player_total = player_hit(hands[0], game_deck)
        
        # Check to see if player has exceeded 21.  
        if player_total > 21:
            print('\nBust. You lose.\n')
            action = 's'
            return

        # Ask if player would like another card
        action = input('\nWould you like to HIT or STAY? (h/s): ').lower()
        
        # Input error checking loop
        while action != 'h' and action != 's':
            print('Invalid input. Please try again.')
            action = input('Would you like to HIT or STAY? (h/s): ').lower()

    dealer_total = dealer_hit(hands[1], game_deck)
    
    if dealer_total > 21:
        print('\nDealer busts. You win!\n')
        return
    elif player_total > dealer_total:
        print('\nYou win!\n')
        return
    elif player_total == dealer_total:
        print('\nDraw.\n')
        return
    else: 
        print('\nDealer wins.\n')
        return

# Program logic
play_again = True
while play_again:
    clear()
    blackjack()
    new_game = input('Would you like to play again? (y/n): ').lower()
    if new_game == 'n' or new_game =='no':
        play_again = False