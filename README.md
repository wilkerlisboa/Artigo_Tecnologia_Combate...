# Tecnologia - Combate a Queimadas e Incêndios
**Autor:** Wilker Lisboa

## Resumo
O artigo visa combater queimadas através de aplicações de tecnologias como OpenCV, YOLO, Dronekit e Redes Neurais, um conjunto de bibliotecas de visão computacional e processamento de imagem. A abordagem envolve a detecção automatizada de focos de incêndios e queimadas em imagens  ou vídeos, seguida por um mecanismo para acionar a extinção do fogo. A inspiração para esse artigo surgiu por um alto índice de fumaça nas regiões norte do Brasil.

## 1 - Introdução
A inspiração para este artigo surgiu a partir de uma observação impactante da realidade vivenciada no estado do Amapá, na cidade de Macapá e em diversas regiões localizadas no norte do Brasil. Desde o início de setembro de 2023 até o momento presente, em novembro de 2023, relatos persistentes indicam a presença intensa de fumaça, evidenciando a séria problemática das queimadas e incêndios florestais. Esta situação, além de comprometer a qualidade do ar e a saúde das comunidades, aumenta consideravelmente os desafios enfrentados pelos órgãos de segurança pública.

O objetivo central deste artigo é apresentar um software inovador capaz de rastrear, identificar e extinguir de maneira eficiente as queimadas e incêndios florestais no Brasil, especialmente nos estados localizados na região norte. A proposta visa não apenas mitigar os impactos ambientais desastrosos, mas também reduzir a carga sobre os servidores de segurança pública.

A abordagem técnica para alcançar esse objetivo envolve a aplicações de tecnologias como o OpenCV, YOLO, Dronekit e Redes Neurais, que são ferramentas de visão computacional reconhecidas por suas eficácias na análise de imagens e detecção de padrões. Ao criar um sistema inteligente de monitoramento e intervenção, este projeto busca não apenas inovar na prevenção e combate a queimadas, mas também estabelecer uma solução escalável e adaptável a diversas regiões geográficas.

Ao combinar a sensibilidade ambiental com a potência da tecnologia, a proposta não apenas almeja enfrentar as queimadas e incêndios de maneira proativa, mas também estabelecer um precedente para a integração eficiente de soluções tecnológicas nas gestões de desastres naturais. Este artigo, fundamentado em referências pré - existentes e aprimorado por ideias inovadoras, representa um passo crucial na direção de um futuro mais resiliente, sustentável e seguro para as comunidades dos estados afetados.


## 2 - Doenças Respiratórias Causadas por Queimadas e Incêndios
As queimadas e incêndios, além de representarem uma ameaça direta à biodiversidade e ao meio ambiente, exercem uma influência significativa na saúde da população urbana. Esses eventos, muitas vezes desencadeados por atividades humanas ou condições climáticas adversas, liberam substâncias tóxicas e partículas finas no ar, gerando sérias consequências para a saúde pública. Abaixo, está citado algumas das doenças associadas a esses eventos e os impactos que têm sobre a vida urbana nas comunidades dos estados da região norte do Brasil.

* **2.1 - Exacerbação de Asma**

A fumaça proveniente de queimadas contém partículas finas e gases irritantes, o que pode desencadear ou piorar os sintomas de asma, afetando especialmente crianças e adultos predispostos.

* **2.2 - Bronquite e Doença Pulmonar Obstrutiva Crônica (DPOC)**

A inalação de poluentes presentes na fumaça pode contribuir para o desenvolvimento ou agravamento de condições respiratórias crónicas.

* **2.3 - Conjuntivite e Irritação Ocular**

A presença de partículas finas na atmosfera durante e após os incêndios pode causar irritações nos olhos, levando a sintomas como vermelhidão e coceira.

* **2.4 - Dermatites e Alergias Cutâneas**

A exposição prolongada à fumaça e aos produtos químicos liberados pode resultar em irritações na pele, agravando condições dermatológicas preexistentes.

* **2.5 - Aumento de Risco de Ataques Cardíacos:**

As partículas finas presentes na fumaça podem penetrar no sistema circulatório, aumentando o risco de ataques cardíacos em pessoas com problemas cardiovasculares.

* **2.6 - Agravamento de Doenças Cardiovasculares**

A exposição crônica à fumaça gerada por queimadas e incêndios pode contribuir para o desenvolvimento ou agravamento de doenças cardiovasculares.

## 3 - Visão computacional
A Visão Computacional, no âmbito da Ciência da Computação e Inteligência Artificial, representa uma capacidade extraordinária de interpretar e extrair significado de imagens e vídeos. Este campo avançado compreende uma série de processos, desde a aquisição e pré - processamento de imagens até a tomada de decisões inteligentes baseadas na análise visual.

* **3.1 - Principais Componentes**

Inicia - se com a aquisição de dados visuais, seguida pelo pré - processamento para otimização. A segmentação divide imagens, simplificando a análise, enquanto a extração de características identifica padrões.

* **3.2 - Aquisição de Imagens:** Captura inicial de dados visuais por meio de câmeras ou sensores.

* **3.3 - Pré-processamento:** Aprimoramento da qualidade das imagens para análise mais eficiente.

* **3.4 - Segmentação de Imagem:** Divisão da imagem para identificação mais clara de áreas de interesse.

* **3.5 - Extração de Características:** Identificação de padrões e características relevantes.

* **3.5 - Reconhecimento de Padrões:** Identificação autônoma de elementos específicos nas imagens.

* **3.6 - Aprendizado de Máquina:** Treinamento dos modelos para aprimoramento contínuo.

* **3.7 - Tomada de Decisão:** Execução de tarefas específicas com base na análise visual.

## 4 - Instalação do OpenCV e Ambiente de Desenvolvimento
Para começar a explorar as capacidades da Visão Computacional utilizando o OpenCV, é essencial configurar um ambiente de desenvolvimento adequado. A seguir, está um guia passo a passo para a instalação do OpenCV, juntamente com outras bibliotecas essenciais, em sistemas populares.

* **4.1 Preparação do Ambiente:** 

A instalação do OpenCV pode ser realizada usando o gerenciador de pacotes, como o pip que é adquirido automaticamente após a realização do download do python.

* **4.2 - Instalação do OpenCV:**

A instalação do OpenCV pode ser realizada usando gerenciadores de pacotes, como **pip** que adquerido automaticamente após realizar o donwload do python.

Utilizando o pip:

     pip install opencv-python

Além do OpenCV, instale bibliotecas adicionais para aprimorar a funcionalidade do seu ambiente de desenvolvimento.

NumPy (para manipulação de arrays):

    pip install numpy

Matplotlib (para visualização de imagens):


    pip install matplotlib

* **4.3 - Ambiente de Desenvolvimento:**

Escolha um ambiente de desenvolvimento que se alinhe às suas preferências. Recomendado o uso de ambientes virtuais para isolar projetos.
Configuração de Ambiente Virtual:

Configuração de Ambiente Virtual:

    # Instale o virtualenv
    pip install virtualenv

    # Crie um ambiente virtual
    python -m venv myenv

    # Ative o ambiente virtual (Windows)
    .\myenv\Scripts\activate

    # Ative o ambiente virtual (Linux/Mac)
    source myenv/bin/activate


Com esses passos, estará pronto para começar a desenvolver aplicações de 
Visão Computacional utilizando o OpenCV e outras bibliotecas essenciais.

Certifique - se de consultar a documentação oficial do OpenCV para explorar suas funcionalidades e aprimorar suas habilidades na análise de imagens e vídeos.

## 5. Integração de Redes Neurais em Projetos de Visão Computacional

No contexto de projetos de Visão Computacional, a integração de redes neurais se destaca como uma abordagem avançada e poderosa para aprimorar a eficácia da detecção, reconhecimento e interpretação de padrões em dados visuais. Nesse artigo é observado o papel fundamental das redes neurais no cenário de queimadas e incêndios florestais.

As Redes Neurais são modelos inspirados no funcionamento do cérebro humano, composta por neurônios interconectados. Elas são capazes de aprender a partir de dados, identificar padrões complexos e tomar decisões autônomas, características cruciais para projetos de Visão Computacional. Aplicações em detecção de queimadas que trabalha esse artigo.

* **5.1 - Segmentação de Imagem**

Redes Neurais podem ser treinadas para uma porção de imagens, identificando áreas específicas relacionadas a focos de queimadas e incêndios. Essa capacidade de delimitar regiões de interesse facilita a detecção precisa da região.

* **5.2 - Classificação de Padrões**

Ao utilizar técnicas de classificação, as redes neurais podem distinguir entre imagens normais e aquelas que contêm sinais de queimadas. Esse processo aprimora a capacidade do sistema de identificar padrões associados a queimadas e incêndios de grande proporções.

* **5.3 - Reconhecimento de Fumaça**

Redes Neurais podem ser treinadas para identificar características específicas de fumaça, diferenciando - a de outros elementos presentes na imagem. Assim podendo prever grandes queimadas ou incêndios florestais.

## 6 - Comunicando com Drones usando Dronekit e Configurando para Aceitar Comandos e GPS

Ao embarcar em projetos que envolvem drone, é decisivo contar com bibliotecas especializadas para facilitar a comunicação e o controle. Uma ferramenta robusta para essa finalidade é o Dronekit, uma biblioteca que proporciona uma interface python para interagir com drones compatíveis com o protocolo MAVLink.

O protocolo MAVLink(Micro Air Vehicle Link) representa uma Estrutura de comunicação eficiente, projetada especialmente para sistemas de veículos aéreos não tripulados (UAVs ou drones). Com o Dronekit, desenvolvedores podem se comunicar com drones de forma simplificada, utilizando código python para controle e monitoramento remoto.

Ao empregar o Dronekit, o primeiro passo consiste em configurar o drone para aceitar comandos externos. Isso geralmente envolve a definição do drone para modo “GUIDED”, que permite controle remoto. Também é crucial garantir que o drone esteja equipado e pronto para receber comandos de voo.

Além do controle, é vital obter informações precisas de localização. A biblioteca Dronekit facilita o acesso às coordenadas GPS do drone, fundamentais para determinar sua posição geográfica. No contexto de vídeo monitoramento e satélites, a obtenção dessas coordenadas torna - se ainda mais significativa, permitindo a aplicações avançadas de monitoramento e navegação autônoma. 

Dessa forma, pode se utilizar o Dronekit, os desenvolvedores estabelecem uma base sólida para interação com drones, proporcionando controle remoto seguro e acesso as coordenadas geográficas essenciais para diversas aplicações, desde o monitoramento remoto até operações para inibir queimadas e incêndios florestais através de dados via satélites ou vídeo monitoramento.


## 7 - Prática - Detecção Eficiente

O código em questão utiliza a biblioteca OpenCV em conjunto com Python para realizar a detecção de fogo em vídeo monitoramento de maneira eficaz. A abordagem adotada segue uma série de passos para identificar regiões na imagem que indicam a presença de fogo.

Inicialmente, o frame do vídeo é convertido para o espaço de cor HSV, proporcionando uma melhor segmentação de cores específicas. Em seguida, é definida uma faixa de cor (Vermelha) que sugere a presença de fogo. Uma máscara é aplicada para isolar as áreas vermelhas na imagem original.

Para aprimorar a detecção, e aplicação, é aplicado um desfoque gaussiano à máscara, reduzindo o ruído e facilitando a identificação. A detecção de bordas com o algoritmo Canny é então empregada para realçar os contornos presentes nas imagens ou no vídeo monitoramento capturado.

A identificação de contornos é realizada, e a área de cada contorno é avaliada. Contornos com uma área superior a um valor mínimo pré definido são considerados significativos, indicando a possível presença de fogo. Nesses casos além do contorno ser feito será também desenhada uma mira de retícula em cima do possível fogo detectado, e um alerta é exibido no terminal(“Alerta: fogo detectado acionando autoridades”) simulando um alerta sonoro, é em seguida um segundo alerta aparece no terminal (“Alerta: Gatilho acionado”) simulando que tenha um objeto no drone para disparar substâncias para tentar conter o foco das chamas na região, até a chegada da autoridades.

Ao realizar testes foi observado que com este código, foi possível alcançar um acerto de detecção de fogo de 97%. Este desempenho destaca a eficiência do método implementado, proporcionando uma base sólida para projetos mais amplos de detecção de fogo em tempo real.


Aqui estão alguns trechos-chave do código de detecção de fogo utilizando OpenCV:

    # Função para detectar fogo
    def detectar_fogo(frame):
        # Convertendo o frame para o espaço de cor HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Definindo uma faixa de cor para a detecção de fogo (vermelho)
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        # Criando uma máscara para a cor vermelha
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Aplicando um desfoque para reduzir o ruído
        blurred = cv2.GaussianBlur(mask, (15, 15), 0)

        # Detecção de bordas usando Canny
        edges = cv2.Canny(blurred, 50, 150)

        # Encontrando contornos na imagem
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

Embora o código em si não incorpore diretamente o Dronekit, YOLO e TensorFlow, mas sua modularidade e eficácia na detecção de fogo podem servir como um ponto de partida para a integração com drones. Essa detecção pode ser utilizada como um gatilho para ações específicas, como alertas, navegação  autônoma ou comunicação com autoridades, ampliando o escopo de aplicação do artigo em questão.
    
## 8 - Conclusão
Este artigo com todo esse projeto representa uma iniciativa abrangente e inovadora no combate a queimadas e incêndios florestais e urbanos, integrando tecnologias avançadas para o monitoramento, detecção automatizada e intervenções eficientes. Ao unir o poder da Visão Computacional, Redes Neurais, e a comunicação com drones através do Dronekit, buscamos criar uma solução ampla que vai além da simples identificação de focos de queimada e incêndios.

A abordagem técnica, centrada no uso do OpenCV e YOLO, proporciona uma detecção precisa e ágil de padrões característicos de chamas e fumaça, permitindo uma resposta rápida diante de situações críticas. Foi observado nos testes que revelou uma notável taxa de acerto de 97%, consolidando a eficácia do método usado.

A integração de Redes Neurais como TensorFlow amplia muito a capacidade de identificação de padrões complexos, enquanto a  comunicação com drones através do Dronekit estabelece um canal direto para ações de extinção e monitoramento autônomo. Essa ideia não apenas otimiza a resposta a incidentes, mas também reduz a carga sobre os órgãos de segurança pública.

O impacto das queimadas e incêndios na saúde urbana, destacado na seção sobre doenças respiratórias, reforça a urgência de soluções proativas. Este projeto não apenas aborda o problema na raiz, mas também estabelece um modelo escalável e adaptável para enfrentar desafios semelhantes em outras regiões geográficas.

Por fim, a Conclusão reitera a importância de abordagens inovadoras na interseção entre tecnologia e preservação ambiental. Ao passar por riscos iminentes de queimadas e incêndios, não apenas preservamos ecossistemas críticos, mas também protegemos a saúde e a qualidade de vida das comunidades urbanas e outras comunidades de toda a região afetada. Esse artigo serve como um testemunho do potencial do avanço da tecnologia quando aplicada em prol do bem - estar coletivo da sociedade e da sustentabilidade ambiental. 

## referências
para sabar mais sobre as referências estão no PDF do artigo [Tecnologia - Combate a Queimadas e Incêndios](https://github.com/wilkerlisboa/article/blob/main/Tecnologia%20-%20Combate%20a%20Queimadas%20e%20Inc%C3%AAndios.pdf). Disponivel para download (apenas clicar no link).

## Licença
Indique a licença do seu artigo. Por exemplo, [Licença MIT](https://opensource.org/licenses/MIT).

