# Quiz 05

<script src="../../assets/js/quiz.js" defer></script>

<style>
@import url("../../assets/css/quiz.css");
</style>

<div class="quiz-container">
  <div class="quiz-item" id="q1">
    <div class="quiz-question">1. Quando ocorre tipicamente um conflito de merge?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> Quando dois arquivos têm nomes diferentes.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">B)</span> Quando a mesma parte do mesmo arquivo foi alterada de formas diferentes em branches diferentes.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Quando a internet cai durante o merge.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Quando o computador está sem memória.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q2">
    <div class="quiz-question">2. Como o Git resolve conflitos na mesma linha automaticamente?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> Ele escolhe a alteração mais recente.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> Ele escolhe a alteração do dono do repositório.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Ele mistura as duas linhas aleatoriamente.
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">D)</span> Ele NÃO resolve automaticamente; ele pausa e pede intervenção humana.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q3">
    <div class="quiz-question">3. O que significam as linhas entre `<<<<<<< HEAD` e `=======`?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> O conteúdo da branch onde você está atualmente (Target).
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> O conteúdo que está vindo da outra branch (Source).
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> O conteúdo original antes de qualquer mudança.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> Um erro de codificação do arquivo.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q4">
    <div class="quiz-question">4. Qual comando usamos para dizer ao Git que o conflito foi resolvido?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">A)</span> `git resolve`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> `git status`
      </div>
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">C)</span> `git add`
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> `git merge --continue`
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
  <div class="quiz-item" id="q5">
    <div class="quiz-question">5. O que devemos fazer com os marcadores de conflito (`<<<<`, `====`, `>>>>`) ao editar o arquivo?</div>
    <div class="quiz-options">
      <div class="quiz-option" data-correct="true" data-feedback="Correto!">
        <span class="option-letter">A)</span> Devemos apagá-los completamente, deixando apenas o código correto.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">B)</span> Devemos mantê-los para histórico.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">C)</span> Devemos transformá-los em comentários.
      </div>
      <div class="quiz-option" data-correct="false" data-feedback="Incorreto.">
        <span class="option-letter">D)</span> O Git apaga sozinho depois do commit.
      </div>
    </div>
    <div class="quiz-feedback"></div>
  </div>
</div>
