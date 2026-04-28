# Made by IST Technology    
# Telegram: @ISToffical
#GitHub: AlMatCod

import pyautogui
import time
import random

# Функция для генерации случайных фраз
def generate_random_message():
    subjects = ["AI", "Minecraft", "Player", "Game", "World", "Block"]
    verbs = ["is exploring", "is crafting", "is building", "is breaking", "is jumping", "is fighting"]
    objects = ["blocks", "mobs", "items", "structures", "caves", "biomes"]
    
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    
    return f"! {subject} {verb} {object}. (made ai in kazak_ai)"

def move_forward(seconds):
    pyautogui.keyDown('w')
    time.sleep(seconds)
    pyautogui.keyUp('w')

def turn_left():
    pyautogui.moveRel(-600, 0)  # Поворачиваем мышь влево на 600 пикселей
    time.sleep(0.1)  # Небольшая задержка, чтобы имитировать движение

def turn_right():
    pyautogui.moveRel(600, 0)  # Поворачиваем мышь вправо на 600 пикселей
    time.sleep(0.1)  # Небольшая задержка, чтобы имитировать движение

def send_random_chat_messages():
    # Отправляем два случайных сгенерированных сообщения
    for _ in range(2):
        message = generate_random_message()
        pyautogui.press('t')          # Нажимаем "T" для открытия чата
        time.sleep(0.5)               # Небольшая задержка перед вводом
        pyautogui.typewrite(message)  # Печатаем сообщение
        pyautogui.press('enter')       # Нажимаем "Enter" для отправки

def send_syntax_error_message():
    error_message = "! SyntaxError: unexpected EOF while parsing (made ai in kazak_ai)"
    pyautogui.press('t')  # Нажимаем "T" для открытия чата
    time.sleep(0.5)       # Небольшая задержка перед вводом
    pyautogui.typewrite(error_message)  # Печатаем сообщение об ошибке
    pyautogui.press('enter')  # Нажимаем "Enter" для отправки

def send_rtp_command():
    pyautogui.press('t')  # Нажимаем "T" для открытия чата
    time.sleep(0.5)       # Небольшая задержка перед вводом
    pyautogui.typewrite('/rtp')  # Печатаем команду /rtp
    pyautogui.press('enter')  # Нажимаем "Enter" для отправки

def ai_loop():
    start_time = time.time()  # Засекаем время для отсчета 30 секунд
    rtp_time = time.time()     # Засекаем время для команды /rtp
    error_time = time.time()   # Засекаем время для сообщения об ошибке

    while True:
        # Генерируем случайное количество секунд для движения вперед (от 1 до 5)
        move_time = random.randint(1, 5)
        move_forward(move_time)

        # Генерируем случайное направление
        direction = random.choice(['left', 'right', 'forward'])
        if direction == 'left':
            turn_left()
        elif direction == 'right':
            turn_right()
        else:
            continue  # Если "forward", ничего не делаем, продолжаем движение вперед

        # Проверка на каждые 30 секунд для отправки сообщений
        if time.time() - start_time >= 15:
            send_random_chat_messages()  # Отправляем два случайных сообщения в чат
            start_time = time.time()  # Обновляем время для нового отсчета 30 секунд

        # Проверка на каждые 40 секунд для отправки команды /rtp
        if time.time() - rtp_time >= 20:
            send_rtp_command()  # Отправляем команду /rtp
            rtp_time = time.time()  # Обновляем время для нового отсчета 40 секунд

        # Проверка на каждую минуту для отправки сообщения об ошибке
        if time.time() - error_time >=30:
            send_syntax_error_message()  # Отправляем сообщение об ошибке
            error_time = time.time()  # Обновляем время для нового отсчета 60 секунд


ai_loop()
