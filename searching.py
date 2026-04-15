from pathlib import Path
import json

from generators import unordered_sequence



"""
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
   # cwd_path = Path.cwd()
    
   # file_path = cwd_path / file_name

import json
def read_data(filename, field):
    with open("sequential.json", "r") as f:
        data = json.load(f)
        if field in data.keys():
            return data[field]
        else:
            return None


def linear_search(searched_data, target):
    positions = []

    for index, value in enumerate(searched_data):
        if value == target:
            positions.append(index)
    return {"positions": positions,
            "count": len(positions)
    }
    count = 0
    idx = 0

    #while idx < len(searched_data):
    #    for i in searched_data:
    #        if i == target:
    #            count += 1
    #            idx += 1
    #positions.append(count, idx)
    #return {searched_data["positions"] = positions
    #searched_data["count"] = count
    #}



def binary_search(searched_data, target):
    sorted(searched_data)
    s = searched_data.sort()
    left = 0
    right = len(s) - 1
    while left <= right:
        middle = (left + right) // 2
        if middle == target:
            return target
        elif middle > target:
            left = middle + 1
        elif middle < target:
            right = middle - 1
    return None



def main():
    sequential_data = read_data("sequential.json", "unordered_sequence()")
    print(sequential_data)
    #linear_data = linear_search(searched_data, target)
    #print(linear_data)



if __name__ == "__main__":
    main()

