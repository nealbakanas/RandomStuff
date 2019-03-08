from __future__ import print_function
from itertools import *
import random
import sys
from fpdf import FPDF

def create_cards(p):
    for min_factor in range(2, 1 + int(p ** 0.5)):
        if p % min_factor == 0:
            break
    else:
        min_factor = p
    cards = []
    for i in range(p):
        cards.append(set([i * p + j for j in range(p)] + [p * p]))
    for i in range(min_factor):
        for j in range(p):
            cards.append(set([k * p + (j + i * k) % p
                              for k in range(p)] + [p * p + 1 + i]))

    cards.append(set([p * p + i for i in range(min_factor + 1)]))
    return cards, p * p + p + 1


def check_cards(cards):
    for card, other_card in combinations(cards, 2):
        if len(card & other_card) != 1:
            print("Cards", sorted(card), "and", sorted(other_card),
                  "have intersection", sorted(card & other_card))


order = 7
cards, num_pictures = create_cards(order)


pdf = FPDF()
positions_dict = {0:(25,125),1:(75,100),2:(45,175),3:(95,150),4:(125,80),5:(35,55),6:(145,135),7:(115,200),8:(85,35)}

query = r'C:\Users\neal\Documents\spotit\{}.jpg'
for card in cards:
    positions = random.sample(range(9), order+1)
    pdf.add_page()
    card = list(card)
    for number in card:
        link_path = query.format(number)
        pdf.image(link_path, positions_dict[positions[card.index(number)]][0],
                  positions_dict[positions[card.index(number)]][1], 50, 50)


pdf.output("momit.pdf", "F")

