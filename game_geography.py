import random
import json
import csv
import numpy as np
from fuzzywuzzy import fuzz

def load_game_state(N):
    try:
        with open(r'C:\Users\quent\OneDrive\Documents\Codes\geography_game_state.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [1] * N
    

def load_countries():
    countries_and_capitals = {"Country":[],"Capital":[]};
    with open(r'C:\Users\quent\OneDrive\Documents\Codes\liste-197-etats-2020.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)        #Don't read the first line
        for row in reader:
            countries_and_capitals["Country"].append(row[0])
            countries_and_capitals["Capital"].append(row[5])
    return countries_and_capitals
    # try:
    #     file_path = r'C:\Users\quent\OneDrive\Documents\Codes\pays-json-master\All_countries.ts'
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #         # Read the content of the file
    #         return file.read()
    # except FileNotFoundError:
    #     return {}

def save_game_state(game_state):
    with open(r'C:\Users\quent\OneDrive\Documents\Codes\geography_game_state.json', 'w') as f:
        json.dump(game_state, f)

def choose_random_pair(weights, list_countries):
    N = len(list_countries['Country'])
    # Create a CDF from the PDF given by the weights
    x = range(0, N)
    cdf_values = [sum(weights[:x[i]])/N for i in range(0, N)]
    random_num = random.uniform(0, 1)
    # Find a pair at random by finding the index of the closest value in cdf_values to random_num
    closest_index = np.abs(np.array(cdf_values) - random_num).argmin()

    return closest_index

def check_correct_answer(real_answer, user_answer):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'orange': '\033[93m',
        'reset': '\033[0m'
    }

    correct = True
    # Define a threshold for similarity (e.g., 85%)
    similarity_threshold = 85

    # Check if the user's answer is similar enough to the correct capital
    similarity_ratio = fuzz.ratio(real_answer.lower(), user_answer.lower())

    if similarity_ratio == 100:
        print(colors['green'] + "Correct!" + colors['reset'])
    elif similarity_ratio >= similarity_threshold:
        print(colors['orange'] + f"Correct! The correct spelling is {real_answer}" + colors['reset'])
    else:
        print(colors['red'] + f"Incorrect! The correct answer was {real_answer}." + colors['reset'])
        correct = False
    return correct


def update_weights(weights, item):
    weights[item] += 1

def main():
    list_countries = load_countries()
    weights = load_game_state(len(list_countries['Capital']))
    print("Welcome to the Country-Capital Guessing Game!")
    print("Enter 'quit' to exit.")
    continue_game = True
    
    while continue_game:
        item = choose_random_pair(weights, list_countries)
        is_find_capital = random.randint(0, 1)

        if is_find_capital:
            question = f"What is the capital of {list_countries['Country'][item]}? "
            real_answer = list_countries['Capital'][item]
        else:
            question = f"What is the country whose capital is {list_countries['Capital'][item]}? "
            real_answer = list_countries['Country'][item]
            
        user_answer = input(question)

        if user_answer.lower() == 'quit':
            save_game_state(weights)
            continue_game = False

        else:
            if not check_correct_answer(real_answer, user_answer):
                update_weights(weights, item)



if __name__ == "__main__":
    main()
