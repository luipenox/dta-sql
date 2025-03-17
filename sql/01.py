import streamlit as st

# Nadpis lekce
st.write("## Lekce: Základy SQL SELECT")

# 1. Co je SQL SELECT
st.write("### 1. Co je SQL SELECT?")
st.write(
    "`SELECT` je základní SQL příkaz, který se používá k načtení dat z databáze. "
    "Je to jeden z nejpoužívanějších příkazů v SQL a umožňuje vám z tabulek filtrovat, třídit a vybírat určitá data."
)
st.write("Syntaxe základního SELECT příkazu vypadá takto:")
st.code(
    "SELECT sloupce\n"
    "FROM tabulka;",
    language="sql"
)
st.write(
    "Příkaz vybere data z jednoho nebo více sloupců dané tabulky.\n"
    "Pokud chcete vybrat všechny sloupce, můžete použít znak `*`."
)

# 2. Příklad s hvězdičkou `*`
st.write("### 2. Příklad: Výběr všech sloupců")
st.write(
    "Předpokládejme, že máte tabulku `customer` a chcete zobrazit všechny sloupce z této tabulky:"
)
st.code(
    "SELECT *\n"
    "FROM customer;",
    language="sql"
)
st.write("Tento příkaz vrátí všechny sloupce a všechny řádky z tabulky `customer`.")

# 3. Výběr specifických sloupců
st.write("### 3. Výběr specifických sloupců")
st.write(
    "Někdy potřebujete pouze některé sloupce z tabulky. Například zobrazíme jména a příjmení zákazníků:"
)
st.code(
    "SELECT first_name, last_name\n"
    "FROM customer;",
    language="sql"
)
st.write("Tento příkaz vrátí pouze dva sloupce: `first_name` a `last_name`.")

# 4. Použití aliasů (AS)
st.write("### 4. Použití aliasů (AS)")
st.write(
    "Pomocí klíčového slova `AS` můžete dát sloupcům nebo tabulkám nové názvy (aliasy) pro snadnější čtení výsledků."
)
st.write("#### Příklad:")
st.code(
    "SELECT first_name AS jmeno, last_name AS prijmeni\n"
    "FROM customer;",
    language="sql"
)
st.write(
    "Tento příkaz vrátí stejná data jako předchozí příklad, ale sloupce budou přejmenovány na `jmeno` a `prijmeni`."
)

# 5. Filtrování dat pomocí WHERE
st.write("### 5. Filtrování dat pomocí WHERE")
st.write(
    "Pomocí `WHERE` klauzule můžete filtrovat řádky, které splňují určitou podmínku."
)
st.write("#### Příklad: Zákazníci z konkrétního města:")
st.code(
    "SELECT first_name, last_name\n"
    "FROM customer\n"
    "WHERE city = 'Prague';",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí pouze zákazníky, kteří žijí ve městě **Prague**."
)

# 6. Třídění výsledků pomocí ORDER BY
st.write("### 6. Třídění výsledků pomocí ORDER BY")
st.write(
    "Data můžete seřadit vzestupně (`ASC`) nebo sestupně (`DESC`) pomocí klauzule `ORDER BY`."
)
st.write("#### Příklad: Seřazení zákazníků podle příjmení:")
st.code(
    "SELECT first_name, last_name\n"
    "FROM customer\n"
    "ORDER BY last_name ASC;",
    language="sql"
)
st.write(
    "Tento příkaz seřadí zákazníky podle jejich příjmení vzestupně. Pokud chcete sestupné pořadí, použijte `DESC`."
)

# 7. Omezování počtu výsledků pomocí LIMIT
st.write("### 7. Omezování počtu výsledků pomocí LIMIT")
st.write(
    "Pomocí `LIMIT` můžete omezit počet vrácených výsledků."
)
st.write("#### Příklad: Zobrazit 10 prvních zákazníků:")
st.code(
    "SELECT first_name, last_name\n"
    "FROM customer\n"
    "LIMIT 10;",
    language="sql"
)
st.write(
    "Tento příkaz vrátí prvních 10 zákazníků z tabulky."
)

# 8. Kombinace: SELECT s WHERE, ORDER BY a LIMIT
st.write("### 8. Kombinace SELECT s WHERE, ORDER BY a LIMIT")
st.write(
    "Můžete kombinovat různé klauzule pro složitější dotazy."
)
st.write("#### Příklad:")
st.code(
    "SELECT first_name, last_name\n"
    "FROM customer\n"
    "WHERE city = 'Berlin'\n"
    "ORDER BY last_name DESC\n"
    "LIMIT 5;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí 5 zákazníků z města **Berlin**, seřazených sestupně podle příjmení."
)

# 9. Cvičení
st.write("### 9. Cvičení: Vyzkoušejte si sami")
st.write("""
1. Zobrazte seznam všech sloupců z tabulky `film`.
2. Vyberte pouze názvy filmů (`title`) a jejich ceny vypůjčky (`rental_rate`) z tabulky `film`.
3. Zobrazte jména zákazníků z města **Paris**, seřazená podle jména vzestupně.
4. Najděte 3 nejdražší filmy z tabulky `film` (seřazené podle `rental_rate` sestupně).
5. Použijte aliasy pro sloupce `first_name` a `last_name` z tabulky `staff` a přejmenujte je na `jmeno` a `prijmeni`.
""")

# Závěr
st.write("### Závěr")
st.write(
    "V této lekci jsme se naučili základy příkazu `SELECT` v SQL, včetně filtrování, třídění, limitování a použití aliasů. "
    "Tyto základy jsou klíčem k úspěšné práci s databázemi."
)
st.write("Pokud máte k dotazům typu `SELECT` otázky nebo potřebujete s něčím pomoci, dejte mi vědět! 😊")
