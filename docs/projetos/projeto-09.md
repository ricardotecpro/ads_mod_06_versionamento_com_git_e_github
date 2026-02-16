# Projeto da Aula 09

## 🚀 Projeto da Aula: Implementando o Fluxo Moderno

Vamos simular um dia de trabalho real.

### Passo 1: Atualizar
Sempre comece o dia garantindo que seu local está igual ao remoto.
```bash
git switch main
git pull
```

### Passo 2: A Tarefa (Feature)
Você precisa adicionar uma lista de "Soft Skills" ao portfólio.
```bash
git switch -c feature-soft-skills
```

### Passo 3: O Trabalho
Edite `sobre.txt`. Adicione:
"Soft Skills: Comunicação, Trabalho em Equipe, Resiliência."
```bash
git add .
git commit -m "Adiciona lista de soft skills"
```

### Passo 4: O Envio
```bash
git push -u origin feature-soft-skills
```

### Passo 5: O PR e Merge
Vá ao GitHub, abra o PR, revise e faça o Merge. Delete a branch remota.

### Passo 6: O Ciclo se Fecha
Volte ao terminal.
```bash
git switch main
git pull
git branch -d feature-soft-skills
```
Agora sua `main` local tem as Soft Skills, e a branch temporária se foi. Limpo e eficiente.
