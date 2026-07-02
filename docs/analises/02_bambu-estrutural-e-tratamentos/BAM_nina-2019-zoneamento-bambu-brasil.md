# Zoneamento Edafoclimático para *Bambusa vulgaris* e *Dendrocalamus giganteus* no Brasil

> Ficha Cavitioli — elaborada a partir do texto completo do artigo (10 p., ~40 mil caracteres). Fonte primária: PDF original (DOI 10.1590/1983-40632019v4953713).

---

## ① Referência (ABNT)

SANTOS, Karina Rodrigues; POMPEU, Patrícia Vieira; MELO, Lucas Amaral de; MACEDO, Renato Luiz Grisi; BOTELHO, Soraya Alvarenga. Zoning for edaphoclimatic aptitude of *Bambusa vulgaris* and *Dendrocalamus giganteus* in Brazil. **Pesquisa Agropecuária Tropical**, Goiânia, v. 49, e53713, 2019. DOI: [10.1590/1983-40632019v4953713](https://doi.org/10.1590/1983-40632019v4953713).

---

## ② Objetivo

Prever áreas favoráveis ao melhor estabelecimento e desenvolvimento de *Bambusa vulgaris* e *Dendrocalamus giganteus* no território brasileiro, funcionando como um zoneamento de aptidão edafoclimática que possa subsidiar a tomada de decisões para o cultivo comercial dessas espécies.

---

## ③ Metodologia

**Abordagem:** Modelagem de distribuição de espécies (SDM) por máxima entropia (MaxEnt), combinando pontos de ocorrência georreferenciados com variáveis ambientais preditoras.

**Dados de ocorrência:**
- Coletados no *Global Biodiversity Information Facility* (GBIF) — herbário virtual.
- Após filtragem (exclusão de dados imprecisos ou duvidosos): **17 pontos** para *B. vulgaris* e **12 pontos** para *D. giganteus*, localizados no sul da Ásia e Oceania.
- Números considerados satisfatórios conforme Wisz et al. (2008), que indica bons resultados com MaxEnt a partir de apenas 10 pontos.

**Variáveis ambientais:**
- **WorldClim v1.4** (1950–2000): 19 camadas climáticas (precipitação e temperatura), resolução ~5 km.
- **SoilGrids**: classificação de solos com base na Base de Referência Mundial da FAO, resolução 1 km.
- **MOD16** (NASA): evapotranspiração potencial (PET) e real (AET), resolução 1 km.
- **Déficit hídrico (WD)**: calculado como WD = PET − AET (Pereira et al. 2002).
- Todas as camadas reamostradas para resolução uniforme de 2,5 arc-min (~5 km).

**Seleção de variáveis:**
1. Três variáveis primárias definidas *a priori*: BIO1 (temperatura média anual), BIO12 (precipitação anual) e déficit hídrico.
2. Teste de correlação de Pearson (|r| ≥ 0,8) entre todas as variáveis nos pontos de ocorrência para eliminar colinearidade.
3. Variáveis não correlacionadas selecionadas separadamente para cada espécie.

**Variáveis finais usadas na modelagem:**

| Espécie | Variáveis |
|---|---|
| *B. vulgaris* | BIO1, BIO12, WD (primárias) + BIO2, BIO3, BIO10, BIO16, BIO17, BIO18, SC (solo) |
| *D. giganteus* | BIO1, BIO12, WD (primárias) + BIO2, BIO3, BIO7, BIO17, BIO18, BIO19, SC (solo) |

- **Análise de Componentes Principais (PCA)**: aplicada para selecionar as variáveis que mais explicam a variabilidade do conjunto de dados multidimensionais.
- **Algoritmo**: MaxEnt v3.4.0 (Phillips et al. 2017), com validação cruzada (*cross-validation*) e 10 réplicas.
- **Métricas de avaliação**: AUC (*Area Under the Curve*) e TSS (*True Skill Statistic*). Modelos considerados bem-sucedidos com AUC > 0,8 e TSS > 0,6 (Gallien et al. 2012).
- **Mapa binário**: gerado no ArcMap 10.3 com limiar logístico de *minimum training presence*, subdividindo áreas aptas em taxas de aptidão.

---

## ④ Resultados

### *Bambusa vulgaris*
- **AUC = 0,92; TSS = 0,68** — desempenho muito bom.
- Área com aptidão ≥ 0,76 (76 %): **≈ 600.000 km²** — equivalente a 10 vezes a área de floresta plantada no Brasil (IBÁ 2017).
- **Distribuição**: concentrada na região Norte (bioma Amazônia), estendendo-se ao longo da costa, com destaque para Bahia e São Paulo (Mata Atlântica).
- **Climas favoráveis**: tropical sem estação seca (Af) — Köppen; secundariamente Aw, Am, Cfa e Cfb.
- **Variáveis mais influentes**: precipitação anual (25,91 %), amplitude diurna média (12,96 %), precipitação do trimestre mais quente (11,94 %) e temperatura média do trimestre mais quente (10,95 %).
- **Curvas de resposta**: aptidão aumenta exponencialmente com precipitação anual até ~3.000 mm, estabilizando; melhor aptidão em temperaturas do trimestre quente próximas a 38 °C.

### *Dendrocalamus giganteus*
- **AUC = 0,94; TSS = 0,83** — desempenho excelente.
- Área com aptidão ≥ 0,76: **≈ 20.000 km²** — área muito mais restrita.
- **Distribuição**: concentrada na costa da região Sudeste, principalmente nordeste de São Paulo e grande parte do Rio de Janeiro.
- **Climas favoráveis**: tropical com inverno seco (Aw) e temperado úmido com inverno seco e verão quente (Cwb) — Köppen.
- **Variáveis mais influentes**: precipitação do trimestre mais frio (23,20 %), precipitação do trimestre mais seco (19,84 %), amplitude diurna média (16,55 %) e déficit hídrico (14,46 %).
- **Curvas de resposta**: melhor aptidão em áreas com menor precipitação nos períodos frio e seco; amplitude diurna ótima entre 2–5 °C; suporta déficit hídrico até ~350 mm, com ótimo próximo a 100 mm.

---

## ⑤ Conclusões dos Autores

1. *Bambusa vulgaris* apresenta maiores áreas de aptidão para cultivo no território brasileiro em relação a *Dendrocalamus giganteus*, sendo mais adequada para as regiões Norte, Nordeste e litorâneas.
2. Para a região Centro-Oeste e áreas de Cerrado, ambas as espécies mostram baixa aptidão, sendo necessário monitoramento do crescimento antes de investimentos comerciais.
3. *B. vulgaris* é mais apta em regiões com altos valores de precipitação e temperatura, enquanto *D. giganteus* desenvolve-se melhor em regiões com estação seca.

---

## ⑥ Contribuições / Observações Críticas

**Contribuições originais:**
- Primeiro zoneamento edafoclimático simultâneo para *B. vulgaris* e *D. giganteus* em escala nacional brasileira utilizando modelagem de nicho (MaxEnt + PCA).
- Identificação das variáveis ambientais mais influentes para cada espécie, permitindo refinamento de modelos futuros.
- Mapas de aptidão disponíveis para integração com SIG — suporte a políticas públicas de fomento ao bambu.
- Demonstração de que a área apta para *B. vulgaris* (600.000 km²) é 30 vezes maior que a de *D. giganteus* (20.000 km²), indicando espécies com perfis ecológicos distintos.

**Limitações apontadas pelos autores:**
- Base de dados com poucos pontos georreferenciados (17 e 12), o que pode subestimar áreas potencialmente aptas.
- Modelagem baseada apenas em dados ambientais; não considera barreiras geográficas, competição ou dispersão.
- Espécies exóticas podem ter nicho fundamental diferente do observado em sua área nativa.
- Estudos prévios sobre a adaptação climática dessas espécies são escassos ou superficiais, dificultando a discussão comparativa.

**Relevância para Tecnologia Takwara:**
- As duas espécies estudadas são as mais utilizadas em sistemas construtivos com bambu no Brasil.
- O zoneamento permite identificar regiões prioritárias para implantação de bambuzais.
- A metodologia (MaxEnt + variáveis ambientais globais) é replicável para outras espécies de interesse (*Guadua*, *Phyllostachys*).
- O déficit hídrico mostrou-se variável crítica para *D. giganteus* — relevante para irrigação e manejo.

---

## ⑦ Palavras-chave

*Species distribution modeling*; bambu; *Bambusa vulgaris*; *Dendrocalamus giganteus*; zoneamento edafoclimático; MaxEnt; georreferenciamento; modelagem de nicho.

---

## ⑧ Dados do Artigo

| Campo | Informação |
|---|---|
| **Título original** | Zoning for edaphoclimatic aptitude of *Bambusa vulgaris* and *Dendrocalamus giganteus* in Brazil |
| **Título em português** | Zoneamento de aptidão edafoclimática de *Bambusa vulgaris* e *Dendrocalamus giganteus* para o Brasil |
| **Autores** | Karina Rodrigues Santos, Patrícia Vieira Pompeu, Lucas Amaral de Melo, Renato Luiz Grisi Macedo, Soraya Alvarenga Botelho |
| **Instituições** | UFLA (Departamento de Ciências Florestais) / UEMS (Aquidauana, MS) |
| **Periódico** | Pesquisa Agropecuária Tropical (PAT), v. 49, e53713 |
| **Ano** | 2019 |
| **DOI** | [10.1590/1983-40632019v4953713](https://doi.org/10.1590/1983-40632019v4953713) |
| **Recebido / Aceito / Publicado** | 27 jun. 2018 / 18 set. 2018 / 04 abr. 2019 |
| **Páginas** | 10 |
| **Idioma** | Inglês (com resumo em português) |
| **Palavras-chave (artigo)** | Species distribution modeling, bamboo, georeferencing |
| **Fomento** | Fapemig, CNPq |

---

*Ficha gerada em 29 jun. 2026 a partir da extração integral do PDF original. Nenhum dado foi inventado — todas as informações foram extraídas do artigo publicado.*
