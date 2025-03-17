import streamlit as st

# Nadpis lekce
st.write("# Základy SQL - SELECT, FROM, AS")

# Úvod
st.write(
    """
    V této lekci se naučíte používat základní příkazy:

    - **SELECT** - výběr sloupců z tabulky
    - **FROM** - definice zdrojové tabulky
    - **AS** - použití aliasů pro přejmenování tabulek nebo sloupců
    """
)

# Sekce 1: SELECT a FROM
st.write("## 1. SELECT a FROM")
st.write(
    """
    Příkaz **SELECT** slouží k výběru dat ze zvolených sloupců tabulky a spolu s 
    **FROM** specifikuje tabulku, ze které se data budou vybírat.

    **Syntaxe:**
    ```sql
    SELECT sloupce
    FROM tabulka;
    ```
    """
)

# Příklad SELECT a FROM
st.write("#### Příklad 1: Výběr všech sloupců z tabulky")
st.code(
    """
    SELECT * 
    FROM Customer;
    """,
    language="sql"
)
st.write("Tento příkaz vybere všechna data (všechny sloupce) z tabulky `customers`.")

st.write("#### Příklad 2: Výběr vybraných sloupců")
st.code(
    """
    SELECT FirstName, LastName
    FROM Customer;
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere pouze sloupce `FirstName` a `LastName` z tabulky `customers`. "
    "Používáme ho, pokud nepotřebujeme všechny sloupce."
)

# Sekce 2: Použití aliasů s AS
st.write("## 2. Alias (AS)")
st.write(
    """
    Alias slouží k přejmenování sloupců nebo tabulek pro zjednodušení nebo zpřehlednění výsledků. 
    Používáme klíčové slovo **AS**, abychom zajistili čitelnější nebo specifický výstup.

    **Syntaxe:**
    ```sql
    SELECT sloupec AS alias
    FROM tabulka;
    ```
    Alias lze použít i pro přejmenování tabulek.
    """
)

# Příklad aliasů
st.write("#### Příklad 3: Použití aliasu na sloupec")
st.code(
    """
    SELECT FirstName AS Jmeno, LastName AS Prijmeni
    FROM customers;
    """,
    language="sql"
)
st.write("Tento příkaz přejmenuje sloupce tak, že `FirstName` se zobrazí jako `Jmeno` a `LastName` jako `Prijmeni`.")

st.write("#### Příklad 4: Použití aliasu na tabulku")
st.code(
    """
    SELECT c.FirstName, c.LastName
    FROM customers AS c;
    """,
    language="sql"
)
st.write(
    "Tento příkaz definuje alias `c` pro tabulku `customers`. Namísto celého názvu tabulky je pak možné použít alias `c`, což zjednodušuje psaní."
)

# Sekce 3: Kombinace SELECT, FROM a AS
st.write("## 3. Kombinace SELECT, FROM a AS")
st.write(
    """
    Můžeme kombinovat příkaz **SELECT**, zdrojovou tabulku pomocí **FROM** a aliasy **AS**, 
    abychom získali dobře strukturované a přehledné výsledky.
    """
)

# Příklad kombinace
st.write("#### Příklad 5: Kombinovaný příkaz")
st.code(
    """
    SELECT c.FirstName AS Jmeno, c.LastName AS Prijmeni
    FROM customers AS c;
    """,
    language="sql"
)
st.write(
    "Výše uvedený příkaz vybírá jména a příjmení zákazníků z tabulky `customers`. "
    "Alias `c` je použit pro zpřehlednění zápisu."
)

# Sekce 4: Cvičení
st.write("## 4. Cvičení na procvičení")
st.write(
    """
**Úkoly**:

1. Vytvořte příkaz, který vybere všechny sloupce z tabulky `albums`.
2. Vyberte pouze název alba (`Title`) z tabulky `albums` a přiřaďte sloupci alias `Nazev_Alba`.
3. Použijte alias pro tabulku `tracks` a vyberte sloupec `Name` (přidejte mu alias `Skladba`) a `UnitPrice`.
"""
)

# Sekce 5: Shrnutí
st.write("## Shrnutí")
st.write(
    """
    V této lekci jsme se naučili používat:

    - **SELECT**: Pro výběr konkrétních sloupců nebo všech dat z tabulky.
    - **FROM**: Pro specifikaci zdrojové tabulky.
    - **AS (alias)**: Pro přejmenování sloupců nebo tabulek v dotazech.

    Tyto základní konstrukce SQL tvoří jádro většiny dotazů. Procvičte si je a postupujte na složitější příkazy!
    """
)
