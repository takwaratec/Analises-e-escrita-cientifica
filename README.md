# 📚 Acervo Soberania Tecnológica

> *"Ninguém educa ninguém, ninguém se educa sozinho. Os homens se educam em comunhão."* — Paulo Freire

---

## 🌱 O que é este acervo

Este repositório é um **acervo científico aberto** de Tecnologias de Baixo Carbono, organizado por **Fabio Takwara** com curadoria documental inspirada no método **Dra. Nathalia Cavichiolli** (8 seções). São **594 fichas técnicas** cobrindo polímeros vegetais, bambu estrutural, habitação social, certificações e perfis de pesquisadores.

**Público-alvo:** Pesquisadores cidadãos, autodidatas, extensionistas universitários, movimentos sociais e qualquer pessoa interessada em construir conhecimento com autonomia.

---

## 🗂️ Estrutura

```
📂 acervo-soberania-tecnologica/
│
├── 📂 01_polimeros-vegetais-e-biocompositos/   ← 330 fichas (POL_)
│   │   Biocompósitos, PU Vegetal, Imperveg, MQTF
│   └── 📷 evidencias/
│
├── 📂 02_bambu-estrutural-e-tratamentos/        ← 112 fichas (BAM_)
│   │   Bambu, pirolenhoso, tratamento ecológico
│   └── 📷 evidencias/
│
├── 📂 03_habitacao-social-e-athis/              ← 64 fichas (SOC_)
│   │   HIS, ATHIS, ECOSALA, UnB/IFB
│   └── 📷 evidencias/
│
├── 📂 04_certificacoes-e-normas/                ← 21 fichas (CER_)
│   │   ITecons, IPT, NBR, ABNT
│   └── 📷 evidencias/
│
├── 📂 05_perfis-e-referencias/                  ← 67 fichas (PER_)
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

### Pelo ChromaDB (busca semântica — para quem usa Python)

O acervo está indexado em um banco vetorial local que permite **buscar por significado**, não apenas por palavras. Exemplo: se você pesquisar "poliuretano vegetal bambu tratamento", ele encontra fichas sobre PU de mamona, impermeabilização de colmos e tratamentos ecológicos — mesmo que os termos exatos não estejam no título.

**Para usar, abra o terminal Python e rode:**

```python
# 1. Conectar ao banco
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="~/.chromadb")
model = SentenceTransformer('all-MiniLM-L6-v2')
collection = client.get_collection("acervo_cientifico")

# 2. Fazer uma pergunta em linguagem natural
query = "poliuretano vegetal bambu tratamento"

# 3. Buscar os resultados mais relevantes
results = collection.query(
    query_embeddings=model.encode(query).tolist(),
    n_results=5  # quantidade de fichas retornadas
)

# 4. Ver os resultados
for i, (meta, dist) in enumerate(zip(results['metadatas'][0], results['distances'][0])):
    print(f"{i+1}. [{meta['aba_title'][:40]}] {meta['arquivo']} (relevância: {1-dist:.2%})")
```

> 💡 **Dica:** Quanto menor a distância (dist), mais relevante é o resultado. Acima de 70% já é uma boa correspondência.

### Pelo .agent-instructions/ (para qualquer pessoa, sem Python)

Na pasta `.agent-instructions/` você encontra prompts prontos para copiar e colar no **GPT, Gemini, Claude** ou qualquer outro assistente de IA. Basta:

1. Abrir o arquivo [`prompt-pesquisa-acervo.json`](.agent-instructions/prompt-pesquisa-acervo.json)
2. Copiar o conteúdo
3. Colar no seu agente de IA favorito
4. Fazer perguntas sobre o acervo em linguagem natural

**Exemplos de perguntas que funcionam bem:**
- "O que o acervo tem sobre tratamento de bambu com pirolenhoso?"
- "Quais fichas tratam de PU vegetal da Imperveg?"
- "Me mostre os perfis de pesquisadores do IFB"
- "Existe material sobre certificação LEED para habitação social?"

---

## 📊 Estatísticas

| Área | Fichas | Prefixo |
|------|:------:|:-------:|
| Polímeros Vegetais e Biocompósitos | 330 | POL_ |
| Bambu Estrutural e Tratamentos | 112 | BAM_ |
| Habitação Social e ATHIS | 64 | SOC_ |
| Certificações e Normas | 21 | CER_ |
| Perfis e Referências | 67 | PER_ |
| **Total** | **594** | |

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
