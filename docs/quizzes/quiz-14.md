# Quiz 14 - Hospedagem com GitHub Pages

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O GitHub Pages é um serviço gratuito para hospedar sites?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É uma das formas mais populares de hospedar portfólios e documentação gratuitamente.">Sim, especialmente para repositórios públicos na plataforma</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É um serviço gratuito oferecido pelo GitHub.">Não, ele exige uma assinatura mensal de 20 dólares</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O acesso é ilimitado conforme o uso justo da plataforma.">Apenas nos primeiros 30 dias de uso do repositório</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Qualquer usuário com conta no GitHub pode usar.">Apenas para quem for estudante da área de TI</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Posso hospedar um site que use linguagem PHP e banco de dados MySQL no GitHub Pages?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub Pages não possui processamento de servidor (backend).">Sim, ele suporta qualquer linguagem de programação moderna</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele aceita apenas arquivos estáticos (HTML, CSS e JavaScript).">Não, ele suporta apenas conteúdo estático (Front-end)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O tamanho do banco não altera o suporte técnico.">Apenas se o banco de dados for menor que 50MB</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É uma limitação técnica da infraestrutura, não do plano comercial.">Apenas se você adquirir o plano Enterprise da empresa</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual é o nome do arquivo obrigatório que o GitHub procura na raiz para carregar como página inicial?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'home.html' é comum, mas o padrão web é 'index'.">home.html</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. PHP não é executado no GitHub Pages.">idex.php</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'index.html' é o ponto de entrada padrão de servidores web.">index.html</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'startup.js' é um script, não um documento HTML.">startup.js</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Onde, dentro do repositório, habilitamos e configuramos o link oficial do site hospedado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A aba 'Code' mostra apenas os arquivos.">Na aba principal de 'Code'</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Issues' serve para gestão de tarefas.">Dentro do menu de gerenciamento de 'Issues'</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Security' é para análise de vulnerabilidades.">Na aba de 'Security' e proteção de código</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Lá você escolhe a branch de origem (ex: main).">Settings > Pages</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Quanto tempo, em média, leva para o site ir ao ar após você realizar o primeiro 'push'?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O processo é muito mais rápido que isso.">Exatamente 24 horas para propagação de DNS</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O GitHub dispara uma 'Action' de build automática que é bem veloz.">Alguns segundos ou poucos minutos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A revisão é feita por algoritmos automatizados em tempo real.">Uma semana completa para revisão humana do código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Existe um pequeno tempo de processamento do servidor.">É instantâneo (menos de 0.1 segundo)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o formato padrão da URL gerada pelo GitHub Pages para usuários comuns?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Exemplo: ricardo.github.io/meu-projeto.">usuario.github.io/nome-do-repositorio</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Este é o link de visualização de código.">github.com/usuario/nome-do-repositorio</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O domínio principal é .io.">www.meu-projeto.com.br</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O link do site não possui o termo 'code'.">link.code.github/usuario</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Para que serve o Jekyll dentro do ecossistema do GitHub Pages?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Jekyll gera sites estáticos.">É um banco de dados para sites em tempo real</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele transforma arquivos Markdown simples em um site HTML completo com temas.">É um gerador de sites estáticos integrado ao GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não tem relação com criptografia de senhas.">Um software para criptografar as senhas do usuário</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Jekyll é o nome do gerador do GitHub.">O nome do servidor físico onde o GitHub está instalado</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. É possível usar um DOMÍNIO CUSTOMIZADO (ex: www.meusite.com) no GitHub Pages?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O GitHub permite configurar o CNAME para apontar para o seu próprio domínio.">Sim, você pode configurar o seu próprio domínio comprado externamente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub é flexível quanto a isso.">Não, o GitHub proíbe o uso de endereços que não tenham 'github.io'</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É permitida qualquer extensão válida.">Apenas se o domínio terminar em .com ou .org</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Essa é uma função básica da plataforma.">Pode, mas você precisa pagar uma taxa extra para o GitHub mensalmente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual a principal vantagem de usar o GitHub Pages em comparação com o 'gh-pages' via terminal?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ambos são rápidos.">O GitHub Pages via site é 100x mais rápido</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A configuração via site é visual.">Não é necessário possuir uma conta no GitHub para usar o site</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A interface visual (GUI) facilita para quem não quer lidar com scripts de deploy complexos.">Oferece uma interface visual simples para escolher a branch e o link</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ambos são recursos para o mesmo fim.">O site garante que o Google te achará mais rápido</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Se você deletar o repositório, o site do GitHub Pages continuará no ar?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A vida do site está vinculada à vida do repositório.">Sim, o GitHub mantém um backup eterno do site no servidor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não existem sites sem código-fonte por trás.">Sim, mas as imagens e cores desaparecerão sozinhas</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O site é servido diretamente dos arquivos do repositório; sem arquivos, sem site.">Não, o site é removido permanentemente junto com o repositório</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O site sairá do ar imediatamente após a confirmação da deleção.">Sim, ele ficará no ar por mais 30 dias de carência</div>
  <div class="quiz-feedback"></div>
</div>
