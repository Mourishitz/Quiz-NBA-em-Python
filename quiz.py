def novo_jogo():
    escolha_usuario = []
    escolha_correta = 0
    numero_questao = 1
    for i in questoes:
        print("---------------------------------------------------------------------")
        print(i)
        for j in opcoes[numero_questao-1]:
            print(j)
        escolha = input("Resposta?: ")
        escolha = escolha.upper()
        escolha_usuario.append(escolha)

        escolha_correta += resposta(questoes.get(i),escolha)
        numero_questao += 1

    pontos(escolha_correta, escolha)



def resposta(resposta_certa, escolha):

    if resposta_certa == escolha:
        print("CORRETO!")
        return 1
    else:
        print("Resposta Errada :(")
        return 0

def pontos(escolha_correta, escolha):
    print("---------------------------------------------------------------------")
    print("Resultados")
    print("---------------------------------------------------------------------")

    print("Respostas: ", end="")
    for k in questoes:
        print(questoes.get(k), end="")
    print()

    score = int((escolha_correta/len(questoes))*100)
    print("Sua pontuação é de: "+str(score)+"%")
def jogar_dnv():

    response = input("Você deseja jogar de novo? (sim/nao): ")
    response = response.upper()

    if response == "SIM":
        return True
    else:
        return False
#----------
questoes = {
        "Qual foi o primeiro time a marcar 72-10 em uma temporada de Basquete?: ": "A",
        "Qual o jogador com mais titulos de campeão da NBA até 2021?: ": "B",
        "Quem é o maior cestinha de todos os tempos da NBA?: ": "C",
        "Quais jogadores faziam parte do famoso 'Big 3' do Miami Heat em 2010?: ": "A"
    }

opcoes = [
        ["A. Chicago Bulls", "B. Los Angeles Lakers", "C. Boston Celtics", "D. Miami Heat"],
        ["A. Michael Jordan", "B. Bill Russel", "C. Shaquille O'Neal", "D. Lebron James"],
        ["A. Kobe Bryant", "B. Karl Malone", "C. Kareem Abdul-Jabbar", "D. Steph Curry"],
        ["A. Lebron James, Dwyane Wade, Chris Bosh", "B. Shaquille O'Neal, Kobe Bryant, Lamar Odom",
         "C. Kyrie Irving, Kevin Durant, James Harden", "D. Anthony Davis, Lebron James, Russel Westbrook"]
    ]
novo_jogo()

while jogar_dnv():
    novo_jogo()

print("Obrigado por jogar!")