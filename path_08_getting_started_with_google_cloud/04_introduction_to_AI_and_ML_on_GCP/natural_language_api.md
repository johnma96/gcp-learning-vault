---
title: "Cloud Natural Language API: entidades, sentimiento, sintaxis y categorías"
authors: ["John Mario Montoya Zapata"]
date: "2026-08-24"
tags: [GCP, NLP, APIs, VertexAI, AI]
links:
  - '[[GCP_Index]]'
  - '[[opciones_desarrollo_ml_gcp]]'
  - '[[prompt_engineering_intro]]'
---
# Cloud Natural Language API
> **Resumen en una frase**: Es una **API preentrenada** que convierte texto sin procesar en datos estructurados mediante cinco análisis independientes —**entidades, sentimiento, sentimiento por entidad, sintaxis y categorías**— sin que tengas que entrenar, desplegar ni mantener ningún modelo.

## 1) Analogía sencilla (Feynman): cinco lectores especializados

Imagina que le entregas el mismo párrafo a cinco personas distintas y a cada una le haces **una sola pregunta**:

- Al **archivista**: *"¿de qué cosas concretas habla este texto?"* → devuelve nombres propios, lugares, fechas, organizaciones. Eso es `analyzeEntities`.
- Al **psicólogo**: *"¿el autor está contento o molesto?"* → devuelve un tono general. Eso es `analyzeSentiment`.
- Al **crítico de restaurantes**: *"¿qué opina de **cada** cosa que menciona?"* → "le encantó la comida, odió el servicio". Eso es `analyzeEntitySentiment`, y es la pregunta más útil de las tres.
- Al **profesor de gramática**: *"desarma la frase"* → sujeto, verbo, complemento, raíz de cada palabra. Eso es `analyzeSyntax`.
- Al **bibliotecario**: *"¿en qué estante va esto?"* → "Finanzas / Inversiones". Eso es `classifyText`.

La clave: **son preguntas independientes sobre el mismo texto**. Elegir el método es elegir qué pregunta hacer, no qué modelo entrenar.

## 2) Los métodos

| Método | Qué responde | Devuelve |
|---|---|---|
| `analyzeEntities` | ¿De qué cosas habla el texto? | Lista de entidades con `name`, `type`, `salience`, `mentions` y `metadata` |
| `analyzeSentiment` | ¿Cuál es el tono del documento? | `score` y `magnitude`, a nivel de documento y de cada oración |
| `analyzeEntitySentiment` | ¿Qué opina de **cada** entidad? | Entidades + `score`/`magnitude` por entidad |
| `analyzeSyntax` | ¿Cómo está construida la frase? | Oraciones y tokens con categoría gramatical, lema y árbol de dependencias |
| `classifyText` | ¿A qué categoría pertenece? | Categorías de contenido. **Requiere mínimo ~20 tokens** |
| `annotateText` | Todo lo anterior de una vez | Combina los análisis solicitados en **una sola** llamada |

> `annotateText` es la que conviene cuando necesitas más de un análisis: una llamada en vez de tres, con el ahorro de latencia y cuota que eso implica.

## 3) Sentimiento: `score` y `magnitude` (el punto que se presta a error)

| Campo | Rango | Qué mide |
|---|---|---|
| **`score`** | **−1.0 a 1.0** | La **dirección** del sentimiento: negativo ↔ positivo |
| **`magnitude`** | **0.0 a +∞** | La **intensidad** emocional acumulada. **No está normalizado**: crece con la longitud del texto |

La trampa está en leer solo el `score`. Un texto largo con elogios furiosos y quejas furiosas se **cancela** y da un `score` cercano a 0 — igual que un texto plano y aburrido. Lo que los distingue es la `magnitude`: alta en el primero, baja en el segundo.

Regla práctica: **`score` ≈ 0 con `magnitude` alta significa "mixto", no "neutral"**. Y como `magnitude` no está normalizada, no compares directamente la de un tuit contra la de un informe: normalízala por longitud o compara documentos de tamaño similar.

Es exactamente el caso donde `analyzeEntitySentiment` resuelve mejor: en vez de un promedio que se anula, te dice *hacia qué* es positivo y *hacia qué* es negativo.

## 4) Entidades: los campos que importan

| Campo | Qué es |
|---|---|
| `name` | Nombre representativo de la entidad |
| `type` | Categoría: `PERSON`, `LOCATION`, `ORGANIZATION`, `ADDRESS`, `DATE`, `NUMBER`, entre otras |
| `salience` | **Importancia relativa dentro del documento**, en el rango (0, 1.0]. Más alto = más central al texto |
| `mentions` | Dónde aparece la entidad, con el tipo de mención: `PROPER` (nombre propio) o `COMMON` (sustantivo común) |
| `metadata` | Información adicional según el tipo (una `ADDRESS` trae `street_name`, `locality`, `country`) |

`salience` es el campo más subestimado: permite **ordenar** las entidades por relevancia en vez de tratarlas todas por igual, que es lo que se necesita para extraer los temas principales de un documento largo.

## 5) Sintaxis: para qué sirve realmente

`analyzeSyntax` descompone el texto en oraciones y tokens, y por cada token devuelve su **categoría gramatical**, su **lema** (la raíz: "corriendo" → "correr") y su lugar en el **árbol de dependencias**.

No es un análisis que se consuma directamente en negocio; es **materia prima**. Sirve para normalizar texto antes de indexarlo, para extraer pares sujeto-verbo-objeto, o para quedarse solo con sustantivos y adjetivos al construir atributos de un modelo posterior.

## 6) Cómo encaja con el resto

Esta API es un caso concreto de la primera columna de [[opciones_desarrollo_ml_gcp]]: **API preentrenada**, sin datos de entrenamiento, sin ajuste de hiperparámetros, sin tiempo de entrenamiento. La contrapartida es que no puedes adaptarla a tu dominio: si tu texto tiene jerga muy específica y la API no reconoce tus entidades, la salida no mejora por más datos que tengas — ahí toca subir un escalón hacia AutoML o entrenamiento personalizado.

También conviene tenerla presente frente a Gemini. Muchas de estas tareas hoy se pueden resolver con un prompt (ver [[prompt_engineering_intro]]), y de hecho Google está absorbiendo varias APIs especializadas dentro de las de Gemini. La diferencia sigue siendo relevante: la Natural Language API devuelve **salida estructurada y determinista** con campos fijos, mientras que un LLM devuelve texto que hay que forzar a un esquema y validar.

## 7) Preguntas Feynman (auto-chequeo)

1. Un texto tiene `score = 0.1` y `magnitude = 8.4`. ¿Qué está pasando y por qué no es lo mismo que `score = 0.1` con `magnitude = 0.3`?
2. ¿Por qué `analyzeEntitySentiment` resuelve un problema que `analyzeSentiment` no puede?
3. ¿Qué significa `salience` y para qué la usarías en un documento largo?
4. Necesitas entidades **y** sentimiento **y** sintaxis del mismo texto. ¿Cuántas llamadas haces y con qué método?
5. ¿En qué caso esta API deja de servirte y tienes que subir a AutoML o a entrenamiento personalizado?
6. ¿Qué le pedirías a `analyzeSyntax` si tu objetivo final es construir atributos para un modelo de clasificación?

## 8) Tarjetas Anki

**Q:** ¿Qué rango tiene el `score` de sentimiento en la Natural Language API y qué mide?
**A:** De **−1.0 a 1.0**; mide la **dirección** del sentimiento (negativo ↔ positivo).

**Q:** ¿Qué rango tiene la `magnitude` de sentimiento y qué mide?
**A:** De **0.0 a infinito**, **sin normalizar**; mide la **intensidad** emocional acumulada, así que crece con la longitud del texto.

**Q:** ¿`score` cercano a 0 con `magnitude` alta?
**A:** Texto **mixto** (fuertes emociones opuestas que se cancelan), no neutral. Un texto realmente neutral tendría magnitude baja.

**Q:** ¿Necesitas saber qué opina el autor sobre **cada** cosa que menciona, no el tono global?
**A:** `analyzeEntitySentiment`.

**Q:** ¿Necesitas entidades, sentimiento y sintaxis del mismo texto en una sola llamada?
**A:** `annotateText`.

**Q:** ¿Qué es `salience` en una entidad y en qué rango está?
**A:** La **importancia relativa de la entidad dentro del documento**, en el rango (0, 1.0]. Sirve para ordenar entidades por relevancia.

**Q:** ¿Qué distingue una mención `PROPER` de una `COMMON`?
**A:** `PROPER` es un nombre propio (una persona o lugar específico); `COMMON` es un sustantivo común (la categoría general).

**Q:** ¿Qué devuelve `analyzeSyntax` por cada token?
**A:** Categoría gramatical, **lema** (raíz de la palabra) y su posición en el **árbol de dependencias**.

**Q:** ¿Qué método clasifica el texto en categorías de contenido y qué restricción tiene?
**A:** `classifyText`; requiere un mínimo de **~20 tokens** para funcionar.

**Q:** ¿Cuándo prefieres la Natural Language API sobre un prompt a Gemini?
**A:** Cuando necesitas **salida estructurada y determinista** con campos fijos (`score`, `salience`, `type`) en vez de texto que hay que forzar a un esquema y validar.

## 9) Registro personal

- El par `score`/`magnitude` es el tipo de detalle que uno cree entender al leerlo y falla al aplicarlo. Me obligo a recordarlo así: **`score` es la dirección, `magnitude` es el volumen**. Un grito de alegría y un grito de rabia en el mismo párrafo dan dirección cero y volumen alto.
- Viniendo de spaCy y NLTK, lo que cambia aquí no es la capacidad sino el modelo operativo: no hay modelo que versionar, ni pipeline que reentrenar, ni tamaño de vocabulario que gestionar. A cambio, no hay forma de adaptarlo a jerga de dominio — y en pensiones y cesantías la jerga es la mitad del texto.
- Conexión con mi contexto: para analizar texto de PQRS o encuestas de afiliados, esta API es la vía más rápida a un piloto. Pero **enviar texto de clientes a una API implica una decisión de tratamiento de datos personales**, no solo una técnica: hay que revisar residencia del dato, retención y finalidad antes de mandar el primer lote. Para el piloto, texto anonimizado o de prueba. Esto es orientativo y debe validarse con las áreas jurídica y de cumplimiento.
- `salience` me parece el campo con más valor práctico inmediato y el que menos aparece en los tutoriales: es lo que convierte una lista plana de entidades en un ranking de temas.
