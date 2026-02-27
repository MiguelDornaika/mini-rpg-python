import random

print("=== 🧟 JOGO DE SOBREVIVÊNCIA ===")

nome = input("Digite o nome do sobrevivente: ")

vida = 100
fome = 100
agua = 100
dia = 1

inventario = {
    "comida": 2,
    "agua": 2,
    "kit_medico": 1
}

# =========================
# FUNÇÕES
# =========================

def mostrar_status():
    print("\n📊 STATUS")
    print(f"Sobrevivente: {nome}")
    print(f"Vida: {vida}")
    print(f"Fome: {fome}")
    print(f"Água: {agua}")
    print(f"Dia: {dia}")

def mostrar_inventario():
    print("\n🎒 INVENTÁRIO")
    for item, qtd in inventario.items():
        print(f"{item} x{qtd}")

def consumir_comida():
    global fome
    if inventario["comida"] > 0:
        inventario["comida"] -= 1
        fome += 30
        if fome > 100:
            fome = 100
        print("🍗 Você comeu comida.")
    else:
        print("❌ Você não tem comida!")

def beber_agua():
    global agua
    if inventario["agua"] > 0:
        inventario["agua"] -= 1
        agua += 30
        if agua > 100:
            agua = 100
        print("💧 Você bebeu água.")
    else:
        print("❌ Você não tem água!")

def usar_kit():
    global vida
    if inventario["kit_medico"] > 0:
        inventario["kit_medico"] -= 1
        vida += 40
        if vida > 100:
            vida = 100
        print("🩹 Você usou um kit médico.")
    else:
        print("❌ Você não tem kit médico!")

def explorar():
    global vida
    evento = random.randint(1, 4)
    
    if evento == 1:
        print("🏚️ Você encontrou suprimentos!")
        inventario["comida"] += 1
        inventario["agua"] += 1
        
    elif evento == 2:
        print("🧟 Você encontrou um zumbi!")
        dano = random.randint(10, 25)
        vida -= dano
        print(f"O zumbi te causou {dano} de dano!")
        
    elif evento == 3:
        print("🎒 Você encontrou um kit médico!")
        inventario["kit_medico"] += 1
        
    else:
        print("😌 Nada aconteceu hoje.")

# =========================
# LOOP PRINCIPAL
# =========================

while vida > 0:
    
    print(f"\n🌅 DIA {dia}")
    
    fome -= 10
    agua -= 10
    
    if fome <= 0 or agua <= 0:
        vida -= 15
        print("⚠️ Você está sofrendo por falta de recursos!")
    
    print("\n1 - Explorar")
    print("2 - Comer")
    print("3 - Beber água")
    print("4 - Usar kit médico")
    print("5 - Status")
    print("6 - Inventário")
    print("7 - Sair")
    
    escolha = input("Escolha: ")
    
    if escolha == "1":
        explorar()
        
    elif escolha == "2":
        consumir_comida()
        
    elif escolha == "3":
        beber_agua()
        
    elif escolha == "4":
        usar_kit()
        
    elif escolha == "5":
        mostrar_status()
        
    elif escolha == "6":
        mostrar_inventario()
        
    elif escolha == "7":
        break
        
    else:
        print("Opção inválida!")
    
    dia += 1

print("\n💀 Você não sobreviveu ao apocalipse...")