estoque = {}
opcoes = ["cadastrar", "alterar", "excluir", "excluir", "listar", "vender"]

while True:
    print(" 1 - Cadastro\n",  
          "2 - Alterar\n",
          "3 - Excluir\n",
          "4 - Listar\n",
          "5 - Vender")
    opcao = input("O que você gostaria de realizar: ")

    if opcao == "1":
        cod= len(estoque) + 1
        nome = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço: "))
        quantidade = int(input("Informe a quantidade disponível: "))
        produtos= [nome, preco, quantidade]
        estoque.update({cod:produtos})
        print('Produto cadastrado com sucesso!')

    elif opcao == "2":
        produto = int(input("Informe o ID do produto: "))
        if produto in estoque.keys():
            nome = input("Informe o nome do produto: ")
            preco = float(input("Informe o preço: "))
            quantidade = int(input("Informe a quantidade disponível: "))
            estoque[produto] = [nome, preco, quantidade]
        else:
            print('Produto não encontrado!')
    
    elif opcao == "3":
        produto = int(input("Informe o código do item que deseja excluir: "))
        if produto in estoque:
            confimar = input(f"Deseja excluir o item {estoque[produto]} (S/N): ")
            if confimar.title() == "S":
                estoque.pop(produto)
                print('Produto excluído com sucesso!')
        
        else:
            print('Produto não encontrado!')

    elif opcao == "4":
        for cod in estoque.keys():
            print(f'Id: {cod} | Produto: {estoque[cod][0]} | Valor: R${estoque[cod][1]} | Unidades: {estoque[cod][2]}')

    elif opcao == "5":
        total=0
        vendendo = True
        while vendendo:
            item= int(input('Qual o código do item que gostaria de vender? '))
            
            if item in estoque.keys():
                un= int(input('Quantas unidades gostaria de vender? '))

                if un <= estoque[item][2]:
                    estoque[item][2] -= un
                    subtotal= un * estoque[item][1]
                    total+=subtotal
                elif un > estoque[item][2]:
                    print("Quantidade indisponível!")

            elif item not in estoque.keys():
                print('Item inválido.')
                continue
            
            add= input("Deseja adicionar algo mais [S/N]? ").upper()

            if add == 'N':
                vendendo= False
                print(f'O total é R${round(total,2)}')
            else:
                continue   
