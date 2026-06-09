def recommend_products(budget):

    if budget > 60000:
        return [
            "Smartphone",
            "Laptop",
            "Gaming Console"
        ]

    elif budget >= 25000:
        return [
            "Watch",
            "Shoes",
            "Headphones"
        ]

    else:
        return [
            "T-Shirt",
            "Groceries",
            "Household Products"
        ]


def match_score(budget):

    if budget > 60000:
        return 95

    elif budget >= 25000:
        return 88

    else:
        return 80