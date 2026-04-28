
import pyautogui
import time
import random
import pygetwindow as gw
import threading
from transformers import pipeline
import keyboard  # pip install keyboard

# --- Инициализация локального ИИ ---
generator = pipeline("text-generation", model="distilgpt2")

# --- Флаги состояния ---
chat_open = False
jump_blocked = False
bot_enabled = True

# --- Настройки ---
JUMP_PRE_DELAY = 1
JUMP_PRESS_TIME = 0.005
EAT_TIMES = 1
EAT_DURATION = 3.0
LONG_PRESS_THRESHOLD = 1.5  # секунд для долгого нажатия

# --- Вспомогательные функции ---
def is_minecraft_active():
    w = gw.getActiveWindow()
    return (w is not None) and ("Minecraft 1.12.2" in w.title)

# Приветственное сообщение
print("🤖 AI-Bot запущен (локальный GPT-2). Начинаем работу...")

# Движение
def move_forward(seconds):
    pyautogui.keyDown('w')
    time.sleep(seconds)
    pyautogui.keyUp('w')
    print(f"[BOT] Двигаюсь вперёд {seconds:.1f} сек")

def turn_left():
    pyautogui.moveRel(-600 + random.randint(-50, 50), 0)
    print("[BOT] Поворот влево")
    time.sleep(random.uniform(0.1, 0.3))

def turn_right():
    pyautogui.moveRel(600 + random.randint(-50, 50), 0)
    print("[BOT] Поворот вправо")
    time.sleep(random.uniform(0.1, 0.3))

# Чат
def generate_ai_message():
    prompt = "write latinec russian you chat gpt."
    
    banned = ["/", ":", ";", "'", "\\", "|", "`",","]
    
    for _ in range(5):
        result = generator(prompt, max_new_tokens=40, temperature=1.2, top_p=0.85, do_sample=True)
        text = result[0]["generated_text"].replace(prompt, "").strip()
        clean = text.split("\n")[0][:70]
        if not any(ch in clean for ch in banned):
            return f"! {clean} (made by ISToffical)"
    return "! Hello i Ai! (made by ISToffical)"

def send_ai_chat_message(custom_msg=None):
    global chat_open
    chat_open = True
    pyautogui.press('t')
    time.sleep(random.uniform(0.3, 0.7))
    msg = custom_msg if custom_msg else generate_ai_message()
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    print(f"[BOT] Сообщение в чат: {msg}")
    chat_open = False

# Еда
def eat_food(times=EAT_TIMES, duration=EAT_DURATION):
    global jump_blocked
    jump_blocked = True
    print("[BOT] Начинаю есть...")
    for i in range(times):
        pyautogui.press('1')
        pyautogui.mouseDown(button='right')
        time.sleep(duration)
        pyautogui.mouseUp(button='right')
        print(f"[BOT] Укус {i+1}/{times}")
        time.sleep(random.uniform(0.2, 0.5))
    print("[BOT] Закончил есть")
    jump_blocked = False

def send_rtp_command():
    cmd = random.choice(["/rtp","/rtp", "/warp spawn"])
    eat_food()
    send_ai_chat_message(cmd)

# Прыжки
def auto_jump():
    while True:
        if bot_enabled and is_minecraft_active() and not chat_open and not jump_blocked:
            time.sleep(JUMP_PRE_DELAY)
            pyautogui.keyDown('space')
            time.sleep(JUMP_PRESS_TIME)
            pyautogui.keyUp('space')
        else:
            time.sleep(0.05)

# Смена предмета
def random_switch_item():
    if random.random() < 0.3:
        slot = str(random.randint(1, 9))
        pyautogui.press(slot)
        print(f"[BOT] Переключил предмет на слот {slot}")

# Крутилка с атакой
def random_attack_spin():
    if random.random() < 0.1:
        print("[BOT] Крутится на 360° и атакует!")
        for i in range(12):
            pyautogui.moveRel(100, 0)
            pyautogui.click(button='left')
            time.sleep(0.05)

# Функция слежения за клавишами
def keyboard_monitor():
    global bot_enabled
    dot_pressed_time = 0
    while True:
        # Выключение при правом Alt
        if keyboard.is_pressed('right alt'):
            if bot_enabled:
                print("[BOT] Правый Alt зажат - бот отключен")
            bot_enabled = False
        else:
            if not bot_enabled:
                print("[BOT] Бот включен")
            bot_enabled = True

        # Долгое нажатие точки
        if keyboard.is_pressed('.'):
            dot_pressed_time += 0.1
            if dot_pressed_time >= LONG_PRESS_THRESHOLD:
                send_ai_chat_message("! Made in IST technology ( pls dont kill bot)")
                dot_pressed_time = 0
        else:
            dot_pressed_time = 0

        time.sleep(0.1)

# Основной цикл
def ai_loop():
    msg_time = time.time()
    rtp_time = time.time()
    threading.Thread(target=auto_jump, daemon=True).start()
    threading.Thread(target=keyboard_monitor, daemon=True).start()

    while True:
        if bot_enabled and is_minecraft_active():
            move_time = random.uniform(1, 5)
            move_forward(move_time)

            direction = random.choice(['left', 'right', 'forward'])
            if direction == 'left':
                turn_left()
            elif direction == 'right':
                turn_right()

            random_switch_item()
            random_attack_spin()

            if time.time() - msg_time >= 15:
                send_ai_chat_message()
                msg_time = time.time()

            if time.time() - rtp_time >= 40:
                send_rtp_command()
                rtp_time = time.time()

        time.sleep(0.2)

# Запуск
ai_loop()

