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
    FROM customers
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

    - **=**: Rovná se
    - **<> nebo !=**: Nerovná se
    - **>**: Větší než
    - **<**: Menší než
    - **>=**: Větší nebo rovno
    - **<=**: Menší nebo rovno
    - **BETWEEN**: Hodnoty v určitém rozsahu
    - **LIKE**: Vyhledávání vzoru
    - **IN**: Kontrola, zda hodnota patří do seznamu
    """
)

st.write("#### Příklad: Použití operátorů")
st.code(
    """
    SELECT * 
    FROM customers
    WHERE Country = 'Canada';
    """,
    language="sql"
)
st.write("Tento příkaz vybere všechny zákazníky z tabulky `customers`, kteří mají zemi `Canada`.")

st.code(
    """
    SELECT * 
    FROM customers
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
    FROM customers
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

    - **%**: Nahrazuje libovolný počet znaků (včetně žádného).
    - **_**: Nahrazuje přesně jeden znak.
    """
)

st.write("#### Příklad: Hledání jmen začínajících na 'A'")
st.code(
    """
    SELECT * 
    FROM customers
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
    FROM customers
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
    FROM customers
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
    FROM customers
    WHERE Country = 'Canada' OR Country = 'USA';
    """,
    language="sql"
)
st.write(
    "Tento příkaz vybere zákazníky, kteří mají zemi `Canada` nebo `USA`. Stačí, aby byla splněna jedna z podmínek."
)

# Cvičení
st.write("## 5. Cvičení na procvičení")
st.write(
    """
**Úkoly**:

1. Vyberte všechny zákazníky, kteří mají `CustomerId` menší než 10.
2. Najděte všechny zákazníky, kteří pochází z Německa (**Germany**) nebo Francie (**France**).
3. Vyberte zákazníky, jejichž jméno obsahuje písmeno `z` (bez ohledu na pozici) pomocí **LIKE**.
4. Najděte zákazníky, kteří mají `CustomerId` v rozsahu od 20 do 30 a pochází z Velké Británie (**United Kingdom**).
"""
)

# Shrnutí
st.write("## Shrnutí")
st.write(
    """
    V této lekci jste se naučili používat klauzuli **WHERE** a její různé možnosti:

    - Filtrování výsledků na základě podmínek.
    - Používání operátorů jako **=**, **>**, **<**, **BETWEEN**, **IN** a **LIKE**.
    - Kombinace více podmínek pomocí logických operátorů **AND** a **OR**.

    Klauzule **WHERE** je klíčem k získání konkrétních dat z databáze. Procvičte si ji na různých příkladech!
    """
)
