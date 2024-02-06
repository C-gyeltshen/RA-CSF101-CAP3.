

# import pygame
# import random

# pygame.init()
# square_width = 750
# pixel_width = 50
# screen = pygame.display.set_mode([square_width] * 2)
# clock = pygame.time.Clock()
# running = True

# # Load the background image
# background_image = pygame.image.load("backgroud2.jpeg")  # Replace "backgroud2.jpeg" with the path to your image file
# background_image = pygame.transform.scale(background_image, (square_width, square_width))

# # Load the target image
# target_image = pygame.image.load("apple 2.jpg")  # Replace "apple 2.jpg" with the path to your target image file
# target_image = pygame.transform.scale(target_image, (pixel_width, pixel_width))

# # Define font and text
# font = pygame.font.SysFont(None, 50)

# def generate_starting_position():
#     position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
#     return [random.randrange(*position_range), random.randrange(*position_range)]

# def reset():
#     snake_pixel.center = generate_starting_position()
#     return snake_pixel.copy()

# def is_out_of_bounds():
#     return snake_pixel.bottom > square_width or snake_pixel.top < 0 \
#         or snake_pixel.left < 0 or snake_pixel.right > square_width

# def snake_collision():
#     head = snake[0]
#     return head.collidelist(snake[1:]) != -1

# def game_over():
#     game_over_text = font.render("Game Over", True, (0, 0, 0))
#     screen.blit(game_over_text, (square_width // 2 - game_over_text.get_width() // 2, square_width // 2 - game_over_text.get_height() // 2))
#     pygame.display.flip()
#     pygame.time.wait(2000)  # Wait for 2 seconds
#     return "Game Over"

# snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
# snake_pixel.center = generate_starting_position()
# snake = [snake_pixel.copy()]
# snake_direction = (0, 0)
# snake_length = 1

# target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
# target.center = generate_starting_position()

# score = 0
# speed_increase_count = 0
# speed = 5

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Blit the background image onto the screen
#     screen.blit(background_image, (0, 0))

#     if is_out_of_bounds() or snake_collision():
#         game_over()
#         running = False

#     if snake_pixel.colliderect(target):
#         # Regenerate target position
#         target.center = generate_starting_position()
#         # Increase snake length
#         snake_length += 1
#         # Increase score
#         score += 1
#         # Increase speed every 3 apples
#         speed_increase_count += 1
#         if speed_increase_count == 3:
#             speed += 1
#             speed_increase_count = 0

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         snake_direction = (0, -pixel_width)
#     if keys[pygame.K_DOWN]:
#         snake_direction = (0, pixel_width)
#     if keys[pygame.K_LEFT]:
#         snake_direction = (-pixel_width, 0)
#     if keys[pygame.K_RIGHT]:
#         snake_direction = (pixel_width, 0)

#     for snake_part in snake:
#         pygame.draw.rect(screen, "green", snake_part)

#     # Blit the target image onto the screen at the target's position
#     screen.blit(target_image, target.topleft)

#     # Display score
#     score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#     screen.blit(score_text, (10, 10))

#     snake_pixel.move_ip(snake_direction)
#     snake.append(snake_pixel.copy())
#     snake = snake[-snake_length:]

#     pygame.display.flip()

#     clock.tick(speed)

# pygame.quit()




import pygame
import random

pygame.init()
square_width = 750
pixel_width = 50
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True

# Load the background image
background_image = pygame.image.load("backgroud2.jpeg")  # Replace "backgroud2.jpeg" with the path to your image file
background_image = pygame.transform.scale(background_image, (square_width, square_width))

# Load the target image
target_image = pygame.image.load("apple 2.jpg")  # Replace "apple 2.jpg" with the path to your target image file
target_image = pygame.transform.scale(target_image, (pixel_width, pixel_width))

# Define font and text
font = pygame.font.SysFont(None, 50)

# Load sound effects
eat_sound = pygame.mixer.Sound("ding.mp3")  # Replace "eat_sound.wav" with the path to your sound file

def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]

def reset():
    snake_pixel.center = generate_starting_position()
    return snake_pixel.copy()

def is_out_of_bounds():
    return snake_pixel.bottom > square_width or snake_pixel.top < 0 \
        or snake_pixel.left < 0 or snake_pixel.right > square_width

def snake_collision():
    head = snake[0]
    return head.collidelist(snake[1:]) != -1

def game_over():
    game_over_text = font.render("Game Over", True, (0, 0, 0))
    screen.blit(game_over_text, (square_width // 2 - game_over_text.get_width() // 2, square_width // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds
    return "Game Over"

snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()

score = 0
speed_increase_count = 0
speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))

    if is_out_of_bounds() or snake_collision():
        game_over()
        running = False

    if snake_pixel.colliderect(target):
        # Play eat sound
        eat_sound.play()
        # Regenerate target position
        target.center = generate_starting_position()
        # Increase snake length
        snake_length += 1
        # Increase score
        score += 1
        # Increase speed every 3 apples
        speed_increase_count += 1
        if speed_increase_count == 3:
            speed += 1
            speed_increase_count = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_direction = (0, -pixel_width)
    if keys[pygame.K_DOWN]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_LEFT]:
        snake_direction = (-pixel_width, 0)
    if keys[pygame.K_RIGHT]:
        snake_direction = (pixel_width, 0)

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    # Blit the target image onto the screen at the target's position
    screen.blit(target_image, target.topleft)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
