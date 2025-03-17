import streamlit as st

# Nadpis lekce
st.write("## Lekce: Subqueries (Poddotazy) v SQL s použitím databáze Chinook")

# Úvod
st.write(
    "Subqueries jsou vnořené SQL dotazy uvnitř jiného dotazu. Umožňují nám analyzovat data efektivněji a "
    "řešit složité problémy v menších krocích. V této lekci budeme používat příklady z databáze Chinook."
)

# 1. Co je subquery
st.write("### 1. Co je subquery?")
st.write(
    "Subquery je SQL dotaz vnořený do hlavního dotazu. Subquery poskytuje data pro hlavní dotaz a nejčastěji se používá "
    "v klauzulích `WHERE`, `FROM` a `SELECT`."
)

# Příklad 1: Subquery v klauzuli WHERE
st.write("#### Příklad: Subquery v klauzuli `WHERE`")
st.write("Najděte názvy alb, která byla vytvořena interpretem 'Queen':")
st.code(
    """
    SELECT Title
    FROM albums
    WHERE ArtistId = (
        SELECT ArtistId
        FROM artists
        WHERE Name = 'Queen'
    );
    """,
    language="sql"
)
st.write(
    "Tento poddotaz nejdříve najde `ArtistId` interpreta 'Queen'. Hlavní dotaz následně vyfiltruje alba tohoto interpreta.")

# 2. Subquery v klauzuli FROM
st.write("### 2. Subquery v klauzuli `FROM`")
st.write(
    "Subquery v klauzuli `FROM` umožňuje vytvořit dočasnou tabulku, která se pak používá v hlavním dotazu."
)

st.write("#### Příklad: Výpočet průměrné délky skladeb podle alb")
st.code(
    """
    SELECT AlbumId, AVG(Milliseconds) AS AvgTrackLength
    FROM (
        SELECT AlbumId, Milliseconds
        FROM tracks
    ) AS TempTable
    GROUP BY AlbumId;
    """,
    language="sql"
)
st.write(
    "V tomto příkladu subquery vytvoří dočasnou tabulku `TempTable` obsahující sloupec `AlbumId` a délku skladeb. Hlavní dotaz poté spočítá průměrnou délku skladeb pro každé album.")

# 3. Subquery v klauzuli SELECT
st.write("### 3. Subquery v klauzuli `SELECT`")
st.write(
    "Subquery v klauzuli `SELECT` se používá pro výpočet hodnot přímo v každém řádku hlavního dotazu."
)

st.write("#### Příklad: Najděte počet skladeb u každého alba")
st.code(
    """
    SELECT Title AS AlbumTitle,
           (SELECT COUNT(*)
            FROM tracks
            WHERE tracks.AlbumId = albums.AlbumId) AS TrackCount
    FROM albums;
    """,
    language="sql"
)
st.write("Tento poddotaz počítá počet skladeb (`TrackCount`) pro každé album (`AlbumTitle`).")

# 4. Korelované a nekorelované subqueries
st.write("### 4. Korelované vs nekorelované subqueries")

# Nekorelované poddotazy
st.write("#### a) Nekorelované subqueries")
st.write("Nekorelovaný subquery je nezávislý na hlavním dotazu a vykoná se nejdříve.")
st.write("Příklad: Zjistěte názvy alb, která mají více skladeb než průměrný počet skladeb na albu:")
st.code(
    """
    SELECT Title
    FROM albums
    WHERE (
        SELECT COUNT(*)
        FROM tracks
        WHERE tracks.AlbumId = albums.AlbumId
    ) > (
        SELECT AVG(TrackCount)
        FROM (
            SELECT COUNT(*) AS TrackCount
            FROM tracks
            GROUP BY AlbumId
        )
    );
    """,
    language="sql"
)
st.write(
    "V tomto příkladu průměrný počet skladeb na albu se počítá samostatně jako nekorelovaný poddotaz."
)

# Korelované poddotazy
st.write("#### b) Korelované subqueries")
st.write(
    "Korelovaný subquery se vykonává pro každý řádek hlavního dotazu a závisí na datech tohoto řádku."
)
st.write(
    "Příklad: Najděte zákazníky, kteří utratili více za nákup než průměrná částka všech zákazníků:"
)
st.code(
    """
    SELECT FirstName, LastName
    FROM customers c
    WHERE (
        SELECT SUM(i.Total)
        FROM invoices i
        WHERE i.CustomerId = c.CustomerId
    ) > (
        SELECT AVG(Total)
        FROM invoices
    );
    """,
    language="sql"
)
st.write(
    "Tento dotaz najde zákazníky, jejichž celková útrata (`SUM(i.Total)`) je vyšší než průměr všech částek (`AVG(Total)`)."
)

# 5. Cvičení na procvičení
st.write("### 5. Cvičení na procvičení")
st.write("Vyřešte následující úlohy s použitím databáze Chinook:")
st.write(
    """
1. Najděte jména interpretů, kteří mají více než jedno album.
2. Najděte názvy skladeb, jejichž délka je delší než průměrná délka všech skladeb.
3. Zjistěte název alba, které má nejvíce skladeb.
4. Najděte zákazníky, kteří nakoupili více než 3 faktury.
"""
)

# Závěr
st.write("### Závěr")
st.write(
    "Subqueries jsou mocným nástrojem, který nám umožňuje řešit komplexní problémy v SQL. Databáze Chinook nabízí skvělá data na procvičení,"
    "takže neváhejte experimentovat s dalšími dotazy!"
)
