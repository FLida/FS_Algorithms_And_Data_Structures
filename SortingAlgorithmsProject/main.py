from InsertionSort import Insertion_Sort
import time
import random
import matplotlib.pyplot as plt

scenario_list = ["good", "base", "worse"]
color_list = ["red", "blue", "green"]
lengths_to_run = list(range(1, 1000, 100))
list_results = []

def Run_Sort(list_, scenario):
    if scenario == "good":
        pass
    elif scenario == "base":
        random.shuffle(list_)
    elif scenario == "worse":
        list_.reverse()

    time_begin = time.time()
    Insertion_Sort(list_to_sort=list_)
    time_end = time.time()
    time_elapsed = time_end - time_begin

    return time_elapsed

if __name__ == '__main__':
    for current_scenario, scenario_color in zip(scenario_list, color_list) :
        for lengths in lengths_to_run:
            list_to_be_sorted = list(range(1, lengths))
            time_elapsed = Run_Sort(list_=list_to_be_sorted, scenario=current_scenario )
            list_results.append(time_elapsed)
        print("scenario:", current_scenario)
        print(list_results)
        plt.plot(lengths_to_run, list_results, color=scenario_color, label=current_scenario)
        list_results.clear()
    plt.legend()
    plt.show()