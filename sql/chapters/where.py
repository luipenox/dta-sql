import streamlit as st

# Nadpis lekce
st.write("# Lekce: Použití WHERE v SQL")

# Úvod
st.write(
    """
    Klauzule **WHERE** slouží k filtrování výsledků dotazu v SQL. 
    Pomocí této klauzule můžeme získat pouze ty řádky, které splňují zadané podmínky.

    **Syntaxe**:
    ```sql
    SELECT sloupce
    FROM tabulka
    WHERE podmínka;
    ```
    """
)

# Základní použití WHERE
st.write("## 1. Základní použití WHERE")
st.write(
    """
    Klauzuli **WHERE** můžeme použít například k hledání záznamů na základě konkrétní hodnoty nebo 
    k filtrování podle specifických kritérií.
    """
)

# Příklad 1: Základní podmínka
st.write("#### Příklad: Filtrování zákazníků s ID větším než 5")
st.code(
    """
    SELECT * 
    FROM Customer
    WHERE CustomerId > 5;
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere všechny sloupce z tabulky `customers`, ale pouze pro záznamy, kde je `CustomerId` větší než 5."
)

# Operátory
st.write("## 2. Operátory v klauzuli WHERE")
st.write(
    """
    Pomocí **WHERE** můžeme používat různé operátory pro vytvoření podmínek:

    - `=` - rovná se
    - `<>` nebo `!=` - nerovná se
    - `>` - větší než
    - `<` - menší než
    - `>=` - větší nebo rovno
    - `<=` - menší nebo rovno
    - `BETWEEN` - hodnoty v určitém rozsahu (`AND` jako spojka mezi hodnotami)
    - `LIKE` - vyhledávání vzoru
    - `IN` - kontrola, zda hodnota patří do seznamu
    """
)

st.write("#### Příklad: Použití operátorů")
st.code(
    """
    SELECT * 
    FROM Customer
    WHERE Country = 'Canada';
    """,
    language="sql"
)
st.write("Tento příkaz vybere všechny zákazníky z tabulky `customers`, kteří mají zemi `Canada`.")

st.code(
    """
    SELECT * 
    FROM Customer
    WHERE CustomerId BETWEEN 10 AND 15;
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere zákazníky s `CustomerId` v rozsahu od 10 do 15 (včetně)."
)

st.code(
    """
    SELECT * 
    FROM Customer
    WHERE Country IN ('USA', 'Canada', 'Mexico');
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere zákazníky ze zemí `USA`, `Canada` nebo `Mexico`. Operátor **IN** je užitečný pro kontrolu více hodnot."
)

# LIKE a vzory
st.write("## 3. Vyhledávání vzorů pomocí LIKE")
st.write(
    """
    Klauzule **LIKE** umožňuje vyhledávat hodnoty, které odpovídají určitému vzoru. Používají se speciální znaky:

    - `%` - nahrazuje libovolný počet znaků (včetně žádného)
    - `_` - nahrazuje přesně jeden znak
    """
)

st.write("#### Příklad: Hledání jmen začínajících na 'A'")
st.code(
    """
    SELECT * 
    FROM Customer
    WHERE FirstName LIKE 'A%';
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere všechny zákazníky, jejichž křestní jméno (`FirstName`) začíná na písmeno `A`."
)

st.write("#### Příklad: Hledání jmen s druhým znakem 'l'")
st.code(
    """
    SELECT * 
    FROM Customer
    WHERE FirstName LIKE '_l%';
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere všechny zákazníky, jejichž křestní jméno má na druhé pozici písmeno `l`."
)

# Logické operátory
st.write("## 4. Kombinace podmínek pomocí AND a OR")
st.write(
    """
    Pomocí logických operátorů **AND** a **OR** můžeme kombinovat více podmínek:

    - **AND**: Obě podmínky musí být splněny.
    - **OR**: Stačí, aby byla splněna alespoň jedna z podmínek.
    """
)

st.write("#### Příklad: Použití AND")
st.code(
    """
    SELECT * 
    FROM Customer
    WHERE Country = 'Canada' AND CustomerId > 5;
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere zákazníky z Kanady, kteří mají `CustomerId` větší než 5. Obě podmínky musí být splněny."
)

st.write("#### Příklad: Použití OR")
st.code(
    """
    SELECT * 
    FROM Customer
    WHERE Country = 'Canada' OR Country = 'USA';
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere zákazníky, kteří mají zemi `Canada` nebo `USA`. Stačí, aby byla splněna jedna z podmínek."
)

st.write("### Použití AND a OR v SQL")

st.write("""
V SQL se klauzule **AND** a **OR** používají k sestavování složitějších podmínek v dotazech.
Pomocí těchto operátorů můžete kombinovat více pravidel v klauzuli **WHERE**. 
Závorky `()` se používají k řízení pořadí vyhodnocování podmínek (prioritizace) a zajištění správného výsledku.
""")

# Ukázka použití
st.write("#### Ukázka: Kombinace AND a OR")
st.code("""
SELECT *
FROM employees
WHERE (Department = 'Sales' OR Department = 'Marketing') AND Status = 'Active';
""", language="sql")
st.write("""
Tento dotaz najde všechny aktivní zaměstnance, kteří pracují buď v oddělení "Sales" nebo "Marketing". 
Závorky určují, že se podmínka OR (Sales nebo Marketing) vyhodnocuje jako první, 
a teprve poté se aplikuje podmínka AND.
""")

# Titulek
st.write("## 5. Práce s NULL v SQL")

# Popis
st.write("""
V SQL můžete v podmínce **WHERE** vyhledávat hodnoty, které jsou `NULL` (nebo naopak nejsou `NULL`), pomocí speciálních výrazů `IS NULL` a `IS NOT NULL`. 
Hodnoty `NULL` představují chybějící nebo neznámá data, a proto vyžadují tyto specifické operátory, protože standardní podmínky jako `=` nebo `!=` s `NULL` nefungují.
""")

# Ukázka: Vyhledávání NULL
st.write("#### Ukázka: Vyhledávání hodnot NULL")
st.code("""
SELECT *
FROM Customer
WHERE Email IS NULL;
""", language="sql")
st.write("Tento dotaz najde všechny zákazníky, kteří nemají zadanou e-mailovou adresu.")

# Ukázka: Vyhledávání hodnot, které nejsou NULL
st.write("#### Ukázka: Vyhledávání nenullových hodnot")
st.code("""
SELECT *
FROM Customer
WHERE Email IS NOT NULL;
""", language="sql")
st.write("Tento dotaz vrátí všechny zákazníky, kteří mají zadanou e-mailovou adresu.")

# Poznámka
st.info("""
**Poznámka:** Operátory `IS NULL` a `IS NOT NULL` jsou nezbytné, 
protože podmínky jako `= NULL` nebo `!= NULL` v SQL nefungují správně. 
V SQL se `NULL` považuje za speciální hodnotu, která není rovná ani jinému `NULL`.
""")

# Cvičení
st.write("## 5. Cvičení na procvičení")
st.write(
    """
**Úkoly**:

1. Vyberte všechny zákazníky, kteří mají `CustomerId` menší než 10.
2. Najděte všechny zákazníky, kteří pochází z Německa (**Germany**) nebo Francie (**France**).
3. Vyberte zákazníky, jejichž jméno obsahuje písmeno `z` (bez ohledu na pozici) pomocí **LIKE**.
4. Najděte zákazníky, kteří mají `CustomerId` v rozsahu od 20 do 30 a pochází z Velké Británie (**United Kingdom**).
5. Najděte všechny zákazníky, kteři nemají vyplněnou společnost.
"""
)

# Shrnutí
st.write("## Shrnutí")
st.write(
    """
    V této lekci jste se naučili používat klauzuli **WHERE** a její různé možnosti:

    - Filtrování výsledků na základě podmínek.
    - Používání operátorů jako `=`, `>`, `<`, `BETWEEN`, `IN` a `LIKE`.
    - Kombinace více podmínek pomocí logických operátorů `AND` a `OR`.

    Klauzule **WHERE** je klíčem k získání konkrétních dat z databáze. Procvičte si ji na různých příkladech!
    """
)
