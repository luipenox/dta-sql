import streamlit as st

# Nadpis lekce
st.write("# Lekce: Primární a cizí klíče v SQL")

# Úvod
st.write(
    """
    Relační databázové tabulky spolu komunikují pomocí klíčů, které umožňují definovat vztahy mezi nimi. 
    V této lekci se zaměříme na dva typy klíčů:

    - **Primární klíč (Primary Key)**: Jednoznačně identifikuje každý řádek v databázové tabulce.
    - **Cizí klíč (Foreign Key)**: Odkazuje na primární klíč v jiné nebo stejné tabulce a vytváří vazbu mezi tabulkami.
    """
)

# Primární klíče
st.write("## 1. Primární klíč (Primary Key)")
st.write(
    """
    Primární klíč je sloupec nebo kombinace sloupců, které jednoznačně identifikují každý řádek v tabulce.
    Žádná hodnota v primárním klíči nesmí být **NULL** ani se nesmí opakovat.
    """
)

# Příklad primárního klíče
st.write("#### Příklad: Definice primárního klíče")
st.code(
    """
    CREATE TABLE employees (
        EmployeeId INT NOT NULL PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50)
    );
    """,
    language="sql"
)
st.write(
    "V tomto příkladu sloupec `EmployeeId` je nastaven jako primární klíč tabulky `employees`. Tento klíč zaručuje, že každé `EmployeeId` bude unikátní."
)

# Cizí klíče
st.write("## 2. Cizí klíč (Foreign Key)")
st.write(
    """
    Cizí klíč slouží k vytvoření vazby mezi tabulkami. Odkazuje na primární klíč jiné (nebo téže) tabulky.
    Používají se pro reprezentaci vztahů, jako je například **jeden na mnoho** nebo **mnoho na mnoho**.
    """
)

# Příklad cizího klíče
st.write("#### Příklad: Definice cizího klíče")
st.code(
    """
    CREATE TABLE orders (
        OrderId INT NOT NULL PRIMARY KEY,
        CustomerId INT NOT NULL,
        OrderDate DATE,
        FOREIGN KEY (CustomerId) REFERENCES customers(CustomerId)
    );
    """,
    language="sql"
)
st.write(
    "Zde sloupec `CustomerId` v tabulce `orders` odkazuje na primární klíč `CustomerId` v tabulce `customers`."
)

# Vztahy mezi tabulkami
st.write("## 3. Vztahy: Primární a cizí klíče")
st.write(
    """
    Pomocí primárních a cizích klíčů definujeme různé vztahy mezi tabulkami:

    - **Jedna na jednu (One-to-One)**: Každý záznam v jedné tabulce odpovídá jednomu záznamu v jiné tabulce.
    - **Jedna na mnoho (One-to-Many)**: Každý záznam v jedné tabulce může odpovídat více záznamům v jiné tabulce.
    - **Mnoho na mnoho (Many-to-Many)**: Relace, která se realizuje pomocí spojovací tabulky (bridge table).
    """
)

# Příklad vztahu Jedna na mnoho
st.write("#### Příklad: Vztah Jedna na mnoho")
st.code(
    """
    -- Tabulka customers
    CREATE TABLE customers (
        CustomerId INT NOT NULL PRIMARY KEY,
        Name VARCHAR(50)
    );

    -- Tabulka orders s cizím klíčem na customers
    CREATE TABLE orders (
        OrderId INT NOT NULL PRIMARY KEY,
        CustomerId INT NOT NULL,
        OrderDate DATE,
        FOREIGN KEY (CustomerId) REFERENCES customers(CustomerId)
    );
    """,
    language="sql"
)
st.write("Zde každý zákazník (`customers`) může mít více objednávek (`orders`).")

# Bridge Table pro Mnoho na mnoho
st.write("#### Příklad: Vztah Mnoho na mnoho")
st.code(
    """
    -- Tabulka students
    CREATE TABLE students (
        StudentId INT NOT NULL PRIMARY KEY,
        Name VARCHAR(50)
    );

    -- Tabulka courses
    CREATE TABLE courses (
        CourseId INT NOT NULL PRIMARY KEY,
        Title VARCHAR(50)
    );

    -- Spojovací tabulka students_courses
    CREATE TABLE students_courses (
        StudentId INT NOT NULL,
        CourseId INT NOT NULL,
        PRIMARY KEY (StudentId, CourseId),
        FOREIGN KEY (StudentId) REFERENCES students(StudentId),
        FOREIGN KEY (CourseId) REFERENCES courses(CourseId)
    );
    """,
    language="sql"
)
st.write(
    """
    V tomto příkladu vztah mezi studenty a kurzy je reprezentován spojovací tabulkou `students_courses`.
    Každý student může být zapsán do více kurzů a každý kurz může mít více studentů.
    """
)

# Odkazy na praktické použití (Chinook)
st.write("## 4. Praktické příklady v databázi Chinook")
st.write(
    """
    V databázi Chinook najdeme mnoho příkladů použití primárních a cizích klíčů:

    - Tabulka `albums`: má primární klíč `AlbumId` a cizí klíč `ArtistId`, který odkazuje na tabulku `artists`.
    - Tabulka `invoices`: má primární klíč `InvoiceId` a cizí klíč `CustomerId`, který odkazuje na tabulku `customers`.
    - Tabulka `playlist_track`: reprezentuje vztah mnoho na mnoho mezi `playlists` a `tracks`.

    Pomocí této struktury relačních klíčů můžeme snadno dotazovat data napříč tabulkami.
    """
)

# Závěr
st.write("## Shrnutí")
st.write(
    """
    Primární a cizí klíče jsou základními stavebními bloky relačních databází. Primární klíč zajišťuje
    unikátnost záznamů v tabulce, zatímco cizí klíč propojuje tabulky a definuje relace mezi nimi.
    """
)
