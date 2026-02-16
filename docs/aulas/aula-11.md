# Aula 11 – Boas práticas de commits e versionamento

## 🎯 Objetivos de Aprendizagem
- Escrever mensagens de commit claras e úteis.
- Entender o conceito de **Commit Atômico**.
- Conhecer o padrão **Conventional Commits**.
- Evitar erros comuns (commits gigantes, mensagens vagas).

## 📚 Conteúdo

### 1. Mensagens de Commit Importam
Imagine ler um histórico assim:
- `correção`
- `arrumando`
- `teste`
- `final`
Isso não ajuda ninguém. O objetivo da mensagem de commit é explicar o PORQUÊ da mudança.

### 2. A Regra do Imperativo
No Git, a convenção é usar o verbo no imperativo presente (como se você estivesse dando uma ordem ao código).
- **Ruim**: "Adicionado botão de login" (Passado) ou "Adicionando botão" (Gerúndio).
- **Bom**: "Adiciona botão de login" (Imperativo).
*Dica*: A mensagem deve completar a frase: "Se eu aplicar este commit, ele irá..." -> "Adicionar botão de login".

### 3. Commits Atômicos
Um commit deve fazer **uma única coisa**.
Se você corrigiu um bug no login E mudou a cor do rodapé:
- **Errado**: `git commit -m "Arruma login e muda cor"` (Misturou assuntos).
- **Certo**: Faça dois commits separados.
Isso facilita reverter uma mudança sem afetar a outra.

### 4. Conventional Commits
Um padrão muito usado na indústria:
- `feat: adiciona filtro de busca` (Nova feature).
- `fix: corrige erro de cálculo` (Correção de bug).
- `docs: atualiza readme` (Documentação).
- `style: formata código` (Espaços, pontuação).
- `refactor: melhora performance` (Sem mudar funcionalidade).

## 📽 Roteiro de Slides
- O Hall da Vergonha: "wip", "fix", "bug".
- A Estrutura Ideal: Título (50 chars) + Corpo (Opcional).
- O Modo Imperativo: "Adiciona", "Remove", "Corrige".
- Commit Atômico: Pequeno e focado.
- Padrões de Mercado: Conventional Commits (`feat:`, `fix:`).
- Por que isso ajuda no Code Review?

## 📝 Quiz
1. Qual é a convenção gramatical recomendada para mensagens de commit em português?
2. O que é um "Commit Atômico"?
3. Qual desses prefixos indica uma nova funcionalidade no padrão Conventional Commits?
4. Por que não devemos misturar correções de bugs com formatação de código no mesmo commit?
5. Qual mensagem é a mais adequada?

## Gabarito
1: B ("Imperativo Presente")
2: A ("Um commit que resolve apenas uma tarefa específica")
3: C ("feat:")
4: D ("Porque dificulta o review e a reversão de mudanças específicas")
5: C ("fix: corrige erro de validação no formulário")

## 🛠 Exercícios
1. **Analise o Histórico**: Dê `git log` no seu projeto. Suas mensagens seguem o padrão? (Provavelmente não, e tudo bem, estamos aprendendo).
2. **Prática de Amend**:
   - Faça uma alteração qualquer e commite com a mensagem "erro".
   - Ops! Mensagem ruim.
   - Use `git commit --amend -m "fix: corrige erro de digitação"` para reescrever o ÚLTIMO commit sem criar um novo.
   - **Cuidado**: Só faça isso se ainda não deu Push!

3. **Divisão**:
   - Faça duas alterações diferentes (ex: crie `a.txt` e `b.txt`).
   - Tente commitar `a.txt` primeiro (`git add a.txt`, `git commit`).
   - Depois commite `b.txt`.
   - Isso é atomicidade.

## 🚀 Projeto da Aula
Vamos limpar o histórico futuro do `portfolio-dev`.
1. Escolha uma tarefa pequena do seu Project Board (ex: Criar arquivo de Estilos ou atualizar Texto).
2. Crie a branch.
3. Faça a mudança.
4. Na hora de commitar, use o padrão Conventional Commit.
   Ex: `feat: adiciona seção de projetos no readme`
5. Veja como fica bonito no histórico do GitHub.
