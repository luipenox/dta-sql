import streamlit as st


st.title("Úvod do SQL")

    # 1. Co je SQL?
st.write("### 1. Co je SQL?")
st.write(
    "SQL (Structured Query Language) je standardizovaný jazyk pro komunikaci s relačními databázemi. "
    "Poskytuje prostředky pro vytváření, manipulaci a dotazování databází. "
    "SQL umožňuje vývojářům ukládat, upravovat, mazat a načítat data z tabulek definovaných v databázi. "
    "Jedná se o neprocedurální jazyk, což znamená, že uživatelé zadávají, co chtějí získat, místo popisu, jak to má být provedeno."
)

# 2. Použití SQL
st.write("### 2. Použití SQL:")
st.write(
    "SQL využívají relační databázové systémy, jako je MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database a další. "
    "Jazyk se používá ve třech hlavních oblastech: Definice dat (DDL) pro definici struktury databáze (tabulky, schémata, indexy), "
    "manipulace s daty (DML) pro přidávání, upravování a odstraňování záznamů a řízení přístupu (DCL) k nastavování práv pro uživatele databáze."
)

# 3. Základní struktura příkazů
st.write("### 3. Základní struktura příkazů:")
st.write(
    "SQL disponuje mnoha příkazy, přičemž mezi nejčastěji používané patří:"
)
st.write("- `SELECT` pro vybírání dat z tabulek.")
st.write("- `INSERT` pro přidání nových záznamů.")
st.write("- `UPDATE` pro aktualizaci existujících dat.")
st.write("- `DELETE` pro odstranění záznamů z tabulek.")
st.write(
    "Například příkaz `SELECT * FROM users;` zobrazí všechny sloupce a řádky z tabulky `users`."
)

# 4. Relační databáze
st.write("### 4. Relační databáze:")
st.write(
    "SQL je úzce spojeno s tzv. relačními databázemi, kde jsou data ukládána v tabulkách (řádky a sloupce). "
    "Každá tabulka má unikátní název, primární klíče a může tvořit vztahy s jinými tabulkami prostřednictvím cizích klíčů. "
    "Tato struktura umožňuje efektivní správu velkého množství dat a jejich rychlé vyhledávání díky optimálnímu indexování."
)

# 5. Varianty a rozšíření SQL
st.write("### 5. Varianty a rozšíření SQL:")
st.write(
    "Různé databázové systémy implementují vlastní rozšíření SQL. "
    "Například Oracle SQL poskytuje proprietární funkce, Microsoft SQL Server má T-SQL, "
    "zatímco PostgreSQL nabízí pokročilé datové typy a rozšíření jazyka. Přesto je jádro SQL standardizováno normou ANSI/ISO, "
    "což zajišťuje jeho obecnou přenositelnost mezi databázemi, byť s drobnými úpravami."
)
