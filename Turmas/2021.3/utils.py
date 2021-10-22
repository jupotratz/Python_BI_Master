from IPython.display import clear_output
import pandas as pd
import time

def orcamento_pintor():

    tabela_rendimentos = {"Marca":list('ABCDEF'),"RT":[4, 6, 8, 10, 12, 14], 'Price':[3.40, 5.10, 6.80, 8.50, 10.20, 11.90]}
    tabela_rendimentos = pd.DataFrame(tabela_rendimentos)
    quantidade_salas = input('Quantas salas existem no seu escritório: ')
    clear_output(wait=True) # ========= clear terminal output
    preco_metro_quadrado = 3.5


    infos_salas, valor_total = [], 0
    for idx  in range(int(quantidade_salas)):
        formato = input(f'Qual o formato da sala {idx+1}?\n\n1 - Quadrada\n2 - Retangular\n\n Escolha uma das opções desejadas: ')
        while formato not in ['1','2']:
            clear_output(wait=True) # ========= clear terminal output
            print('========= OPÇÃO INVÁLIDA =========\n\nTente novament...\n\n')
            formato = input(f'Qual o formato da sala {idx+1}?\n\n1 - Quadrada\n2 - Retangular\n\n Escolha uma das opções desejadas: ')

        clear_output(wait=True) # ========= clear terminal output

        largura = float(input(f'Informe a largura da sala {idx+1}: '))
        altura =  float(input(f'Informe a altura da sala {idx+1}: '))

        if formato == '2':
            comprimento = float(input(f'Informe o comprimento da sala {idx+1}: '))
            area_teto = largura*comprimento
            area_paredes = ((2*(largura*altura))+(2*(comprimento*altura)))*0.95
            area_pintura_aproximada = area_teto + area_paredes 
        else:
            area_teto = largura*largura
            area_paredes = 4*(largura*altura)*0.95
            area_pintura_aproximada = area_teto + area_paredes
        
        valor_sala = area_pintura_aproximada*preco_metro_quadrado
        valor_total += valor_sala

    infos_salas.append([formato,area_pintura_aproximada,valor_sala])
    clear_output(wait=True) # ========= clear terminal output

    print('========= Orçamento =========',end='\n\n')

    print(f'Mão de obra: R$ {round(valor_total,2)}',end='\n\n')
    print('Orçamento estimado do material por marca: ')

    total_p, total_l = 0, 0

    for idx, (_,area_pintura_aproximada,valor_sala) in enumerate(infos_salas):
        tabela_rendimentos[f'Sala_{idx+1}_(Preço)'] = tabela_rendimentos.apply(lambda x: round(area_pintura_aproximada/x.RT,0)*x.Price,axis=1)
        tabela_rendimentos[f'Sala{idx+1}_(Litros)'] = tabela_rendimentos.apply(lambda x: round(area_pintura_aproximada/x.RT,0),axis=1)
        total_p += tabela_rendimentos[f'Sala_{idx+1}_(Preço)'].sum()
        total_l += tabela_rendimentos[f'Sala{idx+1}_(Litros)'].sum()
    print(tabela_rendimentos,end='\n\n')

    print(f'Orçamento estimado do material total: R$ {round(total_p,2)}, sendo {total_l} l de tinta.')


from IPython.display import clear_output


def gerar_grafico_cliente_categorias(lista_produtos_cliente):
  import numpy as np
  import matplotlib.pyplot as plt

  lista_categorias, valor_categoria = [], []
  for produto in lista_produtos_cliente:
    lista_categorias.append(produto[2])
  
  lista_categorias = np.array(lista_categorias)
  unique, counts = np.unique(lista_categorias, return_counts=True)

  for categoria in unique:
    valor_categoria.append(sum([produto[1] for produto in lista_produtos_cliente if produto[-1]==categoria]))
  valor_categoria = np.array(valor_categoria)

  plt.rcParams['figure.figsize'] = (15,7)
  fig, (ax1, ax2) = plt.subplots(1, 2)
  fig.suptitle('Estatistica por categoria de produto')
  ax1.pie(counts/(counts.sum()) ,labels=unique,autopct='%1.1f%%',shadow=True)
  ax1.set_title('Porcentagem de Produtos por categoria')
  ax2.pie(valor_categoria/(valor_categoria.sum()) ,labels=unique,autopct='%1.1f%%')
  ax2.set_title('Porcentagem do valor total por categoria')
  plt.legend(unique,bbox_to_anchor=(1.2, 1), loc=2, borderaxespad=0.)
  plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
  plt.show()



def caixa_sr_joaquin():
  texto_inicial = 'Operações disponíveis\n\n1 - Contabilizar nova compra\n2 - Fechar caixa\n\nDigite a opção desejada: '
  texto_compra_cliente = 'Operações disponíveis\n\n1 - Cadastrar novo produto\n2 - Encerrar compra do cliente\n\nDigite a opção desejada: '''
  dicionario_produtos = {'0':{'preço':7.45,'Nome':'Alvejante','tipo':'limpeza'},
                        '1':{'preço':2,'Nome':'Amaciante','tipo':'limpeza'},
                        '2':{'preço':50,'Nome':'Desinfetante','tipo':'limpeza'},
                        '3':{'preço':34,'Nome':'Detergente','tipo':'limpeza'},
                        '4':{'preço':68,'Nome':'Escovinhas','tipo':'limpeza'},
                        '5':{'preço':102,'Nome':'Esponja de aço','tipo':'limpeza'},
                        '6':{'preço':67,'Nome':'Luvas de borracha','tipo':'limpeza'},
                        '7':{'preço':45,'Nome':'Pá','tipo':'limpeza'},
                        '8':{'preço':12,'Nome':'Pano de chão','tipo':'limpeza'},
                        '9':{'preço':7,'Nome':'Pano de prato','tipo':'limpeza'},
                        '10':{'preço':2,'Nome':'Rodo','tipo':'limpeza'},
                        '11':{'preço':5,'Nome':'Sabão em barra','tipo':'limpeza'},
                        '12':{'preço':19.49,'Nome':'Sabão em pó','tipo':'limpeza'},
                         '13':{'preço':12.59,'Nome':'Vassoura','tipo':'limpeza'},
                         '14':{'preço':6.35,'Nome':'Água sanitária','tipo':'limpeza'},
                         '15':{'preço':9.39,'Nome':'Absorvente','tipo':'higiene pessoal'},
                         '16':{'preço':5.49,'Nome':'Algodão','tipo':'higiene pessoal'},
                         '17':{'preço':18.99,'Nome':'Condicionador','tipo':'higiene pessoal'},
                         '18':{'preço':10.49,'Nome':'Cotonete','tipo':'higiene pessoal'},
                         '19':{'preço':15.49,'Nome':'Escova de dentes','tipo':'higiene pessoal'},
                         '20':{'preço':35.47,'Nome':'Hidratantes','tipo':'higiene pessoal'},
                         '21':{'preço':16.99,'Nome':'Lâmina de barbear','tipo':'higiene pessoal'},
                         '22':{'preço':17.49,'Nome':'Papel higiênico','tipo':'higiene pessoal'},
                         '23':{'preço':13.59,'Nome':'Pasta de dente','tipo':'higiene pessoal'},
                         '24':{'preço':2.49,'Nome':'Sabonetes','tipo':'higiene pessoal'},
                         '25':{'preço':20.99,'Nome':'Shampoo','tipo':'higiene pessoal'},
                         '26':{'preço':4.59,'Nome':'Biscoitos','tipo':'padaria'},
                         '27':{'preço':3.99,'Nome':'Bisnaguinha','tipo':'padaria'},
                         '28':{'preço':7.49,'Nome':'Broinha de milho','tipo':'padaria'},
                         '29':{'preço':6.59,'Nome':'Pães de queijo','tipo':'padaria'},
                         '30':{'preço':4.99,'Nome':'Pão de cachorro-quente','tipo':'padaria'},
                         '31':{'preço':5.89,'Nome':'Pão de forma','tipo':'padaria'},
                         '32':{'preço':4.99,'Nome':'Pão de hambúrguer','tipo':'padaria'},
                         '33':{'preço':7.59,'Nome':'Achocolatados','tipo':'bebidas'},
                         '34':{'preço':1.59,'Nome':'Água','tipo':'bebidas'},
                         '35':{'preço':5.15,'Nome':'Cervejas','tipo':'bebidas'},
                         '36':{'preço':7.89,'Nome':'Energéticos','tipo':'bebidas'},
                         '37':{'preço':8.99,'Nome':'Refrigerantes','tipo':'bebidas'},
                         '38':{'preço':4.99,'Nome':'Sucos','tipo':'bebidas'},
                         '39':{'preço':70.89,'Nome':'Vinhos','tipo':'bebidas'},
                         '40':{'preço':5.99,'Nome':'Vitaminas','tipo':'bebidas'},
                         '41':{'preço':79.99,'Nome':'Vodka','tipo':'bebidas'},
                         '42':{'preço':1.56,'Nome':'banana','tipo':'frutas'},
                         '43':{'preço':7.99,'Nome':'abacate','tipo':'frutas'},
                         '44':{'preço':8.99,'Nome':'mamão','tipo':'frutas'},
                         '45':{'preço':4.99,'Nome':'morango','tipo':'frutas'},
                         '46':{'preço':3.99,'Nome':'manga','tipo':'frutas'},
                         '47':{'preço':7.00,'Nome':'abacaxi','tipo':'frutas'},
                         '48':{'preço':5.99,'Nome':'limão','tipo':'frutas'},
                         '49':{'preço':4.99,'Nome':'laranja','tipo':'frutas'},
                         '50':{'preço':5.99,'Nome':'maça','tipo':'frutas'},
                         '51':{'preço':8.99,'Nome':'pera','tipo':'frutas'},
                         '52':{'preço':3.59,'Nome':'batata','tipo':'legumes'},
                         '53':{'preço':3.15,'Nome':'cenoura','tipo':'legumes'},
                         '54':{'preço':6.55,'Nome':'tomate','tipo':'legumes'},
                         '55':{'preço':4.25,'Nome':'pimentão','tipo':'legumes'},
                         '56':{'preço':3.95,'Nome':'beterraba','tipo':'legumes'},
                         '57':{'preço':4.65,'Nome':'pepino','tipo':'legumes'},
                         '58':{'preço':19.46,'Nome':'alho','tipo':'temperos'},
                         '59':{'preço':10.55,'Nome':'cebola','tipo':'temperos'},
                         '60':{'preço':1.50,'Nome':'cebolinha','tipo':'temperos'},
                         '61':{'preço':1.5,'Nome':'salsa','tipo':'temperos'},
                         '62':{'preço':1.5,'Nome':'coentro','tipo':'temperos'},
                         '63':{'preço':3.5,'Nome':'couve','tipo':'verduras'},
                         '64':{'preço':4.6,'Nome':'alface','tipo':'verduras'},
                         '65':{'preço':3.5,'Nome':'rúcula','tipo':'verduras'},
                         '66':{'preço':5.99,'Nome':'couve-flor','tipo':'verduras'},
                         '67':{'preço':4.99,'Nome':'repolho','tipo':'verduras'},
                         '68':{'preço':21.59,'Nome':'frango','tipo':'congelados'},
                         '69':{'preço':15.99,'Nome':'Hambúrguer','tipo':'congelados'},
                         '70':{'preço':8.99,'Nome':'Lasanha','tipo':'congelados'},
                         '71':{'preço':19.59,'Nome':'Linguiça','tipo':'congelados'},
                         '72':{'preço':11,'Nome':'Pão de queijo','tipo':'congelados'},
                         '73':{'preço':5.87,'Nome':'Petiscos','tipo':'congelados'},
                         '74':{'preço':11,'Nome':'Pratos prontos','tipo':'congelados'},
                         '75':{'preço':16.54,'Nome':'Pizza','tipo':'congelados'},
                         '76':{'preço':7.49,'Nome':'Salsicha','tipo':'congelados'},
                         '77':{'preço':11,'Nome':'salsichão','tipo':'congelados'},
                         '78':{'preço':20.99,'Nome':'Arroz','tipo':'diversos'},
                         '79':{'preço':23.99,'Nome':'Azeite','tipo':'diversos'},
                         '80':{'preço':16.87,'Nome':'Café','tipo':'diversos'},
                         '81':{'preço':5.0,'Nome':'Bolachas e biscoitos','tipo':'diversos'},
                         '82':{'preço':8.59,'Nome':'Chá','tipo':'diversos'},
                         '83':{'preço':15.65,'Nome':'sardinha','tipo':'diversos'},
                         '84':{'preço':39.99,'Nome':'atum','tipo':'diversos'},
                         '85':{'preço':2.35,'Nome':'milho','tipo':'diversos'},
                         '86':{'preço':2.35,'Nome':'ervilha','tipo':'diversos'},
                         '87':{'preço':3.59,'Nome':'Extrato de tomate','tipo':'diversos'},
                         '88':{'preço':3.49,'Nome':'Farinha de milho','tipo':'diversos'},
                         '89':{'preço':3.99,'Nome':'Farinha de mandioca','tipo':'diversos'},
                         '90':{'preço':6.49,'Nome':'Farofa pronta','tipo':'diversos'},
                         '91':{'preço':10.99,'Nome':'Feijão','tipo':'diversos'},
                         '92':{'preço':4.25,'Nome':'Leite','tipo':'diversos'},
                         '93':{'preço':4.99,'Nome':'Macarrão','tipo':'diversos'},
                         '94':{'preço':8.8,'Nome':'Maionese','tipo':'diversos'},
                         '95':{'preço':7.5,'Nome':'Óleo','tipo':'diversos'},
                         '96':{'preço':5.8,'Nome':'Tempero pronto','tipo':'diversos'},
                         '97':{'preço':2.5,'Nome':'Batata palha','tipo':'diversos'}
                        }


  total_por_cliente, total_produtos = [], []
  operacao_caixa = int(input(texto_inicial))
  clear_output(wait=True) # ========= clear terminal output

  while operacao_caixa != 2:
    print(f'=== Cadastrar compras do cliente {len(total_por_cliente)+1} do dia ===',end='\n\n')
    
    compras_cliente = []
    opcao_compra_cliente = int(input(texto_compra_cliente))
    while opcao_compra_cliente != 2:

      cod_barras = input('Digite o código de barras do produto: ')
      clear_output(wait=True) # ========= clear terminal output
      compras_cliente.append((dicionario_produtos[cod_barras]['Nome'],dicionario_produtos[cod_barras]['preço'],dicionario_produtos[cod_barras]['tipo']))
      
      print(f'=== Cadastrar compras do cliente {len(total_por_cliente)+1} do dia ===',end='\n\n')
      for val in compras_cliente:
        print(f'{val[0]} - R$ {round(val[1],2)}')
      
      print()
      opcao_compra_cliente = int(input(texto_compra_cliente))
    
    clear_output(wait=True) # ========= clear terminal output
    total = sum([produto[1] for produto in compras_cliente])
    print(f'=== Conta final do cliente {len(total_por_cliente)+1} do dia ===',end='\n\n')
    for val in compras_cliente:
        print(f'{val[0]} - R$ {round(val[1],2)}')
    
    print(f'\nTotal: R$ {round(total,2)}')
    gerar_grafico_cliente_categorias(compras_cliente)
    
    total_por_cliente.append(total)
    total_produtos += compras_cliente
  
    time.sleep(15)
    print('Pagamento efetuado com sucesso')
    time.sleep(5)
    clear_output(wait=True) # ========= clear terminal output
    print()
    operacao_caixa = int(input(texto_inicial))
  
  valor_total_caixa = sum([preco for (nome,preco,tipo) in total_produtos])

  print(f'O caixa fechou com um total de R$ {valor_total_caixa}')
  gerar_grafico_cliente_categorias(total_produtos)