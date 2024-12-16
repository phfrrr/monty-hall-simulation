import random

# Variáveis
total_simulacoes = 100
acertos_grupo_1 = 0
erros_grupo_1 = 0
acertos_grupo_2 = 0
erros_grupo_2 = 0
revelacao = 0

# Histórico
historico_porta_do_premio = []
historico_escolhas_grupo_1 = []
historico_acertos_grupo_1 = []
historico_erros_grupo_1 = []
historico_primeiras_escolhas_grupo_2 = []
historico_segundas_escolhas_grupo_2 = []
historico_acertos_grupo_2 = []
historico_erros_grupo_2 = []

# Simulação
for i in range(total_simulacoes):
    porta_do_premio = random.randint(1, 3)
    historico_porta_do_premio.append(porta_do_premio)

    # Grupo 1: Não muda a escolha inicial
    chute_grupo_1 = random.randint(1, 3)
    historico_escolhas_grupo_1.append(chute_grupo_1)
    if chute_grupo_1 == porta_do_premio:
        acertos_grupo_1 += 1
        historico_acertos_grupo_1.append(f'acerto na {i + 1}ª vez')
    else:
        erros_grupo_1 += 1
        historico_erros_grupo_1.append(f'erro na {i + 1}ª vez')

    # Grupo 2: Muda a escolha inicial
    chute_grupo_2 = random.randint(1, 3)
    historico_primeiras_escolhas_grupo_2.append(chute_grupo_2)

    # Revelação de uma porta sem prêmio
    revelacao = random.choice([porta for porta in [1, 2, 3] if porta != porta_do_premio and porta != chute_grupo_2])

    # Troca de escolha
    chute_grupo_2 = random.choice([porta for porta in [1, 2, 3] if porta != revelacao and porta != chute_grupo_2])
    historico_segundas_escolhas_grupo_2.append(chute_grupo_2)

    if chute_grupo_2 == porta_do_premio:
        acertos_grupo_2 += 1
        historico_acertos_grupo_2.append(f'acerto na {i + 1}ª vez')
    else:
        erros_grupo_2 += 1
        historico_erros_grupo_2.append(f'erro na {i + 1}ª vez')

# Cálculos de porcentagens
porcentagem_acerto_controle_1 = (acertos_grupo_1 / total_simulacoes) * 100
porcentagem_erro_controle_1 = 100 - porcentagem_acerto_controle_1
porcentagem_acerto_controle_2 = (acertos_grupo_2 / total_simulacoes) * 100
porcentagem_erro_controle_2 = 100 - porcentagem_acerto_controle_2

discrepancia = abs(porcentagem_acerto_controle_1 - porcentagem_acerto_controle_2)

# Resultado final
if porcentagem_acerto_controle_1 > porcentagem_acerto_controle_2:
    print(f'O grupo que manteve a decisão da porta teve maior sucesso por {porcentagem_acerto_controle_1:.2f}% contra {porcentagem_acerto_controle_2:.2f}%, com uma discrepância de {discrepancia:.2f}%')
else:
    print(f'O grupo que mudou a decisão da porta teve maior sucesso por {porcentagem_acerto_controle_2:.2f}% contra {porcentagem_acerto_controle_1:.2f}%, com uma discrepância de {discrepancia:.2f}%')

# Impressão do histórico, se requisitado
print("Histórico geral:")
for i in range(len(historico_porta_do_premio)):
    print(f'\n{i + 1}ª experiência:')
    print(f'Na {i + 1}ª experiência, a porta sorteada foi {historico_porta_do_premio[i]}')
    print(f'Na {i + 1}ª experiência, a escolha do grupo 1 foi {historico_escolhas_grupo_1[i]}')
    if historico_escolhas_grupo_1[i] == historico_porta_do_premio[i]:
        print(f'Grupo 1 acertou na {i + 1}ª experiência')
    else:
        print(f'Grupo 1 errou na {i + 1}ª experiência')
    print(f'Na {i + 1}ª experiência, a primeira escolha do grupo 2 foi {historico_primeiras_escolhas_grupo_2[i]}')
    print(f'Na {i + 1}ª experiência, a segunda escolha do grupo 2 foi {historico_segundas_escolhas_grupo_2[i]}')
    if historico_segundas_escolhas_grupo_2[i] == historico_porta_do_premio[i]:
        print(f'Grupo 2 acertou na {i + 1}ª experiência')
    else:
        print(f'Grupo 2 errou na {i + 1}ª experiência')

print("\nHistórico de acertos do Grupo 1:")
print(historico_acertos_grupo_1)
print(f'Total de acertos do Grupo 1: {len(historico_acertos_grupo_1)}')

print("\nHistórico de erros do Grupo 1:")
print(historico_erros_grupo_1)
print(f'Total de erros do Grupo 1: {len(historico_erros_grupo_1)}')

print("\nHistórico de primeiras escolhas do Grupo 2:")
print(historico_primeiras_escolhas_grupo_2)
print(f'Total de primeiras escolhas do Grupo 2: {len(historico_primeiras_escolhas_grupo_2)}')

print("\nHistórico de segundas escolhas do Grupo 2:")
print(historico_segundas_escolhas_grupo_2)
print(f'Total de segundas escolhas do Grupo 2: {len(historico_segundas_escolhas_grupo_2)}')

print("\nHistórico de acertos do Grupo 2:")
print(historico_acertos_grupo_2)
print(f'Total de acertos do Grupo 2: {len(historico_acertos_grupo_2)}')

print("\nHistórico de erros do Grupo 2:")
print(historico_erros_grupo_2)
print(f'Total de erros do Grupo 2: {len(historico_erros_grupo_2)}')
