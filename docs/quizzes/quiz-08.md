# Quiz 08 - Pull Requests e Code Review

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual é o pré-requisito técnico obrigatório antes de abrir um Pull Request no GitHub?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A deleção da branch auxiliar geralmente ocorre APÓS o merge do PR.">Deletar a sua branch de trabalho localmente</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O PR precisa que o código esteja no servidor para ser comparado e revisado.">Realizar o 'git push' da sua branch para o servidor remoto do GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A comunicação é feita através da própria interface de PR do GitHub.">Enviar um e-mail formal para o dono do projeto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Se você já fez o merge na main, o PR perde o sentido de revisão.">Fazer o Merge manual da sua branch na 'main' do seu computador</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para que serve a aba "Files changed" (Arquivos alterados) dentro da página de um Pull Request?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Esta aba mostra o 'diff' (diferença) entre o código antigo e o novo código proposto.">Para visualizar exatamente o que foi adicionado, removido ou alterado no código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A mudança de nome é feita via commit ou comandos Git.">Para mudar o nome dos arquivos diretamente no servidor sem fazer commit</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Imagens de perfil ficam na aba 'Conversation'.">Para visualizar a galeria de fotos dos desenvolvedores envolvidos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Para baixar o zip, usa-se o botão 'Code' na página principal.">Para baixar o projeto compactado em formato .ZIP</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que define a prática de "Code Review" em um time de desenvolvimento?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não é um exame, mas um processo de colaboração e qualidade.">Um exame de certificação que o desenvolvedor deve passar mensalmente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ferramentas ajudam, mas o Code Review clássico é feito por humanos.">Um sistema de inteligência artificial que corrige erros ortográficos sozinho</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Code Review garante que o código siga os padrões e não introduza novos bugs.">A revisão do código por um colega para garantir qualidade antes de aceitar as mudanças</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso seria escrita de documentação, não revisão de código.">Escrever apenas o arquivo README informando que terminou a tarefa</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Em um fluxo de trabalho profissional, quem deve idealmente realizar o 'Merge' de um PR?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Automerge é perigoso em projetos grandes sem revisão humana.">O próprio desenvolvedor que escreveu o código, assim que terminar o push</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Os revisores revisam; o autor costuma ser quem realiza o merge após aprovação (ou vice-versa, dependendo da política do time).">Um sistema de bot automático que decide baseado na pressa do projeto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não exige ação global do dono do GitHub.">O proprietário mundial da plataforma GitHub</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O merge deve ocorrer apenas após o código ter recebido aprovações (Approve) de revisores.">Outra pessoa do time (ou o líder técnico) após a aprovação da revisão</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Após o merge ser concluído no GitHub, o que os outros desenvolvedores do time devem fazer?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso seria extremamente ineficiente.">Deletar a pasta local e realizar um novo clone do projeto</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O 'pull' baixa as novidades que acabaram de ser incorporadas na main.">Executar o comando 'git pull origin main' para atualizar seus ambientes locais</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git não sincroniza arquivos locais automaticamente sem comando.">Nada, o software Git sincroniza os arquivos via Wi-Fi automaticamente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Sincronização de código não depende de credenciais de hardware.">Trocar a senha do sistema operacional para liberar as novas atualizações</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual o objetivo principal da aba "Conversation" em um Pull Request?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Lá são discutidas mudanças, sugestões e correções necessárias.">Centralizar a discussão técnica e o feedback sobre as alterações propostas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A aba Code é para arquivos; Conversation é para texto.">Guardar os backups de todos os arquivos modificados</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Ferramentas de chat externas como Slack/Teams são para isso.">Servir como chat informal para marcar reuniões e coffee breaks</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O terminal não tem relação com essa aba.">Reiniciar o terminal do Git local via internet</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que acontece com um Pull Request se você enviar novos commits para o mesmo branch antes do merge?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O PR é atualizado automaticamente com as novas mudanças.">O Pull Request é atualizado automaticamente incluindo as novas modificações</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O PR permanece aberto, mas com o conteúdo atualizado.">O Pull Request é fechado e você precisa abrir um novo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Os commits são integrados dinamicamente ao PR.">Os commits são ignorados pelo GitHub até que o PR antigo seja fechado</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. commits não alteram permissões.">O desenvolvedor perde as permissões de edição no repositório</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a diferença entre um Pull Request e um Merge?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. São conceitos complementares.">São exatamente a mesma coisa, apenas nomes diferentes</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O PR é o processo/pedido; o Merge é o ato técnico de unir os códigos.">O PR é uma solicitação de revisão; o Merge é a execução da união do código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O merge pode acontecer no GitHub também.">O PR acontece no terminal e o Merge acontece apenas no site</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O merge é uma ferramenta de gestão de código, não de acesso.">O PR é gratuito e o Merge é uma funcionalidade paga do GitHub</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Um Pull Request pode ser recusado (Closed)?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Se as mudanças não forem desejadas ou estiverem incorretas, o PR pode ser fechado sem merge.">Sim, se o código não estiver de acordo com as necessidades do projeto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Revisão implica possibilidade de aprovação ou recusa.">Não, uma vez aberto, o dono do projeto é obrigado a aceitá-lo</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. PRs podem ser fechados a qualquer momento pelos administradores.">Sim, mas apenas se o próprio autor do código concordar</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A recusa é uma funcionalidade padrão.">Não, o GitHub não permite deletar pedidos de contribuição</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Para que serve o rascunho de Pull Request (Draft Pull Request)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Drafts não são para membros externos.">Para permitir que hackers testem a segurança do seu código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O código é visível, apenas não pronto para merge.">Para esconder o código de outros membros do time temporariamente</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Útil para mostrar o progresso e pedir opiniões enquanto o trabalho ainda acontece.">Para sinalizar que o trabalho está em andamento e ainda não deve ser mergeado</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A limpeza é feita via git branch -d.">Para deletar automaticamente branches que ficaram velhas</div>
  <div class="quiz-feedback"></div>
</div>
