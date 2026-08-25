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

## 25-08-2026

### Trabajo desarrollado
- Se cerró el **curso 04**: se convirtieron las cinco transcripciones finales en `flujo_trabajo_ml_y_mlops` (tres etapas del flujo, Feature Store, matriz de confusión con precisión/recuperación, Explainable AI, las tres formas de servir predicciones, MLOps con Vertex AI Pipelines, componentes y fases de adopción).
- Antes de borrar el PDF de la lista de lectura se **extrajeron sus seis URLs incrustadas** y se incorporaron a la nota como tabla, mapeadas por orden de aparición. Entre ellas, el documento de arquitectura de MLOps de Google (niveles de madurez 0/1/2), que es la fuente canónica de las tres fases de adopción.
- Se resolvió por qué el badge del curso 04 no aparece en Credly: es un **completion badge**, y solo los **skill badges** (los que exigen aprobar un challenge lab) son elegibles. No es un fallo.
- `GCP_Index` a **v0.9**, curso 04 marcado como completado. Mazo en **191 tarjetas** desde 37 notas.

### Próximos pasos — Bloque C (26/08/2026)

> **Advertencia de alcance**: lo que sigue son entre 2 y 3 horas de trabajo, no 50 minutos. Está ordenado por valor decreciente por minuto invertido; conviene partirlo en dos días o aceptar que las tandas 3 y 4 se corren.
> **Choque de agenda**: el miércoles es día de verificación con el tutor según el protocolo. Hacer Bloque C mañana desplaza esa sesión.

**Paso 0 — Recargar el mazo (10 min, va primero porque desbloquea el repaso diario)**

- [ ] Borrar el mazo `GCP` en Anki de escritorio y reimportar `docs/anki/gcp_cards.tsv` (191 tarjetas). Hay que borrar, no actualizar: cambió el frente de todas las tarjetas al mover el título de la nota al anverso.
- [ ] Confirmar FSRS con retención **0.90**, tarjetas nuevas por día en **5**, y el límite de repasos **alto** (100–200; nunca bajo, ver §5 del protocolo).

**Tanda 1 — Limpieza mecánica (~15 min, todo verificado el 25/08)**

- [ ] Wikilink roto `[[gcp_seguridad_disenio_en_capas_feynman]]` → la nota se llama `gcp_seguridad_disenio_en_capas`. Está en **8 notas**: `002_balanceador_red`, `003_balanceador_apps`, `004_balanceador_interno`, `cloud_identity`, `cloud_load_balancing`, `cuentas_servicio`, `gcp-network`, `iaas_paas`. Se arregla en un solo `sed`.
- [ ] `cloud_storage_classes.md` línea 2: el título dice `"Cloud Storage en Google Cloud (Completado)"`. Dos problemas — no es su tema (son las *clases* de almacenamiento) y arrastra un marcador de progreso que se cuela como etiqueta de contexto en las tarjetas Anki.
- [ ] `003_balanceador_apps.md` línea 14: artefacto de pegado `citeturn20search2` con caracteres Unicode invisibles (U+E200). No se ve al leer pero está en el texto.
- [ ] `iaas_paas` y `conectividad_hibrida_gcp` siguen **fuera de `GCP_Index`** — huérfanas del grafo desde el primer commit.

**Tanda 2 — Los seis huecos de contenido del diagnóstico del 19/08**

- [ ] `IAM_intro`: **aditividad** de las allow policies (un hijo no puede restringir lo que el padre concedió) y formato de permiso IAM v2 (`storage.googleapis.com/buckets.delete`). Ojo: las deny policies y su precedencia **ya están** en la nota — el tutor se equivocó en eso.
- [ ] **Nota nueva**: retention policy y bucket lock en Cloud Storage (inmutabilidad WORM, irreversibilidad del lock, no se puede borrar el bucket hasta que todos los objetos cumplan la retención). Desambiguar frente a la sección "Inmutabilidad" de `cloud_storage`, que habla de *versionado* — otro concepto.
- [ ] `herarquia_gcp`: separar "políticas" de IAM de las de **Organization Policy**. La frase sobre excepciones puntuales solo aplica a las segundas.
- [ ] `cloud_run_intro` / `cloud_run_functions`: dejar explícito el eje **request-driven vs. event-driven** y el parámetro **`min instances = 0`** (hoy la nota no lo nombra).
- [ ] `gke_intro`: añadir las primitivas que son la señal de decisión — **DaemonSets, NetworkPolicy, service mesh, taints/afinidad**. Hoy no aparecen en ninguna parte de la nota.
- [ ] `003_balanceador_apps`: nombre oficial **con modificador** (global external / regional external / internal / classic), **dónde termina el TLS** (target HTTPS proxy) y la cadena de componentes **como diagrama, no como tarjeta**.

**Tanda 3 — Nota nueva de Pub/Sub**

- [ ] Nota introductoria de **Pub/Sub**: temas, suscripciones, push vs. pull, entrega *at-least-once*, desacople productor/consumidor.
- [ ] Incluir **Eventarc** y cómo dispara Cloud Run functions desde eventos de Cloud Storage — es exactamente el mecanismo que falló en la P5-C del diagnóstico.
- [ ] Justificación: hoy **ninguna nota del vault está dedicada a Pub/Sub** (solo dos lo mencionan de pasada), es uno de los cuatro servicios del skill badge ya obtenido, y ya figuraba como concepto detectado sin nota en `mapa_dominio`.

**Tanda 4 — Las cinco tarjetas de decisión bloqueadas**

Se escriben *después* de las tandas 2 y 3, porque la regla es no ankificar lo que ninguna nota explica:

- [ ] ¿Inmutabilidad WORM de objetos y del bucket? → retention policy + bucket lock (depende de la tanda 2)
- [ ] ¿Necesito DaemonSets, NetworkPolicy o service mesh? → GKE (depende de la tanda 2)
- [ ] ¿Qué parámetro permite escalar a cero en Cloud Run? → `min instances = 0` (depende de la tanda 2)
- [ ] ¿Dónde termina el TLS en un ALB? → target HTTPS proxy (depende de la tanda 2)
- [ ] Context caching → reutilizar contexto repetido para bajar costo/latencia; no recupera ni actualiza nada. **Sigue sin respaldo**: habría que añadir una sección a `vertex_ai_studio_despliegue_y_tuning` primero.

**Al cerrar el bloque**

- [ ] Regenerar el TSV (`python scripts/export_anki.py`) y verificar que no reporte omisiones.
- [ ] Actualizar `GCP_Index` a **v0.10** con las notas nuevas y las dos huérfanas.
- [ ] Commits y push.
- [ ] Reimportar el mazo en Anki — habrá tarjetas nuevas de las tandas 3 y 4.

### Fuera del alcance del Bloque C (anotado para no perderlo)

- `002_dataflow_templates` del **curso 02 sigue vacío**. Es un vacío frente al dominio de gestión de datos del examen (15 %).
- **Contradicción sin resolver sobre los tipos de datos de AutoML**: `opciones_desarrollo_ml_gcp` §7 dice tabular e imagen; `flujo_trabajo_ml_y_mlops` §4 dice tabular, imagen, texto y video. El propio curso se contradice. Hay que zanjarlo contra la guía oficial del examen y dejar una sola versión.
- **10 notas con frontmatter incompleto** (sin `authors`, y algunas con `tags` en formato lista que el exportador no lee, por lo que no aportan tags temáticos al mazo): `00_proyectos_gcp_que_son`, las tres de balanceadores, `cloud_load_balancing`, `cloud_marketplace`, `cloud_storage_classes`, `gcp-network`, `iaas_paas`, `virtual_private_cloud_networking`.
- Confirmar con el usuario el número y nombre exactos de **`path_17`** tal como aparecen en Google Skills, antes de crear su carpeta.

---
