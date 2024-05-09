# IMPORTAÇÃO DAS BIBLIOTECA
import pandas as pd
import tkinter as tk
from tkinter import ttk, scrolledtext
import folium
from folium.plugins import MarkerCluster
import webbrowser
import keyboard
import pyautogui

# LEITURA DO ARQUIVO EM CSV
nome_arquivo = './queimadas/queimadas1.csv'
dados = pd.read_csv(nome_arquivo)

# LISTA DE ESTADOS EM ORDEM ALFABÉTICA
estados_ordenados = sorted(dados['estado'].unique())


def atualizar_mapa():
    # OBTÉM O ESTADO QUE O USUÁRIO SELECIONOU
    estado_desejado = combo_estados.get().upper()

    # FILTRA O DATAFRAME PELO ESTADO DESEJADO
    dados_estado = dados[dados['estado'] == estado_desejado]

    # VERIFICA SE O ESTADO FOI ENCONTRADO
    if dados_estado.empty:
        adicionar_mensagem(
            f"Estado '{estado_desejado}' não encontrado. Por favor, insira um estado válido.")
    else:

        # PERGUNTA AO USUÁRIO A CLASSIFICAÇÃO DESEJADA
        classificacao_desejada = combo_classificacao.get().capitalize()

        # ADICIONA A COLUNA 'CLASSIFICACAO_RISCO AO DATAFRAME'
        dados['classificacao_risco'] = pd.cut(dados['frp'], bins=[
            -float('inf'), 0, 5, 15, float('inf')],
            labels=['Baixo', 'Médio', 'Alto', 'Emergência'])

        # FILTRA NOVAMENTE PELO ESTADO E CLASSIFICAÇÃO DESEJADA
        dados_filtrados = dados[(dados['estado'] == estado_desejado) & (
            dados['classificacao_risco'] == classificacao_desejada)]

        # REMOVE E SUBSTITUI OS VALORES NAN EM 'LAT E 'LON'
        dados_filtrados = dados_filtrados.dropna(subset=['lat', 'lon'])

        # VERIFICA SE AINDA HÁ DADOS APÓS A REMOÇÃO DOS NANS
        if dados_filtrados.empty:
            adicionar_mensagem(
                f"Não há dados disponíveis para o estado '{estado_desejado}' e a classificação '{classificacao_desejada}'.")
        else:
            # CRIA UM MAPA INTERATIVO COM FOLIUM
            mapa = folium.Map(
                location=[dados_filtrados['lat'].mean(), dados_filtrados['lon'].mean()], zoom_start=8)

            # ADICIONA PONTOS DE MARCADORES
            marker_cluster = MarkerCluster().add_to(mapa)

            # ADICIONA SOBRE AS LINHAS DO DATAFRAME E ADICIONA MARCADORES AO MAPA
            for idx, row in dados_filtrados.iterrows():
                # CRIA UM POP - UP PERSONALIZADO
                pop_up_content = (
                    f"<b>Latitude:</b> {row['lat']}<br>"
                    f"<b>Longitude:</b> {row['lon']}<br>"
                    f"<b>Bioma:</b> {row['bioma']}<br>"
                    f"<b>Estado:</b> {row['estado']}<br>"
                    f"<b>Município:</b> {row['municipio']}<br>"
                    f"<b>Data e Hora:</b> {row['data_hora_gmt']}<br>"
                    f"<b>Classificação de Risco:</b> {row['classificacao_risco']}"
                )

                folium.Marker(
                    location=[row['lat'], row['lon']],
                    popup=folium.Popup(folium.Html(pop_up_content, script=True), max_width=300),
                ).add_to(marker_cluster)

            # SALVA O MAPA COMO UM ARQUIVO HTML TEMPORÁRIO
            mapa.save('mapa_risco.html')

            # ABRE O NAVEGADOR PADRÃO PARA EXIBIR O MAPA E RECARREGAR A PÁGINA
            webbrowser.open('mapa_risco.html', new=2)  # O argumento new=2 abre em uma nova aba

            # AGUARDA UM CURTO PERÍODO E DEPOIS ABRE EM TELA CHEIA
            root.after(2000, abrir_em_tela_cheia)


def abrir_em_tela_cheia():
    # USA O PYAUTOGUI PARA PRESSIONAR A TECLA F11 PARA FICAR EM TELA CHEIA
    pyautogui.press('f11')

    # BLOQUEIA A TECLA F11 PARA EVITAR QUE A JANELA SAIA DO MODO DE TELA CHEIA
    keyboard.block_key('f11')


def adicionar_mensagem(mensagem):
    # ADICIONA UMA MENSAGEM À ÁREA DE TEXTO DA INTERFACE
    texto_area.insert(tk.END, mensagem + '\n')
    # ROLA A BARRA DO CAMPO DE TEXTO DA INTERFACE PARA VISUALIZAR A MENSAGEM
    texto_area.see(tk.END)


# CONFIGURAÇÃO DA INTERFACE GRÁFICA
root = tk.Tk()
root.title("Análise de Queimadas")

# LARGURA E ALTURA DA JANELA DA INTERFACE
largura_janela = 450
altura_janela = 300

# OBTÉM AS DIMENSÕES DA TELA
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# DEFINE A POSIÇÃO NO CANTO SUPERIOR DIREITO DA TELA DO COMPUTADOR DE EXECUÇÃO
pos_x = largura_tela - largura_janela
pos_y = 0

# DEFINE AS DIMENSÕES E A POSIÇÃO DA JANELA PRINCIPAL
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# MANTÉM A JANELA NO TOPO
root.attributes('-topmost', 1)

# O CAMPO PARA ESCOLHER O ESTADO
label_estado = tk.Label(root, text="Escolha o estado:")
combo_estados = ttk.Combobox(root, values=estados_ordenados)
label_estado.grid(row=1, column=1, pady=25)
combo_estados.grid(row=1, column=2, pady=25)

# CAMPO PARA ESCOLHER A CLASSIFICAÇÃO DE RISCO
label_classificacao = tk.Label(root, text="Classificação de risco:")
classificacoes = ['Baixo', 'Médio', 'Alto', 'Emergência']
combo_classificacao = ttk.Combobox(root, values=classificacoes)
label_classificacao.grid(row=2, column=1, pady=18)
combo_classificacao.grid(row=2, column=2, pady=18)

# BOTÃO PARA ATUALIZAR O MAPA
botao_atualizar = tk.Button(
    root, text="Atualizar Mapa", command=atualizar_mapa)
botao_atualizar.grid(row=3, column=2, columnspan=2, pady=30)

# ÁREA DE TEXTO PARA EXIBIR MENSAGENS
texto_area = scrolledtext.ScrolledText( 
    root, wrap=tk.WORD, width=40, height=5)
texto_area.grid(row=4, column=1, columnspan=3, pady=10, padx=10)

# INICIA O LOOP PARA MANTER A INTERFACE GRÁFICA ATIVA ATÉ O USUÁRIO FECHAR
root.mainloop()
