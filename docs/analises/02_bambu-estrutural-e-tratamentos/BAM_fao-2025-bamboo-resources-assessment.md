# Bamboo Resources Assessment — Metodologia SEPAL com Estudos de Caso na Ásia (FAO 2025)

> Publicação técnica da Organização das Nações Unidas para Alimentação e Agricultura (FAO) que apresenta metodologia inovadora para avaliação de recursos de bambu por sensoriamento remoto, utilizando a plataforma SEPAL e dados de satélite de acesso livre. A abordagem integra séries temporais, algoritmos de aprendizado de máquina (Random Forest) e validação por amostragem colaborativa para mapear e quantificar estoques de bambu em Myanmar, Bangladesh (Chittagong) e Tailândia, estabelecendo protocolo replicável para inventários florestais de bambu em escala nacional e regional.

---

## 📁 Ficha Técnica (Seção 1)

- **Título original:** Bamboo resources assessment — A methodological approach using SEPAL with case studies in Asia
- **Autores:** Paing Phyo, Marco Piazza, Lorena Hojas Gascon
- **Instituição:** Food and Agriculture Organization of the United Nations (FAO)
- **Programa:** AIM4Forests – Accelerating Innovative Monitoring for Forests (financiamento do Department for Energy Security and Net Zero do Reino Unido)
- **Ano:** 2025
- **ISBN:** 978-92-5-140007-4
- **DOI:** [10.4060/cd6448en](https://doi.org/10.4060/cd6448en)
- **Tipo:** Relatório técnico / Manual metodológico (FAO)
- **Licença:** CC BY 4.0 International
- **Páginas:** 50
- **Idioma:** Inglês
- **Palavras-chave:** Bambu; Sensoriamento remoto; SEPAL; FAO; Random Forest; CCDC; Inventário florestal; Recursos de bambu; Séries temporais
- **Link:** `open "/Users/fabiotakwara/Documents/BAMBUBR/Bambo-Resources-Assessment.pdf"`
- **Link web:** [Bamboo Extent Explorer](https://ee-bamboo.projects.earthengine.app/view/bamboo-extent-explorer)

---

## 📄 Resumo / Sinopse (Seção 2)

O relatório aborda uma lacuna crítica no conhecimento global sobre recursos de bambu: embora o bambu seja reconhecido como recurso estratégico para desenvolvimento sustentável — ocupando cerca de 35 milhões de ha (FAO, 2020) com mais de 1.600 espécies registradas (INBAR, 2021) — apenas 23 países reportaram informações sobre recursos de bambu no Global Forest Resources Assessment (FRA) de 2020. Faltam metodologias padronizadas, acessíveis e replicáveis para avaliar estoques de bambu em escala nacional.

A publicação propõe uma abordagem simples e prática para mapeamento de bambu em larga escala no Sudeste Asiático, utilizando ferramentas de computação em nuvem: SEPAL (FAO) e Google Earth Engine (GEE). Integra dados de satélite gratuitos — Sentinel-1 (radar) e Sentinel-2 (óptico) em séries temporais de 2022 a agosto de 2024, com foco em meados de março a meados de abril de 2024 — além de dados SRTM de elevação e dados globais de altura de dossel (Lang et al., 2023).

O estudo combina análise de séries temporais CCDC (Continuous Change Detection and Classification) com dados ópticos e de radar, incorporando múltiplos índices de vegetação (NDVI, EVI, GCVI, MTCI, NDFI), além de atributos de textura (GLCM) e topográficos. Uma inovação metodológica chave é o uso de séries temporais para extrair características fenológicas (amplitude, fase, declividade) de bandas espectrais e índices de vegetação, melhorando a acurácia da classificação.

O classificador Random Forest (RF) com 40–100 árvores otimizadas proporciona detecção aprimorada de bambu, e o uso do Collect Earth Online (CEO) para coleta colaborativa de amostras de treinamento aumenta a confiabilidade da classificação.

---

## 📑 Estrutura da Obra / Organização (Seção 3)

O relatório de 50 páginas está organizado em 10 seções principais, além de elementos pré-textuais e pós-textuais:

1. **Introdução** (p. 1–4): Contextualização do bambu, problema de pesquisa, papel do INBAR, revisão bibliográfica, objetivos e áreas de estudo.
2. **Área de Estudo** (p. 4–7): Descrição detalhada de Myanmar, Chittagong Division (Bangladesh) e Tailândia — incluindo mapas de cobertura da terra, elevação SRTM e precipitação média.
3. **Metodologia** (p. 8–14): Algoritmo CCDC, uso do SEPAL, coleta e preparação de dados, processo de mapeamento de bambu (incluindo tuning de hiperparâmetros).
4. **Resultados e Discussão** (p. 15–29): Importância de dados temporais, papel do CEO, importância de atributos por país (Myanmar, Bangladesh, Tailândia), distribuição topológica/geográfica, avaliação de acurácia.
5. **Bamboo Web Portal** (p. 30–31): Descrição do aplicativo web Bamboo Extent Explorer.
6. **Achievements** (p. 32): Principais realizações do estudo.
7. **Limitations** (p. 33): Limitações metodológicas e recomendações.
8. **Implications for Bamboo Management** (p. 33): Implicações para manejo do bambu.
9. **Conclusions** (p. 34): Conclusões e próximos passos.
10. **References** (p. 35–37): 40 referências bibliográficas.

O volume contém ainda 29 figuras (mapas, gráficos de importância de atributos, matrizes de confusão, espectros temporais) e 5 tabelas (dados de satélite utilizados, matrizes de confusão para cada país, acurácia global e coeficiente Kappa).

---

## 🎯 Conteúdo / Principais Tópicos (Seção 4)

### 4.1 Problema central
Apenas 23 países reportaram dados de bambu no FRA 2020, e faltam metodologias padronizadas para avaliação de recursos de bambu — diferentemente do que ocorre com inventários florestais convencionais.

### 4.2 Objetivos
- Desenvolver método prático e replicável para mapeamento de bambu em larga escala usando sensoriamento remoto e plataformas em nuvem.
- Validar a metodologia com estudos de caso em três países do Sudeste Asiático.
- Disponibilizar mapas e ferramentas interativas para tomadores de decisão.

### 4.3 Áreas de estudo
- **Myanmar**: País com extensas áreas de bambu nativo em diferentes contextos ecológicos.
- **Chittagong Division (Bangladesh)**: Região de colinas (Chittagong Hill Tracts) com sistemas agroflorestais tradicionais.
- **Tailândia**: Paisagens complexas com predomínio de vegetação nativa e sistemas agrícolas.

### 4.4 Inovação metodológica
- Uso de séries temporais CCDC para extrair características fenológicas (amplitude, fase) de bandas NIR, SWIR, red-edge e índices EVI e NDFI.
- Integração de dados ópticos (Sentinel-2) e radar (Sentinel-1) com múltiplos índices de vegetação.
- Classificador Random Forest com 40–100 árvores.
- Coleta colaborativa de amostras via CEO combinando interpretação visual com análise de séries temporais.
- Uso da plataforma SEPAL para processamento em nuvem sem necessidade de habilidades de programação.

### 4.5 Web portal
O Bamboo Extent Explorer permite visualizar mapas de distribuição de bambu para 2024, acessar imagens Sentinel-2 e dados ESRI de cobertura da terra, gerar estatísticas por região/província/distrito e fornecer feedback dos usuários.

---

## 🔬 Metodologia (Seção 5)

### 5.1 Dados de entrada
| Tipo de dado | Fonte | Período |
|---|---|---|
| Imagens ópticas | Sentinel-2 (10 m) | 2022 – ago/2024 |
| Imagens de radar | Sentinel-1 (VH, VV) | 2022 – ago/2024 |
| Elevação | SRTM (30 m) | — |
| Altura de dossel | Lang et al. (2023) | 2020 |
| Dados de referência | CEO + NFI (Myanmar, Bangladesh) | 2024 |

### 5.2 Fluxo metodológico
1. Definição da área de estudo e coleta de dados de referência
2. Processamento de imagens no SEPAL (pré-processamento, correções, cálculo de índices)
3. Aplicação do algoritmo CCDC para extração de séries temporais e características fenológicas
4. Classificação por Random Forest com otimização de hiperparâmetros (40–100 árvores)
5. Estimativa de área e validação de acurácia (matriz de confusão, 70% treino / 30% validação)
6. Mapeamento final de distribuição de bambu

### 5.3 Índices espectrais utilizados
- NDVI (Normalized Difference Vegetation Index)
- EVI (Enhanced Vegetation Index)
- GCVI (Green Chlorophyll Vegetation Index)
- MTCI (MERIS Terrestrial Chlorophyll Index)
- NDFI (Normalized Difference Fraction Index)
- NDMI (Normalized Difference Moisture Index)
- LSWI (Land Surface Water Index)
- BI (Bamboo Index)

### 5.4 Resolução espacial
Processamento otimizado para resolução de 20 m (balanço entre viabilidade computacional e detalhamento espacial), utilizando dados originais de 10 m (Sentinel-2).

---

## 📊 Resultados / Contribuições (Seção 6)

### 6.1 Acurácia da classificação

| País | Acurácia global | Coeficiente Kappa |
|---|---|---|
| Myanmar | 94,49% | 0,88 |
| Bangladesh (Chittagong) | 95,95% | 0,89 |
| Tailândia | 91,16% | 0,81 |

### 6.2 Importância de atributos

A análise por categoria de atributos revela padrões distintos:

- **Myanmar**: Time-series (42,5%), Vegetation indices (21,3%), Topographic (7,6%), Geographical (5,7%), Texture (4,9%), Spectral (11,3%), SAR (8,0%)
- **Bangladesh**: Time-series (48,9%), Vegetation indices (16,7%), Topographic (5,3%), Geographical (4,3%), Texture (3,2%), Spectral (16,6%), SAR (5,0%)
- **Tailândia**: Time-series (38,7%), Vegetation indices (20,2%), Topographic (7,3%), Geographical (5,9%), Texture (4,2%), Spectral (15,5%), SAR (4,9%)

**Conclusão**: Atributos de séries temporais (CCDC) dominam a classificação em todas as regiões, confirmando a importância dos padrões fenológicos sazonais para distinguir bambu de outras vegetações.

### 6.3 Distribuição ecológica do bambu
- **Altitude**: 300–750 m (faixa ótima)
- **Declividade**: 8–17 graus (preferencial)
- **Precipitação**: 2.000–3.000 mm/ano (ideal)
- **Tolerância**: declividades de 17–33 graus e precipitação de 1.000–2.000 mm/ano

Bambu mostra-se resiliente em condições semiáridas, encostas íngremes e terras degradadas, funcionando como estabilizador ecológico e espécie adaptada ao clima.

### 6.4 Principais contribuições
- Primeiro mapa em larga escala de extensão de bambu no Sudeste Asiático usando sensoriamento remoto.
- Primeiro manual metodológico completo da FAO para avaliação de recursos de bambu com plataforma de acesso livre.
- Integração de processamento em nuvem (SEPAL/GEE), imagens Sentinel-1/2 e classificação Random Forest especificamente adaptada para bambu.
- Protocolo desenhado para transferência de tecnologia e capacitação de equipes nacionais em países em desenvolvimento.
- Disponibilização do Bamboo Extent Explorer como ferramenta pública interativa.
- Metodologia replicável para outros países e regiões (Lao PDR e Cambodia já indicados como próximos).

---

## ⚠️ Limitações / Críticas (Seção 7)

### 7.1 Limitações apontadas pelos próprios autores
1. **Não diferenciação entre espécies de bambu**: O método identifica presença/ausência de bambu, mas não discrimina espécies.
2. **Dependência de dados de satélite**: Dados de campo limitados — Myanmar e Bangladesh usaram poucas parcelas do NFI; Tailândia usou exclusivamente dados de treinamento derivados de satélite, introduzindo subjetividade.
3. **Variabilidade ecológica**: Resultados variam entre regiões devido a diferenças ecológicas e características específicas de espécies.
4. **Custo computacional**: Processamento de séries temporais em resolução de 10 m é computacionalmente intensivo; foi utilizado 20 m como balanço, o que pode ter reduzido a capacidade de detectar manchas pequenas de bambu.
5. **Defasagem temporal**: Dados de altura de dossel (2020) não aparecem entre os top 20 atributos, possivelmente devido ao descompasso temporal com a classificação de 2024.
6. **Possível omissão de espécies com fenólogia atípica**: Espécies com padrões fenológicos singulares podem não ter sido capturadas.
7. **Validação em campo insuficiente**: Necessidade de coleta de dados de campo direcionada para bambu e validação em maior número de zonas ecológicas.

### 7.2 Observações críticas adicionais
- O estudo concentra-se exclusivamente no Sudeste Asiático; a replicabilidade para outras regiões biogeográficas (América do Sul, África) precisa ser testada.
- A ausência de validação independente (os dados de validação são subconjunto aleatório dos dados de treinamento) limita a robustez das métricas de acurácia reportadas.
- A resolução de 20 m pode ser insuficiente para mapear bambuzais em sistemas agroflorestais fragmentados ou em pequenas propriedades.
- Não há análise de incerteza ou intervalos de confiança para as estimativas de área.

---

## 💡 Relevância para Tecnologia Takwara (Seção 8)

1. **Inventário de bambu no Brasil**: O protocolo SEPAL pode ser diretamente aplicado para mapear bambuzais nativos e cultivados em território brasileiro, gerando dados inéditos sobre distribuição e estoque de bambu — informação crítica para planejamento da cadeia produtiva.

2. **Metodologia aberta e gratuita**: A plataforma SEPAL é gratuita e processa dados em nuvem, eliminando barreiras de infraestrutura computacional para instituições brasileiras. O uso de Google Earth Engine integrado reduz custos operacionais.

3. **Potencial para Amazônia Ocidental**: O método é especialmente relevante para mapear bambuzais nativos de *Guadua* spp. na Amazônia Ocidental (Acre, Rondônia, Mato Grosso), onde o bambu nativo domina extensas áreas — estimadas em milhões de hectares — e carecem de mapeamento sistemático.

4. **Validação de campo**: O manual inclui protocolos de validação em campo que podem ser adaptados para expedições de coleta e caracterização de Bambusoideae brasileiras, especialmente para os gêneros *Guadua*, *Merostachys* e *Chusquea*.

5. **Adaptação para espécies brasileiras**: A metodologia de séries temporais CCDC com índices espectrais pode ser calibrada para espécies de bambu neotropicais, que apresentam padrões fenológicos distintos das espécies asiáticas.

6. **Ferramenta de advocacy**: Mapas de distribuição de bambu gerados com metodologia FAO têm credibilidade internacional e podem apoiar políticas públicas e pleitos de financiamento para a cadeia produtiva do bambu no Brasil.

7. **Capacitação técnica**: O SEPAL foi desenhado para não exigir habilidades avançadas de programação, permitindo que equipes técnicas brasileiras sejam capacitadas rapidamente.

8. **Extensão para Cerrado e Mata Atlântica**: Além da Amazônia, o método pode ser testado para mapear bambuzais no Cerrado (bambus herbáceos) e na Mata Atlântica (bambus lenhosos nativos).

---

## 📚 Referência ABNT

PHYO, Paing; PIAZZA, Marco; HOJAS GASCON, Lorena. **Bamboo resources assessment**: a methodological approach using SEPAL with case studies in Asia. Rome: Food and Agriculture Organization of the United Nations, 2025. 50 p. ISBN 978-92-5-140007-4. DOI: 10.4060/cd6448en.

---

## 📋 Notas Complementares

- **Revisão por pares**: Publicação técnica FAO sem revisão por pares independente explícita, mas com agradecimentos a revisores internos (Julian Fox, Till Neeff, Sven Walter, equipe SEPAL, Durai Jayaraman/INBAR).
- **Financiamento**: AIM4Forests programme, Department for Energy Security and Net Zero, Reino Unido.
- **Parcerias**: FAO em colaboração com INBAR (International Bamboo and Rattan Organisation).
- **Dados complementares**: O estudo produziu mapas e relatórios específicos por país (mencionados mas não incluídos no volume principal).
- **Próximos passos anunciados**: Expansão para Laos e Camboja.
- **Imagens de capa e contracapa**: © INBAR.

---

*Ficha gerada a partir do texto completo do relatório FAO (50 páginas) — PDF extraído via PyMuPDF. Nenhum dado inventado; todas as informações provenientes do documento original.*
