---
title: "Conectividad híbrida y multicloud en GCP"
authors: ["John Mario Montoya Zapata"]
date: "2026-02-19"
tags: [GCP, Networking, Hybrid, Multicloud, Connectivity]
links:
  - '[[GCP_Index]]'
  - '[[gcp-network_updated]]'
  - '[[virtual_private_cloud_networking_updated]]'
  - '[[herarquia_gcp]]'
  - '[[IAM_intro]]'
---
# Conectividad híbrida y multicloud en GCP
> **Resumen en una frase**: Opciones para conectar tu **VPC de Google Cloud** con **on‑premises u otras nubes**: **Cloud VPN (+ Cloud Router/BGP)**, **Peering (Direct/Carrier)**, **Interconnect (Dedicated/Partner)** y **Cross‑Cloud Interconnect**, cada una con requisitos, rendimiento y SLA distintos.

## 1) Analogía sencilla (Feynman)
Piensa en **conectar oficinas**:
- **Cloud VPN** = un **túnel seguro por Internet** entre dos sedes.
- **Cloud Router (BGP)** = el **recepcionista** que **intercambia listas de calles** (rutas) entre sedes; si aparece una calle nueva (subred), el otro edificio la aprende **automáticamente**.
- **Peering (Direct/Carrier)** = **puertas laterales** en un mismo complejo (PoP) para intercambiar tráfico más directo que por Internet público.
- **Interconnect (Dedicated/Partner)** = **líneas privadas** entre edificios con **SLA alto**.
- **Cross‑Cloud Interconnect** = una **línea privada** **entre tu VPC y otra nube**.

> Relacionado: redes y VPC → [[gcp-network_updated]] · [[virtual_private_cloud_networking_updated]]

## 2) Opciones de conectividad (visión general)
- **Cloud VPN** (IPsec sobre Internet). Opcional: **Cloud Router** para rutas **dinámicas BGP**.
- **Peering**: **Direct Peering** o **Carrier Peering** (a través de un proveedor). No tiene SLA de Google.
- **Interconnect**: **Dedicated Interconnect** (enlace físico propio) o **Partner Interconnect** (a través de proveedor). Puede alcanzar **SLA hasta 99.99%** si cumple topología.
- **Cross‑Cloud Interconnect**: enlaces dedicados de **10/100 Gbps** entre Google y **otro CSP** para estrategias **multicloud**.

## 3) Tabla de decisión (guía rápida)
- **¿Necesitas direcciones privadas ↔ privadas?**
  - **Sí**, y tu Internet actual es suficiente → **Cloud VPN** (+ **Cloud Router** si quieres rutas dinámicas).
  - **Sí**, pero necesitas **alto rendimiento**/**baja latencia**/**SLA** → **Dedicated** o **Partner Interconnect**.
- **¿No necesitas privado** (te valen IPs públicas) **y la conexión actual rinde bien** → usar **IPs públicas** a servicios de Google.
- **¿No privado** y **Internet no rinde** → **Peering** (Direct si tienes presencia en un **PoP**; **Carrier** si prefieres un **proveedor** intermedio).
- **¿Multicloud dedicado** → **Cross‑Cloud Interconnect**.

## 4) Pros/Contras (resumen conceptual)
**Cloud VPN (+Cloud Router)**
- ✅ Rápido de implementar, coste bajo, **BGP** dinámico.
- ⚠️ Depende de Internet (latencia/variabilidad), **SLA de Internet**.

**Direct/Carrier Peering**
- ✅ Menos saltos que Internet, acceso directo a productos Google **expuestos por IP pública**.
- ⚠️ **Sin SLA** de Google; Direct requiere **co‑lo/PoP**; Carrier implica dependencia del **ISP**.

**Dedicated Interconnect**
- ✅ **Privado**, alto rendimiento, **SLA hasta 99.99%** si la topología cumple; puedes **respaldar con VPN**.
- ⚠️ Requiere **equipo** y presencia (co‑lo) en PoP, mayor costo/operación.

**Partner Interconnect**
- ✅ Privado via **proveedor**, **SLA hasta 99.99%** (según diseño), flexible para **ancho de banda** menor que 10 G.
- ⚠️ SLA de Google **no cubre** segmentos fuera de su red; dependencia del **partner**.

**Cross‑Cloud Interconnect**
- ✅ Dedicado 10/100 Gbps hacia **otros CSP**; **multicloud** con menos complejidad; **encriptado** y transferencia **site‑to‑site**.
- ⚠️ Diseño multicloud conlleva **gobernanza y costos** añadidos.

## 5) ¿Cuándo usar cada una? (ejemplos)
- **Cloud VPN + Cloud Router**: migración inicial, DR económico, laboratorios híbridos, **aprendizaje automático de subredes** on‑prem ↔ VPC.
- **Direct Peering**: ya tienes **equipo** en un **PoP** y solo necesitas **acceder a servicios públicos** de Google con mejor rendimiento que Internet.
- **Carrier Peering**: no quieres instalar equipo; tu proveedor te acerca al **PoP**.
- **Dedicated Interconnect**: cargas críticas, **SLA y throughput** sostenido; data pipelines grandes.
- **Partner Interconnect**: necesitas **privado** y **SLA**, pero **sin** instalar equipo en PoP; ubicaciones del DC fuera de colos de Google.
- **Cross‑Cloud Interconnect**: escenarios **multicloud** (GCP↔otro CSP) con **alto ancho de banda** y **baja latencia**.

## 6) Diagrama (panorama híbrido/multicloud)
```mermaid
flowchart TB
  subgraph OnPrem[On‑premises / Sede]
    CEQ[Equipo de red]
  end
  subgraph ISP[Internet / Proveedor]
    VPN[Cloud VPN]
    PEER[Carrier Peering]
  end
  subgraph POP[PoP de Google]
    DPEER[Direct Peering]
    DEDIC[Dedicated Interconnect]
    PART[Partner Interconnect]
  end
  subgraph GCP[GCP - VPC]
    VPC[VPC/Subnets]
    CR[Cloud Router (BGP)]
  end
  subgraph OtherCloud[Otra Nube]
    CCI[Cross‑Cloud Interconnect]
  end

  CEQ -- IPsec --> VPN --> VPC
  CEQ -- BGP --> CR
  CEQ -- Proveedor --> PEER --> VPC
  CEQ == enlace dedicado ==> DPEER --> VPC
  CEQ == enlace privado ==> DEDIC --> VPC
  CEQ == a través de partner ==> PART --> VPC
  VPC == dedicated 10/100G ==> CCI == dedicated ==> OtherCloud
```

## 7) Relación con otras notas
- Redes y despliegues en **VPC** → [[virtual_private_cloud_networking_updated]]
- Organización y permisos → [[herarquia_gcp]] · [[IAM_intro]]
- Topologías y regiones → [[gcp-network_updated]]

## 8) Preguntas Feynman (auto‑chequeo)
1. Si agrego una **nueva subnet** en mi VPC, ¿qué opción **propaga rutas automáticamente**?  
2. Si **no** necesito direcciones privadas y mi Internet va bien, ¿qué opción **más simple** puedo usar?  
3. ¿Cuál opción tiene **SLA** de hasta **99.99%** si la topología cumple?  
4. ¿Cuál elijo si **no puedo** instalar equipos en un PoP pero quiero **privado con SLA**?

## 9) Tarjetas Anki
Q: ¿Qué problema resuelve **Cloud Router**?  
A: Intercambio **dinámico** de rutas (BGP) para que on‑prem y VPC aprendan subredes automáticamente.

Q: Diferencia clave **Peering vs Interconnect**.  
A: Peering intercambia tráfico **público** y no tiene **SLA** de Google; Interconnect es **privado** y puede tener **SLA**.

Q: Tamaños típicos de **Cross‑Cloud Interconnect**.  
A: **10 Gbps** y **100 Gbps**.

Q: ¿Cuándo preferir **Partner Interconnect** sobre **Dedicated**?  
A: Cuando **no** puedes instalar equipo en PoP o el **ancho de banda** requerido no justifica 10 Gbps completos.

---
### Registro personal (aprendizajes/notas)
- Priorizar **requerimientos**: ¿privado vs público?, ¿SLA?, ¿latencia/throughput?, ¿co‑lo disponible?, ¿multicloud?  
- Empezar con **VPN** y evolucionar a **Interconnect/CCI** según crezcan las necesidades.
