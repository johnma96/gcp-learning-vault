---
title: "Cloud Marketplace en GCP"
date: 2026-02-16
tags: [GCP, Marketplace, Deploy]
links:
  - '[[GCP_Index]]'
  - '[[herarquia_gcp]]'
  - '[[interactuando_con_gcp]]'
---
# Cloud Marketplace en Google Cloud
Permite lanzar **soluciones preconfiguradas** con múltiples tecnologías y stacks listos para usar.

Ejemplo usado en el lab:
- **LAMP stack** → Linux + Apache + MySQL + PHP.

## Ventajas
- Despliegue rápido sin configurar infraestructura.
- Ajustado a un **proyecto GCP** → relacionado: [[00_proyectos_gcp_que_son]].
- Control de permisos vía IAM → ver: [[IAM_intro]].
- Integración con billing y APIs.

## Casos de uso
- Probar software empresarial.
- Desplegar aplicaciones típicas (CMS, LAMP, WordPress, Redis, Kafka).
- Evaluar soluciones antes de adoptarlas.

## Diagrama conceptual
```mermaid
flowchart LR
  USER[Usuario]
  MP[Cloud Marketplace]
  PROJ[Proyecto GCP]
  RES[Recursos desplegados]

  USER --> MP --> PROJ --> RES
```

## Tarjetas Anki
Q: ¿Qué permite Cloud Marketplace?  
A: Lanzar soluciones preconfiguradas.

Q: Ejemplo de stack desplegado.  
A: LAMP (Linux Apache MySQL PHP).
