 <h2>Sumário</h2>
    <ol>
        <li><a href="#introdução">Introdução</a></li>
        <li><a href="#objetivo">Objetivo</a></li>
        <li><a href="#requisitos">Requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#estrutura-do-projeto">Estrutura do Projeto</a></li>
        <li><a href="#funcionalidades">Funcionalidades</a></li>
        <li><a href="#uso">Uso</a></li>
        <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
        <li><a href="#considerações-finais">Considerações Finais</a></li>
    </ol>


<hr> 

<h2>1. Introdução</h2>
<p>Este projeto é um dashboard interativo desenvolvido em Python usando Streamlit. Ele permite que os usuários selecionem ações de empresas listadas na bolsa e calculem o retorno do portfólio selecionado ao longo do tempo. O dashboard pode ser acessado em: <a href="https://stockdashboard-ibov.streamlit.app/">Stock Dashboard</a>.</p>

<h2>2. Objetivo</h2>
    <p>Fornecer uma ferramenta intuitiva para investidores acompanharem o desempenho de um portfólio personalizado, visualizando os preços históricos ajustados das ações e calculando o retorno do portfólio.</p>

    

    
<h2>3. Requisitos</h2>
    <ul>
        <li>Python 3.8 ou superior</li>
        <li>Streamlit</li>
        <li>pandas</li>
        <li>numpy</li>
        <li>yfinance</li>
        <li>plotly</li>
        <li>streamlit-extras</li>
    </ul>
     <h2>4. Instalação</h2>
    <ol>
        <li>Clone o repositório:<br><code>git clone https://github.com/CaioRibeiro551/Stock_Dashboard/tree/main<br>cd nome-do-repositorio</code></li>
        <li>Instale as dependências:<br><code>pip install -r requirements.txt</code></li>
        <li>Execute a aplicação:<br><code>streamlit run app.py</code></li>
    </ol>
    <h2>5. Estrutura do Projeto</h2>
    <pre>
nome-do-repositorio/
│
├── images/
│   └── logo-250-100-transparente.png
├── tickers_ibra.csv
├── app.py
├── requirements.txt
└── README.md
    </pre>
    <h2>6. Funcionalidades</h2>
    <ul>
        <li><strong>Seleção de Empresas:</strong> Seleção de várias empresas listadas na bolsa.</li>
        <li><strong>Intervalo de Datas:</strong> Definição do intervalo de datas para análise.</li>
        <li><strong>Visualização de Dados:</strong> Exibição de dados de preços ajustados das ações.</li>
        <li><strong>Cálculo de Portfólio:</strong> Cálculo do retorno do portfólio com base na seleção das ações.</li>
        <li><strong>Gráficos Interativos:</strong> Visualização dos dados através de gráficos interativos.</li>
    </ul>
    <h2>7. Uso</h2>
    <ol>
        <li><strong>Inicie a aplicação:</strong><br><code>streamlit run app.py</code></li>
        <li><strong>Interaja com a barra lateral:</strong>
            <ul>
                <li>Selecione as empresas de interesse.</li>
                <li>Defina o intervalo de datas para a análise.</li>
            </ul>
        </li>
        <li><strong>Visualize os dados:</strong>
            <ul>
                <li>O dashboard exibirá os preços ajustados das ações selecionadas.</li>
                <li>O retorno do portfólio será calculado e exibido na interface principal.</li>
            </ul>
        </li>
    </ol>
 <h2>8. Tecnologias Utilizadas</h2>
    <ul>
        <li>Python</li>
        <li>Streamlit</li>
        <li>pandas</li>
        <li>numpy</li>
        <li>yfinance</li>
        <li>plotly</li>
        <li>streamlit-extras</li>
    </ul>
    <h2>Imagens do projeto</h2>
    ![image](https://github.com/CaioRibeiro551/Stock_Dashboard/assets/65637121/84a30f22-d6a2-4e4e-9ff7-9efe667d4536)
    <h2>9. Considerações Finais</h2>
    <p>Este projeto fornece uma base sólida para criar dashboards financeiros interativos. Sinta-se à vontade para contribuir e expandir este projeto conforme suas necessidades.</p>

   
