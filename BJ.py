import random
dealer_cards = []
player_cards = []

def dealCards():
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has X &", dealer_cards[1])

    # Player Cards
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have ", player_cards)
 
    # Sum of the Dealer cards
    if sum(dealer_cards) == 21:
        print("Dealer has 21 and wins!")
    elif sum(dealer_cards) > 21:
        print("Dealer has busted!")

#dealCards()
def hit():
    player_cards.append(random.randint(1, 11))
    print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)

def stay():
    print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
    print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
    while(sum(dealer_cards) < 16):
        dealer_cards.append(random.randint(1, 11))
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
    if (sum(dealer_cards) > sum(player_cards)) and ((sum(dealer_cards) < 22)):
        print("Dealer wins!")
    else:
        print("You win!")
# Sum of the Player cards

#while sum(player_cards) < 21:
 #   action_taken = str(input("Do you want to stay or hit?  "))
  #  if action_taken == "hit":
   #     hit()
    #else:
     #   stay()

def finishRound():
    if sum(player_cards) > 21:
        print("You BUSTED! Dealer wins.")
    elif sum(player_cards) == 21:
        print("You have BLACKJACK! You Win!! 21")