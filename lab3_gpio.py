from machine import Pin
from time import sleep

# Sortie numérique (LED)

def phase2_sortie_numerique():
    """
    Phase 2 - Sortie numérique (LED)
    Branche une LED sur GP15 avec résistance 330Ω
    """
    print("=== PHASE 2 - Sortie numérique (LED) ===")
    print("LED clignotante sur GP15 toutes les 0.5 secondes")
    print("Appuyez sur Ctrl+C pour arrêter")
    
    # Configuration de la LED sur GP15
    led = Pin(15, Pin.OUT)
    
    try:
        while True:
            led.toggle()  # Change l'état de la LED
            sleep(0.5)    # Attend 0.5 seconde
    except KeyboardInterrupt:
        led.off()  # Éteint la LED en quittant
        print("Phase 2 terminée")

# Entrée numérique (bouton)

def phase3_entree_numerique():
    """
    Phase 3 - Entrée numérique (Bouton)
    Bouton poussoir sur GP14 avec pull-down
    """
    print("=== PHASE 3 - Entrée numérique (Bouton) ===")
    print("Bouton sur GP14 contrôle LED sur GP15")
    print("Appuyez sur Ctrl+C pour arrêter")
    
    # Configuration
    led = Pin(15, Pin.OUT)
    button = Pin(14, Pin.IN, Pin.PULL_DOWN)
    
    try:
        while True:
            if button.value() == 1:
                print("Bouton appuyé!")
                led.on()
            else:
                led.off()
            sleep(0.1)  # Délai pour réduire la charge CPU
    except KeyboardInterrupt:
        led.off()
        print("Phase 3 terminée")

#bouton avec anti-rebond

def bouton_anti_rebond():
    """
    Version améliorée avec anti-rebond
    """
    print("=== BOUTON AVEC ANTI-REBOND ===")
    
    led = Pin(15, Pin.OUT)
    button = Pin(14, Pin.IN, Pin.PULL_DOWN)
    
    dernier_etat = 0
    dernier_temps = 0
    delai_rebond = 50  # 50ms pour l'anti-rebond
    
    try:
        while True:
            etat_actuel = button.value()
            temps_actuel = sleep(0) * 1000  # Temps approximatif
            
            # Détection changement d'état
            if etat_actuel != dernier_etat:
                dernier_temps = temps_actuel
            
            # Vérification anti-rebond
            if (temps_actuel - dernier_temps) > delai_rebond:
                if etat_actuel == 1:
                    print("Bouton appuyé (anti-rebond)!")
                    led.on()
                else:
                    led.off()
            
            dernier_etat = etat_actuel
            sleep(0.01)
            
    except KeyboardInterrupt:
        led.off()
        print("Test anti-rebond terminé")

#fonction toggle intégrée

def test_toggle():
    """
    Fonction similaire à toggle.py pour intégration
    LED change d'état à chaque appui sur bouton
    """
    print("=== FONCTION TOGGLE INTÉGRÉE ===")
    
    led = Pin(15, Pin.OUT)
    button = Pin(14, Pin.IN, Pin.PULL_DOWN)
    
    etat_led = False
    dernier_etat_bouton = 0
    
    print("Appuyez sur le bouton pour changer l'état de la LED")
    print("LED initiale: ÉTEINTE")
    
    led.off()  # Éteint la LED au départ
    
    try:
        while True:
            etat_bouton = button.value()
            
            # Détection front montant (appui)
            if etat_bouton == 1 and dernier_etat_bouton == 0:
                sleep(0.05)  # Petit délai anti-rebond
                if button.value() == 1:  # Vérification
                    etat_led = not etat_led
                    led.value(etat_led)
                    print(f"LED {'ALLUMÉE' if etat_led else 'ÉTEINTE'}")
                    sleep(0.2)  # Évite les appuis multiples
            
            dernier_etat_bouton = etat_bouton
            sleep(0.05)
            
    except KeyboardInterrupt:
        led.off()
        print("Test toggle terminé")

#Menu principal 

def main():
    """
    Menu principal pour tester toutes les phases
    """
    print("\n" + "="*50)
    print("LABORATOIRE 3 - GPIO RASPBERRY PI PICO")
    print("SED 1515 - Université d'Ottawa")
    print("="*50)
    
    while True:
        print("\n=== MENU LAB3_GPIO.PY ===")
        print("1. Phase 2 - LED clignotante (GP15)")
        print("2. Phase 3 - Bouton contrôle LED (GP14→GP15)")
        print("3. Bouton avec anti-rebond")
        print("4. Fonction toggle intégrée")
        print("5. Quitter")
        
        choix = input("\nChoisissez une option (1-5): ").strip()
        
        if choix == '1':
            phase2_sortie_numerique()
        elif choix == '2':
            phase3_entree_numerique()
        elif choix == '3':
            bouton_anti_rebond()
        elif choix == '4':
            test_toggle()
        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Option invalide!")

# Exécution du menu principal si le script est exécuté directement

if __name__ == "__main__":
    # Si le fichier est exécuté directement, lancer le menu
    main()
else:
    # Si importé comme module, initialiser les broches
    print("Module lab3_gpio chargé")