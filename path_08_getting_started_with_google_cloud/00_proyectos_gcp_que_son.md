---
title: "¿Qué es un proyecto en GCP?"
date: 2026-02-13
tags: [GCP, Proyectos, IAM]
links:
  - '[[GCP_Index]]'
  - '[[herarquia_gcp]]'
  - '[[IAM_intro]]'
  - '[[interactuando_con_gcp]]'
---
# ¿Qué es un proyecto en Google Cloud?
Un **proyecto de Google Cloud** es la **unidad básica de organización** donde se agrupan recursos como VMs, bases de datos, buckets, redes y configuraciones.citeturn16search1

Los proyectos contienen:
- **Recursos y servicios** (Compute Engine, Cloud Storage, BigQuery, etc.)citeturn16search1
- **Configuraciones de seguridad e IAM** (roles viewer, editor, admin, etc.)citeturn16search1  → Ver: [[IAM_intro]]
- **APIs habilitadas** para permitir el uso de servicios desde UI, CLI o client libraries.citeturn16search1  → Relacionado: [[interactuando_con_gcp]]

## Relación con la jerarquía de GCP
Un proyecto es el **segundo nivel** en la jerarquía de Google Cloud (Organización → Carpetas → Proyectos → Recursos). → Ver: [[herarquia_gcp]]

Esto significa:
- Cada recurso pertenece **a un único proyecto**.
- Las **políticas IAM se heredan** desde niveles superiores.

## APIs y herramientas relacionadas
- Los proyectos administran qué **APIs** están habilitadas.citeturn16search1
- DialogFlow API: para chatbots no‑code.citeturn16search1
- Google APIs Explorer: permite **probar APIs sin código**.citeturn16search1

→ Relacionado: [[interactuando_con_gcp]]

## Tarjetas Anki
Q: ¿Qué es un proyecto en GCP?  
A: Un contenedor donde se organizan recursos, configuraciones, permisos y APIs.

Q: ¿Qué jerarquía tiene el proyecto?  
A: Organización → Carpetas → **Proyecto** → Recursos.

Q: ¿Qué controla IAM dentro del proyecto?  
A: Quién puede hacer qué dentro de los recursos.

---
## Registro personal
- Un proyecto es el centro operativo de cualquier despliegue.
- Relacionar proyectos con carpetas facilita escalabilidad.
