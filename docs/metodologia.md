# Metodologia

## Protocolo de Análise

Cada referência inserida neste repositório passa por um fluxo padronizado de 7 etapas, baseado nos **200+ Prompts para Escrever Artigos Científicos** (Cavichiolli, 2025) e adaptado para análise de trabalhos acadêmicos:

### Etapa 1 — Extração e leitura inicial

- Obtenção do PDF completo
- Extração do texto via PyMuPDF
- Leitura da estrutura: título, autor, instituição, ano, orientador, resumo, palavras-chave
- Identificação do sumário e seções principais

### Etapa 2 — Mapeamento estrutural

- Verificação dos elementos pré-textuais (NBR 14724)
- Identificação da estrutura de capítulos
- Análise da progressão: introdução → referencial → método → resultados → conclusão

### Etapa 3 — Análise do referencial teórico

Identificação de:

- Escola teórica principal (Bourdieu, Weber, Marx, etc.)
- Conceitos-chave operacionalizados
- Autores de referência citados
- Coerência entre teoria e método

### Etapa 4 — Avaliação metodológica

- Abordagem (quali, quanti, mista)
- Técnicas de coleta (entrevistas, questionários, observação)
- Procedimento amostral
- Protocolo de análise dos dados
- Rigor ético (CEP, TCLE, anonimização)
- Limitações metodológicas identificadas

### Etapa 5 — Extração de achados

- Resultados principais (com valores numéricos quando disponíveis)
- Achados secundários relevantes
- Citações ilustrativas (verificadas na fonte original)

### Etapa 6 — Avaliação crítica

- Contribuições originais
- Lacunas e fraquezas
- Qualidade formal (ABNT: NBR 6023, 10520, 6027, 6028)
- Relevância para o repositório

### Etapa 7 — Inserção no estado da arte

- Classificação temática (percepção social, APO, política habitacional)
- Conexão com outras fichas do mesmo eixo
- Identificação de lacunas para pesquisa futura

---

## Prompts utilizados

A análise aplica os seguintes prompts do ebook (ver [wiki de prompts](https://fabiotakwara.github.io/Analises-e-escrita-cientifica/prompts/)):

| Seção do ebook | Prompt aplicado |
|----------------|-----------------|
| B1 — Revisão de Literatura | Planejamento de busca, Estado da arte, Mapa de controvérsias |
| B2 — Processo de Publicação | Análise de adequação, Verificação de conformidade, Análise de impacto |
| B3 — Normas Técnicas | Validação ABNT, Consistência terminológica |
| A2 — Metodologia | Prompt de aprimoramento + prompts específicos |

---

## Template da ficha técnica

Cada ficha segue este formato:

```markdown
> **Resumo:** [síntese em 5-6 linhas: objeto, método, achado central, implicação]

## 1. Dados gerais
[Tabela com título, autor, orientador, instituição, ano, páginas, palavras-chave]

## 2. Estrutura e organização
[Seções, capítulos, progressão]

## 3. Problema e perguntas de pesquisa
[Objetivos, tese central]

## 4. Referencial teórico
[Escola, conceitos, coerência]

## 5. Metodologia
[Abordagem, técnicas, amostra, limitações]

## 6. Principais achados
[Tabela de resultados]

## 7. Avaliação crítica
[Contribuições, lacunas, qualidade formal]

## 8. Inserção no estado da arte
[Conexões com outros trabalhos, relevância para o repositório]
```
