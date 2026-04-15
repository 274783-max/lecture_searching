from random import choices
import json
import random
import time
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

plt.plot(sizes, times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()


def test_complexity(list_of_n):
    for n in list_of_n:
        unordered_data = unordered_sequences(n)
        ordered_data = ordered_sequences(n)
        duration_linear = 0
        repetition = 100
        for measurements in range(repetition):
            sart_time_linear = time.perf_counter()
            found_number = linear_search(unordered_data, target_numbmer)
            end_time_bianry = time.perf_counter()
            duration += end_time - start_time
            times_linear.append(duration linear / repetitions)
            times_binary.append(duration_binary / repetitions)
        print(time_linear)
        print(times_binary)



def unordered_sequence(max_len=100):
    """
    Generates a list of random integers in arbitrary order.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: List of randomly selected integers from range -1000 to 999.
    """
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    """
    Generates a sorted list of random integers.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: Sorted list of randomly selected integers
        from range -1000 to 999.
    """
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    """
    Generates a random DNA sequence.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        str: String composed of characters "A", "C", "G", "T".
    """
    return "".join(choices("ACGT", k=max_len))


def main():
    """
    Runs basic tests for sequence generation functions.
    """
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))


if __name__ == "__main__":
    main()
