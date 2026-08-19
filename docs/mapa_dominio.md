# Mapa de dominio

Estado de dominio por concepto. Es la memoria de largo plazo del agente
`tutor-evaluador`: determina qué se pregunta cada día y cuándo toca repasar.

**Escala:** `0` no lo recuerda · `1` lo reconoce pero no lo explica ·
`2` lo explica de memoria · `3` lo aplica a un escenario nuevo.

**Intervalos:** nivel 0 → +1 día · nivel 1 → +2 días · nivel 2 → +7 días ·
nivel 3 → +21 días. Un concepto que baja de nivel vuelve al intervalo corto.

> **Estado del diagnóstico.** La primera sesión de evaluación se hizo el
> **19/08/2026** y cubrió 6 conceptos de forma directa (bitácora:
> `docs/evaluaciones/2026-08-19_sesion.md`). Los conceptos que siguen marcados
> como `diagnóstico` en la última columna **aún no han sido evaluados** — su
> nivel 0 no significa desconocimiento, significa ausencia de medición.

---

## Curso 01 · Load Balancing on Compute Engine

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Balanceador de red (L4) | `002_balanceador_red` | 0 | — | diagnóstico |
| Balanceador de aplicaciones (L7) | `003_balanceador_apps` | 1 | 19/08/2026 | 21/08/2026 |
| Balanceador interno (L7 interno) | `004_balanceador_interno` | 0 | — | diagnóstico |

## Curso 03 · Google Cloud Fundamentals: Core Infrastructure

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Jerarquía de recursos | `herarquia_gcp` | 0 | 19/08/2026 | 20/08/2026 |
| Proyectos | `00_proyectos_gcp_que_son` | 1 | 19/08/2026 | 21/08/2026 |
| IAM | `IAM_intro` | 0 | 19/08/2026 | 20/08/2026 |
| Cloud Identity | `cloud_identity` | 0 | — | diagnóstico |
| Cuentas de servicio | `cuentas_servicio` | 0 | — | 20/08/2026 |
| Seguridad en capas | `gcp_seguridad_disenio_en_capas` | 0 | — | diagnóstico |
| IaaS vs PaaS | `iaas_paas` | 0 | — | diagnóstico |
| Estructura geográfica y zonas | `gcp-network` | 0 | — | 20/08/2026 |
| VPC networking | `virtual_private_cloud_networking` | 0 | — | diagnóstico |
| Conectividad híbrida | `conectividad_hibrida_gcp` | 0 | — | diagnóstico |
| Cloud Load Balancing (visión general) | `cloud_load_balancing` | 1 | 19/08/2026 | 21/08/2026 |
| Cloud Storage | `cloud_storage` | 0 | — | diagnóstico |
| Clases de almacenamiento | `cloud_storage_classes` | 0 | — | diagnóstico |
| Cloud SQL | `cloud_sql` | 0 | 19/08/2026 | 20/08/2026 |
| Spanner | `spanner` | 0 | 19/08/2026 | 20/08/2026 |
| Firestore | `firestore` | 0 | 19/08/2026 | 20/08/2026 |
| Bigtable | `bigtable` | 0 | 19/08/2026 | 20/08/2026 |
| Comparativa de storage | `comparativa_storage_gcp` | 0 | 19/08/2026 | 20/08/2026 |
| Contenedores | `intro_containers` | 0 | — | diagnóstico |
| Kubernetes | `kubernetes_intro` | 1 | 19/08/2026 | 21/08/2026 |
| GKE | `gke_intro` | 1 | 19/08/2026 | 21/08/2026 |
| Cloud Run | `cloud_run_intro` | 1 | 19/08/2026 | 21/08/2026 |
| Cloud Run Functions | `cloud_run_functions` | 1 | 19/08/2026 | 21/08/2026 |
| Interacción con GCP (consola, SDK, API) | `interactuando_con_gcp` | 0 | — | diagnóstico |
| Cloud Marketplace | `cloud_marketplace` | 0 | — | diagnóstico |
| Prompt engineering (fundamentos) | `prompt_engineering_intro` | 1 | 19/08/2026 | 21/08/2026 |

## Curso 04 · Introduction to AI and ML on Google Cloud

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Arquitectura de GenAI (3 capas) | `genai_arquitectura_google_cloud` | 0 | — | diagnóstico |
| Vertex AI Studio: idea a app | `vertex_ai_studio_idea_to_app` | 0 | — | diagnóstico |
| Parámetros del modelo (temperature, Top K/P) | `vertex_ai_studio_parametros_modelo` | 0 | — | diagnóstico |
| Despliegue, grounding/RAG y tuning | `vertex_ai_studio_despliegue_y_tuning` | 1 | 19/08/2026 | 21/08/2026 |

## Transversales

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Homologación GCP ↔ AWS | `gcp_vs_aws_homologacion` | 0 | — | diagnóstico |

---

## Notas sobre los niveles asignados el 19/08/2026

- **Jerarquía de recursos (0)**: no recuperó ninguno de los cuatro niveles; respondió con
  vocabulario de la estructura geográfica y de otros clouds. Vacío conceptual, no confusión.
- **IAM (0)**: no recuperó la aditividad de las allow policies ni la existencia de deny policies,
  que era el mecanismo que resolvía el escenario.
- **Estructura geográfica (evaluación forzada al 20/08)**: no se preguntó directamente, pero
  contaminó la respuesta de jerarquía. Hay que verificar que distinga los dos ejes.
- **Cuentas de servicio (pregunta planteada, sin responder)**: primera pregunta de la próxima
  sesión, no se le asignó nivel.
- **Bigtable y Firestore (0)**: no aparecieron en tres escenarios donde eran la respuesta. Son los
  dos huecos más grandes del diagnóstico.
- **Spanner y Cloud SQL (0)**: los nombra, pero les falta el discriminador
  regional/vertical vs. global/horizontal — los aplicó cruzados.
- **Balanceador de aplicaciones (1)**: acertó servicio y capa, que es la parte difícil; no recuperó
  el nombre con modificador ("global external") ni la cadena de componentes.
- **Cloud Run / Cloud Run Functions (1)**: conoce ambos productos y los aplicó a los escenarios
  cruzados; el renombramiento de Cloud Functions le solapó los nombres.
- **Kubernetes y GKE (1)**: acertó el escenario de GKE, pero sin justificar el criterio; no se
  midió si reconoce las primitivas (DaemonSets, NetworkPolicy) como la señal de decisión.
- **Prompt engineering (1)**: lo nombró como estrategia válida contra alucinación, sin desarrollar.
- **Despliegue/grounding/tuning (1)**: recuperó RAG, no recuperó "grounding" ni "tuning", y eligió
  context caching para un problema de grounding.

---

## Conceptos detectados en evaluación y sin nota en el vault

Surgieron al calificar la sesión del 19/08/2026. Son contenido examinable que hoy no está
documentado:

- **Deny policies de IAM** — precedencia sobre las allow policies, formato de permiso IAM v2
  (`storage.googleapis.com/buckets.delete`), niveles donde se adjuntan. Es el mecanismo correcto
  para "que nadie pueda, ni el dueño". Debería ampliar `IAM_intro`.
- **Retention policy y bucket lock en Cloud Storage** — inmutabilidad WORM, irreversibilidad del
  lock, imposibilidad de borrar el bucket antes de que todos los objetos cumplan la retención.
  Relevante para conservación de registros en entidad vigilada por la SFC.
- **Organization Policy Service vs. IAM** — restringe configuraciones de recursos, no permisos de
  principals. Es un distractor clásico frente a deny policies.
- **Componentes del Application Load Balancer** — forwarding rule, target HTTPS proxy, URL map con
  host rules y path matchers, backend service, health check, backends (MIGs/NEGs), y el rol del GFE.
- **Context caching en Vertex AI** — optimización de costo y latencia por reutilización de contexto,
  frecuentemente confundida con grounding. (TTL por defecto y mínimo de tokens sin verificar.)
- **Eventarc** — cómo se disparan las Cloud Run functions por eventos de Cloud Storage y Pub/Sub.

---

## Pendientes detectados

- **Ciclo de Anki sin cerrar.** `docs/anki/gcp_cards.tsv` ya existe (121 tarjetas, 29 notas,
  exportadas el 19/08/2026), pero los repasos no han corrido y **el mazo no cubre las dos notas
  donde más falló el diagnóstico**: `comparativa_storage_gcp` (sin sección de tarjetas) y
  `herarquia_gcp` (su encabezado `Tarjetas de memoria (Anki)` no lo reconoce el exportador, igual
  que `Tarjetas de memoria (estilo Anki)` en `gcp_seguridad_disenio_en_capas`). Tampoco tienen
  tarjetas `gcp-network` ni `iaas_paas`. Falta importar el mazo, activar FSRS al 90 %, escribir las
  tarjetas ausentes y normalizar los encabezados. Es la causa raíz de los niveles 0 de hoy, no el
  contenido del vault.
- **Faltan tarjetas de decisión.** Las tarjetas existentes son mayoritariamente de definición. El
  diagnóstico falló en decisiones (¿cuál de estos cuatro servicios?), no en definiciones. Lista
  concreta de tarjetas por crear en la bitácora del 19/08/2026.
- **`002_dataflow_templates` (curso 02) está vacío.** El curso *Prepare Data for ML APIs on GCP* no
  tiene contenido documentado; es un vacío frente al temario del examen (gestión de datos, 15 %).
- **Notas fuera del índice**: `iaas_paas` y `conectividad_hibrida_gcp` existen en el vault pero no
  aparecen en `GCP_Index.md` — quedan huérfanas del grafo.
- **Dominios del examen sin cobertura en el vault**: automatización y orquestación de pipelines
  (18 %), servir y escalar modelos (15 %), monitoreo de soluciones de IA (15 %), escalar prototipos
  (14 %) e IA responsable y en cumplimiento (10 %). Es contenido de la ruta `path_17`, todavía no
  iniciada.
