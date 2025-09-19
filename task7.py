import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(trials=1000000):
    """
    Simulates rolling two dice and calculates the sum of the rolls.

    The function returns two dictionaries: results and probabilities. The results
    dictionary contains the sum of each roll as keys and the number of times
    each sum was rolled as values. The probabilities dictionary contains the
    sum of each roll as keys and the probability of each sum as values.

    Parameters
    ----------
    trials : int
        The number of trials to simulate. Defaults to 1,000,000.

    Returns
    -------
    tuple
        A tuple containing two dictionaries: results and probabilities.
    """
    results = {s: 0 for s in range(2, 13)}
    for _ in range(trials):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        s = roll1 + roll2
        results[s] += 1

    probabilities = {s: count / trials for s, count in results.items()}
    return results, probabilities

if __name__ == "__main__":
    trials = 1000000
    results, probabilities = monte_carlo_dice_simulation(trials)

    print("Сума\tКількість\tІмовірність (%)\tАналітична імовірність (%)\tВідхилиння (%)")
    analytic_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    for s in range(2, 13):
        print(f"{s}\t{results[s]}\t\t{probabilities[s]*100:.2f}\t\t\t{analytic_probs[s]:.2f}\t\t\t{(analytic_probs[s]-probabilities[s]*100):.2f}")

    # Побудова графіка
    sums = list(range(2, 13))
    probs = [probabilities[s] for s in sums]
    analytic = [analytic_probs[s]/100 for s in sums]
    plt.bar(sums, probs, color="#1296F0", label="Монте-Карло")
    plt.plot(sums, analytic, color="red", marker="o", linestyle="--", label="Аналітична")
    plt.xticks(sums)
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Імовірність")
    plt.title(f"Ймовірності сум при киданні двох кубиків ({trials} симуляцій)")
    plt.legend()
    plt.grid(axis='y', linestyle=':')
    plt.show()