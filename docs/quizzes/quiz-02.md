# Quiz 02 - Instalação e Configuração do Git

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual é o site oficial para realizar o download do Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub é uma plataforma de hospedagem, não o site do software Git.">github.com</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git-scm.com é o portal oficial para downloads e documentação.">git-scm.com</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Bitbucket é um concorrente do GitHub.">bitbucket.org</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. GitLab é outra plataforma de hospedagem de código.">gitlab.com</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual comando define o seu NOME de usuário no Git de forma global?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git config --global user.name 'Seu Nome'">git config --global user.name</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'set' não é um subcomando do Git para configuração.">git set user.name</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A estrutura está incorreta.">git username set</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O namespace correto é 'user.name'.">git identity name</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que a opção `--global` faz nas configurações do Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Para o projeto atual, não se usa flag ou usa-se --local.">Aplica a configuração apenas ao repositório atual</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ela apenas sobrescreve ou cria novos valores.">Limpa todas as configurações antigas do sistema</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! As configurações são salvas no seu perfil de usuário do sistema operacional.">Aplica a configuração a todos os repositórios do seu usuário no computador</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Configurações locais não afetam o servidor remoto diretamente.">Envia seus dados para o GitHub automaticamente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual destas ferramentas de terminal é frequentemente instalada com o Git no Windows?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O PowerShell é nativo do Windows, não parte do instalador do Git.">PowerShell</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Prompt de Comando (CMD) é nativo do Windows.">CMD</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O terminal é uma função do editor VS Code.">Terminal do VS Code</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git Bash simula um ambiente Linux/Unix no Windows.">Git Bash</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Como você visualiza todas as configurações atuais do seu Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git status mostra o estado dos arquivos, não as configs.">git status</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git config --list lista todas as variáveis configuradas.">git config --list</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git log mostra o histórico de commits.">git log</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Esse comando não existe no Git.">git check config</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Por que é importante configurar o e-mail no Git?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O e-mail vincula os commits à sua conta do GitHub e gera as estatísticas.">Para identificar quem é o autor de cada commit realizado</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não envia notificações de e-mail por conta própria.">Para o Git enviar avisos quando você esquecer de commitar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O e-mail é apenas uma metadado, não um login.">Para servir como senha de acesso ao terminal</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O e-mail não interfere na performance do histórico.">Para aumentar a velocidade de upload dos arquivos</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como você configura o seu E-MAIL global no Git?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git config --global user.email 'seu@email.com'">git config --global user.email</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O namespace correto é user.email.">git config --global email.set</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O comando é config.">git setup --email</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'email' sozinho não é um comando Git.">git email --global</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual comando mostra a versão do Git instalada no seu computador?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git status não mostra a versão do software.">git status</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git init inicia um repositório.">git init</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git --version retorna a versão atual do executável.">git --version</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git usa o padrão Unix (--version).">git -v</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. No instalador do Windows, o que significa 'Adjusting your PATH environment'?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Isso permite que o comando 'git' funcione em qualquer terminal.">Permitir que o Git seja executado de qualquer terminal (CMD, PowerShell)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O PATH é sobre localização de executáveis.">Colorir a pasta do Windows Explorer</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não gerencia conexões de rede por padrão.">Aumentar a velocidade da sua internet</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O PATH apenas localiza o comando git.">Instalar o Microsoft Office automaticamente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual editor de texto é o padrão "histórico" do Git, que pode abrir se você não configurar outro?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Bloco de Notas (Notepad) não é o padrão nativo do Git.">Notepad</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Vim/Vi é o editor de terminal padrão em sistemas Unix e no Git.">Vim</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O VS Code deve ser configurado manualmente como padrão.">VS Code</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Sublime é um editor externo.">Sublime Text</div>
  <div class="quiz-feedback"></div>
</div>
