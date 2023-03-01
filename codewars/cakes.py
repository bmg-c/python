def cakes(recipe, available):
    for product in recipe:
        if product not in available:
            return 0
        max_cakes = int(available[product] / recipe[product])
        break

    for product in recipe:
        if product not in available:
            return 0
        if max_cakes > int(available[product] / recipe[product]):
            max_cakes = int(available[product] / recipe[product])

    return max_cakes


if __name__ == "__main__":
    cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
