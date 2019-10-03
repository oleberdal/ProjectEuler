"""
Author: Berdal, Ole
Created: 05.02.2019
Edited: 03.10.2019
Version: Python 3.7.4

https://projecteuler.net/problem=15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import time
start_time = time.time()


def routes_in_grid(x, y, routes):
    if (x, y) in routes:
        return routes[x, y]
    elif y > x:
        route = routes_in_grid(x=y, y=x, routes=routes)
    elif y == 0:
        route = 1
    else:
        route = routes_in_grid(x=x, y=y - 1, routes=routes) + routes_in_grid(x=x - 1, y=y, routes=routes)
    routes[x, y] = route
    return route


def main():
    solution = routes_in_grid(x=20, y=20, routes={})

    print('Solution: %s.\nExecution time: %s seconds.' % (solution, time.time() - start_time))


if __name__ == '__main__':
    main()
