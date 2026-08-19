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

## Tarjetas Anki

**Q:** ¿Cuáles son los tres niveles de la estructura geográfica de GCP?
**A:** **Locations → Regiones → Zonas**.

**Q:** ¿La estructura geográfica es lo mismo que la jerarquía de recursos?
**A:** No, son ejes distintos. **Geográfica**: Locations → Regiones → Zonas, define *dónde corre* el recurso. **Jerarquía de recursos**: Recursos → Proyectos → Carpetas → Organización, define *quién administra* y cómo se heredan las políticas.

**Q:** ¿Qué es una zona y para qué sirve?
**A:** Un entorno **aislado** dentro de una región (`us-central1-a`). Distribuir entre zonas da **alta disponibilidad** frente a fallos localizados.

**Q:** Formato del nombre de una región y de una zona.
**A:** Región `us-central1`; zona `us-central1-a` (la región más un sufijo de letra).
