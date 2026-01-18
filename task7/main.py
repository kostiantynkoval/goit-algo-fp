import random
from collections import defaultdict
import matplotlib.pyplot as plt

TWO_DICE_SUM_PROBABILITIES = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}


def monte_carlo_dice_simulation(num_rolls=10000):
    sums_count = defaultdict(int)

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    probabilities = {
        s: count / num_rolls
        for s, count in sums_count.items()
    }
    print(probabilities)
    return probabilities


def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    probs = [probabilities[s] for s in sums]
    theoretical_probs = [TWO_DICE_SUM_PROBABILITIES[s] for s in sums]

    plt.figure(figsize=(9, 5))

    plt.bar(sums, probs,width=0.6,label="Monte Carlo",alpha=0.6, color="blue")
    plt.bar(sums, theoretical_probs,width=0.3,label="Theoretical probability",alpha=0.8,color="green")

    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability")
    plt.title("Sum of Two Dice - Monte Carlo vs Theoretical Probability")
    plt.legend(fontsize=10,frameon=True)
    plt.xticks(sums)
    plt.grid(axis="y", alpha=0.1)
    plt.show()


if __name__ == "__main__":
    probabilities = monte_carlo_dice_simulation(100_000)
    plot_probabilities(probabilities)
    print("Sum | Monte-Carlo | Theoretical")
    print("-------------------------------")
    for s in range(2, 13):
        print(f"{s:>3} | {probabilities[s]:11f} | {TWO_DICE_SUM_PROBABILITIES[s]:9f} |")