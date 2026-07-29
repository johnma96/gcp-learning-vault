---
title: Red y Estructura Geográfica de GCP
links:
  - "[[herarquia_gcp]]"
  - "[[gcp_seguridad_disenio_en_capas]]"
  - "[[IAM_intro]]"
tags:
  - GCP
---
# Networking en GCP
Google organiza su infraestructura global en **Locations → Regiones → Zonas**.

## Relación con jerarquía de recursos
Aunque la jerarquía de red NO es la misma que la jerarquía lógica de recursos, ambas interactúan cuando eliges dónde desplegar proyectos y recursos. Consulta: [[herarquia_gcp]].

## Conceptos
- **Location**: áreas geográficas globales (Norteamérica, Europa, Asia, etc.)
- **Región**: como `us-central1`
- **Zonas**: como `us-central1-a`, `us-central1-b`, entornos aislados dentro de una región

## Relación con seguridad
La separación por regiones y zonas contribuye a la **alta disponibilidad** y forma parte de la seguridad física/infraestructura. Ver: [[gcp_seguridad_disenio_en_capas_feynman]].

## Ejemplo
- Location: América del Norte
- Región: `us-central1`
- Zonas: `us-central1-a`, `us-central1-b`, `us-central1-c`
