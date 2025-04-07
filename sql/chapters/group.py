import sqlite3

import streamlit as st
import pandas as pd


@st.cache_data
def run_query(query):
    with sqlite3.connect("assets/downloads/dta_chinook.sqlite") as conn:
        return pd.read_sql_query(query, conn)


# Datasety pro příklady
DATASET_1 = pd.DataFrame({
    'Kategorie': ['Elektronika', 'Elektronika', 'Domácnost', 'Domácnost', 'Móda'],
    'Zisky': [1000, 2300, 1500, 3200, 1100]
})

DATASET_2 = pd.DataFrame({
    'Oddělení': ['HR', 'HR', 'IT', 'IT', 'Finance'],
    'Zaměstnanci': [5, 10, 20, 15, 7],
    'Mzdy': [25000, 50000, 100000, 75000, 35000]
})

DATASET_3 = pd.DataFrame({
    'Měsíc': ['Leden', 'Leden', 'Únor', 'Únor', 'Březen'],
    'Produkt': ['A', 'B', 'A', 'B', 'A'],
    'Prodej': [100, 150, 200, 100, 300]
})

DATASET_4 = pd.DataFrame({
    'Tým': ['Tým A', 'Tým A', 'Tým B', 'Tým B', 'Tým C'],
    'Body': [10, 15, 20, 25, 30],
    'Kategorie': ['Liga 1', 'Liga 1', 'Liga 2', 'Liga 2', 'Liga 1']
})

DATASET_5 = pd.DataFrame({
    'Obchod': ['Praha', 'Praha', 'Brno', 'Brno', 'Ostrava'],
    'Nákupy': [50, 60, 40, 50, 70],
    'Slevy': [5, 10, 3, 7, 6]
})

# Datasety pro příklady
DATASET_COUNT = pd.DataFrame({
    'Oddělení': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance', 'IT'],
    'Zaměstnanec': ['Jan', 'Petr', 'Anna', 'Eliška', 'Roman', 'Tomáš', 'Karel']
})

DATASET_MIN_MAX = pd.DataFrame({
    'Město': ['Praha', 'Praha', 'Brno', 'Brno', 'Ostrava'],
    'Teplota': [25, 30, 15, 20, 10]
})

# Funkce pro zobrazení teorie GROUP BY

st.title("SQL Tutoriál: GROUP BY")

st.markdown("""
## Co je GROUP BY v SQL?
`GROUP BY` se v SQL používá ke seskupení řádků na základě hodnot ve sloupci a následné aplikaci agregačních funkcí na tyto skupiny.

#### Klíčové funkce, které můžete použít:
- **SUM:** Spočítá celkový součet daného sloupce pro každou skupinu.
- **AVG:** Vypočítá průměr hodnot pro každý sloupec ve skupině.
- **COUNT:** Vrátí počet záznamů v každé skupině.
- **MIN a MAX:** Najdou minimální a maximální hodnotu v každé skupině.

#### Obecná syntaxe:
```sql
SELECT sloupec1, funkcni_agregace(sloupec2)
FROM tabulka
GROUP BY sloupec1;
```

---
## Kde GROUP BY využít?
- Analyzování prodejů podle kategorií.
- Průměrné mzdy podle oddělení firmy.
- Počet zaměstnanců podle regionů.
""")

# Funkce pro interaktivní příklady

st.title("Praktické SQL GROUP BY na databázi Chinook")

example = st.selectbox("Vyberte dotaz:", [
    "1. Počet alb podle umělců (COUNT)",
    "2. Celkový čas skladeb podle žánru (SUM)",
    "3. Průměrná cena skladeb podle médií (AVG)",
    "4. Nejdelší skladby podle žánru (MAX)",
    "5. Nejkratší skladby podle žánru (MIN)"
])

# Dotaz 1: Počet alb podle umělců
if example == "1. Počet alb podle umělců (COUNT)":
    st.subheader("Počet alb podle umělců (COUNT)")
    query = """
    SELECT Artist.Name, COUNT(Album.AlbumId) AS AlbumCount
    FROM artist
    JOIN album ON artist.ArtistId = album.ArtistId
    GROUP BY artist.Name
    ORDER BY AlbumCount DESC
    LIMIT 5;
    """
    st.markdown("""
    **SQL dotaz**:
    ```sql
    SELECT Artist.Name, COUNT(Album.AlbumId) AS AlbumCount
    FROM artist
    JOIN album ON artist.ArtistId = album.ArtistId
    GROUP BY artist.Name
    ORDER BY AlbumCount DESC
    LIMIT 5;
    ```
    """)
    result = run_query(query)
    st.dataframe(result)

# Dotaz 2: Celkový čas skladeb podle žánru
elif example == "2. Celkový čas skladeb podle žánru (SUM)":
    st.subheader("Celkový čas skladeb podle žánru (SUM)")
    query = """
    SELECT genre.Name AS Genre, SUM(track.Milliseconds) / 60000 AS TotalTimeMin
    FROM genre
    JOIN track ON genre.GenreId = track.GenreId
    GROUP BY genre.Name
    ORDER BY TotalTimeMin DESC
    LIMIT 5;
    """
    st.markdown("""
    **SQL dotaz**:
    ```sql
    SELECT genre.Name AS Genre, SUM(track.Milliseconds) / 60000 AS TotalTimeMin
    FROM genre
    JOIN track ON genre.GenreId = track.GenreId
    GROUP BY genre.Name
    ORDER BY TotalTimeMin DESC
    LIMIT 5;
    ```
    """)
    result = run_query(query)
    st.dataframe(result)

# Dotaz 3: Průměrná cena skladeb podle médií
elif example == "3. Průměrná cena skladeb podle médií (AVG)":
    st.subheader("Průměrná cena skladeb podle médií (AVG)")
    query = """
    SELECT MediaType.Name AS TypMedia, AVG(Track.UnitPrice) AS AveragePrice
    FROM MediaType
    JOIN Track ON MediaType.MediaTypeId = Track.MediaTypeId
    GROUP BY MediaType.Name
    ORDER BY AveragePrice DESC
    LIMIT 5;
    """
    st.markdown("""
    **SQL dotaz**:
    ```sql
    SELECT MediaType.Name AS TypMedia, AVG(Track.UnitPrice) AS AveragePrice
    FROM MediaType
    JOIN Track ON MediaType.MediaTypeId = Track.MediaTypeId
    GROUP BY MediaType.Name
    ORDER BY AveragePrice DESC
    LIMIT 5;
    ```
    """)
    result = run_query(query)
    st.dataframe(result)

# Dotaz 4: Nejdelší skladby podle žánru
elif example == "4. Nejdelší skladby podle žánru (MAX)":
    st.subheader("Nejdelší skladby podle žánru (MAX)")
    query = """
    SELECT genre.Name AS Zanr, MAX(track.Milliseconds) / 60000 AS LongestTrackMin
    FROM genre
    JOIN track ON genre.GenreId = track.GenreId
    GROUP BY genre.Name
    ORDER BY LongestTrackMin DESC
    LIMIT 5;
    """
    st.markdown("""
    **SQL dotaz**:
    ```sql
    SELECT genre.Name AS Zanr, MAX(track.Milliseconds) / 60000 AS LongestTrackMin
    FROM genre
    JOIN track ON genre.GenreId = track.GenreId
    GROUP BY genre.Name
    ORDER BY LongestTrackMin DESC
    LIMIT 5;
    ```
    """)
    result = run_query(query)
    st.dataframe(result)

# Dotaz 5: Nejkratší skladby podle žánru
elif example == "5. Nejkratší skladby podle žánru (MIN)":
    st.subheader("Nejkratší skladby podle žánru (MIN)")
    query = """
    SELECT genre.Name AS Zanr, track.Milliseconds / 1000 AS ShortestTrackSec
    FROM genre
    JOIN track ON genre.GenreId = track.GenreId
    GROUP BY genre.Name
    ORDER BY ShortestTrackSec ASC
    LIMIT 5;
    """
    st.markdown("""
    **SQL dotaz**:
    ```sql
    SELECT genre.Name AS Zanr, track.Milliseconds / 1000 AS ShortestTrackSec
    FROM genre
    JOIN track ON genre.GenreId = track.GenreId
    GROUP BY genre.Name
    ORDER BY ShortestTrackSec ASC
    LIMIT 5;
    ```
    """)
    result = run_query(query)
    st.dataframe(result)
