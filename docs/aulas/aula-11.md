# Aula 11 – Boas Práticas: A Arte do Commit

## 🎯 Objetivos de Aprendizagem
- Escrever mensagens de commit claras, úteis e profissionais.
- Entender e aplicar o conceito de **Commit Atômico**.
- Conhecer o padrão global **Conventional Commits**.
- Evitar erros comuns como commits gigantes ou mensagens vagas.

---

## 📚 Conteúdo

### 1. Mensagens que Contam Histórias
Cuidado com o "Hall da Vergonha" do histórico do Git: `ajuste`, `teste`, `arrumando`, `final_v2`. Isso não ajuda ninguém. O objetivo da mensagem de commit é explicar o **porquê** da mudança.

| ❌ Ruim | ✅ Bom | Motivo |
| :--- | :--- | :--- |
| `corrigido` | `fix: corrige erro no login` | Explica o que foi feito. |
| `mais coisas` | `feat: adiciona botão de busca` | Especifica a funcionalidade. |
| `lixo` | `refactor: limpa código morto` | Indica uma melhoria técnica. |

!!! tip "A Regra do Imperativo"
    Escreva a mensagem como se estivesse dando uma ordem ao código: "Adiciona botão", "Remove ícone", "Corrige bug".

### 2. Commits Atômicos: O Superpoder da Reversão
Um commit deve fazer **uma única coisa**. Se você corrigiu um erro no rodapé e mudou a cor do cabeçalho, faça dois commits separados.

!!! failure "Commit Gigante"
    Misturar assuntos dificulta o Code Review e torna quase impossível reverter apenas uma parte da mudança se algo der errado.

### 3. Conventional Commits
Este é o padrão de mercado usado por grandes empresas e projetos Open Source:

*   **`feat:`**: Nova funcionalidade.
*   **`fix:`**: Correção de bug.
*   **`docs:`**: Alteração em documentação.
*   **`style:`**: Formatação (espaços, ponto e vírgula) sem mudar lógica.
*   **`refactor:`**: Melhoria de código que não altera o comportamento.
*   **`test:`**: Adição ou correção de testes.

### 4. Ops, errei a mensagem! (git commit --amend)
Cometeu um erro de digitação no último commit? Não se desespere!

<!-- termynal -->
```bash
# Corrigindo a mensagem do ÚLTIMO commit (antes do push)
$ git commit --amend -m "feat: adiciona busca por categorias"
```

!!! warning "Cuidado"
    Nunca use o `--amend` em commits que você já enviou para o GitHub (`push`), pois isso reescreve o histórico e pode causar problemas para seus colegas.

---

## 📝 Prática

### Exercícios de Fixação
Refine suas mensagens e aprenda a dividir suas tarefas em pequenas entregas.
[:octicons-arrow-right-24: Ver Exercícios da Aula 11](../exercicios/exercicio-11.md)

### Mini-Projeto
Padronizando o histórico do seu portfólio com Conventional Commits.
[:octicons-arrow-right-24: Ver Projeto da Aula 11](../projetos/projeto-11.md)
