import argparse
from typing import List

import numpy as np

def menu(menu: List[str]) -> str:
    dinner = {}
    for _ in range(10000):
        rand = np.random.choice(menu)
        dinner[rand] = dinner.get(rand, 0) + 1
    return max(dinner, key=dinner.get)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="What is your menu")
    parser.add_argument('--menu', type=List[str], required=True,
                         help="Menu list of strings")
    args = parser.parse_args()
    result = menu(args.menu)
    print(f"Your menu is {result}!")
