# String inicial do estoque
estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"


def listar_produtos(estoque_string):
    produtos = []
    itens = estoque_string.split("#")
    for item in itens:
        descricao, codigo, quantidade, custo, preco = item.split(";")
        produtos.append({
            "descricao": descricao,
            "codigo": int(codigo),
            "quantidade": int(quantidade),
            "custo": float(custo),
            "preco_venda": float(preco)
        })
    return produtos

def cadastrar_produto(estoque, descricao, codigo, quantidade, custo, preco_venda):
    if any(produto["codigo"] == codigo for produto in estoque):
        print(f"Erro: Código {codigo} já cadastrado.")
        return estoque
    estoque.append({
        "descricao": descricao,
        "codigo": codigo,
        "quantidade": quantidade,
        "custo": custo,
        "preco_venda": preco_venda
    })
    print(f"Produto '{descricao}' cadastrado com sucesso!")
    return estoque

# estoque inicial
estoque = listar_produtos(estoque_inicial)

# Teste
estoque = cadastrar_produto(estoque, "Câmera Sony", 213, 20, 1200.00, 1800.00)

print("\nEstoque Atualizado:")
for produto in estoque:
    print(produto)

# Exercicio 4
print("\nExercicio 4:")
def ordenar_produtos_crescente(estoque):
    """
    Ordena os produtos no estoque pela quantidade em ordem crescente.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.

    Returns:
        list: Lista de produtos ordenados pela quantidade em ordem crescente.
    """
    estoque_ordenado = sorted(estoque, key=lambda produto: produto["quantidade"])
    print("\nProdutos ordenados por quantidade (Crescente):")
    for produto in estoque_ordenado:
        print(f"{produto['descricao']} - Código: {produto['codigo']} - Quantidade: {produto['quantidade']} - "
              f"Custo: R${produto['custo']:.2f} - Preço de Venda: R${produto['preco_venda']:.2f}")
    return estoque_ordenado

def ordenar_produtos_decrescente(estoque):    
    """
    Ordena os produtos no estoque pela quantidade em ordem decrescente.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.

    Returns:
        list: Lista de produtos ordenados pela quantidade em ordem decrescente.
    """
    estoque_ordenado = sorted(estoque, key=lambda produto: produto["quantidade"], reverse=True)
    print("\nProdutos ordenados por quantidade (Decrescente):")
    for produto in estoque_ordenado:
        print(f"{produto['descricao']} - Código: {produto['codigo']} - Quantidade: {produto['quantidade']} - "
              f"Custo: R${produto['custo']:.2f} - Preço de Venda: R${produto['preco_venda']:.2f}")
    return estoque_ordenado

# Teste
estoque_ordenado_crescente = ordenar_produtos_crescente(estoque)
estoque_ordenado_decrescente = ordenar_produtos_decrescente(estoque)

# Exercicio 6
print("\nExercicio 6:")
def buscar_produto(estoque, *, descricao=None, codigo=None):
    """
    Busca produtos no estoque pelo nome ou código.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.
        descricao (str, opcional): Descrição do produto a ser buscado. (default: None)
        codigo (int, opcional): Código do produto a ser buscado. (default: None)

    Returns:
        list: Lista de produtos encontrados conforme os critérios fornecidos.
    """
    encontrados = []

    if descricao:
        descricao_lower = descricao.lower()
        encontrados = [produto for produto in estoque if descricao_lower in produto["descricao"].lower()]
    elif codigo:
        encontrados = [produto for produto in estoque if produto["codigo"] == codigo]

    if encontrados:
        print(f"\nProdutos encontrados ({len(encontrados)}):")
        for produto in encontrados:
            print(f"{produto['descricao']} - Código: {produto['codigo']} - Quantidade: {produto['quantidade']} - "
                  f"Custo: R${produto['custo']:.2f} - Preço de Venda: R${produto['preco_venda']:.2f}")
    else:
        print("\nNenhum produto encontrado com os critérios especificados.")

    return encontrados


# Teste
buscar_produto(estoque, descricao="Monitor")
buscar_produto(estoque, codigo=203)

# Exercicio 7
print("\nExercicio 7:")
def remover_produto(estoque, codigo):
    """
    Remove um produto do estoque com base no código fornecido.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.
        codigo (int): Código do produto a ser removido.

    Returns:
        list: Lista de estoque atualizada com o produto removido, se encontrado.
    """
    produto_encontrado = None
    for produto in estoque:
        if produto["codigo"] == codigo:
            produto_encontrado = produto
            break

    if produto_encontrado:
        estoque.remove(produto_encontrado)
        print(f"\nProduto '{produto_encontrado['descricao']}' (Código: {codigo}) removido com sucesso.")
    else:
        print(f"\nNenhum produto encontrado com o código {codigo}. Não foi possível remover.")

    return estoque

#Teste:
estoque = remover_produto(estoque, 203)
estoque = remover_produto(estoque, 999)

# Exercicio 8
print("\nExercicio 8:")
def consultar_produtos_esgotados(estoque):
    """
    Consulta produtos que estão esgotados (quantidade igual a zero) no estoque.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.

    Returns:
        None: Exibe no console os produtos esgotados, se houver algum.
    """
    produtos_esgotados = [produto for produto in estoque if produto["quantidade"] == 0]

    if produtos_esgotados:
        print("\nProdutos Esgotados:")
        for produto in produtos_esgotados:
            print(f"Descrição: {produto['descricao']} | Código: {produto['codigo']} | Custo: R${produto['custo']:.2f} | Preço de Venda: R${produto['preco_venda']:.2f}")
    else:
        print("\nNão há produtos esgotados no estoque.")

#Teste
consultar_produtos_esgotados(estoque)

# Exercicio 9 
print("\nExercicio 9:")

def filtrar_produtos_baixa_quantidade(estoque, limite_minimo=5):
    """
    Filtra produtos com quantidade abaixo do limite mínimo no estoque.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.
        limite_minimo (int): O limite mínimo de quantidade para considerar o produto como de baixa quantidade.

    Returns:
        None: Exibe no console os produtos com quantidade abaixo do limite mínimo.
    """
    produtos_baixa_quantidade = [produto for produto in estoque if produto["quantidade"] < limite_minimo]

    if produtos_baixa_quantidade:
        print(f"\nProdutos com Quantidade abaixo de {limite_minimo}:")
        for produto in produtos_baixa_quantidade:
            print(f"Descrição: {produto['descricao']} | Código: {produto['codigo']} | Quantidade: {produto['quantidade']} | Custo: R${produto['custo']:.2f} | Preço de Venda: R${produto['preco_venda']:.2f}")
    else:
        print(f"\nNão há produtos com quantidade abaixo de {limite_minimo} no estoque.")

limite_minimo_usuario = int(input("Digite o limite mínimo de quantidade para filtrar os produtos (valor padrão é 5): ") or 5)

# Teste
filtrar_produtos_baixa_quantidade(estoque, limite_minimo_usuario)

# Exercicio 11
print("\nExercicio 11:validacao dos produtos")
def validar_atualizacao(produto, quantidade_atualizada, novo_preco_venda):
    """
    Valida se as alterações no produto são permitidas (não criar estoque negativo ou preço de venda abaixo do custo).

    Args:
        produto (dict): Dicionário representando o produto a ser validado.
        quantidade_atualizada (int): Quantidade a ser atualizada no estoque.
        novo_preco_venda (float): Novo preço de venda a ser atribuído ao produto.

    Returns:
        bool: Retorna True se a atualização for válida, caso contrário retorna False.
    """
    nova_quantidade = produto["quantidade"] + quantidade_atualizada
    if nova_quantidade < 0:
        print(f"Erro: Não é possível atualizar para uma quantidade negativa. Estoque atual: {produto['quantidade']}")
        return False

    if novo_preco_venda < produto["custo"]:
        print(f"Erro: O preço de venda não pode ser menor que o custo. Custo: R${produto['custo']:.2f} | Novo preço: R${novo_preco_venda:.2f}")
        return False

    return True

# Exercicio 10
print("\nExercicio 10:")

def atualizar_estoque(codigo_produto, quantidade_atualizada, novo_preco_venda=None):
    """
    Atualiza a quantidade e o preço de venda de um produto no estoque.

    Args:
        codigo_produto (int): Código do produto a ser atualizado.
        quantidade_atualizada (int): Quantidade a ser adicionada ou subtraída.
        novo_preco_venda (float, opcional): Novo preço de venda a ser atribuído ao produto. (default: None)

    Returns:
        None: Atualiza o estoque diretamente sem retornar nada.
    """
    for produto in estoque:
        if produto['codigo'] == codigo_produto:
            if novo_preco_venda is None:
                novo_preco_venda = produto['preco_venda']

            if validar_atualizacao(produto, quantidade_atualizada, novo_preco_venda):
                produto['quantidade'] += quantidade_atualizada
                produto['preco_venda'] = novo_preco_venda
                print(f"Produto '{produto['descricao']}' atualizado com sucesso!")
            break
    else:
        print("Produto não encontrado no estoque.")

# Teste
atualizar_estoque(201, -10, 160.00)
atualizar_estoque(213, -60, 150.00) 
atualizar_estoque(204, 10, 100.00) 
atualizar_estoque(205, 5, 700.00)
print(estoque)

# Exercicio 13
print("\nExercicio 13:")

def calcular_valor_total_estoque(estoque):
    """
    Calcula o valor total do estoque com base no preço de venda e quantidade de cada produto.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.

    Returns:
        float: O valor total do estoque.
    """
    valor_total = 0
    for produto in estoque:
        valor_total += produto["quantidade"] * produto["preco_venda"]
    return valor_total

# Teste
valor_total = calcular_valor_total_estoque(estoque)
print(f"\nValor total do estoque: R${valor_total:.2f}")

# Exercicio 14
print("\nExercicio 14:")

def calcular_lucro_presumido(estoque):
    """
    Calcula o lucro presumido do estoque, baseado na diferença entre o preço de venda e o custo de cada item.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.

    Returns:
        float: O lucro presumido total do estoque.
    """
    lucro_total = 0
    for produto in estoque:
        lucro_item = (produto["preco_venda"] - produto["custo"]) * produto["quantidade"]
        lucro_total += lucro_item
    return lucro_total

# Teste
lucro_total = calcular_lucro_presumido(estoque)
print(f"\nLucro total presumido do estoque: R${lucro_total:.2f}")

# Exercicio 15
print("\nExercicio 15:inclusao do DocStrings ")

# Exercicio 5
print("\nExercicio 5:")
def menu_interativo():
    """
    Exibe um menu interativo no terminal para o usuário escolher qual operação
    deseja realizar (adicionar, atualizar, listar, buscar, etc.) no estoque.
    
    O menu será exibido repetidamente até que o usuário escolha a opção de sair.
    """
    estoque = listar_produtos(estoque_inicial)

    while True:
        print("\nMenu de Operações:")
        print("1 - Adicionar Produto")
        print("2 - Atualizar Produto")
        print("3 - Listar Produtos")
        print("4 - Buscar Produto")
        print("5 - Remover Produto")
        print("6 - Relatório Geral do Estoque")
        print("7 - Sair")
        
        opcao = input("Escolha uma opção (1-7): ")

        if opcao == "1":
            descricao = input("Digite a descrição do produto: ")
            codigo = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a quantidade: "))
            custo = float(input("Digite o custo unitário: "))
            preco_venda = float(input("Digite o preço de venda: "))
            estoque = cadastrar_produto(estoque, descricao, codigo, quantidade, custo, preco_venda)
        
        elif opcao == "2":
            codigo_produto = int(input("Digite o código do produto a ser atualizado: "))
            quantidade_atualizada = int(input("Digite a quantidade a ser alterada: "))
            novo_preco_venda = float(input("Digite o novo preço de venda: "))
            atualizar_estoque(codigo_produto, quantidade_atualizada, novo_preco_venda)

        elif opcao == "3":
            print("\nLista de Produtos:")
            for produto in estoque:
                print(f"{produto['descricao']} - Código: {produto['codigo']} - Quantidade: {produto['quantidade']} - "
                      f"Custo: R${produto['custo']:.2f} - Preço de Venda: R${produto['preco_venda']:.2f}")
        
        elif opcao == "4":
            criterio = input("Buscar por descrição ou código? (descricao/codigo): ").lower()
            if criterio == "descricao":
                descricao = input("Digite a descrição do produto para busca: ")
                buscar_produto(estoque, descricao=descricao)
            elif criterio == "codigo":
                codigo = int(input("Digite o código do produto para busca: "))
                buscar_produto(estoque, codigo=codigo)
            else:
                print("Critério inválido.")

        elif opcao == "5":
            codigo_produto = int(input("Digite o código do produto a ser removido: "))
            estoque = remover_produto(estoque, codigo_produto)

        elif opcao == "6":
            relatorio_geral_estoque(estoque)

        elif opcao == "7":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")

# Função principal
if __name__ == "__main__":
    menu_interativo()


# Exercicio 16
print("\nExercicio 16:")
def relatorio_geral_estoque(estoque):
    """
    Exibe um relatório geral do estoque, com informações sobre cada produto,
    incluindo descrição, código, quantidade, custo, preço de venda, valor total
    por item (quantidade * preço), custo total e faturamento total.

    Args:
        estoque (list): Lista de dicionários representando o estoque de produtos.

    Returns:
        None: Exibe o relatório no terminal.
    """
    print("{:<20} {:<10} {:<10} {:<15} {:<15} {:<15}".format(
        "Descrição", "Código", "Quantidade", "Custo Unitário", "Preço de Venda", "Valor Total"))
    print("-" * 85)

    custo_total = 0
    faturamento_total = 0

    for produto in estoque:
        valor_total_item = produto["quantidade"] * produto["preco_venda"]
        custo_total_item = produto["quantidade"] * produto["custo"]

        custo_total += custo_total_item
        faturamento_total += valor_total_item

        print("{:<20} {:<10} {:<10} {:<15.2f} {:<15.2f} {:<15.2f}".format(
            produto["descricao"], produto["codigo"], produto["quantidade"],
            produto["custo"], produto["preco_venda"], valor_total_item))

    print("-" * 85)
    print("{:<55} {:<15.2f}".format("Custo Total do Estoque:", custo_total))
    print("{:<55} {:<15.2f}".format("Faturamento Total do Estoque:", faturamento_total))


relatorio_geral_estoque(estoque)
