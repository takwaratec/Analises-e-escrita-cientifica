---
tipo: Ficha Científica
projeto: ECOSALA / Acervo Científico
referencia: TerImpact Ex-Ante — Aplicação para Avaliação Ex-Ante de Projetos de Pesquisa
autor: Daniela Maciel (Embrapa Territorial)
status: Consolidado
classificacao: Ficha Científica — Ferramenta de Avaliação de Impacto
---

# Ficha Científica: TerImpact Ex-Ante — Avaliação Prévia de Projetos de Pesquisa

## 1. Dados Gerais

| Campo | Dado |
|---|---|
| **Título** | TerImpact Ex-Ante |
| **Autores** | Daniela Maciel Pinto |
| **Instituição** | Embrapa Territorial (Campinas/SP) |
| **Tecnologia** | Streamlit (Python) + Supabase (PostgreSQL) |
| **Repositório** | [github.com/danimaciel/terimpact-exante](https://github.com/danimaciel/terimpact-exante) |
| **Última atualização** | Maio/2026 |
| **Status** | Ativo — 9 commits, última versão v23 |
| **Licença** | Não especificada (código aberto no GitHub) |
| **Área de aplicação** | Avaliação ex-ante de projetos de P&D agropecuário |
| **Palavras-chave** | avaliação ex-ante, impacto, P&D, Streamlit, gestão de CT&I, governança |

## 2. Estrutura

TerImpact Ex-Ante é um aplicativo web desenvolvido em **Python (Streamlit)** com banco de dados **Supabase (PostgreSQL)** para realizar a avaliação ex-ante de propostas de projetos de pesquisa. O app cobre todo o ciclo de vida de uma proposta:

### Fluxo de trabalho (workflow)

```
Rascunho → Enviada ao CTI → Em análise → Ajuste solicitado → Encaminhada à TT → 
Em trabalho → Devolvida ao CTI → Finalizada / Arquivada
```

### Papéis do sistema

| Papel | Atribuições |
|---|---|
| **Proponente** | Cria e submete propostas |
| **CTI** (Coord. Técnico-Científica) | Analisa, aprova, solicita ajustes |
| **TT** (Transferência de Tecnologia) | Avalia potencial de transferência |
| **Admin** | Gerencia o sistema e visualiza todas as propostas |

### Módulos

1. **Cadastro da proposta**: título, proponente, unidade, área temática, portfólio, parceiros, públicos-alvo, resultados esperados
2. **Indicadores de avaliação**: notas em múltiplas dimensões (econômica, social, ambiental, institucional)
3. **Cálculo de índices**: agregação das notas em gráficos Plotly
4. **Painel de governança**: consulta, filtro (por título, proponente, unidade, área, portfólio), exportação CSV/Excel
5. **Autenticação**: Supabase Auth com domínio de email restrito (@embrapa.br)

## 3. Problema

Instituições de pesquisa enfrentam dificuldades para:
- Avaliar **antes da execução** se um projeto tem potencial de impacto
- Padronizar o processo de avaliação entre diferentes unidades e áreas temáticas
- Rastrear o fluxo de aprovação e tramitação das propostas
- Gerar **histórico de avaliações** que retroalimente a gestão estratégica
- Integrar critérios de **transferência de tecnologia** na avaliação preliminar

## 4. Referencial Teórico

O TerImpact Ex-Ante se baseia nos campos de:

1. **Avaliação ex-ante de projetos** — Metodologias para estimar o impacto potencial antes da execução, contrastando com avaliação ex-post (feita após a conclusão)
2. **Gestão de portfólio de P&D** — Técnicas de priorização de projetos com base em critérios multidimensionais
3. **Transferência de Tecnologia (TT)** — Incorporação da dimensão de transferência como etapa do fluxo de avaliação, não como atividade posterior
4. **Indicadores compostos** — Agregação ponderada de múltiplos indicadores em índices sintéticos para tomada de decisão

O diferencial em relação a ferramentas genéricas de gestão de projetos está na incorporação de **dimensões específicas do contexto da pesquisa agropecuária**:
- Áreas temáticas da Embrapa (agroecologia, bioeficiência, transformação digital, etc.)
- Portfólios estratégicos (Sistemas Sustentáveis, Clima, Biodiversidade, etc.)
- Públicos e parceiros típicos do setor
- Critérios de TT e inovação

## 5. Metodologia

O aplicativo implementa:

**Cadastro estruturado** com dados importados de arquivos CSV:
- `unidades.csv` — Unidades da Embrapa
- `areas_tematicas.csv` — Áreas de pesquisa
- `parceiros.csv` — Tipos de parceiros
- `publicos.csv` — Públicos-alvo
- `empregados.csv` — Empregos gerados (indicador)
- `resultados_embrapa.csv` — Tipos de resultados esperados

**Cálculo de indicadores** via algoritmo de agregação ponderada que gera:
- Índices por dimensão (econômica, social, ambiental, institucional)
- Índice geral da proposta
- Visualização em gráfico (Plotly) para comparação entre propostas

**Tramitação** com controle de estado, garantindo rastreabilidade:
- ID único no formato `TER-AAAAMMDD-XXXXXXXX`
- Histórico de mudanças de status
- Comentários associados a cada proposta
- Painel de governança com exportação

**Persistência** em duas camadas:
- Local: arquivo CSV (sempre salvo)
- Nuvem: tabela `avaliacoes` no Supabase (quando configurado)

A arquitetura com login e perfis usa Supabase Auth e uma estrutura de banco relacional com tabelas `profiles`, `propostas`, `proposta_resultados`, `respostas_indicadores`, `indices_avaliacao`, `tramitacoes` e `comentarios`.

## 6. Principais Achados

1. A ferramenta **padroniza** o processo de avaliação ex-ante, reduzindo a subjetividade
2. O **fluxo de governança** (CTI → TT) incorpora a transferência de tecnologia como etapa obrigatória
3. O **painel de governança** permite à gestão visualizar gargalos no processo
4. A **exportação de dados** (CSV/Excel) viabiliza auditoria e prestação de contas
5. A **autenticação por domínio** (@embrapa.br) garante segurança e rastreabilidade

## 7. Avaliação Crítica

**Pontos fortes:**
- Aplicação funcional e completa (não é protótipo conceitual)
- Interface web acessível via navegador
- Código aberto e personalizável
- Fluxo de governança claro e auditável
- Integração com Supabase (escalável)
- Geração de IDs únicos e históricos de tramitação

**Limitações:**
- Atualmente configurado para o domínio @embrapa.br (requer adaptação para outras instituições)
- Os CSVs de base (unidades, áreas, parceiros) são específicos da Embrapa
- A documentação do código é técnica (não há manual do usuário)
- A métrica de impacto ex-ante depende da qualidade dos dados inseridos
- A aplicação piloto não foi validada externamente em outras instituições

## 8. Inserção no Estado da Arte

O TerImpact Ex-Ante contribui para o campo de **avaliação de impacto de pesquisa** ao:

1. **Operacionalizar** princípios de avaliação responsiva em uma ferramenta concreta
2. **Integrar** a transferência de tecnologia como etapa do fluxo de aprovação (não como atividade posterior)
3. **Oferecer** rastreabilidade completa do ciclo de vida da proposta

### Aplicação no ECOSALA / Vaga Lúmen

O TerImpact Ex-Ante pode ser adaptado para uso no ECOSALA:

| Componente Embrapa | Adaptação ECOSALA |
|---|---|
| email @embrapa.br | email aberto + senha |
| Unidades Embrapa | Membros do ECOSALA |
| Portfólios Embrapa | Eixos: bambu, PU vegetal, saneamento, bioeconomia |
| CTI (Coord. Técnica) | Comitê científico do ECOSALA |
| TT (Transf. Tecnologia) | Parceiros (Imperveg, TEIA, MST) |
| Resultados esperados | Produtos: fichas técnicas, patentes, protótipos |

**Benefício direto**: a proposta **Vaga Lúmen** poderia usar a ferramenta para estruturar a seção de **metodologia de avaliação de impacto** e demonstrar à FINEP que o projeto possui governança sobre seus resultados.

---

## 📖 Glossário Didático

| Termo | Significado |
|---|---|
| **Ex-ante** | Em latim, "antes do fato". Avaliação ex-ante é feita **antes** do projeto começar, para estimar se ele terá impacto. Ao contrário de ex-post (depois de terminado) |
| **Streamlit** | Framework Python que transforma scripts em **aplicativos web** automaticamente. O programador escreve o código e o Streamlit gera a interface sozinho |
| **Supabase** | Plataforma que oferece banco de dados PostgreSQL + autenticação + API, tudo pronto para usar. É uma alternativa open-source ao Firebase do Google |
| **PostgreSQL** | Sistema de banco de dados relacional (armazena dados em tabelas ligadas entre si). É o mais robusto e usado do mundo open-source |
| **Workflow / Fluxo de trabalho** | Sequência de etapas que um documento (ou proposta) percorre. Ex: Rascunho → Enviado → Analisado → Aprovado → Arquivado |
| **CTI** | Coordenação Técnico-Científica — instância que avalia o mérito científico de uma proposta |
| **TT** | Transferência de Tecnologia — instância que avalia se o resultado da pesquisa pode chegar à sociedade |
| **Governança** | Conjunto de regras, processos e estruturas que garantem que um projeto seja bem administrado, com responsabilidades claras |
| **Auditável** | Que permite rastrear quem fez o quê, quando — todas as ações ficam registradas com data, autor e status |
| **ID único** | Código gerado automaticamente para cada proposta (ex: `TER-20260627-A1B2C3D4`), que identifica o projeto para sempre |
| **Dashboard / Painel** | Tela que reúne, em um só lugar, os principais indicadores — visão geral para tomada de decisão |
| **CSV** | Arquivo de dados em formato de tabela (abre no Excel). É o formato universal para exportar dados |
| **API** | Interface de programação — um "tradutor" que permite que dois sistemas conversem entre si |

---

### 🎯 Aplicação no ECOSALA — Passo a Passo

#### O que este app faz, em português claro

Imagine que cada projeto do grupo precisa passar por um **processo de aprovação** — igual uma revista científica, mas para projetos. O TerImpact Ex-Ante é o **sistema que gerencia esse processo**:

1. Alguém **cadastra a ideia** do projeto no sistema (web)
2. O **comitê científico** (Marcos, Vicente, Gisele) analisa — aprova ou pede ajustes
3. O **setor de transferência** (André, Imperveg) avalia se a tecnologia chega na ponta
4. Tudo fica **registrado com data, ID e histórico**
5. A diretoria tem um **painel** mostrando todos os projetos e seus status

#### Para que serve na prática

| Problema que o grupo enfrenta | Como TerImpact Ex-Ante resolve |
|---|---|
| "Cada projeto segue um processo diferente" | Todos passam pelo **mesmo fluxo padronizado** |
| "Perdemos o histórico das decisões" | Toda movimentação fica **registrada com ID, data e autor** |
| "Não sabemos quais projetos estão andando" | O **painel** mostra todos os projetos e seus status |
| "A FINEP quer ver governança" | Você **exporta um relatório CSV** com o histórico completo |
| "A transferência de tecnologia é考量 depois" | O fluxo **inclui a TT como etapa obrigatória** antes da aprovação final |

#### Aplicação em cada projeto real

**📋 Vaga Lúmen (FINEP):**

| O que a FINEP quer | Como o TerImpact Ex-Ante entrega |
|---|---|
| "Descreva a metodologia de avaliação do projeto" | O sistema **é** a metodologia — cadastro → indicadores → notas → relatório |
| "Qual a governança do projeto?" | O fluxo mostra quem aprova o quê: proponente → CTI → TT |
| "Como serão medidos os resultados?" | Os **índices calculados** (econômico, social, ambiental) geram métricas |
| "Quem são os parceiros?" | O cadastro lista **parceiros, públicos, unidades e resultados esperados** |

**Resultado**: A seção de **Metodologia de Avaliação de Impacto** da proposta FINEP pode usar este sistema. Você não precisa inventar — o sistema **já faz**.

**🌾 MSTJS / Prêmio Zayed (USD 100.000):**

O Zayed pede **comprovação de impacto mensurável**. O TerImpact permite:

- Cadastrar indicadores de impacto do Viveiro-Educador
- Calcular índices por dimensão (social, ambiental, econômica)
- Gerar relatório de avaliação ex-ante do projeto

**🏭 Fábrica Modelo (André/Maurílio):**

Usar o sistema para **priorizar** quais tecnologias prototipar primeiro:

| Tecnologia | Índice Social | Ambiental | Econômico | Prioridade |
|---|---|---|---|---|
| Forno ecológico | 8 | 9 | 6 | 1º |
| Cúpula geodésica PU | 7 | 8 | 5 | 2º |
| Biorrefinaria | 5 | 9 | 3 | 3º |

#### Plano de adoção (3 passos)

| Passo | O que fazer | Quem | Tempo |
|---|---|---|---|
| 1 | Daniela libera o acesso ou adapta o app | Daniela + Fabio | 1 dia |
| 2 | Trocar os CSVs: unidades = membros, portfólios = eixos do grupo | Fabio | 2 dias |
| 3 | Fazer avaliação piloto com o Vaga Lúmen | Grupo | 1 reunião |

#### Resultados esperados

| Prazo | Resultado |
|---|---|
| 1 mês | App rodando com dados do ECOSALA + 1 avaliação piloto |
| 3 meses | Todas as propostas pelo fluxo de aprovação |
| 6 meses | Relatório ex-ante anexado como prova de governança na FINEP |

---

*Ficha gerada em 27/06/2026 · Fonte: GitHub danimaciel (github.com/danimaciel/terimpact-exante), código-fonte avaliacao_ex_ante_v23.py, SUPABASE.md, arquivos CSV · Tecnologia Takwara*
