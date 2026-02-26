print("=== MINI RPG ===")

# DADOS DO JOGADOR
nome = input("Digite o nome do seu herói: ")
vida_maxima = 100
vida_jogador = vida_maxima
nivel = 1
xp = 0
ouro = 0
dano = 10
pocoes = 1

print("Bem-vindo,", nome)

# LOOP DO JOGO
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

    # ===== BATALHA =====
    while vida_jogador > 0 and vida_inimigo > 0:

        print("\nSua vida:", vida_jogador, "/", vida_maxima)
        print("Vida do inimigo:", vida_inimigo)
        print("Poções:", pocoes)

        acao = input("1 - Atacar | 2 - Usar poção: ")

        if acao == "1":
            vida_inimigo -= dano
            print("Você atacou!")

        elif acao == "2":
            if pocoes > 0:
                vida_jogador += 30
                if vida_jogador > vida_maxima:
                    vida_jogador = vida_maxima
                pocoes -= 1
                print("Você usou uma poção! +30 de vida")
            else:
                print("Você não tem poções!")

        else:
            print("Escolha inválida!")

        if vida_inimigo > 0:
            vida_jogador -= dano_inimigo
            print("O inimigo atacou!")

    # ===== RESULTADO DA BATALHA =====
    if vida_jogador > 0:
        print("🏆 Você venceu!")
        xp += 10
        ouro += 20

        # SUBIR DE NÍVEL
        nivel += 1
        vida_maxima = 100 + (nivel - 1) * 10
        vida_jogador = vida_maxima

        # ===== LOJA =====
        print("\n🏪 LOJA")
        print("Seu ouro:", ouro)
        print("1 - Espada melhor (+5 dano) - 30 ouro")
        print("2 - Comprar poção - 15 ouro")
        print("3 - Continuar")

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
                pocoes += 1
                print("Você comprou uma poção!")
            else:
                print("Ouro insuficiente!")

    else:
        print("💀 Você morreu...")

print("\n===== FIM DO JOGO =====")

if nivel > 5:
    print("🎉 PARABÉNS! Você zerou o jogo!")
