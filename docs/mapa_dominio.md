# Mapa de dominio

Estado de dominio por concepto. Es la memoria de largo plazo del agente
`tutor-evaluador`: determina qué se pregunta cada día y cuándo toca repasar.

**Escala:** `0` no lo recuerda · `1` lo reconoce pero no lo explica ·
`2` lo explica de memoria · `3` lo aplica a un escenario nuevo.

**Intervalos:** nivel 0 → +1 día · nivel 1 → +2 días · nivel 2 → +7 días ·
nivel 3 → +21 días. Un concepto que baja de nivel vuelve al intervalo corto.

> Todos los conceptos arrancan en nivel 0 porque **aún no han sido
> evaluados** — no porque se presuma desconocimiento. La primera sesión de
> diagnóstico con `tutor-evaluador` establece los niveles reales.

---

## Curso 01 · Load Balancing on Compute Engine

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Balanceador de red (L4) | `002_balanceador_red` | 0 | — | diagnóstico |
| Balanceador de aplicaciones (L7) | `003_balanceador_apps` | 0 | — | diagnóstico |
| Balanceador interno (L7 interno) | `004_balanceador_interno` | 0 | — | diagnóstico |

## Curso 03 · Google Cloud Fundamentals: Core Infrastructure

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Jerarquía de recursos | `herarquia_gcp` | 0 | — | diagnóstico |
| Proyectos | `00_proyectos_gcp_que_son` | 0 | — | diagnóstico |
| IAM | `IAM_intro` | 0 | — | diagnóstico |
| Cloud Identity | `cloud_identity` | 0 | — | diagnóstico |
| Cuentas de servicio | `cuentas_servicio` | 0 | — | diagnóstico |
| Seguridad en capas | `gcp_seguridad_disenio_en_capas` | 0 | — | diagnóstico |
| IaaS vs PaaS | `iaas_paas` | 0 | — | diagnóstico |
| Estructura geográfica y zonas | `gcp-network` | 0 | — | diagnóstico |
| VPC networking | `virtual_private_cloud_networking` | 0 | — | diagnóstico |
| Conectividad híbrida | `conectividad_hibrida_gcp` | 0 | — | diagnóstico |
| Cloud Load Balancing (visión general) | `cloud_load_balancing` | 0 | — | diagnóstico |
| Cloud Storage | `cloud_storage` | 0 | — | diagnóstico |
| Clases de almacenamiento | `cloud_storage_classes` | 0 | — | diagnóstico |
| Cloud SQL | `cloud_sql` | 0 | — | diagnóstico |
| Spanner | `spanner` | 0 | — | diagnóstico |
| Firestore | `firestore` | 0 | — | diagnóstico |
| Bigtable | `bigtable` | 0 | — | diagnóstico |
| Comparativa de storage | `comparativa_storage_gcp` | 0 | — | diagnóstico |
| Contenedores | `intro_containers` | 0 | — | diagnóstico |
| Kubernetes | `kubernetes_intro` | 0 | — | diagnóstico |
| GKE | `gke_intro` | 0 | — | diagnóstico |
| Cloud Run | `cloud_run_intro` | 0 | — | diagnóstico |
| Cloud Run Functions | `cloud_run_functions` | 0 | — | diagnóstico |
| Interacción con GCP (consola, SDK, API) | `interactuando_con_gcp` | 0 | — | diagnóstico |
| Cloud Marketplace | `cloud_marketplace` | 0 | — | diagnóstico |
| Prompt engineering (fundamentos) | `prompt_engineering_intro` | 0 | — | diagnóstico |

## Curso 04 · Introduction to AI and ML on Google Cloud

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Arquitectura de GenAI (3 capas) | `genai_arquitectura_google_cloud` | 0 | — | diagnóstico |
| Vertex AI Studio: idea a app | `vertex_ai_studio_idea_to_app` | 0 | — | diagnóstico |
| Parámetros del modelo (temperature, Top K/P) | `vertex_ai_studio_parametros_modelo` | 0 | — | diagnóstico |
| Despliegue, grounding/RAG y tuning | `vertex_ai_studio_despliegue_y_tuning` | 0 | — | diagnóstico |

## Transversales

| Concepto | Nota | Nivel | Última eval. | Próxima eval. |
|---|---|---|---|---|
| Homologación GCP ↔ AWS | `gcp_vs_aws_homologacion` | 0 | — | diagnóstico |

---

## Pendientes detectados

- **`002_dataflow_templates` (curso 02) está vacío.** El curso *Prepare Data
  for ML APIs on GCP* no tiene contenido documentado; es un vacío frente al
  temario del examen (dominio de gestión de datos, 15 %).
- **Notas fuera del índice**: `iaas_paas` y `conectividad_hibrida_gcp` existen
  en el vault pero no aparecen en `GCP_Index.md` — quedan huérfanas del grafo.
- **Dominios del examen sin cobertura en el vault**: automatización y
  orquestación de pipelines (18 %), servir y escalar modelos (15 %),
  monitoreo de soluciones de IA (15 %), escalar prototipos (14 %) e IA
  responsable y en cumplimiento (10 %). Es contenido de la ruta `path_17`,
  todavía no iniciada.
