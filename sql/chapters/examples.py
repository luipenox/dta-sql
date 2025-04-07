import streamlit as st

# Definice příkladů
examples = [
    {
        "level": "Začátečník",
        "title": "01. Seznam všech umělců",
        "description": "Vypište jména všech umělců uložených v databázi.",
        "sql": """
        SELECT 
            ArtistId, Name 
        FROM 
            Artist;
        """
    },
    {
        "level": "Začátečník",
        "title": "02. Všechna alba konkrétního umělce",
        "description": "Najděte všechna alba umělce s názvem 'AC/DC'.",
        "sql": """
        SELECT 
            AlbumId, Title 
        FROM 
            Album
        WHERE 
            ArtistId = (
                SELECT ArtistId 
                FROM Artist 
                WHERE Name = 'AC/DC'
            );
        """
    },
    {
        "level": "Mírně pokročilý",
        "title": "03. Počet skladeb v každém albu",
        "description": "Zjistěte počet skladeb obsažených v každém albu.",
        "sql": """
        SELECT 
            Album.Title AS Album, 
            COUNT(Track.TrackId) AS PocetSkladeb
        FROM 
            Album
        JOIN 
            Track ON Album.AlbumId = Track.AlbumId
        GROUP BY 
            Album.Title
        ORDER BY 
            Album.Title;
        """
    },
    {
        "level": "Mírně pokročilý",
        "title": "04. Zákazníci podle země",
        "description": "Najděte počet zákazníků v každé zemi a seřaďte podle počtu zákazníků.",
        "sql": """
        SELECT 
            Country, 
            COUNT(CustomerId) AS PocetZakazniku
        FROM 
            Customer
        GROUP BY 
            Country
        ORDER BY 
            PocetZakazniku DESC;
        """
    },
    {
        "level": "Pokročilý",
        "title": "05. Nejprodávanější skladby",
        "description": "Zjistěte název skladby a počet prodejů, seřaďte je podle počtu prodejů sestupně.",
        "sql": """
        SELECT 
            Track.Name AS Skladba, 
            COUNT(InvoiceLine.InvoiceLineId) AS PocetProdeju
        FROM 
            Track
        JOIN 
            InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
        GROUP BY 
            Track.Name
        ORDER BY 
            PocetProdeju DESC;
        """
    },
    {
        "level": "Pokročilý",
        "title": "06. Nejčastější žánr skladeb",
        "description": "Zjistěte, který hudební žánr má nejvíce skladeb v databázi.",
        "sql": """
        SELECT 
            Genre.Name AS Zanr, 
            COUNT(Track.TrackId) AS PocetSkladeb
        FROM 
            Genre
        JOIN 
            Track ON Genre.GenreId = Track.GenreId
        GROUP BY 
            Genre.Name
        ORDER BY 
            PocetSkladeb DESC
        LIMIT 1;
        """
    },
    {
        "level": "Expertní",
        "title": "07. Největší útrata zákazníka",
        "description": "Zjistěte jméno zákazníka s nejvyšší útratou a jeho celkovou útratu.",
        "sql": """
        SELECT 
            Customer.FirstName || ' ' || Customer.LastName AS Zakaznik,
            SUM(Invoice.Total) AS CelaUtrata
        FROM 
            Customer
        JOIN 
            Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY 
            Customer.CustomerId
        ORDER BY 
            CelaUtrata DESC
        LIMIT 1;
        """
    },
    {
        "level": "Expertní",
        "title": "08. Průměrná délka skladeb podle žánru",
        "description": "Zjistěte průměrnou délku skladeb (v sekundách) pro každý žánr.",
        "sql": """
        SELECT 
            Genre.Name AS Zanr, 
            AVG(Track.Milliseconds) / 1000 AS PrumernaDelkaSekundy
        FROM 
            Genre
        JOIN 
            Track ON Genre.GenreId = Track.GenreId
        GROUP BY 
            Genre.Name
        ORDER BY 
            PrumernaDelkaSekundy DESC;
        """
    },
    {
        "level": "Expertní",
        "title": "09. Zaměstnanci a počet jejich zákazníků",
        "description": "Zjistěte, kolik zákazníků spravuje každý zaměstnanec.",
        "sql": """
        SELECT 
            Employee.FirstName || ' ' || Employee.LastName AS Zamestnanec,
            COUNT(Customer.CustomerId) AS PocetZakazniku
        FROM 
            Employee
        LEFT JOIN 
            Customer ON Employee.EmployeeId = Customer.SupportRepId
        GROUP BY 
            Employee.EmployeeId
        ORDER BY 
            PocetZakazniku DESC;
        """
    },
    {
        "level": "Expertní",
        "title": "10. Nejlépe prodávané žánry skladeb",
        "description": "Zjistěte, které hudební žánry skladeb mají největší prodeje a jejich celkovou hodnotu.",
        "sql": """
        SELECT
            Genre.Name AS Zanr,
            SUM(InvoiceLine.Quantity) AS PocetProdeju,
            SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS CelkoveTrzby
        FROM 
            Genre
        JOIN 
            Track ON Genre.GenreId = Track.GenreId
        JOIN 
            InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
        GROUP BY 
            Genre.Name
        ORDER BY 
            CelkoveTrzby DESC;
        """
    }
]

# Hlavní funkce aplikace
st.title("Databáze Chinook - SQL Příklady")
st.title("Navigace")

# Výběr příkladu
example_titles = [e["title"] for e in examples]
selected_title = st.selectbox("Vyberte příklad:", options=example_titles)

# Najít odpovídající příklad
selected_example = next(e for e in examples if e["title"] == selected_title)

# Zobrazení zadání a řešení
st.header(selected_example["title"])
st.markdown(f"**Obtížnost:** {selected_example['level']}")
st.markdown(f"**Zadání:** {selected_example['description']}")
st.markdown("**Řešení (SQL dotaz):**")
show_code = st.toggle("Zobrazit řešení")
if show_code:
    st.code(selected_example["sql"], language="sql")
else:
    st.code("... (skryto) ...", language="sql")
