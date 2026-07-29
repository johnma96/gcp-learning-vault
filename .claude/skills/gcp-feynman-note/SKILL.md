---
name: gcp-feynman-note
description: Crea o convierte contenido (transcripciones, apuntes, documentación) en una nota Feynman para el vault de Obsidian de GCP de este repositorio, y actualiza GCP_Index.md como parte obligatoria del mismo cambio. Úsala siempre que se vaya a crear una nota nueva de un concepto/servicio de GCP, o cuando el usuario pida "convertir esto en una nota", "hazme una nota Feynman", o "actualiza el índice".
---

# Nota Feynman para el vault de GCP

Esta skill codifica el patrón de notas que ya existe en este repositorio (`01_...`, `02_...`, `03_...`) para que toda nota nueva sea indistinguible en estilo de las ya escritas, y para que el vault de Obsidian (grafo, backlinks, MOC) nunca quede con notas huérfanas.

Aplica esta skill tanto para **notas escritas desde cero** (a partir de un concepto que el usuario explica) como para **conversión de material fuente** (transcripciones de lecciones, documentación oficial, apuntes sueltos) en una nota Feynman.

## 0) Antes de escribir

1. Identifica la **ruta** (`path_08_getting_started_with_google_cloud/`, u otra `path_XX_.../` — Google Skills reorganiza rutas con frecuencia, así que si vas a crear la carpeta de una ruta nueva confírmale al usuario el nombre/número exacto tal como lo ve en la plataforma; no lo infieras de documentación externa) y dentro de ella, en qué carpeta de curso va la nota (`01_...`, `02_...`, etc., o raíz del repo si es una nota complementaria transversal como `gcp_vs_aws_homologacion.md`).
2. Lee 1-2 notas ya existentes de esa misma carpeta (o de una carpeta hermana si es la primera nota del curso) para calibrar tono y profundidad — no todas las notas tienen exactamente las mismas secciones opcionales, pero todas comparten el esqueleto de la sección 2.
3. Si la nota parte de una **transcripción cruda** (archivo con timestamps, sin frontmatter), trátala como material fuente de solo lectura: no la borres ni la sobrescribas. La nota Feynman es un **archivo nuevo**. Si varias transcripciones son en realidad sub-temas de una sola lección larga, está bien fusionarlas en una nota o dividirlas en varias — usa criterio: una nota por concepto autocontenible que alguien pueda repasar solo.
4. Revisa `GCP_Index.md` para ver qué notas relacionadas ya existen y decidir a cuáles enlazar (no dupliques contenido ya cubierto en otra nota; enlaza a ella).
5. **Curso/laboratorio ya visto en otra ruta**: Google Skills reutiliza el mismo curso o skill badge en varias rutas. Antes de escribir una nota nueva, pregúntale al usuario si ese curso ya lo cursó (y por tanto ya tiene nota) dentro de otra carpeta `path_XX_.../` de este repo. Si es así, **no dupliques la nota**: crea en su lugar una referencia corta (puede ser una entrada directa en `GCP_Index.md`, o una nota mínima de una sección) que enlace con `[[nota_original]]` e indique explícitamente en qué otra ruta se vio primero.

## 1) Nombre de archivo

- `snake_case`, sin espacios ni tildes, extensión `.md`.
- Descriptivo del concepto, no de la lección/timestamp (ej. `vertex_ai_studio_idea_to_app.md`, no `leccion_2.md`).
- Si el curso ya usa prefijos numéricos para sus notas (como `path_08_getting_started_with_google_cloud/01_load_balancing_on_compute_engine/002_balanceador_red.md`), sigue esa convención dentro de ese curso; si el curso usa nombres descriptivos sin prefijo (como en `.../03_google_cloud_fundamentals_core_infrastructure/cloud_sql.md`), sigue esa.

## 2) Frontmatter (obligatorio, exacto)

Este es el frontmatter canónico usado por las notas más recientes del vault (`prompt_engineering_intro.md`, `comparativa_storage_gcp.md`, `gcp_vs_aws_homologacion.md`). Úsalo tal cual, sin añadir ni quitar llaves:

```yaml
---
title: "Título legible de la nota"
authors: ["John Mario Montoya Zapata"]
date: "YYYY-MM-DD"
tags: [GCP, Tema1, Tema2]
links:
  - '[[GCP_Index]]'
  - '[[nota_relacionada_1]]'
  - '[[nota_relacionada_2]]'
---
```

- `date`: fecha real de creación de la nota (no la fecha del curso ni la de la transcripción).
- `tags`: siempre incluye `GCP`; añade 2-4 tags temáticos en PascalCase/CamelCase (ej. `GenAI`, `VertexAI`, `MLOps`) coherentes con tags ya usados en el vault — revisa notas hermanas antes de inventar uno nuevo.
- `links`: **siempre** incluye `[[GCP_Index]]` primero, luego cada nota del vault con la que esta nota tiene relación conceptual directa (prerequisito, comparación, continuación). Estos son los enlaces que Obsidian usará para el grafo — no los omitas aunque el cuerpo de la nota también tenga wikilinks inline.

## 3) Cuerpo de la nota (esqueleto)

No todas las secciones son obligatorias en todas las notas (una nota comparativa no necesita "arquitectura mínima"; una nota de un solo servicio no necesita tabla comparativa), pero el **orden y el espíritu** de estas secciones sí se respeta:

1. `# Título` (igual al `title` del frontmatter).
2. **Blockquote de resumen en una frase** justo debajo del título: `> **Resumen en una frase**: ...` — la idea completa en un solo golpe de vista, sin jerga.
3. **Analogía sencilla (técnica de Feynman)** — sección obligatoria. Explica el concepto con una metáfora cotidiana (una universidad, una central de peajes, un colega sin memoria, dos ciudades). Si no puedes construir una analogía honesta, es señal de que no entendiste el concepto lo suficiente todavía — vuelve a la fuente antes de escribirla.
4. **Contenido clave / conceptos base** — el desarrollo real del tema, en prosa propia, no copiado de la fuente. Usa tablas, listas y sub-secciones `###` libremente. Aquí es donde va, si aplica: diagramas Mermaid (`flowchart`), tablas comparativas, pasos `gcloud`/código, mapas de decisión.
5. **Relación con otras piezas / enlaces cruzados** (si aplica) — cómo se conecta esta nota con conceptos ya vistos, con wikilinks `[[nota]]` inline además de los del frontmatter.
6. **Preguntas Feynman (auto-chequeo)** — 4-6 preguntas que uno debería poder responder de memoria sin releer la nota. Son para forzar recuperación activa, no para repetir el resumen.
7. **Tarjetas Anki** — 4-6 pares `Q:`/`A:` (o `**P:**`/`**R:**`) cortos, atómicos, aptos para repaso espaciado.
8. **Glosario** (opcional, útil si la nota introduce 3+ términos nuevos).
9. **Registro personal** — sección de cierre, siempre presente, en primera persona: lecciones aprendidas, dudas abiertas, siguientes pasos, y —cuando aplique honestamente— la conexión con el contexto profesional del autor (sector financiero colombiano, SAFe/DevSecOps). No la fuerces si no hay conexión real.

Mermaid: usa `flowchart TB` o `flowchart LR` según convenga; evita saltos de línea dentro de una misma etiqueta de nodo (rompen el render en Obsidian).

## 4) Actualizar GCP_Index.md (paso obligatorio, mismo cambio)

Una nota no está terminada hasta que `GCP_Index.md` la referencia. Este paso es parte del mismo trabajo, no una tarea aparte:

1. **Tabla o lista del módulo/curso correspondiente**: añade la nota en la sección que le corresponda (si el curso/módulo aún no tiene sección propia en el índice, créala siguiendo el patrón de las secciones existentes — encabezado `##` con emoji, luego bullets `- Concepto → [[nota]]`).
2. **Diagrama Mermaid** (`flowchart TB` al final del archivo): añade el nodo dentro del `subgraph` de su módulo (o crea el subgraph si es el primero de ese módulo, con un ID corto que no choque con los ya usados — revisa los `subgraph` existentes antes de nombrar uno nuevo) y las flechas hacia/desde conceptos relacionados.
3. **Changelog** (`## 📥 Changelog` al final): agrega una línea nueva con versión incrementada (`v0.X` → `v0.X+1`), fecha de hoy, y una frase de qué se agregó. No reescribas versiones anteriores.
4. **Enlaces bidireccionales**: si la nota nueva completa una relación con una nota ya existente que aún no la menciona (ej. una nota "overview" que ahora tiene una nota "detalle" hija), considera añadir el wikilink de vuelta en la nota existente — pero no lo hagas de forma automática si cambia el sentido de esa nota; usa criterio.

## 5) Checklist final antes de dar por terminada la tarea

- [ ] Frontmatter con `title`, `authors`, `date`, `tags`, `links` (incluye `[[GCP_Index]]`).
- [ ] Analogía Feynman real (no una definición disfrazada de analogía).
- [ ] Al menos una sección de preguntas Feynman y una de tarjetas Anki.
- [ ] Sección "Registro personal" al final.
- [ ] `GCP_Index.md` actualizado: tabla/lista, diagrama Mermaid, changelog.
- [ ] Si la nota vino de una transcripción, el archivo fuente sigue intacto (no se borró ni se sobrescribió).
- [ ] Si el curso ya estaba documentado en otra ruta (`path_XX_.../`), no se duplicó la nota — se usó una referencia cruzada.
