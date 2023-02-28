import random
# наши масти
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
# ранги карт
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    # [0] - запись нужда для "распоковки"
    return f"The {rank[0]} of {card[0]}"

print(pick_a_card())
