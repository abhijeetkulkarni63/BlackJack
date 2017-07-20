import random
import tkinter

player_card_count = 0
dealer_card_count = 0


def load_images(card_images):
    suits = ["club", "diamond", "heart", "spade"]
    face_cards = ["king", "queen", "jack"]

    for suit in suits:
        for numberedCard in range(1, 11):
            name = "cards/{}_{}.png".format(str(numberedCard), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((numberedCard, image,))

        for faceCard in face_cards:
            name = "cards/{}_{}.png".format(str(faceCard), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def deal_dealer_card():
    global dealerTotalScore
    global playerTotalScore
    dealer_score = calculate_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealerCardFrame))
        dealer_score = calculate_hand(dealer_hand)
        dealerScoreLabel.set(dealer_score)

    player_score = calculate_hand(player_hand)
    if player_score > 21:
        resultText.set("Dealer Wins!!")
        dealerTotalScore += 1
        dealerScore.set(dealerTotalScore)
    elif dealer_score > 21 or dealer_score < player_score:
        resultText.set("Player Wins!!")
        playerTotalScore += 1
        playerScore.set(playerTotalScore)
    elif dealer_score > player_score:
        resultText.set("Dealer Wins!!")
        dealerTotalScore += 1
        dealerScore.set(dealerTotalScore)
    else:
        resultText.set("Draw!!")


def deal_player_card():
    global dealerTotalScore
    card = deal_card(playerCardFame)
    player_hand.append(card)
    score = calculate_hand(player_hand)
    playerScoreLabel.set(score)
    if score > 21:
        resultText.set("Dealer Wins!!")
        dealerTotalScore += 1
        dealerScore.set(dealerTotalScore)


def calculate_hand(hand_in):
    score = 0
    ace = False
    for next_card in hand_in:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def new_game():
    global dealerCardFrame
    dealerCardFrame.destroy()
    dealerCardFrame = tkinter.Frame(cardFrame, background="green")
    dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)
    global playerCardFame
    playerCardFame.destroy()
    playerCardFame = tkinter.Frame(cardFrame, background="green")
    playerCardFame.grid(row=2, column=1, sticky="ew", rowspan=2)
    resultText.set("")
    random.shuffle(deck)
    dealer_hand.clear()
    player_hand.clear()
    deal_player_card()
    dealer_hand.append(deal_card(dealerCardFrame))
    dealerScoreLabel.set(calculate_hand(dealer_hand))
    deal_player_card()


mainWindow = tkinter.Tk()
mainWindow.title("BlackJack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText, background="green", fg="white")
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background="green", fg="white").grid(row=1, column=0)

dealerCardFrame = tkinter.Frame(cardFrame, background="green")
dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)

playerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background="green", fg="white").grid(row=3, column=0)

playerCardFame = tkinter.Frame(cardFrame, background="green")
playerCardFame.grid(row=2, column=1, sticky="ew", rowspan=2)

cards = []
load_images(cards)
deck = list(cards)
random.shuffle(deck)
player_hand = []
dealer_hand = []

buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=3, column=0, sticky="w")
dealerButton = tkinter.Button(buttonFrame, text="Dealer Hit", command=deal_dealer_card)
dealerButton.grid(row=0, column=0)
playerButton = tkinter.Button(buttonFrame, text="Player Hit", command=deal_player_card)
playerButton.grid(row=0, column=1)
newGameButton = tkinter.Button(buttonFrame, text="New Game", command=new_game)
newGameButton.grid(row=0, column=2)

scoreFrame = tkinter.Frame(mainWindow, background="green")
scoreFrame.grid(row=0, column=3, sticky="ew")
playerScore = tkinter.IntVar()
tkinter.Label(scoreFrame, text="Player :", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(scoreFrame, textvariable=playerScore, background="green", fg="white").grid(row=0, column=1)
dealerScore = tkinter.IntVar()
tkinter.Label(scoreFrame, text="Dealer :", background="green", fg="white").grid(row=1, column=0)
tkinter.Label(scoreFrame, textvariable=dealerScore, background="green", fg="white").grid(row=1, column=1)

playerTotalScore = 0
dealerTotalScore = 0
deal_player_card()
dealer_hand.append(deal_card(dealerCardFrame))
dealerScoreLabel.set(calculate_hand(dealer_hand))
deal_player_card()

mainWindow.mainloop()
