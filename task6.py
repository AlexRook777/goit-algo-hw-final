
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій/вартість
    """
    Рішення класичної задачі про рюкзак (0/1 knapsack) за допомогою жадібного алгоритму.

    :param items: Словник, де ключ - назва страви, а значення - словник з інформацією про страву.
    :param budget: Бюджет, з якого потрібно вибрати страви.
    :return: Список вибраних страв та їх загальна кількість калорій.
    """
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen = []
    for name, info in sorted_items: # Перебираємо страви у відсортованому порядку
        if total_cost + info['cost'] <= budget: # Якщо вартість страви не перевищує бюджет
            chosen.append(name) # Вибираємо цю страву
            total_cost += info['cost']
            total_calories += info['calories']
    return chosen, total_calories

def dynamic_programming(items, budget):
    """
    Рішення класичної задачі про рюкзак (0/1 knapsack)
    за допомогою динамічного програмування.

    :param items: Словник, де ключ - назва страви, а значення - словник з інформацією про страву.
    :param budget: Бюджет, з якого потрібно вибрати страви.
    :return: Список вибраних страв та їх загальна кількість калорій.
    """
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]  # Таблиця динамічного програмування

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        name = names[i-1]
        cost = items[name]['cost']
        calories = items[name]['calories']
        for w in range(budget + 1): # Перебираємо всі можливі бюджети
            if cost <= w: # Якщо вартість страви не перевищує поточний бюджет
                if dp[i-1][w] < dp[i-1][w-cost] + calories: # Вибираємо максимальне значення
                    dp[i][w] = dp[i-1][w-cost] + calories # Вибираємо цю страву
                else:
                    dp[i][w] = dp[i-1][w] # Не вибираємо цю страву
            else:
                dp[i][w] = dp[i-1][w] # Не вибираємо цю страву

    # Відновлюємо вибрані страви
    res = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name = names[i-1]
            res.append(name)
            w -= items[name]['cost']
    res.reverse()
    return res, dp[n][budget]

if __name__ == "__main__":

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100
    print('There are 2 algorithms to solve the problem of maximizing calories within a budget:')
    print('Budget:', budget)
    print('Items:', items)

    print("Greedy algorithm:")
    chosen, calories = greedy_algorithm(items, budget)
    total_spent = sum(items[name]['cost'] for name in chosen)
    print("Chosen:", chosen)
    print("Total calories:", calories)
    print("Total spent:", total_spent, "of", budget)

    print("\nDynamic programming:")
    chosen, calories = dynamic_programming(items, budget)
    total_spent = sum(items[name]['cost'] for name in chosen)
    print("Chosen:", chosen)
    print("Total calories:", calories)
    print("Total spent:", total_spent, "of", budget)