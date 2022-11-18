from flask import Blueprint,  render_template, request, redirect, url_for, session

actions = Blueprint('actions', __name__)
zuruck = Blueprint('reset', __name__)



@actions.route('actions/', methods = ["POST", "GET"])
def play():
    next_move = (1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1,
     1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 1, 3, 1, 1, 2, 2, 2, 1, 1,
      1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
       2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 1, 3, 3, 3, 2, 1, 1, 3, 1, 1, 3, 3, 1, 3, 3, 3, 1, 1, 1, 1, 1, 3, 2, 1, 2, 1, 1, 1, 1, 1, 3, 2, 3, 3, 3, 3,
         3, 1, 1, 1, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 3, 2, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 2, 2,
          2, 2, 2, 2, 1, 1, 4, 1, 2, 2, 4, 1, 1, 4, 4, 3, 3, 4, 4, 4, 2, 2, 1, 1, 4, 2, 1, 4, 1, 2, 1, 4, 2, 2, 3, 3, 2, 3, 3, 3,
           3, 1, 1, 4, 2, 2, 1, 4, 4, 4, 2, 2, 2, 3, 3, 4, 1, 2, 4, 2, 2, 2, 1, 1, 4, 2, 4, 4, 2, 4, 4, 2, 1, 1, 2, 4, 4, 4, 2, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 4, 4, 3, 3, 3, 4, 4, 4, 4, 2)
    dealer_card1 = request.form.get("card_input_dealer1")
    card1 = request.form.get("card_input1")
    card2 = request.form.get("card_input2")
    card3 = request.form.get("card_input3")
    card4 = request.form.get("card_input4")
    card5 = request.form.get("card_input5")
    card6 = request.form.get("card_input6")
    card7 = request.form.get("card_input7")
    card8 = request.form.get("card_input8")
    card9 = request.form.get("card_input9")
    card10 = request.form.get("card_input10")
    card11 = request.form.get("card_input11")
    amount_of_cards = int(request.form.get("amout_cards"))
    inputs = [dealer_card1, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11]
    ace = False
    pair = False
    move = 0
    legit = True
    for i in range(amount_of_cards+1):
        if inputs[i] == None:
            legit = False
    if legit == True:
        current_hand = []
        for i in range(amount_of_cards+1):
            current_hand.append(int(inputs[i]))
        current_hand.pop(0)
        dealer_cards = [int(inputs[0])]

        if sum(current_hand) > 21:  #überprüfung ob man Ass hat, wenn man zu viel zieht, sonst busted
            for i, card in enumerate(current_hand):
                if card == 11 and sum(current_hand) > 21:
                    current_hand[i] = 1 
                    #print(hand)

        for i, card in enumerate(current_hand):
            if card == 11:
                ace = True
        if current_hand[0] == current_hand[1] and len(current_hand) == 2 :
            pair = True
        if ace == False and pair == False:
            move = next_move[dealer_cards[0] -2 + 10 * (sum(current_hand)-5)]

        elif ace == True and pair == False:
            move = next_move[dealer_cards[0] -2 + 10 * (sum(current_hand)+3)]
        elif pair == True:
            move = next_move[dealer_cards[0] -2 + 10 * (current_hand[0] + 22)]
        print(current_hand)
        if sum(current_hand) == 21:
            return render_template("actions.html", entries = "Du hast bereits eine Summe von 21!")
        if move == 1:
            aktion = "Hit"
        if move == 2:
            aktion = "Stand"
        if move == 3:
            aktion = "Double Down"
        if move == 4:
            aktion = "Split"
        return render_template("actions.html", entries = "Empfohlene Aktion: " + aktion)
    else:
        return redirect(url_for("views.home"))


@zuruck.route('reset', methods = ['POST', 'GET'])
def reset():
    return redirect(url_for("views.home"))