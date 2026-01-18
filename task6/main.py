def max_calories_to_cost_dynamic(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + calories
                )
            else:
                dp[i][b] = dp[i - 1][b]

    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, data = item_list[i - 1]
            chosen_items.append(name)
            b -= data["cost"]

    chosen_items.reverse()

    return {
        "items": chosen_items,
        "total_cost": budget - b,
        "total_calories": dp[n][budget]
    }


def max_calories_to_cost_greedy(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return {
        "items": chosen_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }



if __name__ == "__main__":
    budget = 100
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    print("Food list chosen by greedy algorithm:")
    print(max_calories_to_cost_greedy(items, budget))

    print("Food list chosen by dynamic algorithm:")
    print(max_calories_to_cost_dynamic(items, budget))
