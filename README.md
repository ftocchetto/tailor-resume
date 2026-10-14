# tailor-resume

Gere currículos sob medida para cada vaga, otimizados para ATS e para recrutadores. Markdown → PDF em 1 página.

## Como funciona

1. Você mantém seu perfil base em `in/profile.md` e cola a vaga em `in/job.md` (ou direto no chat).
2. O agente (Claude Code, Codex, Cursor, etc.) segue `START.md`: diagnostica a vaga, calcula match score, reescreve o currículo e entrega `.md` + `.pdf` em `out/`.
3. **Perfil dinâmico:** cada currículo aprovado em `out/` vira base para os próximos. Com o tempo, o agente parte dos currículos mais aderentes, não só do perfil original.

## Quickstart

```bash
git clone https://github.com/ftocchetto/tailor-resume.git
cd tailor-resume
pip install -r requirements.txt
cp in/profile.EXAMPLE.md in/profile.md   # preencha com seus dados
cp in/job.EXAMPLE.md in/job.md           # cole a vaga alvo
```

Depois peça ao agente:

> Gere meu currículo para a vaga em `in/job.md` seguindo `START.md`.

Resultado: `out/<Empresa>_<Cargo>_<PT|EN>.md` + `.pdf`, mais score, keywords e check de eliminatórios no chat.

## Estrutura

```
AGENTS.md                 # porta de entrada do agente
START.md                  # processo completo (modo completo)
in/profile.EXAMPLE.md     # modelo de perfil (copie para profile.md)
in/job.EXAMPLE.md         # modelo de vaga (copie para job.md)
in/base/                  # (opcional) seus currículos atuais — bootstrap, não versionado
out/                      # currículos gerados (.md + .pdf)
scripts/md_resume_to_pdf.py  # conversor Markdown → PDF ATS-friendly
```

## Suporte

- Idiomas de saída: PT-BR e EN (sempre o idioma da vaga).
- ATS Brasil (Gupy, Vagas.com) e gringa (Greenhouse, Workday, Lever).
- Regra de ouro: nada é inventado — sem métrica real, sem número no currículo.

## Privacidade

Este repo é público, mas seus dados não são commitados: `in/profile.md`, `in/job.md` e todo `out/` estão no `.gitignore`. Só os `*.EXAMPLE.md` (fictícios) são versionados.
