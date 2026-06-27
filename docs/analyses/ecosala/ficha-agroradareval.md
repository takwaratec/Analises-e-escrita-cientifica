---
tipo: Ficha Científica
projeto: ECOSALA / Acervo Científico
referencia: AgroRadarEval — Ferramenta de Gestão de P&D&I Orientada a Impacto Societal
autor: Daniela Maciel Pinto (Embrapa Territorial)
doi: 10.4067/S0718-27242024000400089
status: Consolidado
classificacao: Ficha Científica — Metodologia de Avaliação de Impacto
---

# Ficha Científica: AgroRadarEval — Gestão de P&D&I para Impacto Societal

## 1. Dados Gerais

| Campo | Dado |
|---|---|
| **Título completo** | AgroRadarEval — Data-driven RD&I management for societal impacts through evaluation results |
| **Autores** | Daniela Maciel Pinto |
| **Instituição** | Embrapa Territorial (Campinas/SP) |
| **Programa** | Doutorado em Política Científica e Tecnológica (DPCT) — Unicamp |
| **DOI** | [10.4067/S0718-27242024000400089](https://doi.org/10.4067/S0718-27242024000400089) |
| **Licença** | MIT (código aberto) |
| **Repositório** | [github.com/danimaciel/agroradareval](https://github.com/danimaciel/agroradareval) |
| **Ferramenta online** | [Shiny App](https://khi7yy-daniela-maciel0pinto.shinyapps.io/agroradareval_en/) |
| **Data** | 2024 |
| **Linguagem** | R (Shiny) |
| **Palavras-chave** | RRI, RRA, avaliação de impacto, P&D agrícola, gestão da inovação, avaliação responsável |

## 2. Estrutura

AgroRadarEval é uma ferramenta baseada em **R Shiny** que apoia líderes e gestores de P&D agropecuário a refletirem sobre suas capacidades organizacionais. A ferramenta foi desenvolvida a partir de:

- **Revisão sistemática da literatura** sobre uso de resultados de avaliação em programas de CT&I
- **Survey** com gestores de instituições agrícolas de P&D
- **Painéis conceituais** desenvolvidos em Miro
- **Validação** por especialistas

A ferramenta se sustenta em **três pilares**:

1. **Evaluation Capacity Building (ECB)** — Capacitação da organização para conduzir e usar avaliações
2. **Impact-Oriented Evaluation Culture** — Cultura orientada a impacto
3. **Reflexivity** — Reflexão contínua e adaptação

Operacionalizados por **oito dimensões**:

| # | Dimensão | O que mede |
|---|---|---|
| 1 | Participação e Colaboração | Envolvimento de stakeholders no processo avaliativo |
| 2 | Desenvolvimento de Habilidades | Capacitação técnica da equipe |
| 3 | Promoção de Cultura Avaliativa | Valorização da avaliação na organização |
| 4 | Feedback e Adaptação Contínuos | Uso dos resultados para ajustes |
| 5 | Integração com Planejamento Estratégico | Alinhamento entre avaliação e estratégia |
| 6 | Monitoramento | Acompanhamento sistemático de indicadores |
| 7 | Influências do Ambiente Externo | Contexto político, econômico e social |
| 8 | Comunicação | Disseminação dos resultados |

## 3. Problema

Instituições de pesquisa agropecuária frequentemente:
- Produzem avaliações de impacto que **não retroalimentam** a gestão estratégica
- Carecem de **cultura de avaliação** entre gestores e pesquisadores
- Não possuem **métricas padronizadas** para medir impacto societal
- Desconhecem **metodologias de RRI/RRA** para orientar suas decisões

## 4. Referencial Teórico

A ferramenta se fundamenta em dois campos teóricos principais:

1. **Responsible Research and Innovation (RRI)** — Abordagem europeia que propõe que a pesquisa e inovação sejam:
   - **Antecipatórias**: prever impactos antes de ocorrerem
   - **Reflexivas**: autoavaliação constante
   - **Inclusivas**: participação de múltiplos stakeholders
   - **Responsivas**: capacidade de mudar de direção

2. **Responsible Research Assessment (RRA)** — Movimento internacional (DORA, Leiden Manifesto, COARA) que defende:
   - Métricas qualitativas além do fator de impacto
   - Avaliação do impacto societal da pesquisa
   - Diversidade de indicadores

3. **Evaluation Capacity Building (ECB)** — Campo que estuda como organizações desenvolvem competências avaliativas

Os pilares foram operacionalizados através de **oito dimensões** identificadas por análise de conteúdo de entrevistas com gestores de P&D agrícola de múltiplas instituições.

## 5. Metodologia

O desenvolvimento do AgroRadarEval seguiu cinco etapas:

1. **Revisão sistemática** — Levantamento de publicações sobre uso de resultados de avaliação em CT&I nas bases Web of Science, Scopus e Google Scholar
2. **Entrevistas** — Com gestores de P&D agrícola (registradas no repositório agrium)
3. **Painéis Miro** — Sessões de design thinking para estruturar as dimensões
4. **Survey** — Coleta de dados com benchmarks estabelecidos
5. **Desenvolvimento Shiny** — Implementação em R Shiny com visualizações interativas

O código-fonte e os dados brutos estão disponíveis sob licença MIT no GitHub.

## 6. Principais Achados

1. O **uso efetivo** de resultados de avaliação na gestão de P&D agrícola é baixo — a maioria das instituições coleta dados mas não os incorpora ao planejamento estratégico
2. As dimensões **Participação e Colaboração** e **Comunicação** são os maiores gargalos identificados
3. A ferramenta permite **autoavaliação** com benchmark setorial, gerando gráficos radar que facilitam a visualização de pontos fortes e fracos
4. O **Ambiente Externo** (políticas públicas, financiamento, demanda social) é a dimensão que mais influencia o uso de avaliação

## 7. Avaliação Crítica

**Pontos fortes:**
- Código aberto e replicável (MIT)
- Metodologia baseada em evidências (revisão sistemática + survey + entrevistas)
- Interface Shiny acessível a não-programadores
- Framework RRI/RRA alinhado às tendências internacionais de avaliação de pesquisa
- Aplicável a qualquer instituição de P&D, não apenas agrícola

**Limitações:**
- A amostra do survey é focada em instituições brasileiras
- A ferramenta depende de autoavaliação (sujeita a vieses do respondente)
- A versão atual não inclui análise de dados quantitativos de produção científica
- Requer conhecimento de R para customização do código

## 8. Inserção no Estado da Arte

O AgroRadarEval insere-se no movimento global de **transformação da avaliação de pesquisa** — do fator de impacto para o impacto societal. Alinha-se a:

- **DORA** (San Francisco Declaration on Research Assessment, 2012)
- **Leiden Manifesto** (Hicks et al., 2015)
- **COARA** (Coalition for Advancing Research Assessment, 2022)
- **RRI frameworks** da Comissão Europeia (Horizon Europe)

A originalidade está em traduzir esses princípios gerais em uma **ferramenta concreta e operacional** para o contexto da P&D agrícola brasileira.

### Aplicação no ECOSALA

O AgroRadarEval pode ser usado pelo grupo para:

- **Avaliar a maturidade avaliativa** do ECOSALA como organização
- **Estruturar indicadores de impacto** para a proposta Vaga Lúmen
- **Embasar a seção de impacto societal** do Prêmio Zayed
- **Gerar relatórios visuais** (gráficos radar) para financiadores

---

*Ficha gerada em 27/06/2026 · Fonte: GitHub danimaciel (github.com/danimaciel/agroradareval), DOI 10.4067/S0718-27242024000400089, código-fonte e README do repositório · Tecnologia Takwara*
