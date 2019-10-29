#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter, defaultdict
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type=="all":
        wines = [*RED_WINES, *WHITE_WINES, *SPARKLING_WINES]
    elif wine_type == "red":
        wines = RED_WINES
    elif wine_type == "white":
        wines = WHITE_WINES
    elif wine_type == "sparkling":
        wines = SPARKLING_WINES
    else:
        raise ValueError(f"Unknown wine type: {wine_type}")
    result = list()
    wine_cheeses = {k: v for (k,v) in match_wine_5cheeses()}

    for wine in wines:
        result.append((wine, wine_cheeses[wine][0], calc_similarity(wine, wine_cheeses[wine][0])))
    return sorted(result, key=operator.itemgetter(2), reverse=True)[0]
    


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """

    result = [] 
    for wine in [*RED_WINES, *WHITE_WINES, *SPARKLING_WINES]:
        result.append((wine, [n for (n,c) in score_cheeses_for_wine(wine)][:5]))
    return sorted(result, key=operator.itemgetter(0))

def score_cheeses_for_wine(wine):
    """
    Return a sorted list of tuples containing (name, score) of the match with the
    given wine. 
    """
    result = []
    for cheese in CHEESES:
        result.append((cheese,calc_similarity(wine, cheese)))

    result = [(n,s) for n,s in sorted(result, key=operator.itemgetter(0), reverse=False)]
    result = sorted(result, key=operator.itemgetter(1), reverse=True)
    return result


def calc_similarity(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    common_chars= [c for c in name1 if c in name2]
    counter1 = Counter(name1)
    counter2 = Counter(name2)
    result = []
    
    for c,n1 in counter1.items():
        if c not in common_chars:
            continue
        n2 = counter2[c]
        result.append(min(n1,n2))
    return sum(result)/(1 + pow(len(name1) - len(name2),2))

if __name__ == "__main__":
    print(best_match_per_wine())
