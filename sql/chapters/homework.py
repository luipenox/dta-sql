import streamlit as st

examples = [
    # Základní příklady - SQL pro začátečníky
    {
        "level": "Začátečník",
        "title": "01. Seznam všech zákazníků",
        "description": "Vypište seznam všech zákazníků včetně jejich jména, příjmení a země.",
        "sql": """
        SELECT 
            CustomerId, FirstName, LastName, Country 
        FROM 
            Customer
        ORDER BY 
            LastName, FirstName;
        """
    },
    {
        "level": "Začátečník",
        "title": "02. Skladby určitého žánru",
        "description": "Vypište všechny skladby v žánru 'Rock'.",
        "sql": """
        SELECT 
            Name AS Skladba 
        FROM 
            Track
        WHERE 
            GenreId = (
                SELECT GenreId 
                FROM Genre 
                WHERE Name = 'Rock'
            );
        """
    },
    {
        "level": "Začátečník",
        "title": "03. Alba a jejich umělci",
        "description": "Vypište názvy všech alb a jejich umělců.",
        "sql": """
        SELECT 
            Album.Title AS Album,
            Artist.Name AS Umelec
        FROM 
            Album
        JOIN 
            Artist ON Album.ArtistId = Artist.ArtistId
        ORDER BY 
            Umelec, Album;
        """
    },
    {
        "level": "Začátečník",
        "title": "04. Fakturní částky",
        "description": "Zobrazte ID faktury a její celkovou částku.",
        "sql": """
        SELECT 
            InvoiceId, Total AS Castka 
        FROM 
            Invoice
        ORDER BY 
            Total DESC;
        """
    },
    {
        "level": "Začátečník",
        "title": "05. Zákazníci z určité země",
        "description": "Najděte všechny zákazníky, kteří pocházejí z Kanady (Canada).",
        "sql": """
        SELECT 
            CustomerId, FirstName, LastName, Country 
        FROM 
            Customer
        WHERE 
            Country = 'Canada';
        """
    },
    {
        "level": "Začátečník",
        "title": "06. Nejkratší skladba",
        "description": "Najděte název a délku nejkratší skladby v databázi.",
        "sql": """
        SELECT 
            Name AS Skladba, 
            Milliseconds AS Doba 
        FROM 
            Track
        ORDER BY 
            Milliseconds ASC
        LIMIT 1;
        """
    },
    {
        "level": "Začátečník",
        "title": "07. Typy médií",
        "description": "Vypište všechny typy médií (například MP3, AAC).",
        "sql": """
        SELECT 
            * 
        FROM 
            MediaType;
        """
    },
    {
        "level": "Začátečník",
        "title": "08. Fakturní data a částky",
        "description": "Zobrazte všechna data fakturace a jejich celkové částky, seřazené od nejvyšší částky.",
        "sql": """
        SELECT 
            InvoiceDate AS Datum, Total AS Castka 
        FROM 
            Invoice
        ORDER BY 
            Total DESC;
        """
    },
    {
        "level": "Začátečník",
        "title": "09. Počet zákazníků v každé zemi",
        "description": "Zjistěte počet zákazníků v každé zemi.",
        "sql": """
        SELECT 
            Country, COUNT(CustomerId) AS Pocet 
        FROM 
            Customer
        GROUP BY 
            Country
        ORDER BY 
            Pocet DESC;
        """
    },
    {
        "level": "Začátečník",
        "title": "10. Nejnovější faktury",
        "description": "Najděte posledních 5 faktur podle data vydání.",
        "sql": """
        SELECT 
            InvoiceId, InvoiceDate 
        FROM 
            Invoice
        ORDER BY 
            InvoiceDate DESC
        LIMIT 5;
        """
    },

    # Mírně pokročilé příklady
    {
        "level": "Mírně pokročilý",
        "title": "11. Nejdelší skladby podle žánru",
        "description": "Zjistěte nejdelší skladbu pro každý žánr.",
        "sql": """
        SELECT 
            Genre.Name AS Zanr, 
            Track.Name AS Skladba, 
            MAX(Track.Milliseconds) AS NejdelsiDoba 
        FROM 
            Genre
        JOIN 
            Track ON Genre.GenreId = Track.GenreId
        GROUP BY 
            Genre.GenreId
        ORDER BY 
            NejdelsiDoba DESC;
        """
    },
    {
        "level": "Mírně pokročilý",
        "title": "12. Alba obsahující 20 a více skladeb",
        "description": "Najděte názvy alb, která obsahují alespoň 20 skladeb.",
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
        HAVING 
            COUNT(Track.TrackId) >= 20
        ORDER BY 
            PocetSkladeb DESC;
        """
    },
    {
        "level": "Mírně pokročilý",
        "title": "13. Průměrná cena skladeb podle typu médií",
        "description": "Zjistěte průměrnou cenu skladeb pro každý typ média.",
        "sql": """
        SELECT 
            MediaType.Name AS TypMedia, 
            AVG(Track.UnitPrice) AS PrumernaCena 
        FROM 
            MediaType
        JOIN 
            Track ON MediaType.MediaTypeId = Track.MediaTypeId
        GROUP BY 
            MediaType.Name
        ORDER BY 
            PrumernaCena DESC;
        """
    },
    {
        "level": "Mírně pokročilý",
        "title": "14. Zákazníci bez zařazených faktur",
        "description": "Najděte zákazníky, kteří nemají žádné faktury.",
        "sql": """
        SELECT 
            Customer.CustomerId, 
            Customer.FirstName, 
            Customer.LastName 
        FROM 
            Customer
        LEFT JOIN 
            Invoice ON Customer.CustomerId = Invoice.CustomerId
        WHERE 
            Invoice.CustomerId IS NULL;
        """
    },
    {
        "level": "Mírně pokročilý",
        "title": "15. Skladby s cenou přes 1 USD",
        "description": "Zjistěte jména skladeb s cenou vyšší než 1 USD.",
        "sql": """
        SELECT 
            Name AS Skladba, UnitPrice AS Cena 
        FROM 
            Track
        WHERE 
            UnitPrice > 1;
        """
    },

    # Dalších 15 příkladů lze přidat podobně jako je zde uvedeno.

    # Placeholder pro demonstraci
    {
        "level": "Expertní",
        "title": "16. Komplexní dotaz - Prodej podle zaměstnanců",
        "description": """
        Najděte jméno zaměstnance, celkový počet zákazníků, které spravuje, 
        a souhrnnou hodnotu jejich objednávek. Množství zákazníků i částky 
        seřaďte sestupně podle celkové hodnoty objednávek.
        """,
        "sql": """
        SELECT 
            Employee.FirstName || ' ' || Employee.LastName AS Zamestnanec,
            COUNT(Customer.CustomerId) AS PocetZakazniku,
            SUM(Invoice.Total) AS CelkoveTrzby
        FROM 
            Employee
        LEFT JOIN 
            Customer ON Employee.EmployeeId = Customer.SupportRepId
        LEFT JOIN 
            Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY 
            Zamestnanec
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