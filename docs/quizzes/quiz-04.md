# Quiz 04 - Branches e Merges

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual é o nome padrão mais adotado para o branch principal em novos repositórios Git hoje?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'master' era o padrão antigo, agora substituído por questões de nomenclatura.">master</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'developer' costuma ser uma branch de integração, não a principal.">developer</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'main' é o padrão atual no Git e plataformas como GitHub e GitLab.">main</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'trunk' é um termo comum no SVN, não no Git.">trunk</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a principal vantagem de utilizar branches no desenvolvimento de software?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Branches ocupam pouquíssimo espaço adicional.">Para economizar espaço em disco no servidor</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Branches permitem testar ideias isoladamente sem 'quebrar' o código principal estável.">Isolar novas funcionalidades ou correções sem afetar o código principal estável</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não é uma ferramenta de chat/mensageria.">Para enviar mensagens secretas para outros membros do time</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Branches adicionam ao histórico, não o deletam.">Para deletar o histórico de commits antigos permanentemente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual comando cria um novo branch sem automaticamente mudar para ele?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git branch [nome] apenas cria o ponteiro para o commit atual.">git branch nome-da-branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. git switch troca de branch, mas não cria (sozinho).">git switch nome-da-branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. --move é usado para renomear branches existentes.">git branch --move</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. -b cria E muda ao mesmo tempo.">git checkout -b</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual comando é o mais moderno e recomendado para trocar de um branch para outro?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'move' não é usado para navegação entre branches.">git move</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Comando inexistente.">git go to</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Comando inexistente.">git change</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'git switch' foi introduzido para tornar a troca de contextos mais clara.">git switch</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que ocorre tecnicamente durante um `git merge`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O merge preserva os arquivos.">Deleta os arquivos duplicados entre pastas</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git une o histórico e o conteúdo de duas ramificações separadas.">Une as alterações e o histórico de um branch em outro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O diff faz a comparação, o merge faz a união.">Apenas compara dois arquivos diferentes sem alterá-los</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O merge é uma ação de união.">Divide um commit grande em pequenos pedaços</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que é um 'Fast-forward merge'?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Acontece quando a branch de destino não tem novos commits desde a ramificação.">Um merge simples onde o Git apenas move o ponteiro da branch para frente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso seria um merge com conflitos.">Um merge que exige a intervenção manual do desenvolvedor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O merge é sobre conteúdo.">Um merge focado apenas em deletar arquivos inúteis</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O termo indica velocidade e simplicidade.">Um merge que demora muito tempo devido ao tamanho do banco de dados</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual atalho permite CRIAR e MUDAR para um branch em um único comando?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Checkout sozinho apenas muda.">git checkout</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Branch sozinho apenas cria.">git branch</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O comando git switch com a flag -c (create) faz o trabalho completo.">git switch -c nome-da-branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Comando inválido.">git branch --create-and-switch</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Como você deleta um branch que não é mais necessário?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git branch -d [nome] remove a branch local.">git branch -d nome-da-branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'remove' não é o subcomando correto.">git remove branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git usa 'branch -d' para limpeza.">git branch --clean</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Delete não é o primeiro termo.">git delete branch-name</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O que caracteriza o branch `HEAD` no Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O HEAD não é fixo em um branch específico.">É o nome obrigatório do branch principal</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O HEAD é o ponteiro 'você está aqui' para o commit ou branch atual.">Um ponteiro que indica em qual branch/commit você está no momento</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O HEAD é local.">O branch que está armazenado no servidor remoto do GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele é apenas um ponteiro dinâmico.">Um arquivo que contém todas as senhas do projeto</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual comando lista todas as branches existentes no seu repositório local?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! git branch sem argumentos lista as ramificações locais.">git branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Logs mostram commits, não branches.">git log --branches</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Status mostra arquivos.">git status --list</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Show foca em um objeto específico.">git show branches</div>
  <div class="quiz-feedback"></div>
</div>
