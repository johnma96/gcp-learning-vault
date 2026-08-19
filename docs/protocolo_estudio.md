# Protocolo de estudio — 5 días × 1 hora

Protocolo de aprendizaje para la certificación **Google Cloud Professional
Machine Learning Engineer**, diseñado sobre técnicas con respaldo empírico y
adaptado a una restricción real: **una hora al día, de lunes a viernes**.

Resuelve un problema concreto: *"veo los videos y tomo notas, pero nada me
verifica que aprendí"*. La respuesta de la evidencia es que ver y anotar son
actividades de **entrada**; el aprendizaje duradero se produce en la
**salida** — al recuperar de memoria, explicar, aplicar y equivocarse.

---

## 1. Por qué este diseño (fundamento)

El estudio de referencia de Dunlosky et al. (2013) evaluó diez técnicas de
estudio y las clasificó por utilidad:

| Utilidad | Técnicas |
|---|---|
| **Alta** | Práctica de recuperación (autoevaluarse), práctica distribuida (espaciar) |
| **Moderada** | Práctica intercalada, interrogación elaborativa, autoexplicación |
| **Baja** | Releer, subrayar, resumir, mnemotecnias de palabra clave, imaginería |

El dato incómodo: **ver videos y escribir resúmenes cae en la franja baja**.
Las notas Feynman de este vault son mejores que un resumen (incorporan
autoexplicación y analogía, ambas de utilidad moderada), pero por sí solas no
activan la técnica de mayor retorno, que es evaluarse. Las tarjetas Anki que
ya están escritas dentro de cada nota son el activo desaprovechado: existen,
pero nunca se repasan.

Cinco principios sostienen el protocolo:

1. **Efecto de prueba** — evaluarse no es solo medir el aprendizaje, es
   producirlo. Recuperar de memoria consolida más que releer.
2. **Práctica distribuida** — tres sesiones de una hora repartidas en un mes
   retienen más que una sesión de tres horas. El espaciado gana siempre.
3. **Intercalado** — mezclar dominios distintos en una misma sesión obliga a
   identificar qué tipo de problema se enfrenta antes de resolverlo, que es
   exactamente lo que exige un examen de escenarios.
4. **Generación** — producir la respuesta retiene más que leerla. Por eso la
   regla de oro: nunca ver la respuesta antes de intentar.
5. **Dificultades deseables** — las condiciones que hacen el estudio más
   lento y más incómodo en el momento son las que producen más retención a
   largo plazo. La fluidez al releer es una ilusión de dominio.

Corolario práctico: **este protocolo se va a sentir más difícil que ver
videos. Esa es la señal de que funciona.**

---

## 2. Las tres piezas del sistema

| Pieza | Qué hace | Cuándo |
|---|---|---|
| **Claude + skill `gcp-feynman-note`** | Avanzar el curso y construir/refinar notas Feynman | Lun, Mar, Jue |
| **Agente `tutor-evaluador`** | Evaluar, detectar vacíos y auditar la exactitud de las notas | Mié, Jue, Vie + calentamiento diario |
| **Anki (con FSRS)** | Repaso espaciado automático de los hechos atómicos | Todos los días, 10 min |

La separación es deliberada: **quien construye la nota no puede ser el mismo
que certifica que la aprendiste.** El tutor es un evaluador independiente con
instrucción explícita de no editar las notas.

Archivos de estado:

- `docs/mapa_dominio.md` — nivel de dominio por concepto y fecha del próximo
  repaso. Es la memoria de largo plazo del tutor.
- `docs/evaluaciones/` — bitácora de cada sesión de evaluación.
- `docs/work_log.md` y `docs/learnings.md` — bitácora general (skill
  `daily-closeout`).

---

## 3. La semana

**Todos los días arrancan igual**, con el bloque que más rinde por minuto
invertido:

> ### Bloque 0 — Calentamiento de recuperación · 10 min (diario, innegociable)
> - 5–7 min de Anki (la cola del día completa; se dimensiona con el límite de
>   tarjetas nuevas, no con el de repasos — ver §5).
> - 3–5 min: una pregunta de **recuperación libre** del tutor sobre algo visto
>   hace 2–7 días, de un módulo distinto al de hoy (intercalado).
>
> Este bloque es el que convierte el estudio en distribuido. Si un día solo
> alcanzan 10 minutos, que sean estos.

---

### Lunes — Avance · 50 min

Curso nuevo con Claude: ver la lección o hacer el laboratorio, y construir la
nota Feynman con la skill `gcp-feynman-note`.

- 40 min: contenido + nota (analogía, desarrollo, enlaces cruzados).
- 10 min: **ankificar por lotes**. Marcar durante la lección los puntos que
  merecen tarjeta y recién al final convertirlos, en bloque. Interrumpir la
  lección para hacer tarjetas rompe la concentración y produce tarjetas peores.

No se hace evaluación profunda hoy: el material está demasiado fresco y
evaluarlo de inmediato mide memoria de trabajo, no aprendizaje.

---

### Martes — Avance · 50 min

Idéntico al lunes, con la lección siguiente.

Al cerrar, anotar en `docs/learnings.md` los dos o tres puntos donde hubo
fricción real de comprensión. Esa lista es la agenda del miércoles.

---

### Miércoles — Verificación profunda · 50 min

Sesión completa con el agente `tutor-evaluador`. Aquí se cobra lo de lunes y
martes, ya con 24–48 horas de olvido de por medio (que es lo que hace valiosa
la recuperación).

- 25 min — **Recuperación libre** sobre los conceptos de lunes y martes, más
  el intercalado de módulos anteriores. Sin notas a la vista. Formato abierto,
  sin opciones.
- 15 min — **Feynman inverso**: explicarle al tutor un concepto como si fuera
  un analista de negocio sin background técnico. Preparar material para
  enseñar produce mejor desempeño que preparar para un examen.
- 10 min — **Auditoría de nota**: el tutor verifica una nota contra
  documentación oficial y entrega un reporte de errores, desactualizaciones y
  vacíos frente al temario. Las correcciones se aplican después, con la skill
  `gcp-feynman-note`.

---

### Jueves — Avance + práctica aplicada · 50 min

- 25 min — Curso/laboratorio nuevo con Claude (mismo formato del lunes).
- 25 min — **Práctica aplicada** con el tutor, rotando formato cada semana:
  - **Problemas de Parsons**: reordenar los pasos desordenados de un pipeline,
    una secuencia `gcloud` o un flujo de tuning.
  - **Código con huecos**: completar un snippet real del SDK de Vertex AI,
    un YAML de pipeline o un SQL de BigQuery ML, con andamiaje que se va
    retirando semana a semana.
  - **Escenario de caso**: proponer y justificar una arquitectura para un
    problema de negocio que no está resuelto en ninguna nota.

Este bloque existe porque **la repetición espaciada tiene un límite conocido**:
funciona muy bien para hechos y conceptos simples, y pierde utilidad a medida
que sube la complejidad. Una habilidad compuesta como diseñar un pipeline de
MLOps no se adquiere con tarjetas — requiere práctica deliberada en el límite
de la capacidad actual.

---

### Viernes — Simulacro y cierre · 50 min

- 30 min — **Simulacro cronometrado** en formato de examen real: ~15 preguntas
  de opción múltiple y selección múltiple, a razón de 2 minutos por pregunta,
  sin retroalimentación hasta el final, mezclando dominios.
- 12 min — **Análisis de errores**. Más importante que el puntaje: por cada
  fallo, clasificar el tipo de error (vacío conceptual, confusión entre
  servicios, terminología, falla de transferencia, desactualización). El tutor
  actualiza `docs/mapa_dominio.md`.
- 8 min — **Cierre de semana** con la skill `daily-closeout`: `work_log.md`,
  `learnings.md`, commit y push.

Viernes **no se ve material nuevo**. Es día de consolidación.

Sobre el formato: la recuperación libre produce más retención que la opción
múltiple, pero practicar en el formato del examen mejora el desempeño en ese
formato específico (*transfer-appropriate processing*). Por eso la opción
múltiple aparece un solo día: es entrenamiento para el examen, no el motor
del aprendizaje.

---

### Resumen de la semana

| Día | Bloque 0 (10 min) | Bloque principal (50 min) |
|---|---|---|
| **Lunes** | Anki + 1 pregunta libre | Curso nuevo + nota Feynman |
| **Martes** | Anki + 1 pregunta libre | Curso nuevo + nota Feynman |
| **Miércoles** | Anki + 1 pregunta libre | Verificación profunda + auditoría de nota |
| **Jueves** | Anki + 1 pregunta libre | Curso nuevo (25) + práctica aplicada (25) |
| **Viernes** | Anki + 1 pregunta libre | Simulacro (30) + análisis (12) + cierre (8) |

Reparto: **~2,5 días de avance nuevo y ~2,5 días de verificación**, más 50
minutos semanales de recuperación distribuida en el calentamiento diario.

---

## 4. Ciclos largos

- **Cada 4 semanas**: simulacro completo de 50–60 preguntas en 120 minutos,
  en las condiciones del examen real (sin notas, sin pausas, cronómetro
  corriendo). Registrar el puntaje. Esta serie de puntajes es la evidencia
  objetiva de progreso que hoy falta.
- **Cada 8 semanas**: barrido de mantenimiento — el tutor pregunta solo sobre
  conceptos en nivel 3 que llevan más de un mes sin tocarse, para detectar
  decaimiento silencioso.
- **Antes de agendar el examen**: dos simulacros completos consecutivos por
  encima del 80 % y ningún dominio del temario en nivel 0 o 1.

---

## 5. Higiene de tarjetas Anki

Las reglas siguientes vienen del *Janki Method* y de sus refinamientos
posteriores, que documentan los modos de fallo típicos de usar Anki para
programación:

**Sí funcionan:**
- Tarjetas **atómicas**: un hecho, una tarjeta.
- Tarjetas **híbridas**: descripción general del concepto + un ejemplo de
  código real de uso.
- Tarjetas de **decisión**: "¿cuándo prefieres Bigtable sobre Firestore?" —
  más valiosas que las de definición pura.
- Tarjetas de **buena práctica**, que se marcan como falladas si no se ha
  aplicado la práctica recientemente en el trabajo real.

**No funcionan (no las crees):**
- **Procedimientos ordenados de varios pasos** (configurar una VPC paso a
  paso). Nunca se recuerdan completos aunque se repasen mil veces; van en un
  runbook o checklist, no en Anki.
- **Firmas exactas de API**: orden de argumentos, tipos de retorno, nombres
  exactos de parámetros. Se olvidan, cambian entre versiones y el IDE los
  resuelve. Memoriza **qué capacidad existe**, no su firma.
- Tarjetas de tecnología marginal que no se está usando: suspéndelas y
  reactívalas cuando hagan falta.

**Operación:**
- **FSRS activado** (Anki 23.10+), retención deseada **90 %**. FSRS requiere
  entre 20 % y 30 % menos repasos que el algoritmo clásico SM-2 para la misma
  retención.
- **No bajes el límite de repasos diarios: baja el de tarjetas nuevas.**
  "Maximum reviews/day" es un tope de seguridad, no un objetivo. Ponerlo bajo
  no reduce el trabajo — lo **aplaza**, y acumula una cola de tarjetas
  vencidas. Con FSRS eso es peor que inútil: el algoritmo programa cada
  tarjeta para el día en que estarías por olvidarla, así que un tope que la
  empuja más allá de esa fecha degrada sus predicciones. Déjalo en 200 (el
  valor por defecto) o en el mínimo que Anki acepte.
- **El volumen de repaso se controla con las tarjetas nuevas.** Los repasos
  son una *consecuencia*: el manual de Anki estima que 20 tarjetas nuevas al
  día terminan produciendo unos 200 repasos diarios — una proporción cercana a
  **10×**. Para un bloque diario de 10 minutos (~40-60 repasos), el número
  correcto es **5 tarjetas nuevas al día**. Con 153 tarjetas en el mazo, eso
  las introduce todas en unas cinco semanas.
- **Si la cola sigue creciendo con 5 nuevas al día**, el problema no es
  disciplina: es que se están creando tarjetas de más. Borra las que no tengan
  un caso de uso real.
- Si una tarjeta falla tres veces seguidas y no logras identificar un caso de
  uso real para ese dato, **bórrala**. No todo merece memorizarse.
- **Nunca ankifiques algo que no entendiste.** Anki consolida comprensión
  existente; no la produce. Primero la nota Feynman, después la tarjeta.

---

## 6. Consejos y recomendaciones

**Sobre la sensación de estar aprendiendo**

La sensación de fluidez al releer una nota es una **ilusión de dominio**: se
reconoce el texto, no se recupera el concepto. La única prueba válida es
recuperarlo con la nota cerrada. Cuando una sesión se sienta frustrante y
lenta, el diseño está funcionando.

**Sobre la lectura del escenario (protocolo de requisitos duros)**

Dos de los cinco fallos del diagnóstico del 19/08/2026 no fueron de
conocimiento sino de lectura: se ignoró *"ni siquiera el dueño del proyecto"* y
se invirtieron *"offline"* y *"tiempo real"*. En el segundo caso se construyó
una arquitectura coherente sobre el requisito invertido — un modo de error más
peligroso que no saber la respuesta, porque no se siente como duda.

Antes de responder cualquier escenario, sin excepción:

1. **Subraya los requisitos duros.** Son las palabras que, si cambian, cambian
   la respuesta correcta: *global*, *regional*, *ACID*, *consistencia fuerte*,
   *tiempo real*, *offline*, *milisegundos*, *sin endpoint*, *ni siquiera el
   dueño*, *petabytes*, *por row key*.
2. **Enuncia tu candidato** antes de justificarlo.
3. **Verifícalo contra cada requisito, uno por uno.** Si alguno no se cumple,
   el candidato está descartado — no lo rescates con una racionalización.
4. **Descarta las alternativas explícitamente**, cada una por una razón
   concreta. "Es rápido y escala" no descarta nada porque describe a casi
   todos los servicios.

El examen está escrito para que **una sola palabra** cambie la respuesta. Se
gana descartando, no eligiendo.

**Sobre el orden de las cosas**

Entender → escribir la nota Feynman → ankificar → recuperar → aplicar. Saltarse
pasos hacia adelante (ankificar sin entender) produce memorización hueca;
saltarse pasos hacia atrás (aplicar sin recuperar) produce dependencia de la
documentación.

**Sobre el intercalado**

Resistir la tentación de estudiar un módulo entero en bloque hasta dominarlo.
Mezclar produce peor desempeño inmediato y mejor retención posterior — y el
examen es precisamente un intercalado forzado de siete dominios.

**Sobre explicar en voz alta**

En el bloque Feynman del miércoles, explicar **hablando**, no escribiendo.
Hablar impide releer sobre la marcha y expone los huecos de inmediato. El
efecto protégé está bien documentado: quien estudia para enseñar rinde más que
quien estudia para un examen.

**Sobre la elaboración con el contexto profesional**

La sección "Registro personal" de cada nota no es decorativa: conectar el
concepto nuevo con el contexto laboral (gobierno de datos, controles de la
SFC, DevSecOps) es *interrogación elaborativa* — anclar información nueva a
conocimiento existente, que es una de las técnicas de utilidad moderada. Hay
una ventaja concreta aquí: el examen dedica alrededor del 10 % a IA
responsable, segura y en cumplimiento, un terreno donde la experiencia en
sector regulado juega a favor.

**Sobre el tiempo**

Una hora al día es suficiente **si es diaria**. Dos sesiones de 25 minutos
separadas rinden más que 50 minutos seguidos, por el espaciado. Perder un día
no rompe el sistema; perder el bloque de recuperación tres días seguidos, sí.

**Sobre la confianza en el tutor**

El agente puede equivocarse. Tiene instrucción de verificar contra
documentación oficial y de declarar incertidumbre, pero **cualquier dato que
vaya a memorizarse debe contrastarse con la fuente oficial**. Una tarjeta con
un dato falso es peor que no tener la tarjeta.

**Sobre el temario**

Distribución aproximada del examen (verificar siempre contra la guía oficial
vigente, que Google actualiza sin aviso):

| Dominio | Peso aprox. |
|---|---|
| Automatizar y orquestar pipelines de ML | 18 % |
| Colaborar entre equipos para gestionar datos y modelos | 15 % |
| Servir y escalar modelos | 15 % |
| Monitorear soluciones de IA | 15 % |
| Escalar prototipos a modelos de ML/IA | 14 % |
| Arquitecturas de IA low-code | 13 % |
| Diseñar IA responsable, segura y en cumplimiento | 10 % |

Formato: 120 minutos, 50–60 preguntas de opción múltiple y selección múltiple,
200 USD, vigencia de 2 años.

---

## 7. Cómo arrancar

1. Instalar Anki y activar FSRS con retención deseada del 90 %.
2. Importar las tarjetas que ya están escritas dentro de las notas Feynman del
   vault (hoy no están en Anki — es el activo desaprovechado más grande).
3. Sesión inicial con `tutor-evaluador`: diagnóstico de línea base sobre los
   cursos 01 a 04 ya documentados, para poblar `docs/mapa_dominio.md` con
   niveles reales en vez de ceros.
4. Empezar la semana en el día que corresponda; no hace falta esperar a un
   lunes.
