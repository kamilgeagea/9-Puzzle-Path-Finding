import time
from dfs import depth_first_search
from utility_functions import generate_puzzle


def iterative_deepening(matrix):
    start_time = time.time()

    k = 1
    while True:
        if time.time() - start_time > 60:
            return {
                "data": "No solutions - Time exceeded",
                "execution_time": time.time() - start_time
            }

        results = depth_first_search(matrix, k)

        if type(results["data"]) is list:
            finish_time = time.time() - start_time

            return {
                "data": results["data"],
                "execution_time": finish_time
            }

        k = k + 1
