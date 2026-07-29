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
- **Cloud Functions**
- **Cloud Run**
- **App Engine (modo estándar)**

## SaaS (Software as a Service)
Servicios listos para usar.
Ej: Gmail, Drive, Docs.
