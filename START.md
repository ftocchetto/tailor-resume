# START — Processo padrão (modo completo)

Modo único: `completo` = diagnóstico + reescrita + entrega (`md` + `pdf` + report). Sem modos separados.

## 1. Entrada obrigatória

Coletar antes de escrever. Se faltar item crítico, perguntar e pausar.

| Parâmetro | Obrigatório | Exemplo |
|---|---|---|
| `cargo_alvo` | sim | Senior Product Manager |
| `industria_alvo` | sim | SaaS B2B / fintech |
| `nivel_senioridade` | sim | sênior, liderança, C-level |
| `idioma` (PT\|EN) | sim | = idioma da vaga |
| `mercado` (brasil\|gringa\|ambos) | sim | define parser e vocabulário |
| `requisitos_eliminatorios` | sim | inglês fluente, cidade, certificação |
| `descricao_vaga` | preferencial | `in/job.md` ou colada no chat |
| `plataforma_ats` | se souber | Gupy, Vagas.com, Greenhouse, Workday |

Sem `descricao_vaga`: análise fica genérica — avisar. Sem métricas por experiência: pedir ou marcar lacuna, nunca inventar.

## 2. Perfil dinâmico (base viva)

- Fonte factual (ler sempre): `in/profile.md` na íntegra + `in/base/` por afinidade com a vaga (na íntegra na primeira geração). É o registro completo — currículos tailored omitem o irrelevante, então os fatos vivem aqui.
- Referência de formulação: `out/` — os 10 `.md` mais novos **ou** busca por afinidade (mesmo idioma, área, cargo). O mais aderente vira ponto de partida de estilo e posicionamento, nunca de fatos.
- `out/` é a base viva: todo currículo aprovado entra para as próximas rodadas.
- Consolidar fatos de todas as fontes; nunca assumir que só a versão mais recente tem o melhor conteúdo.

## 3. Etapa 1 — Diagnosticar (score + eliminatórios)

1. Extrair keywords da vaga em 3 tipos: hard skills, soft skills, termos da indústria. Priorizar: P1 críticas (eliminam), P2 importantes, P3 desejáveis.
2. Match score = (P1+P2 atendidos / P1+P2 totais) × 100. Alvo: 80%+.
3. Checar cada requisito eliminatório contra o perfil: `ok` / `risco` / `não atende`. Sinalizar risco de eliminação prática.
4. Apontar bullets fracos (tarefa sem impacto), jargão vazio, skill obsoleta, lacuna temporal, inconsistência de datas.
5. Perspectiva dupla: parser ATS **e** recrutador (leitura de 6 segundos).

## 4. Etapa 2 — Reescrever

1. Reconstruir integralmente; não fazer edição superficial. Manter todos os cargos e formações (só remover se a pessoa pedir).
2. Resumo profissional, 3–4 linhas: posicionamento + anos de experiência + top skills da vaga + proposta de valor. Incluir 5–8 keywords P1 aqui.
3. Experiências em ordem reversa, 3–5 bullets cada (4–6 na mais relevante). Formato: **verbo de ação + o quê + como/escopo + resultado**. Mais aderente = mais espaço e bullets primeiro.
4. Skills agrupadas por categoria, com termos exatos da vaga. Sigla + termo por extenso quando útil (`OKRs (Objectives and Key Results)`).
5. Datas: PT por extenso (`Janeiro de 2020 – Dezembro de 2021`), EN `Jan 2020 – Dec 2021`. Reduz erro de parser.
6. Verbos preferidos: Liderou, Implementou, Reduziu, Aumentou, Otimizou, Automatizou, Estruturou, Escalou, Migrou / Led, Built, Scaled, Reduced, Shipped, Drove.
7. Proibido: primeira pessoa (`eu`), foto, tabela, coluna, ícone, emoji, buzzwords vazias (`proativo`, `dinâmico`, `ninja`, `rockstar`, `orientado a resultados` sem dado).
8. Pelo menos ~50% dos bullets com métrica real (%, R$/US$, tempo, volume, pessoas). Sem métrica real: impacto qualitativo, nunca número inventado.

## 5. Etapa 3 — Validar ATS

- Cabeçalhos padrão: `Summary`, `Experience`, `Education`, `Skills`, `Certifications` (ou equivalentes PT). Nada criativo.
- Coluna única, bullets `-`, PDF textual (não imagem), filename `Nome_Sobrenome_Resume.pdf`.
- Mercado `brasil`: otimizar para ranqueamento Gupy/Vagas.com (aderência semântica + eliminatórios + progressão). Mercado `gringa`: Greenhouse/Workday/Lever (keywords exatas + parsing limpo).
- Recalcular score estimado pós-mudanças.

## 6. Etapa 4 — Gerar md + pdf (sempre)

```bash
python3 scripts/md_resume_to_pdf.py "out/ARQUIVO.md" "out/ARQUIVO.pdf"
```

O script ajusta o font-size para caber em 1 página. Se estourar mesmo no mínimo, cortar antes de encolher: condensar experiências menos relevantes, nunca as P1.

## 7. Entrega

1. Arquivos gerados (paths do `.md` e `.pdf`).
2. Score antes → depois, keywords adicionadas e onde (resumo/skills/bullets).
3. Check de eliminatórios (um por linha: ok/risco).
4. 1–2 perguntas de refinamento, se houver lacuna real (métrica, idioma, foco).
5. Se cover letter pedida: paths do `md` + `pdf` da carta.

## 8. Cover letter (quando pedida, após Etapa 2)

Gerar só se a pessoa pedir ou se a vaga exigir. Mesmas fontes de fatos do currículo (`in/profile.md` + `in/base/`) e mesma regra: nada inventado.

1. Idioma = idioma da vaga. 250–350 palavras, 3–4 parágrafos, sem bullets. Cabe em 1 página no mesmo script.
2. Abertura: um gancho específico da vaga (frase do anúncio, produto, missão) + cargo exato. Nada de "To whom it may concern" ou "I want to express my interest".
3. Meio: 2–3 provas concretas que respondem aos P1 da vaga, com as métricas reais do currículo. Recomendação só se constar em `in/profile.md` ou `in/base/` (nome + cargo + trecho curto), nunca inventada.
4. Lacunas: não esconder nem fingir. Se relevante, mostrar o caminho real (ex.: "currently studying React").
5. Fechamento: o que a pessoa quer resolver na empresa + disponibilidade (fuso, remoto). Assinatura com nome, email, LinkedIn e portfólio.
6. Consistência: nenhum fato profissional (cargo, empresa, data, métrica, tecnologia, certificação, idioma, recomendação) fora do currículo enviado junto. Motivação e disponibilidade são a única exceção e não podem contradizer o currículo.
7. Formato: começar com `# Nome` e uma linha de contato; depois parágrafos simples. Gerar `md` + `pdf` com o mesmo script:

```bash
python3 scripts/md_resume_to_pdf.py "out/<Empresa>_<Cargo>_CoverLetter_<PT|EN>.md" "out/<Empresa>_<Cargo>_CoverLetter_<PT|EN>.pdf"
```

## Checklist final (antes de entregar)

- [ ] Vaga lida e P1/P2/P3 extraídos?
- [ ] `in/profile.md` + `in/base/` (fatos) + `out/` (afinidade/10 novos) consolidados?
- [ ] Idioma = idioma da vaga, ortografia correta?
- [ ] Score estimado 80%+? Eliminatórios checados?
- [ ] Resumo com 5–8 keywords P1, sem primeira pessoa?
- [ ] Bullets ação+escopo+resultado, ~50% com métrica real?
- [ ] ATS-safe (coluna única, headers padrão, sem tabela/ícone/foto)?
- [ ] `md` + `pdf` gerados em `out/` com naming correto?
- [ ] Nada inventado?
- [ ] Cover letter (se pedida): gancho específico, 2–3 provas com métrica real, nenhum fato profissional fora do currículo, `md` + `pdf`?

## Naming

`out/<Empresa>_<Cargo>_<PT|EN>.md` + `.pdf`. Iterações: `_v2`, `_v3` (vale também para CoverLetter). Cover letter: `out/<Empresa>_<Cargo>_CoverLetter_<PT|EN>.md` + `.pdf`. Vaga sem empresa clara: `out/<id>_<Cargo>_<PT|EN>.md`.
