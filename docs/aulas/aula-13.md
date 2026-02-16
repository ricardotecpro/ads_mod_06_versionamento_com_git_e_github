# Aula 13 – Trabalhando em Equipe

## 🎯 Objetivos de Aprendizagem
- Entender os níveis de permissão no GitHub.
- Adicionar colaboradores ao seu repositório.
- Compreender a diferença entre Colaborador (Time) e Contribuidor (Comunidade).
- Simular um fluxo de trabalho em par.

## 📚 Conteúdo

### 1. Níveis de Permissão
Por padrão, só você (Owner) pode alterar seu repositório. Para trabalhar com amigos ou colegas, você precisa dar permissão.
Vá em **Settings > Collaborators > Add people**.

### 2. Colaborador vs Contribuidor
- **Colaborador**: Tem permissão de escrita ("Write Access"). Pode dar push direto, criar branches no repo oficial e mergir PRs. É alguém "de casa".
- **Contribuidor**: Não tem permissão. Ele faz um Fork, altera no repo dele e manda um Pull Request de lá. É alguém "de fora".

### 3. O Fluxo de Equipe
Quando você tem um time:
1. Todos clonam o **mesmo** repositório.
2. Cada um cria sua branch (`feature-joao`, `feature-maria`).
3. Todos abrem PRs para a `main`.
4. Todos revisam o código de todos.

### 4. Mantendo-se Atualizado
Antes de começar a trabalhar, a Regra de Ouro é:
```bash
git pull origin main
```
Isso evita que você trabalhe em cima de código velho e tenha conflitos depois.

## 📽 Roteiro de Slides
- O Mito do "Lobo Solitário".
- Configurando o Time: Settings > Collaborators.
- Permissões: Read (Ler), Write (Escrever), Admin (Mandar).
- O Perigo: Colaboradores podem deletar branches (e até o repo, se for Admin). Cuidado!
- Fluxo de Fork (Open Source) vs Fluxo de Colaborador (Empresa).
- A importância do `git pull` diário.

## 📝 Quiz
1. Qual menu do GitHub usamos para adicionar pessoas ao projeto?
2. Um "Colaborador" precisa fazer Fork do projeto para contribuir?
3. Qual a diferença principal entre Owner e Colaborador?
4. O que acontece se seu colega der push na `main` e você tentar dar push também sem atualizar antes?
5. Qual comando baixa as atualizações do time para o seu computador?

## Gabarito
1: B ("Settings > Collaborators")
2: B ("Não, ele tem acesso direto")
3: C ("O Owner pode deletar o repositório")
4: A ("O Git rejeita seu push pedindo para fazer pull primeiro")
5: C ("git pull")

## 🛠 Exercícios
1. **Adicionar Amigo (Simulação)**:
   - Vá em Settings > Collaborators.
   - Clique em "Add people".
   - Digite o usuário de um amigo (ou uma conta secundária sua).
   - Ele receberá um convite por email.

2. **O Erro do Push Rejeitado**:
   - Para simular um colega trabalhando: Vá no GitHub e edite o README direto no navegador. Commite lá ("Simula mudança do colega").
   - Volte pro terminal local. Faça uma mudança no README e tente dar Push.
   - **Erro!** `Updates were rejected because the remote contains work that you do not have locally`.
   - Solução: `git pull`. Resolva o conflito (se houver). Dê push de novo.

## 🚀 Projeto da Aula
No seu `portfolio-dev`:
1. Convide um "colaborador fantasma" (pode ser um amigo ou apenas simule o processo).
2. Adicione uma seção no README:
   ```markdown
   ## 🤝 Colaboradores
   Obrigado às seguintes pessoas que contribuíram para este projeto:
   - @seu-usuario
   ```
3. Use o exercício 2 acima para praticar o `git pull` antes de enviar essa mudança.
