# Aula 04 – Branches e merges

## 🎯 Objetivos de Aprendizagem
- Entender o conceito de Branches (Ramificações).
- Criar e navegar entre branches (`git branch`, `git switch`).
- Realizar a fusão de alterações (`git merge`).
- Compreender a segurança de trabalhar em branches separados.

## 📚 Conteúdo

### 1. O que são Branches?
Imagine que você está criando um jogo. Você tem a versão funcional (chamada `main` ou `master`). Você quer testar uma "fase de gelo", mas não quer estragar o jogo principal se der errado.
No Git, você cria uma **Branch** (ramo/galho). É uma cópia paralela do seu projeto onde você pode experimentar livremente.

### 2. Comandos Principais
- **`git branch`**: Lista todos os branches.
- **`git branch <nome>`**: Cria um novo branch.
- **`git switch <nome>`**: Muda para o branch especificado. (Antigamente usava-se `checkout`).
- **`git merge <nome>`**: Traz as mudanças de OUTRO branch para o branch ATUAL.

### 3. O Fluxo de Trabalho Seguro
Nunca trabalhe direto na `main`!
1. Crie uma branch para sua tarefa: `git branch nova-funcionalidade`.
2. Mude para ela: `git switch nova-funcionalidade`.
3. Trabalhe, adicione e commite à vontade.
4. Volte para a `main` e "puxe" as novidades com `git merge`.

## 📽 Roteiro de Slides
- O conceito de "Multiverso" ou "Linhas do Tempo Paralelas".
- Branch Principal (`main`/`master`) vs Branches de Recurso (`feature`).
- Por que usar branches? (Isolamento de risco).
- Criando (`git branch`) e Trocando (`git switch`).
- Unindo tudo (`git merge`).
- O que acontece com os arquivos quando troco de branch? (Demonstração visual).

## 📝 Quiz
1. Qual é o nome padrão mais comum para o branch principal hoje em dia?
2. Para que serve criar um branch?
3. Qual comando cria um novo branch sem mudar para ele?
4. Qual comando usamos para trocar de branch?
5. O que o `git merge` faz?

## Gabarito
1: C
2: B
3: A
4: D
5: B

## 🛠 Exercícios
1. **Criar Branch**: No seu projeto de teste `teste-git`, crie uma branch chamada `experiencia`.
2. **Mudar**: Mude para essa branch com `git switch experiencia`.
3. **Alterar**: Crie um arquivo `teste.txt` e faça o commit.
4. **Voltar**: Volte para a `main` (`git switch main`).
5. **Observar**: Veja que o arquivo `teste.txt` sumiu! (Ele está seguro na outra "linha do tempo").
6. **Merge**: Estando na `main`, digite `git merge experiencia` para trazer o arquivo de volta.

## 🚀 Projeto da Aula
No seu `meu-portfolio-git`:
1. Crie uma branch chamada `adiciona-contato`.
2. Mude para ela: `git switch adiciona-contato`.
3. Crie um arquivo `contato.txt` com seu email.
4. `git add contato.txt`.
5. `git commit -m "Cria arquivo de contato"`.
6. Volte para a branch principal (`main` ou `master`). Note que o `contato.txt` sumiu da pasta.
7. Faça o merge: `git merge adiciona-contato`.
8. Agora o arquivo existe na branch principal também!
