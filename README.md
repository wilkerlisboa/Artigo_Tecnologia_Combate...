
# 1.	Instalação da Linguagem Python no Windows:
A instalação da linguagem Python para Windows acaba sendo uma forma simples, siga os passos a seguir:

* 1.2	– Entre no site https://www.python.org/downloads/. Aparecera a pagina de download padrão do python, basta clicar no botão amarelo escrito Download Python 3.12.3. Nesse botão está por padrão do site a versão mais recente do python e nesse artigo foi usado o python 3.12.3.

* 1.3	– Após o download, acesse o explorador de arquivo e encontre o arquivo do instalador que acabou de baixar e execute, após executar o instalador, marque as caixinhas que corresponde a Use admin privileges when installing py.exe (Use privilégios de administrador ao instalar py.exe) e Add python.exe to PATH (Adicione python.exe ao PATH), após isso clique em “Customize installation”, vai abrir a página de Optional Features em seguida selecione todas as caixinhas existente nessa tela e clique em “Next”, aparecera uma nova página chamada de Advanced Options, novamente selecione todas as caixinhas e clique em “Install”, após carregar toda a instalação clique em “close” para fecha o instalador.

* 1.4	– Abra o CMD (Prompt de Comando) apertando em seu teclado as teclas “Ctrl + r” aparecerá o executado do Windows, digite CMD e clique em “ok”, no cmd digite “python -–version” e clique em Enter no seu teclado, deve aparecer no cmd “Python 3.12.3”, significa que ocorreu tudo certo na instalação, nesse caso você pode pular para o tópico “2. - Instalação das Bibliotecas Python no Windows”, caso apareça um erro talvez seja o “path” do sistema, não está configurado, siga o próximo passo para realizar a configuração.

* 1.5	– Configuração do “path”, vá no campo de pesquisa do sistema operacional do Windows e digite “variáveis de ambiente” e clique em “Editar as variáveis de ambiente do sistema”, procure a variável chamada de path, selecione editar.

* 1.6	– Na próxima janela, você encontra uma lista de vários paths de outros programas. Para adicionar um novo clique no botão “Novo” e em seguida adicione o caminho do instalador, geralmente o python adiciona um caminho por padrão como por exemplo. “C:\Program Files\Python312“, procure na sua máquina o diretório a onde foi instalado e adicione o caminho na variável de ambiente, clique em ok depois ok novamente e feche a janela, reinicie o sistema operacional Windows.

Com todos esses passos o python já deve está funcionando corretamente na sua máquina Windows, para testar se está tudo funcionando corretamente realize o passo anterior de numero 1.4, caso ainda sofra com problemas na instalação recomendo consultar a documentação oficial da linguagem https://docs.python.org/release/3.12.3/tutorial/index.html. 

# 2.	Instalação das Bibliotecas Python no Windows:
Nesse artigo foi usado as bibliotecas como “pandas”, “folium”, “keyboard”, “pyautogui” que serão instaladas, outras bibliotecas usadas já estão incluídas no python como “tkinter” e “webbrowser”.
Após a Instalação do python vamos apresentar como instalar as bibliotecas como para realizar o algoritmo, usando o PIP (Pip Installs Packages ou Pip instala pacotes) e um gerenciador de pacotes do python, para iniciar vamos ao passo a passo.

* 2.1	–  Abra o terminal conhecido no Windows como CMD digite “pip install --upgrade pip” apenas como uma boa prática esse comando inicia a atualização do pip.

        pip install --upgrade pip

    Após executar esse comando aparecera a mensagem de “Requirement already satisfied: pip”

    Indicando que a versão mais recente já está instalada no seu ambiente de desenvolvimento.

        pip install pandas

    E cole no seu terminal cmd do Windows e clique em enter no seu teclado.

    Após isso se iniciara a instalação da biblioteca e o final aparecera a mensagem de “Successfully installed pandas-2.2.2”, significando que a instalação foi realizada com sucesso no seu ambiente de desenvolvimento.

        pip install folium
    
    Após isso clique em enter no teclado.

    Aparecera no seu terminal cmd Windows a mensagem de “Installing collected packages: folium”, significando que foi realizado a instalação correta da biblioteca no seu ambiente de desenvolvimento.

        pip install keyboard

    Clique em enter no seu teclado e em seguida aparecera na sua tela.
    Após isso aparecera a mensagens “Sucessfully installed keyboard-0.13.5”, significando que ocorreu tudo certo na instalação.

# 3.	Instalação da IDE – Visual Studio Code no Windows:
Com o ambiente quase todo configurado para rodar o algoritmo, agora fazer a instalação do vs code (Visual Studio Code) para a escrita do algoritmo mais apresentável e mais apropriada no desenvolvimento. Para realizar o download do vs code acesse o link https://code.visualstudio.com/download
Ao acessar o link selecione o sistema operacional Windows no qual e usado no desenvolvimento do algoritmo.

* 3.1	– A instalação do vs code também não e muito difícil após baixar o instalador, basta abrir o explorador de arquivos e executar o instalador baixado.

* 3.2	– Aceite os termos de uso e clique em próximo na janela seguinte marque todas as caixinhas e clique novamente em próximo, basta esperar carregar a instalação após isso aparecera a janela de conclusão e basta clicar em concluir.

Após finalizar as etapas anteriores você já tem instalado todas as dependências para realizar e acessar o software que esse artigo apresenta. 
Lembrando que para compilar o código em python basta abrir o terminal dentro da pasta do seu diretório que este seu arquivo em python e digitar.

        “py nomeDoSeuArquivo.py” 
    

Onde “py” e usado para chamar o compilador e o “nomeDoSeuArquivo.py” e para o compilador entender que isso que você está tentando rodar.

Lembre-se que para o algoritmo dessa apresentação funcionar o arquivo em python tem que estar no mesmo diretório dos arquivos adquiridos no site do INPE (Instituto Nacional de Pesquisas Espaciais).

# 4.	– Código:
A seguir o código foi usando dentro do vs code (Visual Studio Code) esse código apresenta uma implementação em python.

        # IMPORTAÇÃO DAS BIBLIOTECA
        import pandas as pd
        import tkinter as tk
        from tkinter import ttk, scrolledtext
        import folium
        from folium.plugins import MarkerCluster
        import webbrowser
        import keyboard
        import pyautogui

O código a cima importa as bibliotecas necessárias para manipulação de dados (pandas), criação de interface o (tkinter), geração de mapas interativos (folium), controle de navegador web (webbrowser), controle de teclado (keyboard) e mecanização de interface gráfica (pyautogui).

    # LEITURA DO ARQUIVO EM CSV
    nome_arquivo = './queimadas/11-03-2024.csv'
    dados = pd.read_csv(nome_arquivo)

Nessa parte do código lê um arquivo CSV que contém dados de queimadas adquirido no site https://dataservercoids.inpe.br/queimadas/queimadas/focos/csv/diario/America_Sul/
A variável ‘nome_arquivo’ especifica o caminho relativo do arquivo adquirido no site do INPE. E os dados são carregados para o DataFrame ‘dados’ utilizando a função ‘pd.read_csv(nome_arquivo)’.

    # LISTA DE ESTADOS EM ORDEM ALFABÉTICA
    estados_ordenados = sorted(dados['estado'].unique())

Uma lista de estados em ordem alfabética é criada a partir dos dados carregados do CSV. A função ‘unique()’ retorna os valores únicos da coluna ‘estado’ e ‘sorted()’ ordena esses valores alfabeticamente.

    def atualizar_mapa():
    # OBTÉM O ESTADO QUE O USUÁRIO SELECIONOU
    estado_desejado = combo_estados.get().upper()

Esta função é chamada quando o usuário clica no botão “Atualizar Mapa”. Ela obtém o estado selecionado pelo usuário na interface gráfica e converte para letras maiúsculas.

    # FILTRA O DATAFRAME PELO ESTADO DESEJADO
    dados_estado = dados[dados['estado'] == estado_desejado]

Os dados do DataFrame são filtrados para incluir apenas as linhas onde o estado e igual ao estado selecionado pelo usuário.

    # VERIFICA SE O ESTADO FOI ENCONTRADO
        if dados_estado.empty:
            adicionar_mensagem(
                f"Estado '{estado_desejado}' não encontrado. Por favor, insira um estado válido.")

É verificado se existem dados para o estado selecionado. Se não houver dados, uma mensagem de erro é exibida na interface gráfica.

        else:

        # PERGUNTA AO USUÁRIO A CLASSIFICAÇÃO DESEJADA
        classificacao_desejada = combo_classificacao.get().capitalize()

Se o estado selecionado tiver dados, a função pergunte ao usuário qual classificação de risco ele deseja visualizar e converte a resposta para capitalizada.

        # ADICIONA A COLUNA 'CLASSIFICACAO_RISCO AO DATAFRAME'
        dados['classificacao_risco'] = pd.cut(dados['frp'], bins=[
            -float('inf'), 0, 5, 15, float('inf')],
            labels=['Baixo', 'Médio', 'Alto', 'Emergência'])

Uma nova coluna chamada ‘classificacao_risco’ é adicionanda ao DataFrame ‘dados’, com base nos valores da coluna frp (Fire Radiative Power ou Potência Radiativa do Fogo). Essa coluna é categorizada em diferentes níveis de risco: Baixo, Médio, Alto e Emergência.

Para ver o codigo na pratica basta acessar o link do arquivo aqui no github "codigo".
