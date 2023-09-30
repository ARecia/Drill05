from pico2d import *
import random
import math

# Initialize Pico2D
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow_image = load_image('hand_arrow.png')

def handle_events():
    global running, boy_x, boy_y
    global hand_y, boy_direction

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
boy_x, boy_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)  # 마우스 위치 초기화
boy_direction = 1

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow_image.draw(hand_x, hand_y)

    dx = hand_x - boy_x
    dy = hand_y - boy_y
    distance = math.sqrt(dx**2 + dy**2)

    if distance > 0:
        boy_x += (dx / distance) * 2
        boy_y += (dy / distance) * 2

    if dx < 0:
        boy_direction = -1  # Left
    elif dx > 0:
        boy_direction = 1  # Right

    if abs(dx) <= 2 and abs(dy) <= 2:
        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

    character.clip_draw(0, 0, 100, 100, boy_x, boy_y, boy_direction * 100, 100)
    update_canvas()
    handle_events()

close_canvas()