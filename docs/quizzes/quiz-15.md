# Quiz 15

<link rel="stylesheet" href="../../assets/css/quiz.css">
<script src="../../assets/js/quiz.js" defer></script>

<div class="quiz-container">
  <div class="quiz-item" id="q1">
    <div class="quiz-question">1. O que o comando `git restore arquivo.txt` faz (em versões modernas do Git)?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> Restaura o arquivo do último backup do Windows.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">B)</span> Descarta as mudanças feitas no arquivo no Working Directory, revertendo para o estado do último commit.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Apaga o arquivo para sempre.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Envia o arquivo para a lixeira.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q2">
    <div class="quiz-question">2. Qual a diferença entre `git reset --soft` e `git reset --hard`?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> O Soft apaga tudo; o Hard mantém.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">B)</span> O Soft mantém suas mudanças na área de Stage; o Hard apaga todas as mudanças e reverte os arquivos.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Não há diferença.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> O Hard é mais rápido.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q3">
    <div class="quiz-question">3. Para que serve o `git stash`?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> Para guardar mudanças temporariamente ("na gaveta") sem commitar, permitindo trocar de branch com segurança.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> Para deletar branches.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Para ver o histórico.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Para criar tags.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q4">
    <div class="quiz-question">4. Se eu fiz um commit numa branch, mudei para outra e perdi o commit (Detached HEAD), onde posso encontrar o hash dele para recuperar?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> No `git status`.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> No `git log` da main.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">C)</span> No `git reflog`.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Google.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q5">
    <div class="quiz-question">5. O que fazer se o Git disser `error: Your local changes to the following files would be overwritten by checkout`?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> Chorar.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">B)</span> Commitar suas mudanças ou usar `git stash` antes de trocar de branch.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Forçar a troca e perder tudo.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Desinstalar o Git.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
</div>
