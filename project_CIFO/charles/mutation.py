from random import random, randint, sample, choice
import numpy as np


def swap_mutation(individual):
    """Swap mutation for an individual.
    Swaps the position of two randomly chosen genes.

    Args:
        individual (Individual): An individual object.

    Returns:
        Individual: Mutated individual in place.
    """
    mut_indexes = sample(range(0, len(individual)), 2)
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]
    return individual


def creep_mutation(individual):
    """
    Creep mutation for an individual.
    Slightly alters the value of a randomly chosen gene.

    Args:
        individual (Individual): An individual object where each gene represents a certain quantity.

    Returns:
        Individual: Mutated individual in place.
    """
    index = randint(0, len(individual) - 1)  # select a random index
    individual[index] += choice([-0.05, 0.05])  # slightly alter its value
    individual[index] = min(max(0, individual[index]), 1)  # ensure the quantity stays within bounds
    return individual


def uniform_mutation(individual, mutation_rate=0.5):
    """
    Uniform mutation changes the value of a gene chosen uniformly at random  from a set of all possible values.
    This implementation uses a mutation rate to decide whether a gene should be mutated.
    Each gene in the individual can be mutated with a probability equal to the mutation rate.

    Args:
        individual (list): The individual to mutate.
        mutation_rate (float): The probability of each gene being mutated.

    Returns:
        list: The mutated individual.
    """
    mutated_solution = individual[:]  # Create a copy of the original solution

    for i in range(len(mutated_solution)):
        if random() < mutation_rate:
            mutated_solution[i] = choice(np.arange(0, 1.01, 0.01))

    return mutated_solution


def random_resetting(individual):
    """
    Random resetting mutation for an individual.
    Randomly assigns a new value to a selected gene.

    Args:
        individual (Individual): An individual object where each gene represents a certain quantity.

    Returns:
        Individual: Mutated individual in place.
    """
    index = randint(0, len(individual) - 1)  # select a random index
    individual[index] = choice(np.arange(0, 1.01, 0.01))  # reset its value to a random quantity
    return individual
