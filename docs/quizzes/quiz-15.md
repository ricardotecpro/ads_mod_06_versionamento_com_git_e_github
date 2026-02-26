# Quiz 15 - Resolvendo Problemas e Desfazendo Erros

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que significa estar no estado "Detached HEAD" (Cabeça Desprendida) no Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O login e a conta não são afetados pelo estado do repositório.">Que você perdeu sua conta do GitHub e não pode mais logar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É um estado local do Git, não um problema de rede.">Que o servidor do GitHub caiu e seu computador perdeu a conexão</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Você está olhando para um commit específico do passado, em vez de estar na ponta de uma branch ativa.">Que você não está em nenhuma branch, mas visitando um commit específico</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O software Git continua funcionando normalmente para recuperação.">Que o software Git foi corrompido e precisa ser desinstalado</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual comando desfaz o último commit, mas MANTÉM seus arquivos modificados prontos para commitar novamente?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O '--soft' move o ponteiro de volta mas preserva o que está na Staging Area.">git reset --soft HEAD~1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O '--hard' apaga permanentemente as mudanças não commitadas.">git reset --hard HEAD~1</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'delete' não é um subcomando de histórico do Git.">git delete last-commit</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git usa o termo 'revert' ou 'reset', não 'undo'.">git undo</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Se o `git push` for rejeitado por um erro "non-fast-forward", qual deve ser sua primeira ação?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Deletar a pasta .git destrói todo o seu versionamento local.">Deletar a pasta escondida .git e começar tudo do zero</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Você precisa baixar o que o servidor tem para depois subir as suas novidades.">Executar um 'git pull' para sincronizar seu PC com o servidor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Reiniciar não altera o histórico de commits do Git.">Reiniciar o computador para limpar o cache do terminal</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não há necessidade de novo repositório, apenas de sincronização.">Criar um repositório novo no GitHub e mudar de projeto</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O comando `git reset --hard` é considerado perigoso por qual motivo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele é extremamente rápido.">Porque ele deixa o computador muito lento por várias horas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele afeta os arquivos que você está editando e não foram salvos no Git.">Porque ele envia todas as suas senhas para o GitHub em modo público</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ele limpa o estado de trabalho dos arquivos locais.">Porque ele formata o HD do computador se você errar a senha</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Use apenas quando tiver certeza absoluta de que quer descartar o trabalho atual.">Porque ele apaga permanentemente mudanças que ainda não foram commitadas</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual comando "mágico" mostra um diário completo de todos os movimentos que você fez (resets, switches, commits)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'git log' mostra apenas os commits da branch atual.">git log --all-history</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'history' não é um comando padrão do CLI.">git history --detailed</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Reflog é a rede de segurança final do Git; se o commit existiu no seu PC, ele estará lá.">git reflog</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O status mostra apenas o estado presente dos arquivos.">git status --verbose</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que o comando `git revert` faz de diferente em relação ao `git reset`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O 'revert' é seguro para o histórico compartilhado porque ele não apaga o passado, ele adiciona uma correção.">Ele cria um NOVO commit que desfaz exatamente o que o commit anterior fez</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ambos são comandos do Git.">O 'revert' só funciona em projetos privados e o 'reset' em públicos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Revert é técnico, não apenas visual.">O 'revert' serve apenas para mudar a cor do terminal para verde</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Revert não apaga histórico.">O 'revert' apaga permanentemente todos os registros do servidor</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como você pode ver a diferença entre o que você editou e o último commit salvo ANTES de dar 'git add'?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'status' diz QUAIS arquivos mudaram, mas não o CONTEÚDO.">git status --detailed</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O 'git diff' mostra linha por linha o que foi adicionado (+) e removido (-).">git diff</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'check' não é comando de visualização de mudanças.">git check content</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Use o diff para isso.">git view differences</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a função do comando `git stash`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Útil quando você precisa mudar de branch no meio de um trabalho que ainda não está pronto para commit.">Guardar temporariamente suas mudanças não terminadas em uma área escondida</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Stash é temporário por natureza.">Deletar para sempre os arquivos do projeto para começar do zero</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Stash não é para desinstalação.">Desinstalar o Git do computador sem deixar rastros</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Stash é sobre arquivos modificados, não ocultos por atributo de sistema.">Tornar o repositório invisível para outros usuários do GitHub</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Recebi um erro de "Merge Conflict". Isso significa que perdi meu código?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Conflitos são naturais no trabalho em equipe.">Sim, o Git apaga os dois arquivos para evitar confusão</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não requer reformatação.">Sim, você precisa formatar o computador e clonar tudo de novo</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git apenas pede que você escolha qual versão daquela linha de código deve permanecer.">Não, é apenas um aviso que duas pessoas mexeram na mesma linha e você deve escolher uma.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A resolução exige intervenção humana.">Sim, mas o GitHub consegue resolver sozinho via Wi-Fi</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que faz o comando `git checkout .` (ponto)?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele descarta todas as mudanças atuais não salvas no arquivo para voltar ao estado do último commit.">Descarta todas as alterações locais não commitadas no diretório atual</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Checkout . é para descartar mudanças.">Publica o código diretamente no site oficial do produto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O ponto simboliza o diretório atual.">Muda para a branch chamada 'ponto'</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O checkout apenas altera arquivos, não envia e-mails.">Envia um e-mail para todos os colaboradores avisando que você terminou</div>
  <div class="quiz-feedback"></div>
</div>
