---
title: "Cloud Load Balancing en GCP (visión completa)"
date: 2026-02-16
aliases: [cloud_load_balancing]
tags: [GCP, LoadBalancing, Networking]
links:
  - '[[GCP_Index]]'
  - '[[herarquia_gcp]]'
  - '[[gcp-network_updated]]'
  - '[[virtual_private_cloud_networking]]'
  - '[[gcp_seguridad_disenio_en_capas]]'
  - '[[IAM_intro]]'
  - '[[003_balanceador_apps]]'
  - '[[002_balanceador_red]]'
  - '[[004_balanceador_interno]]'
---
# Cloud Load Balancing en Google Cloud
> **Resumen**: Servicio **distribuido y definido por software** para repartir tráfico hacia backends en GCP. Soporta **balanceo global (L7)**, **regional (L4/L7)**, y variantes **externas** e **internas**, con **autoscaling**, **health checks** y **alta disponibilidad**. citeturn20search3

## 1) Analogía Feynman
Imagina una **central de peajes** que distribuye autos (peticiones) hacia diferentes carreteras (backends). Según el tipo de peaje (L4 vs L7), puede mirar solo la placa (IP/puerto) o también el destino exacto (URL/host) para decidir por dónde enviarte. citeturn20search3

## 2) Tipos principales
- **Application Load Balancer (L7)**: entiende HTTP(S), reglas por **host/path**, TLS, URL maps, integración con backends y serverless. (→ [[003_balanceador_apps]]) citeturn20search3
- **Network Load Balancer (L4)**: balanceo a nivel **TCP/UDP** (passthrough), preserva IP de origen, latencia muy baja, regional. (→ [[002_balanceador_red]]) citeturn20search3
- **Internal Application Load Balancer (L7 interno)**: HTTP(S) **dentro de la VPC**, IP interna, ideal para microservicios privados. (→ [[004_balanceador_interno]]) citeturn20search3

> **Región/Global**: Los ALB externos pueden ser **globales**; NLB y ALB internos suelen ser **regionales**. La selección depende de alcance del tráfico y requisitos de latencia/privacidad. citeturn20search3

## 3) Componentes (L7 típico)
- **Forwarding rule** → **Target HTTP(S) Proxy** → **URL Map** → **Backend Service** → **Instance Group/NEG**. (NEG también puede apuntar a **Cloud Run/App Engine/Functions**)

## 4) ¿Cuándo usar L4 vs L7?
- **L4**: TCP/UDP, baja latencia, preservar IP, protocolos no HTTP. (p. ej., bases de datos, juegos, IoT) → [[002_balanceador_red]]
- **L7**: HTTP(S), enrutamiento por host/path, TLS, headers, integración con CDN/Cloud Armor, escalado web. → [[003_balanceador_apps]]

## 5) Relación con otras piezas
- **Red y VPC**: necesitas subredes, reglas de **firewall** y rutas. → [[gcp-network_updated]] · [[virtual_private_cloud_networking_updated]]
- **Jerarquía y IAM**: los LBs viven en **proyectos** y respetan permisos/políticas. → [[herarquia_gcp]] · [[IAM_intro]]
- **Seguridad en capas**: TLS, GFE/edge, DoS, health checks. → [[gcp_seguridad_disenio_en_capas_feynman]]

## 6) Diagrama (panorama)
```mermaid
flowchart TB
  EXT[Cliente/Internet]
  INT[Cliente interno]
  subgraph Edge[Edge / GFE]
    ALB[ALB externo
HTTP(S) global]
  end
  subgraph VPC[VPC]
    NLB[NLB
L4 regional]
    IALB[ALB interno
HTTP(S) regional]
    BE[Backend Service]
    MIG[Instance Group/NEG]
  end
  EXT --> ALB --> BE --> MIG
  INT --> IALB --> BE
  EXT --> NLB --> MIG
```

## 7) Checklist rápida
- Definir **alcance**: interno/externo, global/regional.
- Elegir **capa**: L4 vs L7.
- Preparar **backends** (MIG/NEGs) y **health checks**.
- Abrir **firewall** para health checks y puertos.
- Configurar **TLS** (si HTTPS) y **URL maps** (L7).

## 8) Tarjetas Anki
- **P:** ¿Qué diferencia clave hay entre L4 y L7 en GCP? **R:** L4 enruta por IP/puerto (TCP/UDP); L7 entiende HTTP(S) y reglas por host/path. 
- **P:** ¿Cuándo usar interno? **R:** Para servicios **privados** en VPC (microservicios, backends).
