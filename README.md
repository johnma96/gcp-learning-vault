# gcp-learning-vault — Vault de estudio: Google Cloud Platform

Vault personal de [Obsidian](https://obsidian.md) con las notas de estudio de John Mario Montoya Zapata sobre Google Cloud Platform (GCP), construidas con la **técnica Feynman**, con la meta de certificarse como **Google Cloud Professional Machine Learning Engineer** antes de que termine el año.

El repositorio está pensado para alojar **todas** las rutas de aprendizaje (learning paths) de [Google Skills](https://www.skills.google/) que se vayan cursando — no solo una. Cada ruta vive en su propia carpeta de nivel superior.

## Cómo abrir este repositorio

Este repositorio **es** un vault de Obsidian (la configuración vive en `.obsidian/`). Ábrelo directamente como vault en la aplicación de Obsidian para navegar el grafo de enlaces, usar el panel de backlinks y visualizar los diagramas Mermaid embebidos en las notas. También se puede leer como Markdown plano desde GitHub/VS Code, pero se pierde la vista de grafo.

## Estructura

```
gcp-learning-vault/
├── GCP_Index.md                                            # Mapa maestro (MOC): punto de entrada a todas las notas
├── 00_proyectos_gcp_que_son.md                              # Nota introductoria (jerarquía/proyectos)
├── gcp_vs_aws_homologacion.md                               # Nota complementaria: homologación GCP ↔ AWS
├── path_08_getting_started_with_google_cloud/               # Ruta de Google Skills: "Getting Started with Google Cloud"
│   ├── 01_load_balancing_on_compute_engine/                 # Curso/skill badge: Load Balancing on Compute Engine
│   ├── 02_prepare_data_for_ml_apis_on_gcp/                  # Curso: Prepare Data for ML APIs on GCP
│   ├── 03_google_cloud_fundamentals_core_infrastructure/    # Curso: Google Cloud Fundamentals: Core Infrastructure
│   └── 04_introduction_to_AI_and_ML_on_GCP/                 # Curso: Introduction to AI and ML on GCP (en progreso)
├── images/                                                  # Imágenes referenciadas por las notas
└── .obsidian/                                                # Configuración del vault (no editar a mano)
```

Cada carpeta `path_XX_...` corresponde a una **ruta de aprendizaje** de Google Skills; dentro de ella, cada carpeta numerada es un **curso** de esa ruta. Dentro de cada curso, cada archivo `.md` es en principio una nota Feynman sobre un concepto o servicio de GCP. La excepción es el curso 04, que actualmente contiene también **transcripciones crudas** de lecciones (texto con timestamps, sin frontmatter) pendientes de convertir en notas.

### Rutas compartidas entre paths

Google Skills reutiliza cursos y laboratorios entre distintas rutas. Cuando un curso de una ruta nueva ya se cursó como parte de otra ruta ya presente en este repo, **no se duplica la nota**: se añade una nota corta de referencia (o una entrada en `GCP_Index.md`) que enlaza al curso ya documentado, indicando en qué otra ruta se vio primero.

## GCP_Index.md: el mapa maestro

`GCP_Index.md` es el **Map of Content (MOC)** del vault: agrupa las notas por módulo/curso, muestra un diagrama Mermaid con las relaciones entre conceptos, y lleva un changelog de cómo ha evolucionado el vault. Es el punto de partida recomendado para entender qué se ha estudiado y cómo se conecta entre sí.

**Regla del vault**: toda nota nueva debe quedar referenciada en `GCP_Index.md` (tabla del módulo, diagrama Mermaid y changelog). Una nota que no aparece en el índice es una nota huérfana en el grafo.

## Metodología de las notas (técnica Feynman)

Cada nota sigue una estructura consistente pensada para forzar comprensión real (no copiar y pegar documentación):

1. **Resumen en una frase** — la idea central, sin jerga.
2. **Analogía sencilla** — explicar el concepto con una metáfora cotidiana.
3. **Contenido clave** — lo importante del material fuente, en lenguaje propio.
4. **Diagramas/ejemplos** — Mermaid, tablas comparativas o comandos `gcloud` cuando aplica.
5. **Preguntas Feynman** — auto-chequeo: preguntas que uno debería poder responder sin mirar la nota.
6. **Tarjetas Anki** — pares pregunta/respuesta para repaso espaciado.
7. **Registro personal** — aprendizajes, dudas, próximos pasos y conexión con el contexto profesional del autor.

El procedimiento completo (frontmatter exacto, checklist de creación, y el paso obligatorio de actualizar `GCP_Index.md`) está definido como skill de Claude Code en [`.claude/skills/gcp-feynman-note/SKILL.md`](.claude/skills/gcp-feynman-note/SKILL.md), para que cualquier nota nueva —manual o asistida— siga el mismo patrón.

## Estado de las rutas y cursos

| Ruta / Curso | Estado |
|---|---|
| **path_08 · Getting Started with Google Cloud** | 🟠 En progreso |
| 01 · Load Balancing on Compute Engine | ✅ Notas completas |
| 02 · Prepare Data for ML APIs on GCP | 🟡 Parcial |
| 03 · Google Cloud Fundamentals: Core Infrastructure | ✅ Notas completas |
| 04 · Introduction to AI and ML on GCP | 🟠 En progreso |
| **path_17 · Professional Machine Learning Engineer** | ⬜ Aún no iniciada como carpeta propia |
