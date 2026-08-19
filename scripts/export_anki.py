#!/usr/bin/env python3
"""
Extrae las tarjetas Anki escritas dentro de las notas Feynman del vault y las
exporta a un TSV listo para importar en Anki.

Uso:
    python scripts/export_anki.py

Salida:
    docs/anki/gcp_cards.tsv

El TSV lleva cabecera con directivas (#separator, #deck, #tags column...), así
que Anki lo importa sin configuración manual. La primera columna (pregunta) es
la clave de deduplicación: al reimportar con "Update existing notes when first
field matches", las tarjetas existentes se actualizan en vez de duplicarse.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "docs" / "anki" / "gcp_cards.tsv"
MAZO = "GCP"

# Carpetas que no contienen notas de estudio.
EXCLUIDAS = {".git", ".obsidian", ".claude", "docs", "scripts", "images"}

# Encabezado de la sección de tarjetas dentro de cada nota.
SEC_ANKI = re.compile(r"^#{1,4}\s*\d*\)?\s*Tarjetas Anki\s*$", re.I | re.M)
# Cualquier otro encabezado de nivel <= 3 corta la sección.
SIG_SECCION = re.compile(r"^#{1,3}\s+\S", re.M)

# Marcadores de pregunta y respuesta. El vault usa dos convenciones —
# Q/A (inglés) y P/R (español) — con o sin negritas, y a veces dentro de una
# viñeta. La respuesta puede ir en línea nueva o en la misma línea.
MARCA_Q = re.compile(
    r"(?:^|\n)[ \t]*(?:[-*][ \t]+)?\*{0,2}[QP][:.]\*{0,2}[ \t]*", re.I
)
MARCA_A = re.compile(
    r"(?:"
    r"(?:^|\n)[ \t]*(?:[-*][ \t]+)?\*{0,2}[AR][:.]\*{0,2}[ \t]*"  # inicio de línea
    r"|[ \t]{2,}\*{0,2}[AR][:.]\*{0,2}[ \t]*"                     # misma línea, 2+ espacios
    r"|[ \t]\*\*[AR][:.]\*\*[ \t]*"                               # misma línea, negrita
    r")",
    re.I,
)

FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.S)


def leer_frontmatter(texto):
    """Devuelve (titulo, [tags]) del frontmatter YAML de la nota."""
    m = FRONTMATTER.match(texto)
    if not m:
        return None, []
    bloque = m.group(1)
    titulo = None
    tags = []
    mt = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', bloque, re.M)
    if mt:
        titulo = mt.group(1).strip()
    mg = re.search(r"^tags:\s*\[(.*?)\]", bloque, re.M)
    if mg:
        tags = [t.strip().strip("\"'") for t in mg.group(1).split(",") if t.strip()]
    return titulo, tags


def a_html(texto):
    """Markdown mínimo -> HTML, y aplana el texto para que quepa en un TSV."""
    t = texto.strip()
    t = re.sub(r"\\s*$", "", t, flags=re.M)          # continuaciones de línea
    t = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", t)  # wikilinks
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = t.replace("\t", " ")
    t = re.sub(r"\n+", "<br>", t)
    t = re.sub(r"\s{2,}", " ", t)
    return t.strip()


def normalizar_tag(tag):
    """Anki no admite espacios dentro de un tag."""
    return re.sub(r"\s+", "_", tag.strip())


def extraer_seccion(texto):
    """Devuelve el cuerpo de la sección 'Tarjetas Anki', o None."""
    m = SEC_ANKI.search(texto)
    if not m:
        return None
    resto = texto[m.end():]
    corte = SIG_SECCION.search(resto)
    return resto[: corte.start()] if corte else resto


def extraer_tarjetas(seccion):
    """Parte la sección en pares (pregunta, respuesta)."""
    tarjetas = []
    for bloque in MARCA_Q.split(seccion)[1:]:
        partes = MARCA_A.split(bloque, maxsplit=1)
        if len(partes) != 2:
            continue
        pregunta, respuesta = a_html(partes[0]), a_html(partes[1])
        if pregunta and respuesta:
            tarjetas.append((pregunta, respuesta))
    return tarjetas


def main():
    filas = []
    sin_tarjetas = []
    total_notas = 0

    for md in sorted(RAIZ.rglob("*.md")):
        if any(p in EXCLUIDAS for p in md.relative_to(RAIZ).parts[:-1]):
            continue
        texto = md.read_text(encoding="utf-8")
        seccion = extraer_seccion(texto)
        if seccion is None:
            continue

        total_notas += 1
        titulo, tags_fm = leer_frontmatter(texto)
        tarjetas = extraer_tarjetas(seccion)

        if not tarjetas:
            sin_tarjetas.append(md.relative_to(RAIZ).as_posix())
            continue

        # Tags: los del frontmatter + la carpeta del curso + el nombre de la nota.
        partes = md.relative_to(RAIZ).parts
        tags = {normalizar_tag(t) for t in tags_fm}
        for p in partes[:-1]:
            if re.match(r"^\d\d_", p):
                tags.add(normalizar_tag("curso_" + p))
        tags.add(normalizar_tag("nota::" + md.stem))
        etiquetas = " ".join(sorted(tags))

        for pregunta, respuesta in tarjetas:
            origen = f'<br><br><span style="color:#888;font-size:0.8em">{titulo or md.stem}</span>'
            filas.append((pregunta, respuesta + origen, etiquetas))

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with SALIDA.open("w", encoding="utf-8", newline="\n") as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#notetype:Basic\n")
        f.write(f"#deck:{MAZO}\n")
        f.write("#columns:Front\tBack\tTags\n")
        f.write("#tags column:3\n")
        for fila in filas:
            f.write("\t".join(fila) + "\n")

    print(f"Notas con seccion 'Tarjetas Anki': {total_notas}")
    print(f"Tarjetas exportadas: {len(filas)}")
    print(f"Archivo: {SALIDA.relative_to(RAIZ).as_posix()}")
    if sin_tarjetas:
        print("\nAVISO - notas con seccion Anki pero sin tarjetas parseables:")
        for n in sin_tarjetas:
            print(f"  - {n}")
        print("Revisa el formato: se esperan pares Q:/A: o P:/R: (con o sin negritas).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
