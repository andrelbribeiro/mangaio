import streamlit as st
import streamlit.components.v1 as components
from streamlit_sortables import sort_items


def sidebar_historia2():
    # with st.sidebar.expander("História", expanded=False):
    #     st.markdown("### Subtemas")
    #     st.radio("Escolha um subtema", [
    #              "Crise do Primeiro Reinado", "Insatisfação do Nordeste "], key="subtema")

    # Tabs com conteúdos variados
    abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "Caça Palavras", "🧠 Quiz"])

    with abas[0]:
        st.header("Introdução")
        st.write("""
        A Crise do Primeiro Reinado (1822–1831) foi marcada por instabilidade política, econômica e social.
        A Confederação do Equador surge como uma reação ao autoritarismo de D. Pedro I.
        """)
        st.video("https://www.youtube.com/watch?v=_n6mLwFB1ss")
    with abas[1]:
        st.header("Linha do Tempo")
        st.markdown("""
        - **1822**: Independência do Brasil  
        - **1824**: Constituição outorgada  
        - **1824**: Eclosão da Confederação do Equador  
        - **1825**: Repressão e execução de líderes
        """)

    with abas[2]:
        st.header("Personagens Importantes")
        st.write("""
        - **Frei Caneca** – líder intelectual e político.
        - **Dom Pedro I** – Imperador autoritário que centralizou o poder.
        """)

    with abas[3]:

        st.header("Caça-palavras")
        st.write("🎮 Aqui é onde o jogo vai!")
        html_code = """
        <style>
        table {
            border-collapse: collapse;
            margin-bottom: 10px;
            color: white;
        }
        td {
            border: 1px solid white;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
            user-select: none;
        }
        td.selected {
            background-color: yellow;
        }
        td.found {
            background-color: lightgreen;
        }
        p{
            color: white;
        }

        button {
            padding: 10px 20px;
            border-radius: 10px;
            background-color: #4CAF50; /* verde suave */
            color: white;
            border: none;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        button:active {
            background-color: #3e8e41;
            transform: scale(0.98);
        }
        </style>

        <div id="game"></div>
        <button onclick="checkWord()">Verificar</button>
        <p id="status"></p>
        <p><b>Palavras para encontrar:</b> <span id="word-list"></span></p>

        <script>
        const words = ["PYTHON", "STREAMLIT", "JAVASCRIPT", "DATA"];
        let foundWords = [];
        let selectedCells = [];

        const grid = [
            ["S", "T", "R", "E", "A", "M", "L", "I", "T"],
            ["P", "Y", "T", "H", "O", "N", "D", "A", "A"],
            ["J", "A", "V", "A", "S", "C", "R", "T", "P"],
            ["T", "R", "U", "E", "E", "U", "A", "G", "X"],
            ["B", "U", "G", "L", "Z", "D", "Q", "P", "K"]
        ];

        function renderGrid() {
            let html = "<table>";
            for (let i = 0; i < grid.length; i++) {
            html += "<tr>";
            for (let j = 0; j < grid[i].length; j++) {
                html += `<td onclick="selectCell(this, ${i}, ${j})" data-i="${i}" data-j="${j}">${grid[i][j]}</td>`;
            }
            html += "</tr>";
            }
            html += "</table>";
            document.getElementById("game").innerHTML = html;
            document.getElementById("word-list").textContent = words.join(", ");
        }

        function selectCell(cell, i, j) {
            if (cell.classList.contains("found")) return;

            if (cell.classList.contains("selected")) {
            cell.classList.remove("selected");
            selectedCells = selectedCells.filter(c => !(c.i === i && c.j === j));
            } else {
            cell.classList.add("selected");
            selectedCells.push({ i, j, letter: grid[i][j], cell });
            }
        }

        function checkWord() {
            const formedWord = selectedCells.map(c => c.letter).join("");
            const upperWord = formedWord.toUpperCase();
            const status = document.getElementById("status");

            if (words.includes(upperWord) && !foundWords.includes(upperWord)) {
            selectedCells.forEach(c => c.cell.classList.add("found"));
            foundWords.push(upperWord);
            status.textContent = `✅ Palavra encontrada: ${upperWord}`;
            } else {
            status.textContent = `❌ Palavra inválida: ${upperWord}`;
            }

            selectedCells.forEach(c => c.cell.classList.remove("selected"));
            selectedCells = [];
        }

        renderGrid();
        </script>
        """
        components.html(html_code, height=450)

    with abas[4]:
        st.header("Quiz Rápido")
        pergunta = st.radio("O que foi a Confederação do Equador?", [
            "Movimento separatista em São Paulo",
            "Revolta contra o autoritarismo no Nordeste",
            "Conflito entre Portugal e Brasil"
        ])

        if pergunta:
            if pergunta == "Revolta contra o autoritarismo no Nordeste":
                st.success("✅ Resposta correta!")
            else:
                st.error("❌ Resposta incorreta.")


def sidebar_historia_deflagracao_revolta_1824():
    # with st.sidebar.expander("História", expanded=False):
    #     st.markdown("### Subtemas")
    #     st.radio("Escolha um subtema", [
    #              "Crise do Primeiro Reinado", "Insatisfação do Nordeste "], key="subtema")

    # Tabs com conteúdos variados
    abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "Caça Palavras", "🧠 Quiz"])
    
    with abas[0]:
        st.header("Introdução")
        st.write("""
            A Deflagração da Revolta de 1824 marca o início da Confederação do Equador. 
            Em 2 de julho de 1824, Manoel de Carvalho Paes de Andrade, presidente da província de Pernambuco, 
            declarou a separação da província e proclamou a Confederação como forma de resistência ao centralismo 
            do governo imperial. 

            A revolta rapidamente ganhou apoio em outras regiões do Nordeste. Províncias como Ceará, 
            Rio Grande do Norte e Paraíba aderiram ao movimento, evidenciando o descontentamento regional 
            com as decisões do governo de D. Pedro I e a busca por maior autonomia política.
            """)
        st.video("https://www.youtube.com/watch?v=2vfKe0kBJw4")
    
    with abas[1]:
        st.header("Linha do Tempo")
        st.markdown("""
        - **02 de julho de 1824**: Manoel de Carvalho Paes de Andrade declara a separação de Pernambuco e a criação da Confederação do Equador  
        - **Julho de 1824**: Províncias do Ceará, Rio Grande do Norte e Paraíba aderem ao movimento  
        - **Agosto de 1824**: Tropas imperiais são enviadas para reprimir a revolta  
        - **Setembro de 1824**: Ocupação de Recife pelas forças imperiais  
        - **Outubro de 1824**: Prisões e execução de líderes revolucionários
        """)

    with abas[2]:
        st.header("Personagens Importantes")

        personagens = [
            {
                "titulo": "Frei Caneca",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "João Ribeiro Pessoa de Melo Montenegro",
                "idade": "49 anos (em 1824)",
                "carreira": "Religioso, jornalista e professor",
                "influencia": "Um dos principais líderes intelectuais da Confederação do Equador",
                "funcoes": "Articulador político, escritor de manifestos e líder ideológico"
            },
            {
                "titulo": "Manoel de Carvalho Paes de Andrade",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "Manoel de Carvalho Paes de Andrade",
                "idade": "aproximadamente 36 anos (em 1824)",
                "carreira": "Político e jornalista",
                "influencia": "Presidente da província de Pernambuco e líder da proclamação da Confederação",
                "funcoes": "Chefe político da revolta, proclamou a separação"
            },
            {
                "titulo": "Dom Pedro I",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "Pedro de Alcântara Francisco António João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim",
                "idade": "25 anos (em 1824)",
                "carreira": "Imperador do Brasil",
                "influencia": "Figura central do Império e da repressão à revolta",
                "funcoes": "Autoridade máxima do Império, liderou a repressão"
            },
            {
                "titulo": "Francisco de Lima e Silva",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "Francisco de Lima e Silva",
                "idade": "43 anos (em 1824)",
                "carreira": "Militar",
                "influencia": "Liderou a repressão contra os revoltosos",
                "funcoes": "Chefe militar das tropas imperiais enviadas ao Nordeste"
            }
        ]

        for p in personagens:
            st.subheader(p["titulo"])
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(p["imagem"], width=150)

            with col2:
                st.markdown(f"""
                **Nome completo:** {p["nome"]}  
                **Idade em 1824:** {p["idade"]}  
                **Carreira:** {p["carreira"]}  
                **Influência:** {p["influencia"]}  
                **Funções:** {p["funcoes"]}
                """)
            st.markdown("---")


    with abas[3]:
        st.header("Caça-palavras")
        st.write("🎯 Encontre as palavras relacionadas à Revolta de 1824!")
        html_code = """
        <style>
        table {
            border-collapse: collapse;
            margin-bottom: 10px;
            color: white;
        }
        td {
            border: 1px solid white;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
            user-select: none;
        }
        td.selected {
            background-color: yellow;
        }
        td.found {
            background-color: lightgreen;
        }
        p {
            color: white;
        }
        button {
            padding: 10px 20px;
            border-radius: 10px;
            background-color: #4CAF50; /* verde suave */
            color: white;
            border: none;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        button:active {
            background-color: #3e8e41;
            transform: scale(0.98);
        }
        </style>

        <div id="game"></div>
        <button onclick="checkWord()">Verificar</button>
        <p id="status"></p>
        <p><b>Palavras para encontrar:</b> <span id="word-list"></span></p>

        <script>
        const words = ["REVOLTA", "PERNAMBUCO", "CONFEDERACAO", "FREICANECA", "DOMPEDRO", "SEPARACAO"];
        let foundWords = [];
        let selectedCells = [];

        const grid = [
            ["C", "O", "N", "F", "E", "D", "E", "R", "A", "C", "A", "O"],
            ["A", "P", "Q", "S", "T", "L", "V", "A", "I", "T", "S", "S"],
            ["S", "E", "P", "R", "E", "V", "O", "L", "T", "A", "Z", "E"],
            ["E", "R", "I", "O", "P", "A", "Q", "W", "D", "S", "A", "P"],
            ["R", "N", "D", "F", "R", "E", "I", "C", "A", "N", "E", "A"],
            ["Ç", "A", "S", "Q", "S", "T", "B", "E", "W", "T", "V", "R"],
            ["X", "M", "O", "L", "Q", "C", "B", "N", "M", "K", "L", "A"],
            ["A", "B", "A", "S", "N", "M", "L", "P", "Z", "I", "O", "C"],
            ["T", "U", "L", "S", "I", "L", "B", "T", "J", "E", "A", "A"],
            ["M", "C", "S", "A", "E", "A", "E", "C", "L", "G", "S", "O"],
            ["D", "O", "M", "P", "E", "D", "R", "O", "Z", "B", "E", "J"]
        ];

        function renderGrid() {
            let html = "<table>";
            for (let i = 0; i < grid.length; i++) {
                html += "<tr>";
                for (let j = 0; j < grid[i].length; j++) {
                    html += `<td onclick="selectCell(this, ${i}, ${j})" data-i="${i}" data-j="${j}">${grid[i][j]}</td>`;
                }
                html += "</tr>";
            }
            html += "</table>";
            document.getElementById("game").innerHTML = html;
            document.getElementById("word-list").textContent = words.join(", ");
        }

        function selectCell(cell, i, j) {
            if (cell.classList.contains("found")) return;

            if (cell.classList.contains("selected")) {
                cell.classList.remove("selected");
                selectedCells = selectedCells.filter(c => !(c.i === i && c.j === j));
            } else {
                cell.classList.add("selected");
                selectedCells.push({ i, j, letter: grid[i][j], cell });
            }
        }

        function checkWord() {
            const formedWord = selectedCells.map(c => c.letter).join("");
            const upperWord = formedWord.toUpperCase();
            const status = document.getElementById("status");

            if (words.includes(upperWord) && !foundWords.includes(upperWord)) {
                selectedCells.forEach(c => c.cell.classList.add("found"));
                foundWords.push(upperWord);
                status.textContent = `✅ Palavra encontrada: ${upperWord}`;
            } else {
                status.textContent = `❌ Palavra inválida: ${upperWord}`;
            }

            selectedCells.forEach(c => c.cell.classList.remove("selected"));
            selectedCells = [];
        }

        renderGrid();
        </script>
        """
        components.html(html_code, height=590)
    

    with abas[4]:
        st.header("Quiz Rápido: Deflagração da Revolta de 1824")

        perguntas = [
            {
                "pergunta": "Quem declarou a separação da província de Pernambuco em 1824?",
                "alternativas": [
                    "Frei Caneca",
                    "Dom Pedro I",
                    "Manoel de Carvalho Paes de Andrade"
                ],
                "correta": "Manoel de Carvalho Paes de Andrade"
            },
            {
                "pergunta": "Qual era o principal objetivo da Confederação do Equador?",
                "alternativas": [
                    "Separar o Brasil de Portugal",
                    "Lutar contra o autoritarismo imperial",
                    "Fortalecer o poder do imperador"
                ],
                "correta": "Lutar contra o autoritarismo imperial"
            },
            {
                "pergunta": "Qual destas províncias aderiu à revolta de 1824?",
                "alternativas": [
                    "Minas Gerais",
                    "Rio de Janeiro",
                    "Ceará"
                ],
                "correta": "Ceará"
            },
            {
                "pergunta": "Qual foi uma das consequências da Confederação do Equador?",
                "alternativas": [
                    "Criação de uma nova Constituição",
                    "Repressão violenta e execução de líderes",
                    "Independência de Pernambuco"
                ],
                "correta": "Repressão violenta e execução de líderes"
            },
            {
                "pergunta": "Quem foi uma figura importante no movimento, conhecido por sua atuação intelectual e política?",
                "alternativas": [
                    "José Bonifácio",
                    "Frei Caneca",
                    "Pedro II"
                ],
                "correta": "Frei Caneca"
            }
        ]

        for i, p in enumerate(perguntas):
            st.subheader(f"{i+1}. {p['pergunta']}")
            col1, col2, col3 = st.columns(3)

            if f"resposta_deflagracao_revolta{i}" not in st.session_state:
                st.session_state[f"resposta_deflagracao_revolta{i}"] = None

            for j, alternativa in enumerate(p["alternativas"]):
                col = [col1, col2, col3][j % 3]
                if col.button(alternativa, key=f"q{i}_a{j}"):
                    st.session_state[f"resposta_deflagracao_revolta{i}"] = alternativa

            resposta = st.session_state[f"resposta_deflagracao_revolta{i}"]
            if resposta:
                if resposta == p["correta"]:
                    st.success(f"✅ Resposta correta: {resposta}")
                else:
                    st.error(f"❌ Resposta incorreta: {resposta}. Resposta certa: **{p['correta']}**")

def sidebar_historia_repressao_imperial():
    # with st.sidebar.expander("História", expanded=False):
    #     st.markdown("### Subtemas")
    #     st.radio("Escolha um subtema", [
    #              "Crise do Primeiro Reinado", "Insatisfação do Nordeste "], key="subtema")

    # Tabs com conteúdos variados
    abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                   "👤 Personagens", "📅 Ordem Cronológica", "🧠 Quiz"])
    
    with abas[0]:
        st.header("Repressão Imperial")
        st.write("""
            Após a proclamação da Confederação do Equador, o governo imperial respondeu com severidade. 
            Dom Pedro I enviou tropas terrestres e uma esquadra naval comandada pelo almirante Thomas Cochrane 
            com o objetivo de sufocar a revolta nas províncias do Nordeste.

            Os confrontos resultaram na derrota militar dos líderes da Confederação, que foram capturados, 
            julgados e condenados. Muitos deles foram executados como forma de exemplo para impedir futuras rebeliões.

            Entre os condenados, destaca-se Frei Caneca — líder intelectual do movimento — que, após ter sua execução 
            por enforcamento recusada pelo carrasco, foi fuzilado em 1825. Sua morte simboliza a repressão implacável 
            imposta pelo Império àqueles que buscavam maior autonomia regional.
        """)
        st.video("https://www.youtube.com/watch?v=nwvyizAG7PY")
    
    with abas[1]:
        st.header("Linha do Tempo da Repressão Imperial")
        st.markdown("""
        - **Julho de 1824**: Dom Pedro I decide agir contra a Confederação do Equador e autoriza o envio de tropas e navios de guerra  
        - **Agosto de 1824**: O almirante Thomas Cochrane lidera a esquadra imperial em direção ao Nordeste para sufocar a revolta  
        - **Setembro de 1824**: Tropas imperiais invadem e ocupam Recife, capital da província de Pernambuco  
        - **Outubro de 1824**: Rebeldes são presos em diversas províncias; inicia-se a repressão judicial e militar  
        - **Janeiro de 1825**: Início dos julgamentos e condenações públicas dos líderes da Confederação  
        - **13 de janeiro de 1825**: Frei Caneca é executado por fuzilamento, após o carrasco se recusar a enforcá-lo  
        """)
    
    with abas[2]:
        st.header("Personagens Importantes")

        personagens = [
            {
                "titulo": "Frei Caneca",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "João Ribeiro Pessoa de Melo Montenegro",
                "idade": "49 anos (em 1824)",
                "carreira": "Religioso, jornalista e professor",
                "influencia": "Um dos principais líderes intelectuais da Confederação do Equador",
                "funcoes": "Articulador político, escritor de manifestos e líder ideológico"
            },
            {
                "titulo": "Thomas Cochrane",
                "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Lord_Cochrane_by_James_Ramsay.jpg/330px-Lord_Cochrane_by_James_Ramsay.jpg",
                "nome": "Thomas Alexander Cochrane",
                "idade": "Cerca de 49 anos",
                "carreira": "Almirante da Marinha",
                "influencia": "Líder militar da repressão naval",
                "funcoes": "Comandou a esquadra enviada para combater os revolucionários"
            },
            {
                "titulo": "Manoel de Carvalho Paes de Andrade",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "Manoel de Carvalho Paes de Andrade",
                "idade": "aproximadamente 36 anos (em 1824)",
                "carreira": "Político e jornalista",
                "influencia": "Presidente da província de Pernambuco e líder da proclamação da Confederação",
                "funcoes": "Chefe político da revolta, proclamou a separação"
            },
            {
                "titulo": "Dom Pedro I",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "Pedro de Alcântara Francisco António João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim",
                "idade": "25 anos (em 1824)",
                "carreira": "Imperador do Brasil",
                "influencia": "Figura central do Império e da repressão à revolta",
                "funcoes": "Autoridade máxima do Império, liderou a repressão"
            },
            {
                "titulo": "Francisco de Lima e Silva",
                "imagem": "data:image/jpeg;base64,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",
                "nome": "Francisco de Lima e Silva",
                "idade": "43 anos (em 1824)",
                "carreira": "Militar",
                "influencia": "Liderou a repressão contra os revoltosos",
                "funcoes": "Chefe militar das tropas imperiais enviadas ao Nordeste"
            }
        ]

        for p in personagens:
            st.subheader(p["titulo"])
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(p["imagem"], width=150)

            with col2:
                st.markdown(f"""
                **Nome completo:** {p["nome"]}  
                **Idade em 1824:** {p["idade"]}  
                **Carreira:** {p["carreira"]}  
                **Influência:** {p["influencia"]}  
                **Funções:** {p["funcoes"]}
                """)
            st.markdown("---")
    
       
    with abas[3]:
        
        st.header("📅 Ordem Cronológica - Confederação do Equador")
        st.write("🔁 Reorganize os eventos na ordem correta! Arraste os blocos para cima ou para baixo.")

        html_code = """
        <style>
        .container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 20px;
        }

        .item {
            padding: 18px 20px;
            background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
            border: 1px solid #00acc1;
            border-radius: 12px;
            font-weight: 600;
            font-size: 17px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #004d40;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            cursor: grab;
            user-select: none;
            transition: transform 0.2s, box-shadow 0.2s, background 0.3s;
        }

        .item:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            background: linear-gradient(135deg, #b2ebf2, #80deea);
        }

        .item.dragging {
            opacity: 0.5;
        }

        button {
            padding: 10px 20px;
            border-radius: 10px;
            margin: 10px 0;
            background-color: #4CAF50; /* verde suave */
            color: white;
            border: none;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        button:active {
            background-color: #3e8e41;
            transform: scale(0.98);
        }
        </style>

        <div id="eventos" class="container" ondragover="allowDrop(event)">
        <div class="item" draggable="true" ondragstart="drag(event)" id="e1">Tropas imperiais enviadas para reprimir</div>
        <div class="item" draggable="true" ondragstart="drag(event)" id="e2">Prisões e execuções, incluindo Frei Caneca</div>
        <div class="item" draggable="true" ondragstart="drag(event)" id="e3">Separação de Pernambuco e proclamação da Confederação</div>
        <div class="item" draggable="true" ondragstart="drag(event)" id="e4">Adesão do Ceará, RN e Paraíba</div>
        <div class="item" draggable="true" ondragstart="drag(event)" id="e5">Ocupação de Recife pelos imperiais</div>
        </div>

        <button onclick="verificarOrdem()">Verificar Ordem</button>
        <p id="mensagem"></p>

        <script>
        let dragItem = null;

        function drag(ev) {
            dragItem = ev.target;
        }

        function allowDrop(ev) {
            ev.preventDefault();
            const container = document.getElementById("eventos");
            const afterElement = getDragAfterElement(container, ev.clientY);
            if (afterElement == null) {
            container.appendChild(dragItem);
            } else {
            container.insertBefore(dragItem, afterElement);
            }
        }

        function getDragAfterElement(container, y) {
            const draggableElements = [...container.querySelectorAll('.item:not(.dragging)')];

            return draggableElements.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
            }, { offset: Number.NEGATIVE_INFINITY }).element;
        }

        function verificarOrdem() {
            const ordemCerta = ["e3", "e4", "e1", "e5", "e2"];
            const itens = Array.from(document.querySelectorAll(".item"));
            const ordemAtual = itens.map(el => el.id);

            const mensagem = document.getElementById("mensagem");
            if (JSON.stringify(ordemAtual) === JSON.stringify(ordemCerta)) {
                mensagem.innerHTML = "✅ Parabéns! Ordem correta!";
                mensagem.style.color = "white";
                mensagem.style.backgroundColor = "#4CAF50";
                mensagem.style.fontWeight = "bold";
                mensagem.style.padding = "10px";
                mensagem.style.borderRadius = "10px";
                mensagem.style.textAlign = "center";
                mensagem.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.1)";
            } else {
                mensagem.innerHTML = "❌ Ordem incorreta. Tente novamente.";
                mensagem.style.color = "red";
                mensagem.style.backgroundColor = "#ffebee";
                mensagem.style.fontWeight = "bold";
                mensagem.style.padding = "10px";
                mensagem.style.borderRadius = "10px";
                mensagem.style.textAlign = "center";
                mensagem.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.1)";
            }
        }
        </script>
        """

        components.html(html_code, height=650)

    with abas[4]:
        st.markdown("## Quiz Rápido: Repressão Imperial")
        

        perguntas = [
            {
                "pergunta": "Quem foi o comandante da esquadra naval enviada por Dom Pedro I para reprimir a revolta?",
                "alternativas": [
                    "Frei Caneca",
                    "Thomas Cochrane",
                    "José Bonifácio"
                ],
                "correta": "Thomas Cochrane"
            },
            {
                "pergunta": "Qual foi o destino dos líderes da Confederação do Equador após a derrota?",
                "alternativas": [
                    "Foram exilados",
                    "Foram executados",
                    "Foram libertados"
                ],
                "correta": "Foram executados"
            },
            {
                "pergunta": "Quem foi o líder intelectual da Confederação do Equador que foi fuzilado em 1825?",
                "alternativas": [
                    "José Bonifácio",
                    "Manoel de Carvalho Paes de Andrade",
                    "Frei Caneca"
                ],
                "correta": "Frei Caneca"
            },
            {
                "pergunta": "Qual foi uma das principais consequências da repressão à Confederação do Equador?",
                "alternativas": [
                    "Aumento do poder das províncias",
                    "Reafirmação do poder centralizado de Dom Pedro I",
                    "Independência do Brasil"
                ],
                "correta": "Reafirmação do poder centralizado de Dom Pedro I"
            },
            {
                "pergunta": "Como foi a morte de Frei Caneca, líder da revolta?",
                "alternativas": [
                    "Foi enforcado após a recusa do carrasco",
                    "Foi fuzilado após tentativa de enforcamento",
                    "Foi decapitado"
                ],
                "correta": "Foi fuzilado após tentativa de enforcamento"
            }
        ]

        for i, p in enumerate(perguntas):
            st.markdown(f"### {i+1}. {p['pergunta']}")
            col1, col2, col3 = st.columns(3)

            if f"resposta_repressao_imperial{i}" not in st.session_state:
                st.session_state[f"resposta_repressao_imperial{i}"] = None

            for j, alternativa in enumerate(p["alternativas"]):
                col = [col1, col2, col3][j % 3]
                if col.button(f"{alternativa}", key=f"q{i}_a{j}"):
                    st.session_state[f"resposta_repressao_imperial{i}"] = alternativa

            resposta = st.session_state[f"resposta_repressao_imperial{i}"]
            if resposta:
                if resposta == p["correta"]:
                    st.success(f"✅ Boa! Resposta correta: **{resposta}**")
                else:
                    st.error(f"❌ Opa! Resposta errada: **{resposta}**\n\n💡 Resposta certa: **{p['correta']}**")

    
def sidebar_historia_consequencias():
    # with st.sidebar.expander("História", expanded=False):
    #     st.markdown("### Subtemas")
    #     st.radio("Escolha um subtema", [
    #              "Crise do Primeiro Reinado", "Insatisfação do Nordeste "], key="subtema")

    # Tabs com conteúdos variados
        abas = st.tabs(["📖 Introdução", "🕒 Linha do Tempo",
                    "👤 Personagens", "📅 Ordem Cronológica", "🧠 Quiz"])
        
        with abas[0]:
            st.header("Consequências da Confederação do Equador")
            st.write("""
                A Confederação do Equador deixou marcas profundas na história política do Brasil Império. 
                A repressão ao movimento teve consequências significativas, tanto imediatas quanto de longo prazo:

                - **Reafirmação do poder centralizado de Dom Pedro I**: A violenta repressão à revolta mostrou que o imperador não toleraria ameaças à autoridade imperial, reforçando o caráter autoritário do regime.

                - **Fortalecimento da repressão contra movimentos separatistas**: O governo passou a vigiar com mais rigor qualquer sinal de insubordinação nas províncias, atuando com rapidez para conter novas tentativas de autonomia regional.

                - **Legado revolucionário no Nordeste**: Apesar da derrota, a Confederação inspirou futuras revoltas e resistências no século XIX, como a Revolta Praieira, alimentando o desejo por mais liberdade e participação política nas províncias nordestinas.

                O movimento revelou os conflitos entre o projeto centralizador do Império e os anseios de autonomia das elites provinciais, sendo um marco importante nas lutas políticas do período.
            """)
            st.video("https://www.youtube.com/watch?v=hcYZZ6gYjoM")
        
        with abas[1]:
            st.header("Linha do Tempo das Consequências da Confederação do Equador")
            st.markdown("""
                - **1824**: **Reafirmação do poder centralizado de Dom Pedro I**: Após a supressão da revolta, o Imperador consolidou seu poder central, impondo uma maior autoridade sobre as províncias que haviam se rebelado.
                
                - **1824-1825**: **Fortalecimento da repressão imperial contra movimentos separatistas**: Com a derrota da Confederação, o Império intensificou suas ações contra outros movimentos separatistas, estabelecendo uma vigilância mais rigorosa nas províncias do Nordeste.
                
                - **Década de 1830**: **Legado revolucionário no Nordeste**: O movimento da Confederação do Equador deixou um legado importante, com a memória das lutas por maior autonomia no Nordeste, o que inspirou outras revoltas e movimentos de caráter regionalista ao longo do século XIX, como a Revolta dos Malês e outras insurreições contra o domínio imperial.
            """)
        
        with abas[2]:
            st.header("Personagens Importantes")

            personagens = [
                {
                    "titulo": "Frei Caneca",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "João Ribeiro Pessoa de Melo Montenegro",
                    "idade": "49 anos (em 1824)",
                    "carreira": "Religioso, jornalista e professor",
                    "influencia": "Um dos principais líderes intelectuais da Confederação do Equador",
                    "funcoes": "Articulador político, escritor de manifestos e líder ideológico"
                },
                {
                    "titulo": "José Bonifácio",
                    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Jesus%2C_Benedito_Calixto_de_-_Retrato_de_Jos%C3%A9_Bonif%C3%A1cio_de_Andrada_e_Silva.jpg/250px-Jesus%2C_Benedito_Calixto_de_-_Retrato_de_Jos%C3%A9_Bonif%C3%A1cio_de_Andrada_e_Silva.jpg",
                    "nome": "José Bonifácio de Andrada e Silva",
                    "idade": "61 anos (em 1824)",
                    "carreira": "Estadista, naturalista e ministro do Império",
                    "influencia": "Considerado o 'Patriarca da Independência', teve grande influência na organização do Estado brasileiro e apoiou o centralismo imperial",
                    "funcoes": "Conselheiro de Dom Pedro I, atuou na formulação de políticas que fortaleceram o poder central após a revolta"
                },
                {
                    "titulo": "Thomas Cochrane",
                    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Lord_Cochrane_by_James_Ramsay.jpg/330px-Lord_Cochrane_by_James_Ramsay.jpg",
                    "nome": "Thomas Alexander Cochrane",
                    "idade": "Cerca de 49 anos",
                    "carreira": "Almirante da Marinha",
                    "influencia": "Líder militar da repressão naval",
                    "funcoes": "Comandou a esquadra enviada para combater os revolucionários"
                },
                {
                    "titulo": "Manoel de Carvalho Paes de Andrade",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "Manoel de Carvalho Paes de Andrade",
                    "idade": "aproximadamente 36 anos (em 1824)",
                    "carreira": "Político e jornalista",
                    "influencia": "Presidente da província de Pernambuco e líder da proclamação da Confederação",
                    "funcoes": "Chefe político da revolta, proclamou a separação"
                },
                {
                    "titulo": "Dom Pedro I",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "Pedro de Alcântara Francisco António João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim",
                    "idade": "25 anos (em 1824)",
                    "carreira": "Imperador do Brasil",
                    "influencia": "Figura central do Império e da repressão à revolta",
                    "funcoes": "Autoridade máxima do Império, liderou a repressão"
                },
                {
                    "titulo": "Francisco de Lima e Silva",
                    "imagem": "data:image/jpeg;base64,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",
                    "nome": "Francisco de Lima e Silva",
                    "idade": "43 anos (em 1824)",
                    "carreira": "Militar",
                    "influencia": "Liderou a repressão contra os revoltosos",
                    "funcoes": "Chefe militar das tropas imperiais enviadas ao Nordeste"
                }
            ]

            for p in personagens:
                st.subheader(p["titulo"])
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image(p["imagem"], width=150)

                with col2:
                    st.markdown(f"""
                    **Nome completo:** {p["nome"]}  
                    **Idade em 1824:** {p["idade"]}  
                    **Carreira:** {p["carreira"]}  
                    **Influência:** {p["influencia"]}  
                    **Funções:** {p["funcoes"]}
                    """)
                st.markdown("---")
        
        
        with abas[3]:
            st.header("🎯 Associe os Conceitos às Consequências")
            st.write("Arraste cada consequência para o personagem ou ideia correta e clique em **Verificar Respostas**.")

            html_code = """
            <style>
                .drag-container {
                    display: flex;
                    justify-content: space-between;
                    margin-top: 20px;
                    font-family: Arial, sans-serif;
                }

                .drag-list, .drop-list {
                    width: 45%;
                    padding: 10px;
                    background-color: #f9f9f9;
                    border-radius: 10px;
                    border: 1px solid #ddd;
                }

                .drag-item {
                    padding: 10px;
                    margin: 8px 0;
                    background-color: #ffffff;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    cursor: move;
                }

                .drop-zone {
                    min-height: 50px;
                    margin: 10px 0;
                    padding: 12px;
                    border: 2px dashed #aaa;
                    background-color: #e6f7ff;
                    border-radius: 5px;
                }

                #resultado {
                    margin-top: 20px;
                    font-weight: bold;
                }

                button {
                    padding: 10px 20px;
                    margin: 10px 0;
                    border-radius: 10px;
                    background-color: #4CAF50; /* verde suave */
                    color: white;
                    border: none;
                    font-weight: bold;
                    font-size: 14px;
                    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
                    cursor: pointer;
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }
                button:hover {
                    background-color: #45a049;
                    transform: scale(1.05);
                }
                button:active {
                    background-color: #3e8e41;
                    transform: scale(0.98);
                }
            </style>

            <div class="drag-container">
                <div class="drag-list">
                    <h4>Consequências</h4>
                    <div id="item1" class="drag-item" draggable="true" ondragstart="drag(event)">Reafirmação do poder central</div>
                    <div id="item2" class="drag-item" draggable="true" ondragstart="drag(event)">Repressão violenta</div>
                    <div id="item3" class="drag-item" draggable="true" ondragstart="drag(event)">Legado revolucionário no Nordeste</div>
                </div>

                <div class="drop-list">
                    <h4>Associe com:</h4>
                    <div class="drop-zone" id="drop1" ondrop="drop(event)" ondragover="allowDrop(event)">Dom Pedro I</div>
                    <div class="drop-zone" id="drop2" ondrop="drop(event)" ondragover="allowDrop(event)">Líderes da revolta</div>
                    <div class="drop-zone" id="drop3" ondrop="drop(event)" ondragover="allowDrop(event)">Movimentos futuros no século XIX</div>
                </div>
            </div>

            <button onclick="verificarRespostas()">Verificar Respostas</button>

            <div id="resultado"></div>

            <script>
                function allowDrop(ev) {
                    ev.preventDefault();
                }

                function drag(ev) {
                    ev.dataTransfer.setData("text", ev.target.id);
                }

                function drop(ev) {
                    ev.preventDefault();
                    var data = ev.dataTransfer.getData("text");
                    var draggedElement = document.getElementById(data);
                    if (!ev.target.classList.contains("drop-zone")) return;
                    if (ev.target.children.length === 0) {
                        ev.target.appendChild(draggedElement);
                    }
                }

                function verificarRespostas() {
                    const corretas = {
                        "drop1": "item1",  // Dom Pedro I → Reafirmação do poder central
                        "drop2": "item2",  // Líderes da revolta → Repressão violenta
                        "drop3": "item3"   // Movimentos futuros no século XIX → Legado revolucionário no Nordeste
                    };

                    let acertos = 0;
                    for (let dropId in corretas) {
                        const zona = document.getElementById(dropId);
                        const filho = zona.children[0];
                        if (filho && filho.id === corretas[dropId]) {
                            acertos++;
                            zona.style.backgroundColor = "#d4edda";  // verde
                        } else {
                            zona.style.backgroundColor = "#f8d7da";  // vermelho
                        }
                    }

                    let resultado = document.getElementById("resultado");
                    resultado.innerHTML = "Você acertou " + acertos + " de 3!";
                    resultado.style.backgroundColor = "#28a745"; // verde moderno
                    resultado.style.color = "white";
                    resultado.style.fontWeight = "bold";
                    resultado.style.textAlign = "center";
                    resultado.style.padding = "12px";
                    resultado.style.borderRadius = "8px";
                    resultado.style.marginTop = "20px";
                }
            </script>
            """

            st.components.v1.html(html_code, height=700)

        with abas[4]:
            st.markdown("## Quiz Rápido: Consequências da Revolta")

            perguntas = [
                {
                    "pergunta": "Qual foi uma das principais consequências políticas da Confederação do Equador?",
                    "alternativas": [
                        "Adoção do parlamentarismo no Brasil",
                        "Reafirmação do poder centralizado de Dom Pedro I",
                        "Libertação de todos os líderes rebeldes"
                    ],
                    "correta": "Reafirmação do poder centralizado de Dom Pedro I"
                },
                {
                    "pergunta": "Como o governo imperial respondeu aos movimentos separatistas após a revolta?",
                    "alternativas": [
                        "Promoveu o diálogo com as lideranças regionais",
                        "Fortaleceu a repressão contra novas revoltas",
                        "Aprovou uma nova constituição liberal"
                    ],
                    "correta": "Fortaleceu a repressão contra novas revoltas"
                },
                {
                    "pergunta": "Que legado a Confederação do Equador deixou para o Nordeste brasileiro?",
                    "alternativas": [
                        "Um movimento de apoio ao Império",
                        "Um sentimento de resignação política",
                        "Um espírito revolucionário que influenciou futuras revoltas"
                    ],
                    "correta": "Um espírito revolucionário que influenciou futuras revoltas"
                },
                {
                    "pergunta": "O que simbolizou a execução de Frei Caneca?",
                    "alternativas": [
                        "O fim da monarquia brasileira",
                        "A tolerância do Império com a oposição",
                        "A repressão implacável contra a dissidência"
                    ],
                    "correta": "A repressão implacável contra a dissidência"
                },
                {
                    "pergunta": "Após a Confederação do Equador, como ficou o controle do Império sobre as províncias?",
                    "alternativas": [
                        "Mais descentralizado, com maior autonomia regional",
                        "Inalterado, mantendo o mesmo nível de controle",
                        "Mais centralizado e autoritário"
                    ],
                    "correta": "Mais centralizado e autoritário"
                }
            ]

            for i, p in enumerate(perguntas):
                st.markdown(f"### {i+1}. {p['pergunta']}")
                col1, col2, col3 = st.columns(3)

                # Usando chaves únicas no st.session_state para isolar as respostas
                if f"resposta_consequencias_{i}" not in st.session_state:
                    st.session_state[f"resposta_consequencias_{i}"] = None

                for j, alternativa in enumerate(p["alternativas"]):
                    col = [col1, col2, col3][j % 3]
                    if col.button(f"{alternativa}", key=f"q1_{i}_a{j}"):
                        st.session_state[f"resposta_consequencias_{i}"] = alternativa

                resposta = st.session_state[f"resposta_consequencias_{i}"]
                if resposta:
                    if resposta == p["correta"]:
                        st.success(f"✅ Boa! Resposta correta: **{resposta}**")
                    else:
                        st.error(f"❌ Opa! Resposta errada: **{resposta}**\n\n💡 Resposta certa: **{p['correta']}**")
