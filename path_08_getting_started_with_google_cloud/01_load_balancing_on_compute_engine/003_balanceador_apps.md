---
title: "Balanceador de Carga de Aplicaciones (L7)"
date: 2026-02-16
aliases: ["003_balanceador_apps_updated"]
tags: [GCP, LoadBalancing, L7]
links:
  - '[[GCP_Index]]'
  - '[[herarquia_gcp]]'
  - '[[gcp-network_updated]]'
  - '[[virtual_private_cloud_networking_updated]]'
  - '[[gcp_seguridad_disenio_en_capas_feynman]]'
---
# Application Load Balancer (HTTP/HTTPS)
> **Resumen**: Balanceador **L7 global** (externo) que entiende HTTP(S): soporta **URL maps**, **TLS**, **enrutado por host/path**, y backends en **MIG/NEGs** (incluido **serverless**). Ideal para apps web y APIs. citeturn20search2

## 1) Analogía Feynman
Es un **recepcionista** que mira la **dirección completa** (dominio + ruta) y decide a qué equipo enviar cada solicitud. citeturn20search2

## 2) Arquitectura L7
```mermaid
flowchart TB
  U[Usuario]
  FR[Forwarding Rule (80/443)]
  TP[Target HTTP(S) Proxy]
  URL[URL Map]
  BS[Backend Service]
  NEG[NEG/MIG/Serverless]
  HC[Health Check]

  U --> FR --> TP --> URL --> BS --> NEG
  BS -. verifica .-> HC
```

## 3) Funciones clave
- **TLS** (certificados), **HTTP/2**, **enrutado** por **host/path**.
- Integración con **NEGs** para **Cloud Run/App Engine/Functions**.
- Compatible con **autoscaling** y **health checks**.

## 4) Pasos rápidos (gcloud)
```bash
# Health check HTTP
gcloud compute health-checks create http web-hc --port=80

# Backend service (global)
gcloud compute backend-services create web-bs   --global   --protocol=HTTP   --health-checks=web-hc

# Asociar MIG (zonal)
gcloud compute backend-services add-backend web-bs   --global   --instance-group=MIG_NAME   --instance-group-zone=ZONE

# URL map
gcloud compute url-maps create web-map --default-service=web-bs

# Proxy HTTP(S)
gcloud compute target-http-proxies create web-proxy --url-map=web-map

# IP y regla de reenvío
gcloud compute addresses create web-ip --global

gcloud compute forwarding-rules create web-fr   --address=web-ip   --global   --target-http-proxy=web-proxy   --ports=80
```

> Para HTTPS, usa `target-https-proxies` y gestiona **certificados**.

## 5) Seguridad y operaciones
- Añade **firewall** para **rangos de health checks**.
- Integra con controles de **identidad** e infraestructura de seguridad. → [[IAM_intro]] · [[gcp_seguridad_disenio_en_capas_feynman]]

## 6) Troubleshooting
- `get-health` al backend service.
- Revisar **URL map** y rutas.
- Ver certificados y puertos abiertos.

## 7) Tarjetas Anki
- **P:** ¿Qué permite el URL map? **R:** Enrutado por host y path a distintos backends.
- **P:** ¿Cuándo usar NEGs? **R:** Cuando quieres conectar a backends **serverless** o endpoints específicos.
