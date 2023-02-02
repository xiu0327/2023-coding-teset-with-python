from itertools import product

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

n = len(emoticons)

discount = [10, 20, 30, 40]
cases = product(discount, repeat=n)

result = []


def get_price(price, disc):
    return int(price - (price * disc * 0.01))


for i, case in enumerate(cases):
    amount = 0
    subscriber = 0

    for user in users:
        user_discount, user_price = user
        user_amount = sum([get_price(emoticons[j], item) for j, item in enumerate(case) if item >= user_discount])

        if user_amount >= user_price:
            subscriber += 1
        else:
            amount += user_amount

    result.append([subscriber, amount])

print(sorted(result, key=lambda x: [-x[0], -x[1]])[0])
