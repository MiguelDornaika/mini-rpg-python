print("=== MINI RPG ===")

# =========================
# DADOS DO JOGADOR
# =========================

nome = input("Digite o nome do seu herói: ")
vida_maxima = 100
vida_jogador = vida_maxima
nivel = 1
xp = 0
ouro = 0
dano = 10

# 🎒 INVENTÁRIO
inventario = {
    "pocao": 2,
    "bomba": 3
}

print("Bem-vindo,", nome)

# =========================
# LOOP PRINCIPAL DO JOGO
# =========================

while vida_jogador > 0 and nivel <= 5:

    print("\n===== NÍVEL", nivel, "=====")

    # Criar inimigo
    if nivel == 5:
        vida_inimigo = 120
        dano_inimigo = 15
        print("👑 O CHEFÃO apareceu!")
    else:
        vida_inimigo = 50
        dano_inimigo = 5
        print("Um monstro apareceu!")

    # =========================
    # BATALHA
    # =========================

    while vida_jogador > 0 and vida_inimigo > 0:

        print("\nSua vida:", vida_jogador, "/", vida_maxima)
        print("Vida do inimigo:", vida_inimigo)
        print("Poções:", inventario["pocao"])
        print("Bombas:", inventario["bomba"])

        acao = input("1 - Atacar | 2 - Usar poção | 3 - Usar bomba: ")

        if acao == "1":
            vida_inimigo -= dano
            print("⚔️ Você atacou!")

        elif acao == "2":
            if inventario["pocao"] > 0:
                vida_jogador += 30
                if vida_jogador > vida_maxima:
                    vida_jogador = vida_maxima
                inventario["pocao"] -= 1
                print("🧪 Você usou uma poção! +30 de vida")
            else:
                print("Você não tem poções!")

        elif acao == "3":
            if inventario["bomba"] > 0:
                dano_bomba = 40
                vida_inimigo -= dano_bomba
                inventario["bomba"] -= 1
                print("💣 BOOM! Você causou", dano_bomba, "de dano!")
            else:
                print("Você não tem bombas!")

        else:
            print("Escolha inválida!")

        # Ataque do inimigo
        if vida_inimigo > 0:
            vida_jogador -= dano_inimigo
            print("O inimigo atacou!")

    # =========================
    # RESULTADO DA BATALHA
    # =========================

    if vida_jogador > 0:
        print("🏆 Você venceu!")
        xp += 10
        ouro += 20

        # Subir nível
        nivel += 1
        vida_maxima = 100 + (nivel - 1) * 10
        vida_jogador = vida_maxima

        # =========================
        # LOJA
        # =========================

        print("\n🏪 LOJA")
        print("Seu ouro:", ouro)
        print("1 - Espada melhor (+5 dano) - 30 ouro")
        print("2 - Comprar poção - 15 ouro")
        print("3 - Comprar bomba - 25 ouro")
        print("4 - Continuar")

        escolha = input("O que deseja fazer? ")

        if escolha == "1":
            if ouro >= 30:
                ouro -= 30
                dano += 5
                print("Você comprou espada melhor!")
            else:
                print("Ouro insuficiente!")

        elif escolha == "2":
            if ouro >= 15:
                ouro -= 15
                inventario["pocao"] += 1
                print("Você comprou uma poção!")
            else:
                print("Ouro insuficiente!")

        elif escolha == "3":
            if ouro >= 25:
                ouro -= 25
                inventario["bomba"] += 1
                print("Você comprou uma bomba!")
            else:
                print("Ouro insuficiente!")

    else:
        print("💀 Você morreu...")

print("\n===== FIM DO JOGO =====")

if nivel > 5:
    print("🎉 PARABÉNS! Você zerou o jogo!")    

