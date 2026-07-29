---
title: "De la idea a la app: Vertex AI Studio"
authors: ["John Mario Montoya Zapata"]
date: "2026-07-27"
tags: [GCP, GenAI, VertexAI, PromptEngineering, Gemini]
links:
  - '[[GCP_Index]]'
  - '[[genai_arquitectura_google_cloud]]'
  - '[[prompt_engineering_intro]]'
  - '[[vertex_ai_studio_parametros_modelo]]'
---
# De la idea a la app: Vertex AI Studio
> **Resumen en una frase**: **Vertex AI Studio** es la puerta de entrada de bajo código/no código a los modelos fundacionales de Google, y permite recorrer todo el ciclo **prompt → producción** (diseñar, evaluar, refinar, construir y desplegar) sin necesitar experiencia técnica profunda.

## 1) Analogía sencilla (Feynman)
Vertex AI Studio es un **taller de artesanía de última generación**: los modelos de Gen AI son la **materia prima**, tú eres el **artesano**, y el conjunto de herramientas del Studio es tu **caja de herramientas** para tallar y refinar esa materia prima hasta convertirla en una solución de IA útil — sin tener que fundir el metal tú mismo (entrenar un modelo desde cero).

## 2) Caso de uso: Cymbal Insurance
Tres personas de una aseguradora nacional, cada una con una necesidad distinta frente a Gen AI:

| Persona | Rol | Necesidad |
|---|---|---|
| **Bea** | Analista de negocio (sin background técnico) | Prototipar rápido una idea de app de Gen AI para automatizar análisis de riesgo y generación de reportes |
| **Ann** | Desarrolladora de IA | Plataforma amigable para *prompt engineering*: redactar, evaluar, refinar y gestionar prompts |
| **Ian** | Ingeniero de ML | Herramienta robusta, segura y escalable para construir pipelines que lleven prompts a producción y hagan fine-tuning de modelos |

Vertex AI Studio, Agent Builder/Gemini Enterprise y NotebookLM cubren estas tres necesidades respectivamente (ver [[genai_arquitectura_google_cloud]] para el panorama completo).

## 3) ¿Qué es Vertex AI Studio?
- Interfaz **intuitiva** entre desarrolladores y los modelos fundacionales.
- Permite construir apps de Gen AI en modo **low-code/no-code**: prototipar y probar rápido, ajustar modelos con datos propios, aumentarlos con información actualizada, y desplegar a producción con **código auto-generado**.
- El ciclo completo **prompt-to-production** incluye: **diseñar → evaluar → refinar** prompts, **construir y probar** la aplicación, y **monitorear y optimizar** el modelo en producción.

## 4) Anatomía de un prompt (Task · Context · Examples)

| Componente | ¿Obligatorio? | Qué es | Ejemplo |
|---|---|---|---|
| **Task** | ✅ Sí | La instrucción central para el modelo | *"Conduct a risk analysis for an insurance company"* |
| **Context** | Opcional | Información de fondo o instrucciones de sistema que "ponen el escenario" | *"You are a business analyst overseeing risk assessment..."* |
| **Examples** | Opcional | Demostraciones de la respuesta deseada, pasos o formatos — también llamado *few-shot prompting* | Plantilla de reporte con ejemplos previos |

> Un **task** simple puede resolverse solo con *zero-shot* (sin ejemplos). Tareas complejas se benefician de **examples** (*few-shot*). Esta terminología (Task/Context/Examples) es la que usa la interfaz de Vertex AI Studio; en [[prompt_engineering_intro]] vimos el mismo concepto con los nombres **Input** (= Task) y **Preámbulo** (= Context), y los tipos de prompt **zero-shot/one-shot/few-shot/role prompt** como formas de construir Context + Examples.

## 5) Contenido vs. estructura de un buen prompt
- **Contenido**: incluir toda la información relevante — instrucciones claras, contexto, ejemplos.
- **Estructura**: organizar esa información para que el modelo la entienda — orden, etiquetas, delimitadores.

### Ejercicio de evaluación
De estas tres opciones para pedir un análisis de riesgo:
- **A**: *"Provide a risk assessment report."* — vago, sin contexto ni ejemplos.
- **B**: *"Conduct a market risk analysis for a health insurance company in the United States."* — tiene task + algo de context, sin ejemplos.
- **C**: rol + contexto geográfico específico + tarea + pasos A/B/C + plantilla de reporte.

**C es la respuesta correcta**: incluye explícitamente los tres componentes (Task, Context, Examples), lo que guía al modelo de forma mucho más efectiva que A o B.

## 6) De la idea al prototipo
- **Help me write**: asistente de IA integrado en Vertex AI Studio que ayuda a redactar, clarificar y formatear el prompt.
- **Prompt gallery**: ejemplos filtrables por modalidad (audio, documento, texto, imagen, video), tarea (responder preguntas, clasificar, código) y feature.
- **Prompts multimodales**: se pueden incrustar documentos, PDFs, imágenes, videos y contenido de YouTube directamente en el prompt, y obtener respuestas en formatos igualmente multimodales.
- **Build with Code + Deploy as App**: con un par de clics, Vertex AI Studio genera automáticamente una **aplicación web** a partir del prompt prototipado — sin que Bea (sin background técnico) tenga que escribir código.

## 7) Preguntas Feynman (auto-chequeo)
1. ¿Cuáles son los tres componentes de la anatomía de un prompt y cuál es el único obligatorio?
2. ¿Por qué el prompt C del ejercicio es mejor que el A y el B, componente por componente?
3. ¿Cómo se relaciona el par Task/Context de Vertex AI Studio con Input/Preámbulo de [[prompt_engineering_intro]]?
4. ¿Qué necesidad distinta tiene cada una de las tres personas de Cymbal Insurance (Bea, Ann, Ian) frente a Gen AI?
5. ¿Qué hace "Deploy as App" y por qué es relevante para un usuario sin experiencia técnica?

## 8) Tarjetas Anki
**Q:** ¿Cuáles son los tres componentes de un prompt en Vertex AI Studio?
**A:** Task (obligatorio), Context (opcional), Examples (opcional).

**Q:** ¿Cómo se llama el uso de ejemplos dentro de un prompt?
**A:** Few-shot prompting.

**Q:** ¿Qué es Vertex AI Studio en una frase?
**A:** La interfaz low-code/no-code de Google Cloud para prototipar, evaluar y desplegar aplicaciones de Gen AI sobre modelos fundacionales.

**Q:** ¿Qué feature genera una app web funcional a partir de un prompt prototipado?
**A:** "Build with Code" + "Deploy as App".

**Q:** Los dos ejes de un buen prompt son...
**A:** Contenido (qué información incluye) y Estructura (cómo se organiza esa información).

## 9) Registro personal
- La distinción Task/Context/Examples es más operativa que la de Preámbulo/Input que ya tenía anotada — me sirve como checklist rápido al escribir un prompt: ¿tengo una tarea clara? ¿di contexto? ¿necesito ejemplos?
- El caso Bea/Ann/Ian es un buen recordatorio de que "prompt engineering" no es solo una habilidad de desarrollador: en mi organización, un analista de negocio también podría prototipar con Vertex AI Studio sin pasar primero por el equipo de tecnología — lo cual tiene implicaciones de gobierno que vale la pena anticipar (quién aprueba qué se despliega, con qué datos).
- Siguiente paso: profundizar en los parámetros del modelo (temperature, Top K, Top P) y cómo Vertex AI Studio los expone — ver [[vertex_ai_studio_parametros_modelo]].
