# Aula 05 – Resolução de Conflitos

---

## O que é um Conflito?

- O Git une arquivos automaticamente... exceto se:
- **Duas pessoas alterarem a mesma linha** de formas diferentes.
- O Git entra em modo de segurança e pede ajuda humana.

---

## Anatomia do Conflito

```text
<<<<<<< HEAD
Meu título é Vermelho! (Sua versão)
=======
Este título é Azul! (Versão que vem do merge)
>>>>>>> feature-cores
```
- **HEAD**: Onde você está agora.
- **=======**: O divisor de águas.
- **>>>>>>>**: A origem da mudança externa.

---

## Como Resolver: 3 Etapas

1. **Editar**: Escolha o código final e **apague os marcadores**.
2. **Add**: `git add [arquivo]` (Marca como resolvido).
3. **Commit**: `git commit` (Finaliza a fusão).

---

## Dica: Ferramentas Visuais

- O VS Code destaca o conflito com cores.
- Botões: *Accept Current*, *Accept Incoming* ou *Accept Both*.
- Use a ferramenta para ganhar tempo!

---

## Regra de Ouro da Equipe

- Conflito não é erro, é **comunicação**.
- Se estiver na dúvida, chame o colega e discutam qual versão é a melhor para o projeto.
