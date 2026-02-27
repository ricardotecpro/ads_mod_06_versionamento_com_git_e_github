# Quiz 07 - Sincronização e Comandos Remotos

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual comando envia seus commits locais para o servidor remoto do GitHub?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git pull traz alterações do servidor para o seu PC.">git pull</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git commit salva localmente, mas não envia para a nuvem.">git commit</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git push 'empurra' suas versões locais para o servidor.">git push</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'upload' não é um comando Git; use 'push'.">git upload</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. No comando `git push origin main`, o que representa o termo "origin"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A pasta local não tem nome obrigatório.">O nome da sua pasta de projeto no computador</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Origin é o apelido do endereço (URL) do repositório no GitHub.">O apelido padrão para o link do repositório remoto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O nome de usuário é parte da URL, mas não é o origin.">O seu nome de usuário no GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É um termo específico do Git, não do Windows/Linux.">Uma configuração de rede do sistema operacional</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual comando cria uma cópia local completa de um repositório existente no GitHub?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git clone baixa o histórico e os arquivos do projeto.">git clone `[URL]`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não possui o comando copy.">git copy</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Use o termo técnico 'clone' no Git.">git download</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git init cria um repo novo vazio localmente.">git init --remote</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Para que serve o arquivo especial `.gitignore`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Senhas nunca devem estar no Git, nem no gitignore.">Para armazenar senhas e chaves de segurança</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele faz exatamente o oposto: ignora arquivos.">Para forçar o Git a subir todos os arquivos, mesmo os grandes</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O histórico de commits é gerenciado pelos comandos de commit.">Para apagar o histórico de commits antigos do projeto</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O .gitignore evita que arquivos inúteis (como pastas de sistema ou compilados) subam.">Listar arquivos e pastas que o Git NUNCA deve rastrear ou enviar</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Como baixar as ATUALIZAÇÕES de um repositório que você já clonou anteriormente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Clonar de novo criaria uma cópia duplicada e ineficiente.">Executando o comando git clone novamente em outra pasta</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git pull sincroniza seu PC com as novidades do servidor.">Utilizando o comando git pull</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Sincronização não requer deleção de arquivos.">Deletando a pasta local e baixando tudo do zero</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Init não atualiza arquivos existentes.">Usando git init para reiniciar a conexão</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O Git funciona sem internet?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git é local; a internet só é necessária para interagir com o GitHub.">Sim, você pode commitar e criar branches normalmente offline</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Essa é a principal vantagem do Git ser distribuído.">Não, ele exige conexão constante para registrar qualquer mudança</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A visualização offline é completa através dos arquivos locais.">Sim, mas você não consegue ver o histórico de commits anteriores</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git é estável em qualquer situação.">Não, o banco de dados do Git corrompe se faltar internet</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que o comando `git fetch` faz de diferente em relação ao `git pull`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O fetch é apenas o primeiro passo do pull.">O fetch envia código para o GitHub e o pull baixa</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O fetch apenas 'escuta' as novidades sem alterar seus arquivos locais.">O fetch apenas baixa as metadados/novidades sem unir ao seu código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O pull é uma ação local.">O fetch é para membros seniores e o pull para estagiários</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Fetch não é sobre o arquivo .gitignore.">O fetch limpa o arquivo .gitignore automaticamente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a forma correta de conectar um repositório local existente a um novo repositório no GitHub?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O remote add cria a ponte 'origin' entre local e remoto.">git remote add origin [URL]</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Links não conectam repositórios no Git.">git link origin [URL]</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Init apenas cria a base, não conecta ao remoto.">git init [URL]</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Push falhará se o remote não for configurado antes.">Basta dar git push sem configurar nada antes</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual protocolo é mais comum e seguro para interagir com o GitHub via terminal atualmente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O FTP é para transferência de arquivos genéricos, não Git.">FTP</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Tanto HTTPS (com Token) quanto SSH são os padrões recomendados.">HTTPS ou SSH</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Bluetooth não é usado para versionamento de código.">Bluetooth</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. POP3 é para e-mails.">POP3</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Se você tentar dar `git push` e o servidor remoto tiver commits que você não tem localmente, o que acontece?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O push falhará por segurança.">O Git apaga os commits do servidor para aceitar os seus</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O erro se chama 'Rejected' e exige que você faça um 'pull' primeiro.">O Git rejeita o envio e solicita que você faça um pull primeiro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não possui essa automação devido a riscos de conflito.">O Git une tudo sozinho em um novo repositório oculto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub é muito estável.">O site do GitHub fica fora do ar temporariamente</div>
  <div class="quiz-feedback"></div>
</div>
