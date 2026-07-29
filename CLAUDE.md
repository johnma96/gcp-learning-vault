# CLAUDE.md

Guía de contexto para Claude Code (u otro asistente) al trabajar en este repositorio.

## Qué es este repositorio

Este es el **vault de estudio personal de John Mario Montoya Zapata** sobre Google Cloud Platform, estructurado como una bóveda de **Obsidian** (ver `.obsidian/`). No es un proyecto de software: es un espacio de aprendizaje activo cuyo objetivo es certificarse oficialmente como **Google Cloud Professional Machine Learning Engineer** antes de que termine el año.

El repositorio aloja **todas** las rutas de aprendizaje (learning paths) de [Google Skills](https://www.skills.google/) que el usuario vaya cursando, no solo una. Cada ruta es una carpeta de nivel superior con el patrón `path_XX_nombre_de_la_ruta/`, y dentro de ella cada curso de esa ruta vive en su propia carpeta numerada:

| Carpeta de ruta | Ruta de Google Skills | Cursos dentro |
|---|---|---|
| `path_08_getting_started_with_google_cloud/` | Getting Started with Google Cloud | `01_load_balancing_on_compute_engine`, `02_prepare_data_for_ml_apis_on_gcp`, `03_google_cloud_fundamentals_core_infrastructure`, `04_introduction_to_AI_and_ML_on_GCP` |

Los cursos 01, 02 y 03 ya están desarrollados con notas Feynman. El curso 04 está **en progreso**: contiene también transcripciones crudas de lecciones (archivos `.md` sin frontmatter, texto con timestamps) pendientes de convertir a notas.

**Cursos y laboratorios compartidos entre rutas**: Google Skills reutiliza el mismo curso o laboratorio en varias rutas distintas. Cuando el usuario empiece una ruta nueva (ej. `path_17_professional_ml_engineer`) y se tope con un curso que ya vive en otra carpeta de ruta (ej. dentro de `path_08_...`), **no dupliques la nota** — crea una referencia corta (o una entrada en `GCP_Index.md`) que enlace al curso ya documentado, indicando en qué otra ruta se cursó primero. Antes de crear una carpeta de ruta nueva, pregúntale al usuario el número/nombre exacto de la ruta tal como aparece en Google Skills — no lo infieras de documentación externa, ya que el catálogo de rutas cambia con frecuencia y el usuario tiene la fuente de verdad (lo que ve en la plataforma).

El archivo [`GCP_Index.md`](GCP_Index.md) es el **mapa maestro (MOC)** del vault: conecta todas las notas entre sí y con los módulos del curso, y alimenta el grafo de Obsidian. Es el punto de entrada obligatorio para entender cómo se relacionan los conceptos ya vistos.

## Cómo debe trabajar el asistente aquí

- **Este no es un repo de código productivo.** No apliques aquí instintos de ingeniería de software (no propongas CI/CD, linters, tests, `package.json`, etc.) a menos que el usuario lo pida explícitamente para una herramienta puntual.
- **Idioma**: todas las notas y toda la comunicación son en **español**.
- **Metodología de notas**: toda nota nueva de contenido de GCP se crea siguiendo la técnica Feynman (analogía simple, preguntas de auto-chequeo, tarjetas Anki, registro personal). El procedimiento exacto — estructura, frontmatter, checklist — está codificado en la skill **`gcp-feynman-note`** (`.claude/skills/gcp-feynman-note/SKILL.md`). Úsala siempre que se cree o edite una nota de este vault; no improvises un formato distinto.
- **Actualización del índice**: cada vez que se crea o renombra una nota, **`GCP_Index.md` debe actualizarse en el mismo cambio** (tabla del módulo correspondiente, diagrama Mermaid y changelog). Una nota sin entrada en el índice queda huérfana del grafo y del mapa mental. La skill mencionada arriba incluye este paso como parte obligatoria del flujo.
- **Transcripciones fuente**: las lecciones nuevas se dejan primero como transcripciones crudas (con timestamps) dentro de la carpeta del módulo correspondiente. Estas son material fuente, no notas — no las conviertas en la nota final ni las borres sin confirmar con el usuario; la nota Feynman se crea como un archivo nuevo a partir de ellas.
- **No generes resúmenes ejecutivos ni documentos adicionales** (planning docs, resúmenes de sesión) salvo que el usuario los pida explícitamente.
- **Enlaces bidireccionales**: usa siempre wikilinks `[[nota]]` para conectar con notas existentes y con `[[GCP_Index]]`, respetando los nombres de archivo tal cual (sin extensión `.md`) para que Obsidian resuelva el enlace.

## Contexto profesional del usuario

El usuario trabaja en tecnología en el sector financiero colombiano (fondos de pensiones y cesantías, entidad vigilada por la SFC) bajo metodologías SAFe y DevSecOps. Aunque este repo es de estudio personal y no de trabajo, cuando el usuario conecte un concepto de GCP con su contexto profesional (gobierno de datos, seguridad, cumplimiento), vale la pena reflejar esa conexión en la sección "Registro personal" de la nota — así como ya lo ha hecho en notas como `gcp_vs_aws_homologacion`.
