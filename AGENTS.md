# tailor-resume

Gerador de currículos tailored + ATS-friendly (Markdown → PDF). Modo único: completo.

## Ordem de leitura (sempre, antes de qualquer geração)

1. `START.md` — processo completo, regras e checklist. Leitura obrigatória.
2. `in/profile.md` — perfil base da pessoa (seed). Se não existir, copiar de `in/profile.EXAMPLE.md` e preencher. Se `in/base/` tiver currículos antigos, consolidar os fatos de todos eles junto com o seed.
3. `in/job.md` — vaga alvo atual. Ou a vaga colada no chat.
4. `out/` — currículos já gerados (referência de formulação). Ler os 10 `.md` mais novos ou buscar por afinidade com a vaga; o mais aderente vira ponto de partida de estilo. Fatos valem sempre de `in/profile.md` + `in/base/`. `out/` vazio = partir só do seed.

## Regras inegociáveis

- Veracidade absoluta: nunca inventar cargo, empresa, data, métrica, tecnologia, certificação ou idioma.
- Idioma final = idioma da vaga.
- Saída sempre dupla: `out/<Empresa>_<Cargo>_<PT|EN>.md` + `.pdf` via `scripts/md_resume_to_pdf.py`. Nunca entregar só o `.md`.
- Cover letter só quando pedida: seguir `START.md` seção 8, salvar `out/<Empresa>_<Cargo>_CoverLetter_<PT|EN>.md` + `.pdf`.
- Todo output vem com: match score (alvo 80%+), keywords faltantes/adicionadas e check de requisitos eliminatórios.
- 1 página preferencial, ATS-safe: sem tabelas, colunas, ícones, fotos, emojis. Cabeçalhos padrão.
- Nunca sobrescrever arquivos em `out/`; iterar com sufixo `_v2`, `_v3`.

## Comandos

```bash
pip install -r requirements.txt
python3 scripts/md_resume_to_pdf.py "out/ARQUIVO.md" "out/ARQUIVO.pdf"
```

## Privacidade (repo público)

Nunca versionar dados reais: `in/profile.md`, `in/job.md` e `out/` estão no `.gitignore`. Só os `*.EXAMPLE.md` são commitados.
