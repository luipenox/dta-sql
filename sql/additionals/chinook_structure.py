import streamlit as st

# Nadpis
st.write("# Struktura databáze Chinook")

# Úvod
st.write(
    "Databáze **Chinook** je relační databáze inspirovaná scénářem digitálního obchodu s hudbou. "
    "Obsahuje data o interpretech, albech, skladbách, zákaznících, fakturách a dalších. "
    "Níže je popis hlavních tabulek a jejich relací:"
)

st.image("assets/images/diagram.png")

# Tabulka 1: Artists
st.write("## Tabulka: `Artist`")
st.write("Obsahuje informace o hudebních interpretech.")
st.write("**Sloupce:**")
st.write(
    """
- `ArtistId`: Jedinečný identifikátor interpreta (Primární klíč).
- `Name`: Jméno interpreta.
""")

# Tabulka 2: Albums
st.write("## Tabulka: `Album`")
st.write("Obsahuje seznam alb, která vydali interpreti.")
st.write("**Sloupce:**")
st.write(
    """
- `AlbumId`: Jedinečný identifikátor alba (Primární klíč).
- `Title`: Název alba.
- `ArtistId`: Identifikátor interpreta (Cizí klíč na tabulku `artists`).
"""
)

# Tabulka 3: Tracks
st.write("## Tabulka: `Track`")
st.write("Obsahuje seznam skladeb, které patří k jednotlivým albům.")
st.write("**Sloupce:**")
st.write(
    """
- `TrackId`: Jedinečný identifikátor skladby (Primární klíč).
- `Name`: Název skladby.
- `AlbumId`: Identifikátor alba (Cizí klíč na tabulku `albums`).
- `MediaTypeId`: Identifikátor mediálního formátu (Cizí klíč na tabulku `media_types`).
- `GenreId`: Identifikátor žánru (Cizí klíč na tabulku `genres`).
- `Composer`: Skladatel skladby.
- `Milliseconds`: Délka skladby v milisekundách.
- `Bytes`: Velikost skladby v bytech.
- `UnitPrice`: Cena skladby.
"""
)

# Tabulka 4: Genres
st.write("## Tabulka: `Genre`")
st.write("Obsahuje seznam hudebních žánrů.")
st.write("**Sloupce:**")
st.write(
    """
- `GenreId`: Jedinečný identifikátor žánru (Primární klíč).
- `Name`: Název žánru.
"""
)

# Tabulka 5: Media_types
st.write("## Tabulka: `MediaType`")
st.write("Obsahuje dostupné mediální formáty.")
st.write("**Sloupce:**")
st.write(
    """
- `MediaTypeId`: Jedinečný identifikátor mediálního formátu (Primární klíč).
- `Name`: Název mediálního formátu.
"""
)

# Tabulka 6: Playlists
st.write("## Tabulka: `Playlist`")
st.write("Obsahuje seznamy playlistů.")
st.write("**Sloupce:**")
st.write(
    """
- `PlaylistId`: Jedinečný identifikátor playlistu (Primární klíč).
- `Name`: Název playlistu.
"""
)

# Tabulka 7: Playlist_track
st.write("## Tabulka: `PlaylistTrack`")
st.write("Propojuje tabulky `playlists` a `tracks`. Umožňuje vytvářet vztah mnoho-na-mnoho.")
st.write("**Sloupce:**")
st.write(
    """
- `PlaylistId`: Identifikátor playlistu (Cizí klíč na tabulku `playlists`).
- `TrackId`: Identifikátor skladby (Cizí klíč na tabulku `tracks`).
"""
)

# Tabulka 8: Customers
st.write("## Tabulka: `Customer`")
st.write("Obsahuje údaje o zákaznících, kteří nakupují mediální obsah.")
st.write("**Sloupce:**")
st.write(
    """
- `CustomerId`: Jedinečný identifikátor zákazníka (Primární klíč).
- `FirstName`: Jméno zákazníka.
- `LastName`: Příjmení zákazníka.
- `Company`: Firma zákazníka (volitelné).
- `Address`: Adresa zákazníka.
- `City`: Město.
- `State`: Stát.
- `Country`: Země.
- `PostalCode`: PSČ.
- `Phone`: Telefonní číslo.
- `Fax`: Faxové číslo.
- `Email`: Emailová adresa.
- `SupportRepId`: Identifikátor obchodního zástupce (Cizí klíč na tabulku `employees`).
"""
)

# Tabulka 9: Invoices
st.write("## Tabulka: `Invoice`")
st.write("Obsahuje informace o fakturách.")
st.write("**Sloupce:**")
st.write(
    """
- `InvoiceId`: Jedinečný identifikátor faktury (Primární klíč).
- `CustomerId`: Identifikátor zákazníka (Cizí klíč na tabulku `customers`).
- `InvoiceDate`: Datum vydání faktury.
- `BillingAddress`: Fakturační adresa.
- `BillingCity`: Fakturační město.
- `BillingState`: Fakturační stát.
- `BillingCountry`: Fakturační země.
- `BillingPostalCode`: Fakturační PSČ.
- `Total`: Celková částka na faktuře.
"""
)

# Tabulka 10: Invoice_items
st.write("## Tabulka: `InvoiceLine`")
st.write("Obsahuje jednotlivé položky na fakturách.")
st.write("**Sloupce:**")
st.write(
    """
- `InvoiceLineId`: Jedinečný identifikátor položky na faktuře (Primární klíč).
- `InvoiceId`: Identifikátor faktury (Cizí klíč na tabulku `invoices`).
- `TrackId`: Identifikátor skladby (Cizí klíč na tabulku `tracks`).
- `UnitPrice`: Cena za jednotku.
- `Quantity`: Množství položek.
"""
)

# Tabulka 11: Employees
st.write("## Tabulka: `Employee`")
st.write("Obsahuje údaje o zaměstnancích, včetně obchodních zástupců.")
st.write("**Sloupce:**")
st.write(
    """
- `EmployeeId`: Jedinečný identifikátor zaměstnance (Primární klíč).
- `FirstName`: Jméno zaměstnance.
- `LastName`: Příjmení zaměstnance.
- `Title`: Pozice zaměstnance.
- `ReportsTo`: Identifikátor nadřízeného (Cizí klíč na tabulku `employees`).
- `BirthDate`: Datum narození.
- `HireDate`: Datum nástupu do zaměstnání.
- `Address`: Adresa.
- `City`: Město.
- `State`: Stát.
- `Country`: Země.
- `PostalCode`: PSČ.
- `Phone`: Telefonní číslo.
- `Fax`: Faxové číslo.
- `Email`: Emailová adresa.
"""
)

# Závěr
st.write(
    "Databáze Chinook je skvělý nástroj pro výuku relačních databází a práce se SQL. "
    "Nabízí realistická data a umožňuje procvičit operace jako `JOIN`, `GROUP BY` nebo práci s poddotazy."
)
