---
title: "Modelos de Servicio: IaaS vs PaaS vs Serverless vs SaaS"
links:
  - "[[gcp_seguridad_disenio_en_capas_feynman]]"
  - "[[herarquia_gcp]]"
tags:
  - GCP
  - Cloud
---
# IaaS, PaaS, Serverless y SaaS en GCP

## Relación con seguridad
Cada modelo delega un nivel diferente de responsabilidad, conectándose con la seguridad en capas: [[gcp_seguridad_disenio_en_capas_feynman]].

## Relación con jerarquía
Los servicios deben desplegarse dentro de **proyectos**, usando recursos que viven en la jerarquía de GCP: [[herarquia_gcp]].

## IaaS (Infrastructure as a Service)
Recursos de cómputo, red y almacenamiento de bajo nivel.
Ej: **Compute Engine**.
Pago: por recursos reservados.

## PaaS (Platform as a Service)
Plataformas gestionadas para ejecutar aplicaciones sin administrar servidores.
Ej: **App Engine**.
Pago: por uso.

## Serverless
Servicios completamente gestionados.
- **Cloud Run functions** (antes Cloud Functions)
- **Cloud Run**
- **App Engine (modo estándar)**

## SaaS (Software as a Service)
Servicios listos para usar.
Ej: Gmail, Drive, Docs.

## Tarjetas Anki

**Q:** ¿Qué modelo entrega cómputo, red y almacenamiento de bajo nivel, y cómo se paga?
**A:** **IaaS** (ej. Compute Engine). Se paga por **recursos reservados**, corran o no.

**Q:** ¿Qué modelo permite correr aplicaciones sin administrar servidores, y cómo se paga?
**A:** **PaaS** (ej. App Engine). Se paga **por uso**.

**Q:** ¿Necesito controlar el sistema operativo y el tamaño de la máquina?
**A:** **IaaS** (Compute Engine). Si no necesitas ese control, sube de nivel: PaaS o serverless.

**Q:** ¿Qué diferencia el modelo de cobro de IaaS frente al de PaaS?
**A:** IaaS cobra por **capacidad reservada**; PaaS cobra por **consumo real**.

**Q:** Ejemplos de serverless en GCP.
**A:** **Cloud Run**, **Cloud Run functions** y **App Engine** en modo estándar.
