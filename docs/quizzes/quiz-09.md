# Quiz 09 - Fluxos de Trabalho (GitHub Flow)

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. No GitHub Flow, a branch `main` deve estar em qual estado permanentemente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A 'main' não deve ser usada para desenvolvimento instável.">Em desenvolvimento constante e instável</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A branch principal deve ser o espelho do que está rodando em produção.">Sempre estável e pronta para deploy (produção)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ela contém o código base estável do projeto.">Vazia, servindo apenas para guardar tags de versão</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ela deve ser legível por todos os colaboradores.">Bloqueada para leitura por usuários comuns</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a principal vantagem do GitHub Flow em relação ao Git Flow tradicional?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O GitHub Flow reduz a burocracia de múltiplas branches de vida longa.">É mais simples, leve e focado em entrega contínua (CD)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Pelo contrário, ele foca na simplicidade.">É muito mais complexo e possui regras rígidas de hierarquia</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É um fluxo de versionamento agnóstico à linguagem.">Só funciona para projetos escritos em Python ou Ruby</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Branches são o coração deste fluxo.">Ele proíbe o uso de Branches auxiliares para o trabalho</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que deve ser feito ANTES de iniciar qualquer mudança de código no GitHub Flow?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Jamais altere a 'main' diretamente em um fluxo profissional.">Comitar as alterações diretamente na branch principal (main)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O PR exige que o código já tenha sido enviado.">Abrir um Pull Request vazio para avisar que vai começar</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O isolamento em branches é fundamental para proteger a estabilidade.">Criar uma nova branch descritiva a partir da main</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Sincronização é necessária, não deleção.">Deletar o repositório local e baixar os arquivos novamente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Quando o código deve ir para o ar (Deploy) no modelo GitHub Flow?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O modelo foca em velocidade e agilidade.">Apenas uma vez por mês após uma reunião de gerência</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Embora a aprovação seja parte do PR, o deploy é técnico.">Apenas após o CEO da empresa aprovar manualmente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Pequenos commits frequentes são melhores que grandes blocos.">Quando a branch de feature atingir exatamente 100 commits</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O merge na 'main' significa que o código passou nos testes e está pronto.">Logo após o merge bem-sucedido do Pull Request na branch main</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que deve ser feito com a branch de feature no servidor após o merge ser concluído?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A 'main' permanece como branch de produção definitiva.">Ela deve ser renomeada para se tornar a nova branch main</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Manter branches antigas polui o projeto e confunde o time.">Ela deve ser deletada para manter o histórico do repositório limpo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não há necessidade de bloqueio permanente.">Ela deve ser bloqueada para qualquer alteração futura sem deletar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O nome original costuma ser mantido no histórico de merge.">Ela deve ser renomeada obrigatoriamente para 'fixed_feature'</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Como garantir que sua nova branch está partindo da versão mais atual da `main`?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sempre dê um pull na main antes de ramificar sua tarefa.">Dando um 'git pull origin main' antes de criar a nova branch</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O status apenas mostra mudanças locais.">Apenas rodando 'git status' para ver se não há erros</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O checkout não atualiza o conteúdo com o servidor.">Mudando para a main com 'git checkout' sem baixar as mudanças</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O GitHub sincroniza via comandos manuais do usuário.">O GitHub faz isso sozinho sem necessidade de comandos no terminal</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual o papel das Discussões (Conversas) em um Pull Request no GitHub Flow?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A conversa foca em feedback técnico e melhorias.">Elas servem para reclamar de outros desenvolvedores</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A discussão é onde ocorre a revisão e o aprendizado em equipe.">São usadas para revisar o código, tirar dúvidas e sugerir melhorias</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não é o local para discutir cronogramas financeiros.">Serve para marcar o horário de almoço do time de design</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Pelo contrário, as discussões aceleram a entrega com qualidade.">Atrasar o projeto propositalmente para revisão burocrática</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. É permitido fazer vários commits em uma mesma branch de feature antes do PR?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Cada commit deve representar um passo lógico da sua tarefa.">Sim, você deve commitar frequentemente conforme avança na tarefa</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Um único commit gigante é difícil de revisar.">Não, cada branch deve ter obrigatoriamente apenas um único commit</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Commits devem ser significativos, independentemente da quantidade.">Apenas se os commits forem feitos em dias diferentes de semana</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Fazer commits é a base do versionamento.">Sim, mas apenas o último commit será visto pelo time no PR</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o estado ideal de um repositório após um ciclo completo de GitHub Flow?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso indica um projeto bagunçado.">Ter 50 branches abertas esperando por revisão</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Commits na main devem vir apenas via PR.">Ter vários commits de mensagem 'teste' na branch main</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A main deve estar atualizada e as branches auxiliares removidas.">Uma branch principal única e estável, com as tarefas integradas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O histórico de commits é a alma do projeto.">Não possuir nenhum histórico de commits anteriores para ser rápido</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Se um Pull Request for rejeitado, o que o desenvolvedor deve fazer?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Erros fazem parte do desenvolvimento.">Trocar de carreira e desistir da programação</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Subir sem correção causará novos problemas.">Abrir um novo PR exatamente igual no dia seguinte</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O feedback do PR serve para evoluir o código.">Ler o feedback, corrigir na mesma branch e enviar novos commits</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Sincronização não resolve erros de lógica ou estilo apontados.">Apenas dar um 'git pull' e tentar dar 'push' novamente</div>
  <div class="quiz-feedback"></div>
</div>
