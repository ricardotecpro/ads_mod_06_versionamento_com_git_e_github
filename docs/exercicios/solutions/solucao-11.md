# Solução – Exercícios da Aula 11

Aqui você encontra as respostas sugeridas para os exercícios de Boas Práticas de Commit da Aula 11.

### 1. Gramática do Commit
Exemplos de verbos no imperativo: **Adiciona**, **Remove**, **Corrige**, **Atualiza**, **Refatora**.
*Mensagem exemplo*: "Adiciona ícone de busca ao topo".

### 2. Trabalhando em Camadas
Para adicionar apenas um arquivo específico:
```bash
git add nome-do-arquivo.ext
```
Isso garante a atomicidade, enviando para o Stage apenas o que você deseja registrar naquele momento.

### 3. Padrões de Indústria
As mensagens aparecem prefixadas, facilitando a leitura rápida:
- `feat: ...`
- `docs: ...`
Ao usar `git log --oneline`, o histórico fica visualmente categorizado.

### 4. O Corretor de Mensagens
O comando para alterar a mensagem do último commit é:
```bash
git commit --amend -m "Sua nova mensagem aqui"
```

### 5. Entendendo a Atomicidade
Commits atômicos (focados em uma única tarefa) são essenciais porque, se a nova funcionalidade causar um erro mas a correção de bug for necessária, você pode usar o comando `git revert` apenas no commit da funcionalidade. Se ambos estivessem no mesmo commit, você teria que reverter a correção do bug junto, ou desfazer as mudanças manualmente, o que gera risco e perda de tempo.
