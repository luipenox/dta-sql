import streamlit as st

st.write("# Lekce: Práce s daty v SQLite")

# Úvod
st.write(
    """
    SQLite podporuje práci s daty pomocí textových řetězců v ISO formátu (YYYY-MM-DD pro datum nebo YYYY-MM-DD HH:MM:SS pro datum a čas). 
    Pro manipulaci s těmito typy nabízí SQLite řadu funkcí. Tato lekce vás provede:

    - Filtrováním datových hodnot v tabulkách.
    - Použitím vestavěných funkcí pro práci s daty.
    - Možnostmi převodů a manipulací.
    """
)

# Datové typy
st.write("## 1. Datové typy v SQLite")
st.write(
    """
    V SQLite nejsou speciální datové typy jako `DATE` nebo `DATETIME`. Místo nich používá běžné typy, jako je `TEXT`, k ukládání dat ve standardním formátu:

    - **ISO 8601 formát pro datum**: `YYYY-MM-DD` (například `2023-10-01`).
    - **ISO 8601 formát pro datum a čas**: `YYYY-MM-DD HH:MM:SS` (například `2023-10-01 14:30:00`).

    **Například:**
    ```sql
    CREATE TABLE orders (
        InvoiceId INTEGER PRIMARY KEY,
        CustomerId INTEGER,
        InvoiceDate TEXT  -- Datum ve formátu 'YYYY-MM-DD'
    );
    ```
    """
)

# Filtrování pomocí WHERE
st.write("## 2. Filtrování dat pomocí klauzule WHERE")
st.write(
    """
    K vyfiltrování řádků podle hodnot datumů použijeme klauzuli `WHERE`. 
    Veškeré porovnávání dat v SQLite probíhá jako textové porovnávání ve formátu **ISO 8601** (YYYY-MM-DD), což je výhodné, pokud je formát stabilní.
    """
)

st.write("### Příklad: Filtrování podle určitého datumu")
st.code(
    """
SELECT * 
FROM Invoice 
WHERE InvoiceDate > '2009-02-01';
    """,
    language="sql"
)
st.write("Tento dotaz vrátí všechny faktury vytvořené 1. října 2023.")

st.write("### Příklad: Filtrování faktur po určitém datu")
st.code(
    """
SELECT * 
FROM Invoice 
WHERE DATE(InvoiceDate) = '2009-02-01';
    """,
    language="sql"
)
st.write("Tento dotaz vybere všechny faktury vystavené po 1. lednu 2023.")
# Poznámka
st.info("""
**Poznámka:** Převod sloupce na `DATE` je potřebný s ohledem na typ dat, kdy dle formátu můžeme zjistit, že data jsou DATETIME s nulovým časem. Proto by nám podmínka bez převodu přímo na den nefungovala
""")

st.write("### Příklad: Použití BETWEEN pro rozsah dat")
st.code(
    """
SELECT * 
FROM Invoice
WHERE DATE(InvoiceDate) BETWEEN '2009-01-01' AND '2009-06-30';
""",
    language="sql"
)
st.write("Tento dotaz vybere všechny faktury vytvořené od 01.01.2009 do 30.06.2009.")
st.info("""
**Poznámka:** Převod sloupce na `DATE` je zde z podobného důvodu, krajní den v podmínce by nebyl zahrnut.
""")

# Vestavěné funkce pro data v SQLite
st.write("## 3. Vestavěné funkce pro práci s daty v SQLite")
st.write(
    """
    SQLite obsahuje funkce, které usnadňují práci s datumy a časy. Tyto funkce vrací text ve formátu ISO 8601 nebo numerické hodnoty podle potřeby:

    - **`DATE()`**: Vrátí pouze datum (YYYY-MM-DD).
    - **`DATETIME()`**: Vrátí datum a čas (YYYY-MM-DD HH:MM:SS).
    - **`JULIANDAY()`**: Vrátí juliánské datum (počet dní od 24. listopadu 4714 př.n.l.).
    - **`STRFTIME()`**: Umožňuje formátování datumu a času.
    - **`CURRENT_DATE`**: Vrátí aktuální datum.
    - **`CURRENT_TIMESTAMP`**: Vrátí aktuální datum a čas.
    """
)

st.write("### Příklad: Získání aktuálního datumu a času")
st.code(
    """
    SELECT CURRENT_DATE AS DnesniDatum, CURRENT_TIMESTAMP AS AktualniCas;
    """,
    language="sql"
)
st.write("Tento příkaz vrátí aktuální datum a aktuální čas ve formátu ISO 8601.")

st.write("### Příklad: Převod na jiné formáty pomocí `STRFTIME()`")
st.code(
    """
    SELECT 
        STRFTIME('%d.%m.%Y', InvoiceDate) AS FormatovaneDatum
    FROM Invoice;
    """,
    language="sql"
)
st.write("Tento dotaz převádí datum objednávky na český formát den.měsíc.rok.")

st.write("### Příklad: Výpočet rozdílu mezi datumy")
st.code(
    """
    SELECT 
        InvoiceId, 
        JULIANDAY(DATE('now')) - JULIANDAY(InvoiceDate) AS PocetDni
    FROM Invoice;
    """,
    language="sql"
)
st.write(
    "Tento dotaz vrací počet dnů mezi datem objednávky (`InvoiceDate`) a datem dnešním datem (`DATE('now')`)."
)

# Přidávání a odečítání dnů
st.write("## 4. Přidávání a odečítání dnů")
st.write(
    """
    Pomocí funkcí `DATE()` a `DATETIME()` můžeme manipulovat s daty tak, že přidáváme nebo odečítáme určité časové intervaly.

    - **`+N DAYS`**: Přidá k datumu N dní.
    - **`-N DAYS`**: Odečte od datumu N dní.
    - **Další intervaly dostupné v SQLite**:
        - `N MONTHS`, `N YEARS`, `N HOURS`, `N MINUTES`, `N SECONDS`.
    """
)

st.write("### Příklad: Přidávání dnů k datu objednávky")
st.code(
    """
SELECT 
    InvoiceId AS 'Č. faktury',
    DATE(InvoiceDate) AS 'Datum vystavení', 
    DATE(InvoiceDate, '+14 DAYS') AS 'Datum splatnosti'
FROM Invoice;
""",
    language="sql"
)
st.write(
    "Tento dotaz přidá 7 dnů k datumu vystavení faktury a vypočítá datum splatnosti."
)

# Cvičení
st.write("## 5. Cvičení pro procvičení")
st.write(
    """
**Úkoly:**

1. Vyberte faktury, které byly vystaveny po `1. srpnu 2009`.
2. Vypočítejte datum splatnosti, pokud nastává vždy měsíc po datu vystavení faktury.
3. Převádějte datum vystavení faktury do jiného formátu (například DD.MM.YYYY) s použitím `STRFTIME`.
4. Vyberte faktury, které byly vytvořeny v roce 2009.
"""
)

# Shrnutí
st.write("## Shrnutí")
st.write(
    """
    V této lekci jsme se naučili pracovat s datumy v SQLite:
    - Ukládání datumů jako text ve formátu ISO 8601.
    - Filtrování dat pomocí klauzule WHERE.
    - Používání funkcí `DATE()`, `DATETIME()`, `JULIANDAY()`, `STRFTIME()` a manipulací s datumy.
    - Převod formátu datumů a výpočty (např. rozdíl mezi datumy).

    Praktická práce s datumy usnadňuje vytváření přehledů a analýz založených na čase. 😊
    """
)
