# Quiz 12 - Documentação com Markdown e README

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual caractere é utilizado para criar títulos (Heading) no padrão Markdown?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O asterisco é usado para listas ou negrito/itálico.">*</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O número de '#' define o nível do título (ex: # Título 1, ## Título 2)."># (Cerquilha/Hashtag)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O traço (-) cria listas com marcadores.">-</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O sinal de maior (>) cria citações/quotes.">></div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a forma correta de aplicar NEGRITO em uma palavra usando Markdown?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Dois asteriscos rodeando o texto aplicam o negrito.">**Texto em negrito**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Um asterisco (*) ou um underline (_) aplicam Itálico.">*Texto em negrito*</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tildes (~~) aplicam o efeito riscado/strikethrough.">~~Texto em negrito~~</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Colchetes são usados em links.">[Texto em negrito]</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal diferença visual na sintaxe de um Link e de uma Imagem no Markdown?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ambos possuem sintaxe parecida, mas não idêntica.">Não há diferença nenhuma, o navegador decide o que é imagem sozinho</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O link é definido pela sua estrutura syntax, não pela cor no editor.">O link é sempre azul no editor e a imagem é verde</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ponto de exclamação indica que o conteúdo deve ser 'injetado' (renderizado) em vez de apenas linkado.">A imagem começa com um ponto de exclamação `!` seguido de colchetes `![]()`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ambas as estruturas usam parênteses para a URL.">A imagem usa chaves `{}` e o link usa colchetes `[]`</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Como você cria um BLOCO DE CÓDIGO de várias linhas com coloração de sintaxe?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Uma crase aplica código 'inline' no meio de uma frase.">Usando uma crase (`) no início e uma no fim do texto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Aspas duplas são para strings em programação.">Usando aspas duplas ("") rodeando o bloco todo</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Você também pode indicar a linguagem após as primeiras crases (ex: ```javascript).">Usando três crases (```) no início e no fim do bloco de código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Recuo de 4 espaços funciona em Markdown básico, mas crases são o padrão GFM.">Colocando 4 espaços no início de cada linha de texto normal</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual desses serviços é amplamente utilizado por desenvolvedores para gerar escudos (badges) automáticos no README?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Google Fonts é para tipografia web.">Google Fonts</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Shields.io permite exibir versão de software, status de build, etc.">Shields.io</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Imgur é apenas um serviço de hospedagem de imagens.">Imgur</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Wikipedia é uma enciclopédia online.">Wikipedia</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que o arquivo "README.md" representa para o seu perfil no GitHub?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É o seu portfólio e a primeira impressão para quem visita seu projeto.">É o seu cartão de visitas, servindo de documentação e guia do projeto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. README é para documentação legível por humanos.">É o arquivo que contém as senhas de acesso ao servidor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É um arquivo essencial para a comunicação do projeto.">É um arquivo de sistema que deve ser mantido em segredo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O código-fonte fica em arquivos de programação específicos.">É onde você deve colar todo o código fonte do programa</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como você cria uma CHECKLIST (lista de tarefas) no Markdown?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Este é o padrão de citação.">Usando o caractere '>' antes de cada linha</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O GitHub renderiza isso como uma caixa clicável visualmente.">Usando '- [ ]' para vazio e '- [x]' para marcado</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Parênteses não criam caixas de seleção.">Usando '( )' no início de cada frase da lista</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso cria uma lista numerada.">Usando '1.', '2.', '3.' seguidos de texto</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a sintaxe correta para criar um LINK EXTERNO (URL)?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O texto visível vai em colchetes e o destino em parênteses.">[Texto Visível](https://link-do-site.com)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Sintaxe invertida."> (https://link-do-site.com)[Texto Visível]</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tags HTML não são recomendadas em Markdown puro."><link src="https://link-do-site.com"></div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Use a sintaxe de colchetes e parênteses.">{Link: https://link-do-site.com}</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Para que serve o arquivo "LICENSE.md" em um repositório?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É sobre direitos de uso, não sobre o código em si.">Para explicar passo a passo como rodar o programa</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Define se o código é MIT, GPL, Apache, etc.">Definir os termos legais de como outras pessoas podem usar seu código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Licenças não têm relação com drivers.">Instalar os drivers de teclado necessários para programar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A segurança é feita por criptografia no GitHub.">Bloquear o acesso de estrangeiros ao seu repositório</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Como se cria uma TABELA básica no Markdown?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O pipe '|' separa colunas e o hífen '-' separa o cabeçalho.">Usando o caractere de barra vertical (pipe '|') e hifens</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Excel não faz parte do motor Markdown.">Importando uma planilha do Excel via botão de upload</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Desenhar com texto não gera tabelas estruturadas.">Desenhando o contorno da tabela com a letra 'X'</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tabs não alinham colunas consistentemente em Markdown.">Apenas teclando 'Tab' várias vezes entre as palavras</div>
  <div class="quiz-feedback"></div>
</div>
