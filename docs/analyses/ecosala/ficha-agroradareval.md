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

---

## 📖 Glossário Didático

| Termo | Significado |
|---|---|
| **RRI** *(Responsible Research and Innovation)* | Metodologia europeia que defende que pesquisa e inovação sejam feitas **com** a sociedade, não **para** a sociedade. Quatro pilares: antecipar impactos, refletir sobre consequências, incluir diversos atores, responder a mudanças |
| **RRA** *(Responsible Research Assessment)* | Movimento internacional que critica o uso do fator de impacto como única métrica de qualidade. Defende avaliar a pesquisa pelo **impacto societal** que gera, não apenas por citações |
| **ECB** *(Evaluation Capacity Building)* | Processo de **capacitar** uma organização para fazer e usar avaliações — ensinar as pessoas a avaliar, criar infraestrutura de dados, incorporar a avaliação na rotina |
| **Shiny** | Framework do R que permite criar **aplicativos web interativos** sem saber HTML/JavaScript. O usuário acessa pelo navegador, mexe em controles, e vê os resultados em tempo real |
| **Benchmark** | Nota de referência. O AgroRadarEval compara as respostas da sua organização com a média de outras instituições que já responderam. Isso permite saber se você está acima ou abaixo da média |
| **Gráfico Radar** | Gráfico em forma de teia de aranha com vários eixos saindo do centro. Cada eixo é uma dimensão avaliada. Quanto mais longe do centro, melhor o desempenho naquela dimensão |
| **Stakeholder** | Qualquer pessoa ou grupo que é **afetado** pelo projeto ou **pode afetá-lo**: comunidades, financiadores, parceiros, poder público, universidades |
| **CT&I** | Ciência, Tecnologia e Inovação |
| **P&D&I** | Pesquisa, Desenvolvimento e Inovação |
| **Survey** | Questionário estruturado aplicado a um grupo de pessoas para coletar dados padronizados |
| **Revisão Sistemática** | Método de pesquisa que **levanta TODOS os artigos publicados** sobre um tema, seguindo um protocolo rigoroso, para responder uma pergunta específica |

---

### 🎯 Aplicação no ECOSALA — Passo a Passo para os Projetos Reais

#### Como usar na prática (sem precisar programar)

1. **Acesse o app pronto**: [khi7yy-daniela-maciel0pinto.shinyapps.io/agroradareval_en/](https://khi7yy-daniela-maciel0pinto.shinyapps.io/agroradareval_en/) — funciona no navegador, não precisa instalar nada
2. **Cada membro responde** o questionário (leva cerca de 15 minutos)
3. **O app gera automaticamente** o gráfico radar mostrando os pontos fortes e fracos do grupo
4. **Você usa esse diagnóstico** para justificar ações corretivas na proposta de edital

#### Aplicação direta em cada projeto

**📋 Vaga Lúmen (FINEP):**

A FINEP exige que o proponente demonstre **capacidade de gestão e governança**. O AgroRadarEval fornece:

| O que a FINEP quer | Como o AgroRadarEval responde |
|---|---|
| "Qual a experiência da equipe em gestão de projetos?" | Gráfico radar mostrando as 8 dimensões avaliadas → prova visual |
| "Como serão monitorados os resultados?" | A dimensão **Monitoramento** (6) tem nota e justificativa no relatório |
| "Como a comunidade participa do projeto?" | A dimensão **Participação e Colaboração** (1) mostra como o grupo envolve stakeholders |
| "Qual a estratégia de comunicação?" | A dimensão **Comunicação** (8) já avalia isso |

**Resultado concreto**: Você anexa ao formulário FINEP um **Relatório de Autoavaliação ECOSALA** com:
- Gráfico radar colorido (impacto visual)
- Diagnóstico de cada dimensão
- Plano de melhoria baseado nas notas mais baixas

**🌾 MSTJS / Prêmio Zayed (USD 100.000):**

O Prêmio Zayed avalia **impacto em comunidades**. O AgroRadarEval mede justamente:

- **Participação e Colaboração** (dimensão 1) → como o Viveiro-Educador envolve a comunidade do assentamento
- **Influências do Ambiente Externo** (dimensão 7) → como políticas públicas e contexto local afetam o projeto
- **Comunicação** (dimensão 8) → como os resultados são divulgados

**Resultado concreto**: O diagnóstico do AgroRadarEval vira parte do dossiê do Prêmio Zayed, mostrando que o grupo tem **maturidade de gestão** — um diferencial que muitos projetos comunitários não têm.

**🌱 ECOSALA (funcionamento interno):**

| Problema que o grupo enfrenta | Como o AgroRadarEval ajuda |
|---|---|
| Difícil coordenar 12 pesquisadores de áreas diferentes | A dimensão **Participação e Colaboração** identifica gargalos de articulação |
| Não sabemos se estamos no caminho certo | A dimensão **Feedback e Adaptação** avalia se o grupo aprende com os erros |
| Falta métrica para mostrar resultado para parceiros | As 8 dimensões viram indicadores objetivos |

---

*Ficha gerada em 27/06/2026 · Fonte: GitHub danimaciel (github.com/danimaciel/agroradareval), DOI 10.4067/S0718-27242024000400089, código-fonte e README do repositório · Tecnologia Takwara*
