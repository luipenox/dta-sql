import streamlit as st

# Nadpis lekce
st.write("## Lekce: Datové typy v SQLite")

# Úvod
st.write(
    "Datové typy v SQLite se liší od některých jiných relačních databází, protože používají koncept **type affinities** "
    "(propojení typu) místo přísných datových typů. To znamená, že každý sloupec má preferovaný typ, ale může uchovávat data jiného typu."
)

# 1. Základní datové typy
st.write("### 1. Základní datové typy v SQLite")
st.write(
    "SQLite podporuje následující 5 kategorií datových typů, které se nazývají **storage classes**:"
)
st.write("""
1. **NULL** - Reprezentuje neznámou nebo prázdnou hodnotu.
2. **INTEGER** - Celá čísla (kladná nebo záporná), ukládaná jako 1, 2, 3, 4, 6 nebo 8 bajtů v závislosti na velikosti hodnoty.
3. **REAL** - Desetinná čísla (hodnoty v plovoucí řádové čárce), ukládaná ve formátu 8-bytového IEEE floating point čísla.
4. **TEXT** - Textové znaky (řetězce) uložené v kódování UTF-8, UTF-16BE nebo UTF-16LE.
5. **BLOB** - Binární data uložená přesně tak, jak byla zadána, např. obrázky nebo soubory.
""")

# 2. Přehled type affinities
st.write("### 2. Type Affinities")
st.write(
    "SQLite přiřazuje sloupcům tzv. **type affinities**, což určuje, jaký typ dat se do sloupce obvykle ukládá. "
    "Existují čtyři hlavní type affinities (plus jedna speciální):"
)
st.write("""
1. **TEXT** - Preferován pro textová data. Slouží pro ukládání řetězců.
2. **NUMERIC** - Ukládá číselné hodnoty a automaticky přizpůsobuje typy dat jako `INTEGER`, `REAL` nebo `TEXT` pro čísla.
3. **INTEGER** - Ukládá celá čísla.
4. **REAL** - Ukládá desetinná čísla (hodnoty v plovoucí čárce).
5. **NONE** - Nemá žádné konkrétní propojení typu, přijímá jakýkoli typ dat.
""")

# 3. Automatická konverze dat
st.write("### 3. Automatická konverze dat")
st.write(
    "SQLite je flexibilní a umožňuje ukládat jiný typ dat, než je očekávaný `type affinity`, protože se snaží data automaticky převést. "
    "Například:"
)
st.code(
    "CREATE TABLE osoba (\n"
    "    id INTEGER PRIMARY KEY,\n"
    "    vek TEXT\n"
    ");\n"
    "\n"
    "INSERT INTO osoba (id, vek) VALUES (1, 25);  -- Vejde se, i když vek má TEXT affinity.",
    language="sql"
)
st.write(
    "V tomto případě `vek` očekává textová data, ale je zde uloženo celé číslo."
)

# 4. Specifikace datových typů
st.write("### 4. Specifikace datových typů při tvorbě tabulek")
st.write(
    "Při vytváření tabulek můžete definovat sloupce s konkrétní datovou specifikací. "
    "SQLite se však nejprve pokusí rozpoznat type affinity. Pokud rozpoznání selže, datový typ bude `NONE`."
)
st.write("#### Příklad:")
st.code(
    "CREATE TABLE skladba (\n"
    "    id INTEGER PRIMARY KEY,\n"
    "    nazev TEXT,\n"
    "    delka REAL,\n"
    "    velikost BLOB\n"
    ");",
    language="sql"
)
st.write(
    "Tento příkaz vytvoří tabulku s několika sloupci a jejich odpovídajícími type affinities."
)

# 5. Výchozí hodnoty
st.write("### 5. Výchozí hodnoty pro datové typy")
st.write(
    "SQLite umožňuje definovat výchozí hodnoty pro sloupce. Například:"
)
st.code(
    "CREATE TABLE uzivatel (\n"
    "    id INTEGER PRIMARY KEY,\n"
    "    jmeno TEXT NOT NULL,\n"
    "    zaregistrovan DATETIME DEFAULT CURRENT_TIMESTAMP\n"
    ");",
    language="sql"
)
st.write(
    "Zde je `zaregistrovan` nastaveno na aktuální datum a čas, pokud není specifikováno jinak při vložení dat."
)

# 6. Přehled kompatibility s jinými SQL databázemi
st.write("### 6. Přehled kompatibility s jinými SQL databázemi")
st.write(
    "SQLite nemá pevně definované datové typy jako například MySQL nebo PostgreSQL. "
    "Přesto SQLite rozpoznává a mapuje běžné typy dat na své vlastní `affinities`. Například:"
)
st.code(
    "-- Tvorba tabulky s tradičními SQL datovými typy\n"
    "CREATE TABLE priklad (\n"
    "    name VARCHAR(50),\n"
    "    age INT,\n"
    "    salary NUMERIC(10, 2),\n"
    "    created_at TIMESTAMP\n"
    ");",
    language="sql"
)
st.write(
    "SQLite tyto typy přeloží takto:\n"
    "- `VARCHAR(50)` → type affinity `TEXT`\n"
    "- `INT` → type affinity `INTEGER`\n"
    "- `NUMERIC(10, 2)` → type affinity `NUMERIC`\n"
    "- `TIMESTAMP` → type affinity `NUMERIC`"
)

# Závěr
st.write("### Závěr")
st.write(
    "Datové typy v SQLite jsou velmi flexibilní díky `affinities`. I když můžete ukládat data různých typů, je důležité porozumět, "
    "jak databáze pracuje při ukládání a načítání hodnot."
)
