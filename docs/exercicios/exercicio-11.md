# Exercícios da Aula 11

## 🛠 Boas Práticas: A Arte do Commit Profissional

### Nível: Básico

1.  **Gramática do Commit**:
    - Escolha uma alteração recente no seu código. Escreva uma mensagem de commit curta e direta utilizando o **Modo Imperativo**. Qual foi o verbo utilizado?

2.  **Trabalhando em Camadas**:
    - Realize duas alterações diferentes em arquivos distintos do seu projeto. 
    - Realize o commit de apenas **um** deles primeiro. Qual comando você utilizou para garantir que apenas um arquivo fosse para o "palco" (Staging Area)?

### Nível: Intermediário

3.  **Padrões de Indústria (Conventional Commits)**:
    - Utilize o prefixo `feat:` para registrar uma nova funcionalidade pequena e o prefixo `docs:` para registrar uma melhora no seu README.
    - Como as mensagens aparecem no seu `git log` após esses commits?

4.  **O Corretor de Mensagens**:
    - Realize um commit com uma mensagem genérica como "ajuste".
    - Sem fazer novas alterações nos arquivos, utilize o comando para **emendar** (amend) esse commit, trocando a mensagem para algo no padrão Conventional Commits (ex: `refactor: organiza estrutura de pastas`).

### Nível: Desafio

5.  **Entendendo a Atomicidade**:
    - Pesquise e explique com suas palavras por que é considerado uma "má prática" commitar uma correção de bug de lógica e uma alteração de cor de botão no mesmo commit. Como isso afeta o processo de `revert`?

---

[:octicons-arrow-right-24: Ver Solução](solutions/solucao-11.md)
