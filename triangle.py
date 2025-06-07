import turtle
import random

TRIANGLE_HEIGHT = 400
BACKGROUND_COLOR = 'black'
DEFAULT_PLOT_COLOR = 'yellow'
PLOT_SPEED = 0
DOT_COUNT = 10_000


def draw_triangle(height, plot_func):
    """Draws an equilateral triangle and returns its vertices."""
    a = (0, height / 2)
    b = (height / 2, -height / 2)
    c = (-height / 2, -height / 2)
    for vertex in (a, b, c):
        turtle.penup()
        turtle.goto(vertex)
        plot_func()
    return (a, b, c)


def random_point_in_triangle(vertices, plot_func):
    """Returns a random point inside the triangle defined by vertices."""
    a, b, c = vertices
    r1 = random.random()
    r2 = random.random()
    sqrt_r1 = r1 ** 0.5
    x = (1 - sqrt_r1) * a[0] + (sqrt_r1 * (1 - r2)) * \
        b[0] + (sqrt_r1 * r2) * c[0]
    y = (1 - sqrt_r1) * a[1] + (sqrt_r1 * (1 - r2)) * \
        b[1] + (sqrt_r1 * r2) * c[1]
    turtle.penup()
    turtle.goto(x, y)
    plot_func()
    return (x, y)


def chaos_game(start_point, vertices, count, plot_func):
    """Performs the chaos game algorithm to plot points."""
    point = start_point
    for _ in range(count):
        vertex = random.choice(vertices)
        midpoint = ((vertex[0] + point[0]) / 2, (vertex[1] + point[1]) / 2)
        point = midpoint
        turtle.penup()
        turtle.goto(midpoint)
        plot_func()


def get_user_input():
    """Gets all customizable options from user."""
    bg_color = input(
        f"Enter background color (default '{BACKGROUND_COLOR}'): ") or BACKGROUND_COLOR
    plot_color = input(
        f"Enter plot color (default '{DEFAULT_PLOT_COLOR}'): ") or DEFAULT_PLOT_COLOR
    try:
        plot_speed = int(input(
            f"Enter plot speed (0=fastest, default {PLOT_SPEED}): ") or PLOT_SPEED)
    except ValueError:
        plot_speed = PLOT_SPEED
    try:
        dot_count = int(input(
            f"Enter dot count (default {DOT_COUNT}): ") or DOT_COUNT)
    except ValueError:
        dot_count = DOT_COUNT
    try:
        triangle_height = int(input(
            f"Enter triangle height (default {TRIANGLE_HEIGHT}): ") or TRIANGLE_HEIGHT)
    except ValueError:
        triangle_height = TRIANGLE_HEIGHT
    text = input("Enter text if you want to plot text (leave blank for dot): ")
    char_only = False
    if text:
        char_bool = input(
            "Should we randomize the character on the text (Y/N)? ")
        char_only = char_bool.strip().lower() == "y"
    return plot_color, bg_color, plot_speed, dot_count, triangle_height, text, char_only


def make_plot_func(plot_color, plot_text, char_only):
    """Returns a plot function customized with user input."""
    def plot():
        turtle.color(plot_color)
        if plot_text:
            if char_only:
                turtle.write(random.choice(plot_text))
            else:
                turtle.write(plot_text)
        else:
            turtle.dot(plot_color)
    return plot


def main():
    customize = input(
        "Do you want to customize the plotting? (Y/N): ").strip().lower()
    if customize == "y":
        plot_color, bg_color, plot_speed, dot_count, triangle_height, plot_text, char_only = get_user_input()
    else:
        plot_color = DEFAULT_PLOT_COLOR
        bg_color = BACKGROUND_COLOR
        plot_speed = PLOT_SPEED
        dot_count = DOT_COUNT
        triangle_height = TRIANGLE_HEIGHT
        plot_text = ""
        char_only = False
    plot_func = make_plot_func(plot_color, plot_text, char_only)
    turtle.bgcolor(bg_color)
    turtle.speed(plot_speed)
    vertices = draw_triangle(triangle_height, plot_func)
    start_point = random_point_in_triangle(vertices, plot_func)
    chaos_game(start_point, vertices, dot_count, plot_func)
    turtle.done()


if __name__ == "__main__":
    main()
