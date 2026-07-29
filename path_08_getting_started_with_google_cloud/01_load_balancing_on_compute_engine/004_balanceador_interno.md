---
title: "Balanceador Interno de Aplicaciones (L7 interno)"
date: 2026-02-16
aliases: ["004_balanceador_interno_updated"]
tags: [GCP, LoadBalancing, Internal, L7]
links:
  - '[[GCP_Index]]'
  - '[[herarquia_gcp]]'
  - '[[gcp-network_updated]]'
  - '[[virtual_private_cloud_networking_updated]]'
  - '[[gcp_seguridad_disenio_en_capas_feynman]]'
---
# Internal Application Load Balancer
> **Resumen**: Balanceador **HTTP(S) interno** para **tráfico dentro de la VPC** (IP privada). Ideal para **microservicios**, **backends internos** y comunicación este‑oeste sin exponer a Internet. citeturn21search1

## 1) Analogía Feynman
Un **recepcionista interno** que solo atiende llamadas **dentro de la oficina** (VPC). Desde fuera nadie puede marcarlo. citeturn21search1

## 2) Arquitectura mínima
```mermaid
flowchart LR
  CINT[Cliente interno
(VM/Pod/OnPrem via VPN)]
  IPINT[IP Interna]
  PROXY[Target HTTP Proxy interno]
  URL[URL Map]
  BS[Backend Service]
  MIG[Instance Group/NEG]
  HC[Health Check]

  CINT --> IPINT --> PROXY --> URL --> BS --> MIG
  BS -. verifica .-> HC
```

## 3) Pasos clave
1. Reservar **IP interna** en la **subnet**.
2. Crear **health check** HTTP.
3. Crear **backend service** (scheme `INTERNAL_MANAGED`).
4. Crear **URL map** y **target HTTP proxy** interno.
5. Crear **forwarding rule** interna sobre la IP.
6. Abrir **firewall**: puertos del servicio + **rangos de health check**.

> Recuerda: todo ocurre **dentro de la VPC**; asegúrate de conectividad desde clientes (subnets/VPN/peering). (Se basa en tu nota original de balanceador interno con pasos `gcloud`). citeturn21search1

## 4) ¿Cuándo usarlo?
- APIs internas, **microservicios**.
- Separación **privada** de tráfico entre servicios.
- Cumplimiento que exige **no exponer** endpoints a Internet.

## 5) Troubleshooting
- `get-health` y logs del backend.
- Reglas de **firewall** (subnets correctas, rangos HC).
- DNS interno apuntando a la **IP interna** del LB.

## 6) Tarjetas Anki
- **P:** ¿Qué diferencia a un ALB interno? **R:** Usa **IP privada** y solo atiende clientes en la **VPC** (o conectados a ella).
- **P:** ¿Qué *scheme* debe usarse? **R:** `INTERNAL_MANAGED`.
