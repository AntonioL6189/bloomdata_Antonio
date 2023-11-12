import random
import numpy as np
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    adj = random.choice(ADJECTIVES)
    noun = np.random.choice(NOUNS)
    random_names = adj + ' ' + noun
    random_price = random.randint(5, 100)
    random_weight = random.randint(5, 100)
    random_flammability = random.uniform(0.0, 2.5)
    for i in range(num_products):
        products.append(Product(random_names, random_price,
                        random_weight, random_flammability))
    return products


def inventory_report(products):
    unique_product_names = len(set(product.name for product in products))

    total_price = sum(product.price for product in products)
    average_price = total_price / len(products)

    total_weight = sum(product.weight for product in products)
    average_weight = total_weight / len(products)

    total_flammability = sum(product.flammability for product in
                             products)
    average_flammability = total_flammability / len(products)

    return (unique_product_names, average_price, average_weight,
            average_flammability)


if __name__ == '__main__':
    print(inventory_report(generate_products()))
