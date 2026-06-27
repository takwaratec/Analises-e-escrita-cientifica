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

*Ficha gerada em 27/06/2026 · Fonte: GitHub danimaciel (github.com/danimaciel/terimpact-exante), código-fonte avaliacao_ex_ante_v23.py, SUPABASE.md, arquivos CSV · Tecnologia Takwara*
