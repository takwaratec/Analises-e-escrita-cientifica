---
tipo: Auditoria de Proveniência
projeto: Tecnologia Takwara / Acervo Científico
data: 27/06/2026
autor: Hermes Agent (revisão solicitada por Fabio Takwara)
classificacao: Auditoria Interna
---

# Auditoria de Proveniência, Autoria e Veracidade — Documentos de Advocacy do Acervo

> **Contexto**: Em 27/06/2026, a ficha `ficha-casa-floresta-cop30.md` foi identificada como portadora de erros graves de autoria e classificação. A correção exigiu 4 versões e revelou fragilidades no processo de catalogação de documentos de advocacy do ecossistema Takwara. Esta auditoria sistematiza as lições e padroniza a verificação.

## 1. O Caso-Cabeça: Lições da Ficha Casa da Floresta COP30

| Erro cometido | Causa | Correção aplicada |
|---|---|---|
| Atribuição de autoria a terceiros (arquiteta UNESP) sem verificação | Documento extraído do Takwara-Tech, autoria presumida pelo contexto | Autoria corrigida: Fabio Takwara |
| Tratamento de advocacy como fato consumado ("projeto real") | Texto irônico/sátira técnica interpretado como documental | Reclassificado como "Estudo de Caso" com evidências primárias |
| Dados não verificados externamente (inauguração, parceiros, programação) | Conteúdo extraído sem checagem | Verificação externa via Jornal da Unesp + Portal UNESP Proec |
| Ausência de distinção entre "documento fonte" e "documento analisado" | Fusão acrítica entre o texto original e a análise | Separação clara: seção 1 (projeto real) vs. seção 2 (texto de advocacy) |

## 2. Critérios de Verificação — Padronizados

A partir deste caso, todo documento do acervo deve ser verificado contra:

### 2.1 Autoria

| Critério | Regra |
|---|---|
| Documentos sem autor explícito no YAML | **Não publicar** — consultar Fabio Takwara |
| Documentos do repositório Takwara-Tech | **Autoria: Fabio Takwara** salvo indicação em contrário |
| Citações textuais de terceiros | **NUNCA atribuir** sem transcrição verificada ou fonte original |
| Documentos de advocacy/ironia/sátira | **Explicitar a natureza** no campo `tipo:`

### 2.2 Fonte

| Origem do dado | Tratamento |
|---|---|
| Takwara-Tech (acervo próprio) | Síntese Técnica — **NÃO** é fonte terceira independente |
| Artigo com DOI | Fonte verificável — citar DOI completo |
| Chat/WhatsApp | Evidência primária — anexar transcrição; citar linha e data |
| Relato pessoal | Identificar como "Relato de Fabio Takwara" — **não** tratar como fato verificado externamente |

### 2.3 Natureza do documento

| Natureza | Classificação `tipo:` |
|---|---|
| Análise de artigo com DOI | `Ficha Científica` |
| Compilação do acervo Takwara-Tech | `Síntese Técnica` |
| Denúncia / Advocacy | `Documento de Advocacy` ou `Estudo de Caso` |
| Perfil de pesquisador | `Perfil de Pesquisador` |
| Texto irônico / sátira técnica | `Sátira Técnica — Documento de Advocacy` |

## 3. Documentos Auditados

### 3.1 Documentos de Advocacy e Política Pública

| Arquivo | Autoria | Fontes | Veracidade | Ação |
|---|---|---|---|---|
| `ficha-casa-floresta-cop30.md` | Fabio Takwara ✅ | Takwara-Tech + Jornal Unesp + Chat WhatsApp | ✅ Corrigida (4 versões) | Finalizada |
| `ficha-analise-cop30.md` | Fabio Takwara ✅ | Takwara-Tech + DOI externo | ✅ Autoria corrigida | OK |
| `ficha-dossie-cop30.md` | Fabio Takwara ✅ | Takwara-Tech | ⚠️ Depende de checagem externa parcial | Autoria corrigida |
| `ficha-floresta-em-pe.md` | Fabio Takwara ✅ | Takwara-Tech + Medium | ✅ Autoria corrigida | OK |
| `ficha-decreto-presidencial-bambu.md` | Fabio Takwara ✅ | Documentos legislativos públicos | ✅ Autoria corrigida | OK |
| `resenha-ultimato-climatico.md` | Fabio Takwara ✅ | Relatório externo + análise | ✅ Autoria presente | OK |

### 3.2 Sínteses Técnicas (anteriormente sem YAML)

| Arquivo | Ação realizada |
|---|---|
| `ficha-critica-tratamento-quimico-bambu.md` | YAML adicionado + autoria Fabio Takwara |
| `ficha-carbono-bambu.md` | YAML adicionado + classificação "Síntese Técnica" |
| `ficha-domos-geodesicos.md` | YAML adicionado + classificação "Síntese Técnica" |
| `ficha-forno-ecologico-multifuncional.md` | YAML adicionado + classificação "Síntese Técnica" |
| `ficha-reforco-interno-bambu-pu.md` | YAML adicionado + classificação "Síntese Técnica" |
| `ficha-paineis-bambu.md` | YAML adicionado + classificação "Síntese Técnica" |

## 4. Regras para Futuras Catalogações

1. **NUNCA atribuir autoria a terceiros** sem confirmar com Fabio Takwara
2. Documentos do acervo Takwara-Tech sem autoria declarada = **Fabio Takwara** até prova em contrário
3. **Sempre verificar a natureza do documento fonte**: é paper publicado? É advocacy? É ironia/sátira? É relato pessoal?
4. **Diferenciar claramente** na ficha: (a) o documento fonte; (b) os fatos verificados externamente; (c) a análise do autor
5. **Sempre que uma ficha citar "Takwara-Tech" como fonte**, marcar como `Síntese Técnica` no YAML e incluir `autor: Fabio Takwara`
6. Documentos de denúncia/advocacy devem ter no YAML o campo `classificacao_atualizada` alertando que **não são artigos revisados por pares**

---

*Auditoria gerada em 27/06/2026 · Hermes Agent · Tecnologia Takwara*
