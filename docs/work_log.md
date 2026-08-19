# Work Log

Bitácora diaria de trabajo en el repositorio `gcp-learning-vault`. Cada entrada resume, a partir de los commits reales del día, el trabajo desarrollado y los próximos pasos. Se alimenta mediante la skill `daily-closeout` (`.claude/skills/daily-closeout/SKILL.md`) al cierre de cada jornada.

---

## 29-07-2026

### Trabajo desarrollado
- Se convirtió la transcripción cruda `deployment_and_model_tuning.md` en la nota Feynman `vertex_ai_studio_despliegue_y_tuning.md` (curso 04), cubriendo despliegue (SDK/API/Cloud Run), grounding/RAG y tuning de modelos (prompt design, adapter tuning, full fine-tuning).
- Se actualizó `GCP_Index.md` (tabla del Curso 04, diagrama Mermaid, changelog a v0.7) y se eliminaron las 4 transcripciones crudas del curso 04 ya convertidas.
- Se hizo el primer versionado de todo el vault en 6 commits: config/Obsidian, guía del proyecto, cursos 01-03, curso 04, índice maestro y nota complementaria GCP↔AWS.
- Se conectó el repositorio local a GitHub (`origin/main`) y se hizo el primer push.
- Se agregó la skill `daily-closeout` junto con `docs/work_log.md` y `docs/learnings.md` (con entradas de ejemplo) para llevar bitácora de las próximas sesiones.

### Próximos pasos
- Confirmar con el usuario el nombre/número exacto de la ruta `path_17_...` en Google Skills antes de crear su carpeta.
- Continuar el curso 04 con las lecciones restantes de "Introduction to AI and ML on GCP".
- Repasar con tarjetas Anki las notas de Vertex AI Studio ya creadas.

---

## 19-08-2026

### Trabajo desarrollado
- Primera sesión de evaluación con el agente `tutor-evaluador` (bitácora en `docs/evaluaciones/2026-08-19_sesion.md`): diagnóstico de línea base sobre cursos 01, 03 y 04. Ninguna respuesta completamente correcta; niveles asignados en `docs/mapa_dominio.md`.
- **Bloque A — arreglada la tubería de Anki.** Se reescribió `scripts/export_anki.py` para reconocer las variantes de encabezado del vault y, sobre todo, **reportar qué notas quedaron fuera y por qué**. Antes se saltaba notas en silencio: `herarquia_gcp` y `gcp_seguridad_disenio_en_capas` tenían tarjetas escritas que nunca llegaron al mazo.
- Se normalizaron los tres encabezados divergentes (`Tarjetas de memoria (Anki)`, `Tarjetas de memoria (estilo Anki)`, y un `#` en vez de `##`) al canónico `## N) Tarjetas Anki`.
- Se añadió la sección 3.1 a la skill `gcp-feynman-note` fijando encabezado, formato y **mezcla obligatoria de tipos de tarjeta** (concepto, decisión, discriminación), más qué no ankificar.
- **Bloque B — cerrado el mazo.** Se escribieron las secciones de tarjetas de `comparativa_storage_gcp` (9, la de máxima prioridad del diagnóstico), `gcp-network` (4) e `iaas_paas` (5), y se distribuyeron 4 tarjetas de decisión en `IAM_intro`, `cloud_run_intro`, `cloud_run_functions` y `vertex_ai_studio_despliegue_y_tuning`.
- El mazo pasó de **121 a 153 tarjetas**, con **34 de 34 notas** aportando tarjetas y cero omisiones reportadas.
- Se corrigió el nombre desactualizado "Cloud Functions" → "Cloud Run functions" en `iaas_paas`.
- **Bloque D — hábito de examen.** Se añadió el *protocolo de requisitos duros* a `docs/protocolo_estudio.md` (subrayar los requisitos que cambian la respuesta, enunciar el candidato, verificarlo contra cada requisito, descartar alternativas por razón concreta), y una sección equivalente en el agente `tutor-evaluador` para que lo **exija** antes de aceptar cualquier respuesta a escenario — incluso cuando la respuesta sea correcta, porque lo que se entrena es el método.

### Verificación del diagnóstico del tutor
Tres de sus cuatro afirmaciones se confirmaron. **Una es falsa**: `IAM_intro` **sí** cubre deny policies y su precedencia (líneas 44-46, 107 y 120). Lo que realmente falta ahí es la **aditividad** de las allow policies. Se endureció la regla de auditoría del agente: antes de afirmar que una nota no cubre algo debe buscarlo y **citar dónde buscó**; si no lo verificó, debe escribir "no encontré, pero no busqué exhaustivamente".

### Próximos pasos — el lunes 24/08 se arranca con el Bloque C

Los bloques A, B y D quedaron cerrados hoy. **El C es lo único pendiente**: contenido por ampliar o corregir en notas.

- `IAM_intro`: añadir la **aditividad** de las allow policies (un hijo no puede restringir lo que el padre concedió) y el formato de permiso IAM v2.
- Nota nueva sobre **retention policy y bucket lock** en Cloud Storage (inmutabilidad WORM). No existe nada en el vault y es directamente aplicable a conservación de registros en entidad vigilada. Ojo: `cloud_storage.md` ya usa el título "Inmutabilidad" para hablar de versionado, que es otro concepto — hay que desambiguar.
- `herarquia_gcp`: separar "políticas" de IAM de las de Organization Policy. La frase sobre excepciones puntuales solo aplica a las segundas.
- `cloud_run_intro`: dejar explícito el eje *request-driven* vs. *event-driven* y el parámetro **min instances = 0** (hoy la nota no lo nombra).
- `gke_intro`: añadir las primitivas que son la señal de decisión (DaemonSets, NetworkPolicy, service mesh, taints/afinidad). Hoy no aparecen.
- `003_balanceador_apps`: nombre oficial con modificador (global external / regional external / classic), dónde termina el TLS (target HTTPS proxy) y la cadena de componentes **como diagrama, no como tarjeta**. Además tiene un artefacto de pegado (`citeturn20search2`) en la línea 14.

**Cinco tarjetas de decisión quedaron pendientes a propósito**, porque ninguna nota respalda todavía su contenido y la regla es no ankificar lo que la nota no explica: bucket lock, context caching, primitivas de GKE, `min instances = 0` y terminación de TLS. Se escriben cuando el Bloque C cierre esos vacíos.

Además, fuera del Bloque C: `gcp-network` e `iaas_paas` tienen wikilinks rotos a `gcp_seguridad_disenio_en_capas_feynman` (la nota se llama `gcp_seguridad_disenio_en_capas`) y frontmatter incompleto, por lo que no aportan tags temáticos al mazo.

---
