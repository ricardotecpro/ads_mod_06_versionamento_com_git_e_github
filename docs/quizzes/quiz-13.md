# Quiz 13 - Trabalho em Equipe e Colaboração

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual menu do GitHub utilizamos para adicionar colaboradores a um repositório privado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A aba principal de código não gerencia permissões.">Aba 'Code' e botão 'Add file'</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Em 'Settings > Collaborators' você convida pessoas pelo nome de usuário ou e-mail.">Settings > Collaborators</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Pull Requests' é para revisar código, não gerenciar membros.">Pull Requests > Invite Members</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Insights' mostra estatísticas de uso.">Insights > Team management</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Um colaborador com acesso de escrita (Write) precisa fazer Fork do projeto para contribuir?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Fork é para quem não tem permissão de escrita no repositório original.">Sim, o Fork é obrigatório para qualquer contribuição no GitHub</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele pode criar branches e dar push direto no repositório oficial do time.">Não, ele pode criar branches e dar push direto no repositório oficial</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Permissão de escrita independe da visibilidade ser pública.">Apenas se o projeto for público (Public)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. A plataforma Git é agnóstica ao sistema operacional.">Apenas se ele estiver usando o sistema operacional Windows</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal diferença de poder entre o dono (Owner) e um Colaborador comum?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Existem níveis hierárquicos bem definidos.">Nenhuma, ambos possuem as mesmas permissões em 100% das vezes</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Colaboradores podem ler e escrever no código conforme a permissão.">O Colaborador não pode ver o código fonte, apenas o dono vê</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Owner gerencia o repositório como um todo, incluindo sua existência física.">O Owner pode deletar o repositório e gerenciar configurações críticas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Owner é quem costuma fazer mais commits no início.">O Owner é proibido de fazer commits, servindo apenas como gerente</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que acontece se seu colega der 'push' na branch `main` e você tentar subir seu código sem sincronizar?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Git detecta que seu histórico está atrasado (non-fast-forward) e bloqueia o push por segurança.">O Git rejeita seu push e solicita que você faça um 'pull' primeiro</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O Git protege o trabalho de todos os colaboradores.">O seu código substitui e apaga o que seu colega acabou de fazer</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O computador não sofre danos por problemas de sincronização.">O seu computador trava até que o outro desenvolvedor desconecte</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O versionamento é feito no mesmo repositório original.">O GitHub cria automaticamente um clone do projeto para você</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual comando é responsável por baixar as novidades do time para o seu computador?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'download' não é um comando oficial do Git.">git download --updates</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'sync' é uma função de interfaces visuais, não do terminal puro.">git sync --force</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O pull sincroniza seu estado local com o estado do servidor.">git pull origin main</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Push faz o caminho inverso: do seu PC para a nuvem.">git push --receive</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que é uma 'Organization' (Organização) no GitHub?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Organizações permitem gerenciar times, repositórios e faturamento de forma profissional.">Um espaço para empresas ou grandes projetos gerenciarem múltiplos membros e times</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É uma estrutura gratuita para projetos básicos.">Um plano pago obrigatório para quem tem mais de 2 arquivos</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Organizações são estruturas de conta.">Um robô que escreve o código sozinho para o desenvolvedor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Organizações são sobre colaboração humana.">O nome técnico para o software Git quando instalado em rede</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Para que serve o recurso de 'Mention' (@username) em um comentário?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Serve para comunicação, não segurança.">Para bloquear aquele usuário de comentar no seu projeto</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A pessoa recebe um e-mail ou notificação visual no site.">Para disparar uma notificação específica para aquela pessoa</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Star' é para favoritos.">Para dar uma estrela de presente para o desenvolvedor</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O código-fonte é separado dos comentários.">Para esconder o comentário da visualização pública</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual a melhor prática para evitar conflitos de merge em um time grande?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sincronização constante (pull) e commits pequenos reduzem as chances de colisão.">Fazer 'git pull' frequentemente e manter comunicação clara com o time</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Isso impossibilita o trabalho em equipe.">Proibir os outros colegas de mexerem no código durante o dia</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. O versionamento local é importante.">Committar apenas uma vez por mês para não poluir o histórico</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Falta de internet impede o trabalho em equipe no GitHub.">Desligar a internet para que ninguém veja o que você está fazendo</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. No GitHub, o que significa o nível de permissão 'Admin' para um colaborador?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Admin' é o nível mais alto de colaboração.">Ele pode apenas ler as mensagens e não pode ver o código</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. 'Admin' pode deletar issues e gerenciar membros.">Ele tem as mesmas permissões que um visitante comum do site</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Administradores podem gerenciar todas as configurações do repositório.">Poder total de gerenciamento, incluindo adicionar outros membros</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Admin é uma função de controle, não de remoção automática de código.">Ele serve para deletar o código de todo mundo que errar o commit</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual a vantagem de usar 'Teams' (Equipes) dentro de uma Organização?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Você pode adicionar permissão para 50 pessoas de uma vez apenas citando o Time.">Facilitar a gestão de permissões em massa para grupos de pessoas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. GitHub Teams é independente do Microsoft Teams, embora possam ser integrados.">É a única forma de fazer chamadas de vídeo pelo GitHub</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. É sobre gestão de acesso.">Diminuir o tamanho total do código fonte do projeto</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Não há gamificação desse tipo no GitHub.">Ganhar pontos extras para trocar por descontos em hardware</div>
  <div class="quiz-feedback"></div>
</div>
