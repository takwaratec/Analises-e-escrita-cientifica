# 📚 Acervo Soberania Tecnológica

> *"Ninguém educa ninguém, ninguém se educa sozinho. Os homens se educam em comunhão."* — Paulo Freire

---

## 🌱 O que é este acervo

Este repositório é um **acervo científico aberto** de Tecnologias de Baixo Carbono, organizado por **Fabio Takwara** com curadoria documental inspirada no método **Dra. Nathalia Cavichiolli** (8 seções). São **695 fichas técnicas** cobrindo polímeros vegetais, bambu estrutural, habitação social, certificações e perfis de pesquisadores.

**Público-alvo:** Pesquisadores cidadãos, autodidatas, extensionistas universitários, movimentos sociais e qualquer pessoa interessada em construir conhecimento com autonomia.

---

## 🗂️ Estrutura

```
📂 acervo-soberania-tecnologica/
│
├── 📂 01_polimeros-vegetais-e-biocompositos/   ← 421 fichas (POL_)
│   │   Biocompósitos, PU Vegetal, Imperveg, MQTF
│   └── 📷 evidencias/
│
├── 📂 02_bambu-estrutural-e-tratamentos/        ← 119 fichas (BAM_)
│   │   Bambu, pirolenhoso, tratamento ecológico
│   └── 📷 evidencias/
│
├── 📂 03_habitacao-social-e-athis/              ← 65 fichas (SOC_)
│   │   HIS, ATHIS, ECOSALA, UnB/IFB
│   └── 📷 evidencias/
│
├── 📂 04_certificacoes-e-normas/                ← 21 fichas (CER_)
│   │   ITecons, IPT, NBR, ABNT
│   └── 📷 evidencias/
│
├── 📂 05_perfis-e-referencias/                  ← 69 fichas (PER_)
│   │   Pesquisadores, literatura, referências
│   └── 📷 evidencias/
│
├── 📂 .agent-instructions/                       ← Prompts prontos
│   ├── prompt-pesquisa-acervo.json
│   ├── prompt-esteira-ingestao.md
│   └── chromadb-schema.json
│
└── 📄 README.md                                  ← Você está aqui
```

---

## 🔍 Como usar

### Pelo GitHub (mais simples)
Navegue pelas pastas e abra os arquivos `.md`. Cada ficha tem 8 seções padronizadas.

### Pelo ChromaDB (busca semântica)
```python
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="~/.chromadb")
model = SentenceTransformer('all-MiniLM-L6-v2')
collection = client.get_collection("acervo_cientifico")

query = "poliuretano vegetal bambu tratamento"
results = collection.query(
    query_embeddings=model.encode(query).tolist(),
    n_results=5
)
```

### Pelo .agent-instructions/
Copie o prompt em `prompt-pesquisa-acervo.json` para seu agente de IA favorito (GPT, Gemini, Claude) e faça perguntas sobre o acervo.

---

## 📊 Estatísticas

| Área | Fichas | Prefixo |
|------|:------:|:-------:|
| Polímeros Vegetais e Biocompósitos | 421 | POL_ |
| Bambu Estrutural e Tratamentos | 119 | BAM_ |
| Habitação Social e ATHIS | 65 | SOC_ |
| Certificações e Normas | 21 | CER_ |
| Perfis e Referências | 69 | PER_ |
| **Total** | **695** | |

---

## ⚖️ Direitos e Uso

- **Conteúdo original** de terceiros: protegido por direitos autorais. As fichas são resenhas técnicas (uso justo), não substituem os originais.
- **Conteúdo de autoria de Fabio Takwara:** CC BY 4.0, salvo indicação contrária.
- **Método Cavichiolli:** Metodologia documental de autoria da **Dra. Nathalia Cavichiolli** (https://www.doutoranathalia.com.br/). O acervo original é comercializado por ela. Este repositório não distribui ou copia o produto original.

---

## 🤝 Como contribuir

1. Abra uma issue com sugestão de ficha ou correção
2. Envie um pull request com novas fichas no formato Cavichiolli (8 seções)
3. Compartilhe o acervo com quem possa se beneficiar

---

*Acervo mantido por Fabio Takwara · Tecnologia Takwara · 2026*
