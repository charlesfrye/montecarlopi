"""Compute pi using monte carlo approach."""
import math
import multiprocessing
import random
import time

import psutil


def mcpi(iterations):
    num_cpus = psutil.cpu_count(logical=True)  # real and virtual

    now = time.time()
    total_inside = proc_monte_carlo_pi(num_cpus, iterations)

    stop = time.time()
    total_iterations = num_cpus * iterations
    elapsed = stop - now
    pi = total_inside / total_iterations * 4
    calculations_string = round(total_iterations / elapsed)
    return (pi, f'{calculations_string:,}')


def monte_compute(iterations):
    inside = 0
    random.seed()
    for _ in range(iterations):
        a = random.random()
        b = random.random()
        c = math.pow(a, 2.0) + math.pow(b, 2.0)
        if c <= 1.0:
            inside += 1
    return inside


def proc_monte_carlo_pi(num_cpus, iterations):
    with multiprocessing.Pool(num_cpus) as p:
        results = p.map(monte_compute, [iterations] * num_cpus)
        total_inside = sum(results)
    return total_inside
