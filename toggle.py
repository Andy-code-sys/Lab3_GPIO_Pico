from machine import Pin
import time

led = Pin(18, Pin.OUT)
bouton = Pin(22, Pin.IN, Pin.PULL_DOWN)

etat_led = False
dernier_appui = 0
delai_min = 200  # 200ms entre les appuis

print("Toggle LED Simple - Appuyez sur le bouton")

while True:
    if bouton.value() == 1:  # Bouton appuyé
        temps_actuel = time.ticks_ms()
        
        # Vérifier si assez de temps s'est écoulé depuis le dernier appui
        if temps_actuel - dernier_appui > delai_min:
            etat_led = not etat_led
            led.value(etat_led)
            print(f"LED {'ON' if etat_led else 'OFF'}")
            dernier_appui = temps_actuel
        
        # Attendre que le bouton soit relâché
        while bouton.value() == 1:
            time.sleep_ms(10)