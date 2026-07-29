---
title: "Vertex AI Studio: diseño de prompts, parámetros del modelo y evaluación"
authors: ["John Mario Montoya Zapata"]
date: "2026-07-27"
tags: [GCP, GenAI, VertexAI, MLOps, Gemini]
links:
  - '[[GCP_Index]]'
  - '[[vertex_ai_studio_idea_to_app]]'
  - '[[prompt_engineering_intro]]'
  - '[[genai_arquitectura_google_cloud]]'
---
# Vertex AI Studio: diseño de prompts, parámetros del modelo y evaluación
> **Resumen en una frase**: Más allá de escribir el prompt, Vertex AI Studio permite elegir **qué modelo** usar, controlar **qué tan predecible o creativa** es su salida (temperature, Top K, Top P), y **comparar/evaluar** variantes antes de guardarlas en un repositorio de prompts listo para producción.

## 1) Analogía sencilla (Feynman): el jardín incompleto
Imagina la frase: *"El jardín estaba lleno de hermosas ___"*. El modelo calcula, para cada palabra posible, qué tan probable es que continúe la frase: *flores* (muy probable), *árboles* (probable), *hierbas* (menos probable), *bichos* (poco probable). Elegir **siempre** la palabra más probable da texto repetitivo y sesgado; elegir **al azar entre todas** puede darte "el jardín estaba lleno de hermosos libros" (sin sentido). **Temperature, Top K y Top P son los tres diales** que controlan, de formas distintas, en qué punto de ese espectro se mueve el modelo.

## 2) Diseño del prompt en la interfaz
- **System instructions** (izquierda): el contexto — equivalente al *Context* de [[vertex_ai_studio_idea_to_app]].
- **Prompt** (sección principal): la tarea o pregunta — equivalente al *Task*.
- **Gemini asistente integrado**: ayuda a redactar el prompt si no sabes por dónde empezar.
- **Datos multimodales**: se pueden incorporar documentos, imágenes y videos desde Cloud Storage, Google Drive, el computador local, una URL o un link de YouTube.
- **Examples**: se pueden añadir con el formato por defecto (input/output) o personalizarlo a pregunta/respuesta; usuarios enterprise pueden importar archivos de ejemplo con datos propios de la compañía.

### Prompt templates (variables reutilizables)
Un **prompt template** funciona como una **función en programación**, pero en lenguaje natural: defines variables reemplazables y reutilizas el mismo prompt cambiando solo los valores. Por ejemplo, un mismo template de "análisis de riesgo" puede recibir como variable *"tasa de vacancia de arriendo en Los Ángeles"* o *"tasa de criminalidad anual"* sin reescribir el prompt completo — solo cambias el argumento.

## 3) Selección de modelo
Vertex AI Studio ofrece modelos de Google y de terceros:

| Familia | Modelos | Uso típico |
|---|---|---|
| **Gemini** (propósito general) | Gemini Flash, Gemini Pro | Multimodal, uso general |
| **Modelos de especialidad** | Imagen (imágenes), Chirp (voz), Veo (video), Lyria (música) | Generación de medios específicos en "Media Studio" |
| **Terceros** | Anthropic Claude, Meta Llama, OpenAI GPT | Cuando se necesita un modelo fuera del ecosistema Google |

> La ventaja diferencial de Vertex AI Studio es el acceso nativo a los modelos de punta de Google (Gemini), aunque también permite comparar contra modelos de terceros dentro de la misma interfaz.

## 4) Parámetros del modelo

| Parámetro | Qué controla | Valor bajo | Valor alto |
|---|---|---|---|
| **Temperature** | Grado de aleatoriedad general de la salida | Rango angosto → palabras de alta probabilidad, típicas. Ideal para *question answering* y *summarization* | Rango amplio → palabras de baja probabilidad, más inusuales. Ideal para contenido creativo |
| **Top K** | El modelo elige al azar entre las **K palabras más probables** (todas con igual chance) | K pequeño → más control, pero si la distribución está muy sesgada puede dar resultados extraños (elegir "libros" con 10% de probabilidad igual que "flores" con 80%) | K grande → más variedad |
| **Top P** | El modelo muestrea del **conjunto más pequeño de palabras cuya probabilidad acumulada supera P** | P bajo → conjunto pequeño, más conservador | P alto (ej. 75%) → incluye más candidatos (en el ejemplo del jardín: *flores, árboles, hierbas*) |

> No es necesario ajustar Top K/Top P constantemente — son *fine-tuning* fino sobre el comportamiento que ya da la temperature.

## 5) Evaluación y refinamiento
- **Comparación lado a lado**: Vertex AI Studio permite comparar prompts para ver cuál produce el mejor resultado, y así entender cómo influyen distintos prompts, modelos o parámetros.
- **Ground truth**: puedes generar tus propias métricas de evaluación agregando la respuesta "ideal" (según tu conocimiento de dominio) contra la cual se comparan las respuestas del modelo.
- **Colab Enterprise**: para optimización más profunda, se pueden añadir ejemplos etiquetados en un notebook y refinar resultados ahí.
- Todo esto vive bajo el menú **Prompt management**.

## 6) Prompt management
Piensa en Prompt management como un **repositorio** para guardar y compartir prompts para uso futuro y colaboración, con herramientas de **control de versiones** y **seguridad** — análogo a un repositorio de código, pero para prompts.

## 7) Usos específicos más allá del prompt genérico
Las mismas técnicas y herramientas de Vertex AI Studio aplican a tareas especializadas: generación de streaming en tiempo real, creación de contenido multimedia, traducción de contenido, y conversión voz↔texto.

## 8) Preguntas Feynman (auto-chequeo)
1. Con el ejemplo del jardín, explica la diferencia entre Temperature, Top K y Top P sin usar la palabra "probabilidad" más de una vez por parámetro.
2. ¿Por qué Top K puede dar resultados extraños cuando la distribución de probabilidad está muy sesgada?
3. ¿Cuándo preferirías temperature baja vs. alta? Da un ejemplo de tarea para cada caso.
4. ¿Qué es un prompt template y en qué se parece a una función de programación?
5. ¿Qué rol cumple el "ground truth" en la evaluación de prompts?

## 9) Tarjetas Anki
**Q:** ¿Qué controla la temperature en un LLM?
**A:** El grado de aleatoriedad de la salida: baja = respuestas típicas/predecibles, alta = respuestas más creativas/inusuales.

**Q:** ¿Cómo funciona Top K?
**A:** El modelo elige al azar entre las K palabras más probables, dándoles a todas la misma probabilidad de selección.

**Q:** ¿Cómo funciona Top P?
**A:** El modelo muestrea del conjunto más pequeño de palabras cuya probabilidad acumulada supera P.

**Q:** ¿Qué es un prompt template en Vertex AI Studio?
**A:** Un prompt con variables reemplazables, reutilizable como una función, cambiando solo los valores de entrada.

**Q:** ¿Dónde se guardan y versionan los prompts en Vertex AI Studio?
**A:** En Prompt management.

**Q:** Nombra dos modelos de especialidad de Google para generación de medios.
**A:** Imagen (imágenes) y Veo (video) — también Chirp (voz) y Lyria (música).

## 10) Registro personal
- El ejemplo del jardín es la mejor analogía que he visto para explicar temperature/Top K/Top P sin fórmulas — la voy a reusar cuando tenga que explicarle esto a alguien de negocio.
- Conexión con mi contexto profesional: en un entorno regulado (SFC), para casos de uso donde la reproducibilidad y la trazabilidad de la respuesta importan (ej. generación de texto para reportes o comunicaciones a clientes), tiene sentido operar con **temperature baja** y documentar los parámetros usados como parte de la evidencia de control — no es solo un ajuste "creativo", es una decisión de gobierno.
- Pendiente: entender cómo estos parámetros se exponen luego vía API/SDK (Vertex AI) para cuando pase de prototipar en la consola a integrarlo en un pipeline de MLOps real.
