import turtle
import math

def draw_pythagoras_tree(t, length, level):
    """
    Рекурсивно малює гілку дерева Піфагора.

    :param t: Об'єкт Turtle для малювання.
    :param length: Довжина поточної гілки.
    :param level: Поточний рівень рекурсії, що залишився.
    """
    # Базовий випадок: якщо рівень рекурсії 0, припиняємо малювати.
    if level == 0:
        # Додамо невеликий "листочок" для кращого візуального ефекту
        t.dot(4, "green")
        return

    # Встановлюємо колір та товщину гілки залежно від рівня
    # Чим глибше, тим гілки тонші та зеленіші
    t.width(level)
    if level > 5:
        t.color("#8B4513") # Коричневий для стовбура
    else:
        t.color("#228B22") # Лісовий зелений для гілок

    # 1. Малюємо поточну гілку (стовбур)
    t.forward(length)

    # 2. Зберігаємо поточну позицію та напрямок
    current_pos = t.pos()
    current_heading = t.heading()

    # 3. Малюємо ліву гілку
    t.left(45)
    # Рекурсивно викликаємо функцію для меншої гілки.
    # Нова довжина = length / sqrt(2) ≈ length * 0.707
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    # 4. Повертаємося до точки розгалуження, щоб намалювати праву гілку
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown()

    # 5. Малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

    # 6. Повертаємося у вихідну точку та відновлюємо напрямок
    # Це критично важливо, щоб черепашка повернулася у стан, 
    # в якому вона була до виклику поточної функції.
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown()


    t.width(level)
    t.backward(length)


def main():
    """
    Основна функція для налаштування сцени та запуску малювання.
    """
    # Налаштування вікна для малювання
    screen = turtle.Screen()
    screen.title("Фрактал 'Дерево Піфагора'")
    screen.bgcolor("lightblue")

    # Запитуємо у користувача рівень рекурсії
    try:
        level = int(screen.numinput("Рівень рекурсії", "Введіть бажаний рівень рекурсії (рекомендовано 1-12):", default=10, minval=1, maxval=15        ))
    except (TypeError, ValueError):
        # Випадок, коли користувач закриває вікно вводу
        return

    # Налаштування "черепашки" (об'єкта, що малює)
    t = turtle.Turtle()
    t.speed(0)  # 0 - максимальна швидкість малювання
    t.hideturtle() # Ховаємо саму черепашку
    t.left(90)   # Повертаємо її вгору

    # Початкова позиція внизу по центру екрана
    t.penup()
    initial_length = screen.window_height() / 4
    t.goto(0, -screen.window_height() / 2 + 20)
    t.pendown()
    
    # Запускаємо рекурсивне малювання
    draw_pythagoras_tree(t, initial_length, level)

    # Програма чекає, доки користувач закриє вікно
    screen.mainloop()

if __name__ == "__main__":
    main()
