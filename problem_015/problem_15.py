"""
Author: Berdal, Ole
Created: 05.02.2019
Edited: 07.02.2019
Version: Python 3.6.7

https://projecteuler.net/problem=15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import time
start_time = time.time()


def routes_in_grid(x, y, routes):
    if (x, y) in routes:
        return routes[x, y]
    elif x > y:
        route = routes_in_grid(y, x, routes)
    elif x == 0:
        route = 1
    else:
        route = routes_in_grid(x - 1, y, routes) + routes_in_grid(x, y - 1, routes)
    routes[x, y] = route
    return route


def main():
    solution = routes_in_grid(20, 20, {})

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
