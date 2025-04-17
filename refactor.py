import pygame
from pygame.gfxdraw import ellipse, circle


def draw_hare(surface, x, y, width, height, color):
    body_width = width // 1.5
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)

    # Рисуем розовое пузико (овал чуть меньше тела)
    belly_width = body_width // 1.2
    belly_height = body_height // 1.5
    draw_belly(surface, x, body_y, belly_width, belly_height)

    head_size = height // 4  # Размер квадратной головы
    head_y = y - head_size // 2
    draw_head(surface, x, head_y, head_size, color)

    # Рисуем глаза после головы, чтобы они были поверх
    eye_size = head_size // 8
    draw_eyes(surface, x, head_y, head_size, eye_size)

    # Добавляем ресницы к глазам
    draw_eyelashes(surface, x, head_y, head_size, eye_size)

    # Рисуем розовый рот после головы
    mouth_width = head_size // 4
    mouth_height = head_size // 10
    mouth_y = head_y + head_size // 4
    draw_mouth(surface, x, mouth_y, mouth_width, mouth_height)

    # Рисуем усы после рта
    draw_whiskers(surface, x, mouth_y, head_size)

    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2 - 30
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)

    # Нижние лапы (задние)
    leg_height = height // 16
    leg_y = y + height // 2 + 20 - leg_height // 2
    for leg_x in (x - width // 4 - 20, x + width // 4 + 20):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)

    # Верхние лапы (передние)
    leg_height = height // 16
    leg_y = y + height // 2 - 120 - leg_height // 2
    for leg_x in (x - width // 4 - 20, x + width // 4 + 20):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)


def draw_eyelashes(surface, head_x, head_y, head_size, eye_size):
    """Рисуем ресницы для глаз"""
    # Положение глаз относительно центра головы
    eye_y = head_y - head_size // 10




def draw_belly(surface, x, y, width, height):
    belly_color = (255, 182, 193)  # Розовый цвет
    pygame.draw.ellipse(surface, belly_color,
                        (x - width // 2, y - height // 2, width, height))


def draw_whiskers(surface, x, y, head_size):
    whisker_length = head_size // 1.5
    # Вертикальное смещение для верхних и нижних усов
    for dy in (-head_size // 12, 0, head_size // 12):
        # Левые усы (3 линии)
        pygame.draw.line(surface, (0, 0, 0),
                         (x, y + dy),
                         (x - whisker_length, y + dy - head_size // 12), 1)
        pygame.draw.line(surface, (0, 0, 0),
                         (x, y + dy),
                         (x - whisker_length, y + dy), 1)
        pygame.draw.line(surface, (0, 0, 0),
                         (x, y + dy),
                         (x - whisker_length, y + dy + head_size // 12), 1)
        # Правые усы (3 линии)
        pygame.draw.line(surface, (0, 0, 0),
                         (x, y + dy),
                         (x + whisker_length, y + dy - head_size // 12), 1)
        pygame.draw.line(surface, (0, 0, 0),
                         (x, y + dy),
                         (x + whisker_length, y + dy), 1)
        pygame.draw.line(surface, (0, 0, 0),
                         (x, y + dy),
                         (x + whisker_length, y + dy + head_size // 12), 1)


def draw_mouth(surface, x, y, width, height):
    mouth_color = (255, 105, 180)  # Ярко-розовый цвет
    pygame.draw.rect(surface, mouth_color, (x - width // 2, y - height // 2, width, height))


def draw_eyes(surface, head_x, head_y, head_size, eye_size):
    # Положение глаз относительно центра головы
    eye_y = head_y - head_size // 10  # Чуть выше центра головы
    for eye_x in (head_x - head_size // 6, head_x + head_size // 6):
        # Белок глаза
        pygame.draw.circle(surface, (255, 255, 255), (eye_x, eye_y), eye_size)
        # Зрачок
        pygame.draw.circle(surface, (0, 0, 0), (eye_x, eye_y), eye_size // 2)


def draw_body(surface, x, y, width, height, color):
    pygame.draw.rect(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    pygame.draw.rect(surface, color, (x - size // 2, y - size // 2, size, size))


def draw_ear(surface, x, y, width, height, color):
    # Внешняя часть уха
    pygame.draw.rect(surface, color, (x - width // 2, y - height // 2, width, height))
    # Внутренняя розовая часть уха (меньше по размеру)
    inner_width = width // 1.5
    inner_height = height // 1.5
    inner_color = (255, 182, 193)  # Розовый цвет
    pygame.draw.rect(surface, inner_color,
                     (x - inner_width // 2, y - inner_height // 2 + height // 8,
                      inner_width, inner_height))


def draw_leg(surface, x, y, width, height, color):
    pygame.draw.rect(surface, color, (x - width // 2, y - height // 2, width, height))


# Пример использования
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

# Рисуем зайца
draw_hare(screen, 400, 300, 200, 400, (150, 150, 150))

pygame.display.flip()

# Ждем закрытия окна
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()