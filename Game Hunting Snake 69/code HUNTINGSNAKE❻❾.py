import pygame
import time
import random
import webbrowser

pygame.init()

# Các biến âm thanh
game_over_sound = pygame.mixer.Sound('mixkit-arcade-retro-game-over-213.wav')
item_pickup_sound = pygame.mixer.Sound('item-pick-up-38258.mp3')
level_up_sound = pygame.mixer.Sound('message-incoming-132126.mp3')
finalmap_sound = pygame.mixer.Sound('level-up-bonus-sequence-3-186892.mp3')
superitem_pickup_sound = pygame.mixer.Sound('chaos-emerald-15983.mp3')
button_click_sound = pygame.mixer.Sound('click-124467.mp3')
intro_sound = pygame.mixer.Sound('neon-gaming-128925.mp3')

# Các màu sắc
purple = (153, 0, 76)
silver = (255, 204, 204)
white = (255, 255, 255)
orange = (255, 128, 0)
red = (204, 0, 0)
blue = (0, 128, 255)
green = (0, 255, 0)
pink = (255, 51, 153)
black = (0, 0, 0)
ored = (255, 69, 0)

# Kích thước màn hình mặc định
dis_width = 800
dis_height = 700

# Thiết lập màn hình
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('HUNTING SNAKE ❻❾')

clock = pygame.time.Clock()

snake_block = 10

# Thiết lập phông chữ
font_path = 'D:\\NHT\\PixeloidSansBold-PKnYd.ttf'
retro_font = pygame.font.Font(font_path, 20)
score_font = pygame.font.Font(font_path, 30)
font_style = pygame.font.Font(font_path, 22)
details_style = pygame.font.Font(font_path, 25)

# Điểm cao
high_score = 0

#Đường link giới thiệu
desired_url = "https://www.facebook.com/profile.php?id=100073106232050"

#Hàm truy cập link
def redirect_to_url(url):
    webbrowser.open(url)

# Tựa đề
def message_details(msg, color):
    mesg = details_style.render(msg, True, color)
    text_width, text_height = font_style.size(msg)
    x = (dis_width - text_width) // 2
    y = 20  # You can adjust this value to move the message higher or lower
    dis.blit(mesg, [x, y])


def draw_button():
    button_width, button_height = 120, 50
    button_x = (dis_width - button_width) // 2
    button_y = (dis_height - button_height) // 2 - 10
    pygame.draw.rect(dis, orange, [button_x, button_y, button_width, button_height])

    button_text = retro_font.render("START", True, white)
    text_width, text_height = retro_font.size("START")
    text_x = button_x + (button_width - text_width) // 2
    text_y = button_y + (button_height - text_height) // 2
    dis.blit(button_text, [text_x, text_y])


# Thêm hàm vẽ nút "DETAILS"
def draw_details_button():
    details_button_width, details_button_height = 120, 50
    details_button_x = (dis_width - details_button_width) // 2
    details_button_y = (dis_height - details_button_height) // 2 + 63  # Khoảng cách từ Start button

    pygame.draw.rect(dis, orange, [details_button_x, details_button_y, details_button_width, details_button_height])

    details_button_text = retro_font.render("DETAILS", True, white)
    details_text_width, details_text_height = retro_font.size("DETAILS")
    details_text_x = details_button_x + (details_button_width - details_text_width) // 2
    details_text_y = details_button_y + (details_button_height - details_text_height) // 2
    dis.blit(details_button_text, [details_text_x, details_text_y])

def draw_daily_button():
    details_button_width, details_button_height = 120, 50
    details_button_x = (dis_width - details_button_width) // 2
    details_button_y = (dis_height - details_button_height) // 2 + 136  # Khoảng cách từ Start button

    pygame.draw.rect(dis, orange, [details_button_x, details_button_y, details_button_width, details_button_height])

    details_button_text = retro_font.render("DAILY", True, white)
    details_text_width, details_text_height = retro_font.size("DAILY")
    details_text_x = details_button_x + (details_button_width - details_text_width) // 2
    details_text_y = details_button_y + (details_button_height - details_text_height) // 2
    dis.blit(details_button_text, [details_text_x, details_text_y])

# Thêm hàm hiển thị màn hình giới thiệu chi tiết
def show_details_screen():
    dis.fill(silver)
    message_details("GAME DETAILS", purple)
    intro_sound.stop()
    button_click_sound.play()
    intro_sound.play()
    details = [
        "1. Use arrow keys to control the snake.",
        "2. Eat the red apples to grow the snake.",
        "3. Avoid collisions with black apples.",
        "4. Gold apples give you 10 points.",
        "5. The snake speeds up over time.",
        "6. Reach point 15 to enter the Final Map.",
        "7. After get 15 points your speed will be random.",
        "8. Have fun and aim for the highest score!"
    ]

    y_offset = 60
    for detail in details:
        detail_text = retro_font.render(detail, True, black)
        dis.blit(detail_text, [50, y_offset])
        y_offset += 30

    back_button_width, back_button_height = 100, 50
    back_button_x = (dis_width - back_button_width) // 2
    back_button_y = dis_height - back_button_height - 20
    pygame.draw.rect(dis, orange, [back_button_x, back_button_y, back_button_width, back_button_height])

    back_button_text = retro_font.render("BACK", True, white)
    back_text_width, back_text_height = retro_font.size("BACK")
    back_text_x = back_button_x + (back_button_width - back_text_width) // 2
    back_text_y = back_button_y + (back_button_height - back_text_height) // 2
    dis.blit(back_button_text, [back_text_x, back_text_y])

    pygame.display.update()

    back_button_rect = pygame.Rect((dis_width - 100) // 2, dis_height - 70, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    intro_sound.stop()
                    button_click_sound.play()
                    return


# Thêm nút "DETAILS" vào hàm start_screen
def start_screen():
    start = True
    while start:
        dis.fill(silver)
        message("HUNTING SNAKE 69", purple)
        draw_button()
        draw_details_button()  # Vẽ nút "DETAILS"
        draw_daily_button()
        intro_sound.set_volume(0.3)
        intro_sound.play()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                start_button_rect = pygame.Rect((dis_width - 100) // 2, (dis_height - 50) // 2, 120, 50)
                details_button_rect = pygame.Rect((dis_width - 100) // 2, (dis_height - 50) // 2 + 63, 120, 50)
                daily_button_rect = pygame.Rect((dis_width - 100) // 2, (dis_height - 50) // 2 + 136, 120, 50)

                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    intro_sound.stop()
                    button_click_sound.play()
                    start = False
                elif details_button_rect.collidepoint(mouse_x, mouse_y):
                    show_details_screen()  # Hiển thị màn hình giới thiệu chi tiết
                elif daily_button_rect.collidepoint(mouse_x, mouse_y):
                    intro_sound.stop()
                    button_click_sound.play()
                    redirect_to_url(desired_url)

    return start


def Your_score(score):
    global high_score
    value = score_font.render("YOUR SCORE: " + str(score), True, white)
    dis.blit(value, [5, 0])
    bestscore = retro_font.render("BEST SCORE: " + str(high_score), True, white)
    text_width, text_height = retro_font.size("BEST SCORE: " + str(high_score))
    margin = 10
    dis.blit(bestscore, [dis_width - text_width - margin, dis_height - text_height - margin])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def draw_black_apple(apple_x, apple_y):
    pygame.draw.rect(dis, black, [apple_x, apple_y, snake_block, snake_block])


def is_collision_with_apple(x, y, apple_x, apple_y):
    if x == apple_x and y == apple_y:
        return True
    return False


def draw_gold_apple(apple_x, apple_y):
    pygame.draw.rect(dis, (255, 255, 0), [apple_x, apple_y, snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_width, text_height = font_style.size(msg)
    x = (dis_width - text_width) // 2
    y = (dis_height - text_height) // 2.5
    dis.blit(mesg, [x, y])


def gameLoop():
    global game_over_sound, level_up_sound, item_pickup_sound, high_score

    start_screen()

    game_over = False
    game_close = False

    last_sound_time = time.time()
    gold_apple_visible = True

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    black_apple_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    black_apple_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    gold_apple_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    gold_apple_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    last_black_apple_time = time.time()
    last_gold_apple_time = time.time()

    while not game_over:

        while game_close:
            dis.fill(silver)
            message("GAME OVER! PRESS -R TO REPLAY OR -Q TO QUIT", purple)
            Your_score(Length_of_snake - 1)

            # Phát âm thanh khi game over
            if time.time() - last_sound_time >= 2.15:
                game_over_sound.play()
                last_sound_time = time.time()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        if Length_of_snake <= 5:
            dis.fill(pink)
            t = 7
        elif Length_of_snake > 5 and Length_of_snake <= 10:
            dis.fill(blue)
            t = 5
        elif Length_of_snake > 10 and Length_of_snake <= 15:
            dis.fill(orange)
            t = 3
        else:
            dis.fill(ored)
            t = 1.5
            if gold_apple_visible:
                draw_gold_apple(gold_apple_x, gold_apple_y)
                if is_collision_with_apple(x1, y1, gold_apple_x, gold_apple_y):
                    superitem_pickup_sound.play()
                    Length_of_snake += 10
                    gold_apple_visible = False
                    last_gold_apple_time = time.time()
                    if Length_of_snake > high_score:
                        high_score = Length_of_snake - 1

            if not gold_apple_visible:
                if time.time() - last_gold_apple_time > 5:
                    gold_apple_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    gold_apple_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    gold_apple_visible = True

        draw_black_apple(black_apple_x, black_apple_y)

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        if time.time() - last_black_apple_time > t:
            black_apple_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            black_apple_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            last_black_apple_time = time.time()

        if is_collision_with_apple(x1, y1, black_apple_x, black_apple_y):
            game_close = True

        if Length_of_snake > 1 and Length_of_snake <= 16:
            # Phát âm thanh Final Map
            if Length_of_snake == 16:
                if time.time() - last_sound_time >= 0.2565:
                    finalmap_sound.play()
                    last_sound_time = time.time()
            # Phát âm thanh Level Up
            else:
                if Length_of_snake % 5 == 1:
                    if time.time() - last_sound_time >= 9:
                        level_up_sound.play()
                        last_sound_time = time.time()

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

            # Phát âm thanh khi ăn một vật phẩm
            if Length_of_snake > 1:
                if Length_of_snake > 16:
                    item_pickup_sound.play()
                else:
                    if Length_of_snake % 5 != 1:
                        item_pickup_sound.play()

            # Cập nhật điểm cao nếu vượt qua
            if Length_of_snake > high_score:
                high_score = Length_of_snake - 1

        if Length_of_snake <= 5:
            clock.tick(10)
        elif Length_of_snake > 5 and Length_of_snake <= 10:
            clock.tick(20)
        elif Length_of_snake > 10 and Length_of_snake <= 15:
            clock.tick(30)
        else:
            if time.time() - last_sound_time >= 2:
                Speed = random.randint(30, 37)
                last_sound_time = time.time()
            clock.tick(Speed)

    pygame.quit()
    quit()


gameLoop()
