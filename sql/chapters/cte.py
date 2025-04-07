import sqlite3

import streamlit as st
import pandas as pd

@st.cache_data
def run_query(query):
    with sqlite3.connect("assets/downloads/dta_chinook.sqlite") as conn:
        return pd.read_sql_query(query, conn)

# Titulek aplikace
st.title("Výuková kapitola: Common Table Expressions (CTE) v SQL pro Chinook DB")

# Teoretická část
st.header("Teorie")
st.markdown("""
Common Table Expressions (CTE) jsou dočasné výsledky pojmenované v rámci jednoho SQL dotazu. 
Umožňují udělat SQL kód přehlednější a snadno čitelný. Definují se pomocí klíčového slova `WITH` 
a mohou být opakovaně využity v hlavním dotazu.

### Syntaxe:
```sql
WITH CTEName AS (
    -- Dotaz nebo výpočet
    SELECT column1, column2
    FROM TableName
    WHERE conditions
)
SELECT *
FROM CTEName;
```

### Výhody CTE:
1. **Čitelnost**: Části dotazu jsou separovány do logických bloků.
2. **Opakované použití**: CTE lze použít vícekrát ve stejném dotazu.
3. **Rekurzivita**: Podpora rekurzivních dotazů (např. pro hierarchie).

**Rekurzivní CTE** umožňuje dotazovat se na hierarchická data tím, že volá samy sebe.
""")

# Přehled příkladů
st.header("Příklady použití CTE v SQL s Chinook DB")

# Příklad 1
st.subheader("Příklad 1: Nejprodávanější skladby")
st.markdown("""
**Zadání**: Vytvořte CTE, který spočítá celkový výnos pro jednotlivé skladby 
a vybere pouze ty skladby, jejichž celkový výnos přesahuje 1,90. 
""")
code1 = '''
WITH TrackSales AS (
    SELECT
        t.TrackId,
        t.Name AS TrackName,
        SUM(il.Quantity * il.UnitPrice) AS TotalRevenue
    FROM InvoiceLine il
    INNER JOIN Track t ON il.TrackId = t.TrackId
    GROUP BY t.TrackId, t.Name
)
SELECT TrackId, TrackName, TotalRevenue
FROM TrackSales
WHERE TotalRevenue > 1.90;
'''
st.code(code1, language="sql")
result = run_query(code1)
st.dataframe(result)

# Příklad 2
st.subheader("Příklad 2: Průměrná délka alb")
st.markdown("""
**Zadání**: Pomocí CTE vypočítejte průměrnou délku skladeb na každém albu 
a vyberte pouze alba s průměrnou délkou skladby větší než 300 sekund.
""")
code2 = '''
WITH AlbumTrackDurations AS (
    SELECT 
        a.AlbumId,
        a.Title AS AlbumTitle,
        AVG(t.Milliseconds / 1000) AS AvgTrackDuration
    FROM Album a
    INNER JOIN Track t ON a.AlbumId = t.AlbumId
    GROUP BY a.AlbumId, a.Title
)
SELECT AlbumId, AlbumTitle, AvgTrackDuration
FROM AlbumTrackDurations
WHERE AvgTrackDuration > 300
ORDER BY AvgTrackDuration DESC;
'''
st.code(code2, language="sql")
result = run_query(code2)
st.dataframe(result)

# Příklad 3
st.subheader("Příklad 3: Rekurzivní hierarchie zaměstnanců")
st.markdown("""
**Zadání**: Pomocí rekurzivního CTE zobrazte celou hierarchii zaměstnanců od nejvýše postaveného manažera.
""")
code3 = '''
WITH EmployeeHierarchy AS (
    SELECT 
        e.EmployeeId, 
        e.FirstName || ' ' || e.LastName AS EmployeeName,
        e.ReportsTo AS ManagerId
    FROM Employee e
    WHERE e.ReportsTo IS NULL  -- Start with top-level manager (no ReportsTo)
    UNION ALL
    SELECT 
        e.EmployeeId, 
        e.FirstName || ' ' || e.LastName AS EmployeeName,
        e.ReportsTo
    FROM Employee e
    INNER JOIN EmployeeHierarchy eh ON e.ReportsTo = eh.EmployeeId
)
SELECT EmployeeId, EmployeeName, ManagerId
FROM EmployeeHierarchy;
'''
st.code(code3, language="sql")
result = run_query(code3)
st.dataframe(result)

# Příklad 4
st.subheader("Příklad 4: Zákazníci s velkým počtem objednávek")
st.markdown("""
**Zadání**: Získejte seznam zákazníků, kteří mají více než 10 objednávek (Invoice).
""")
code4 = '''
WITH CustomerOrderCounts AS (
    SELECT 
        c.CustomerId,
        c.FirstName || ' ' || c.LastName AS CustomerName,
        COUNT(i.InvoiceId) AS OrderCount
    FROM Customer c
    INNER JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId, c.FirstName, c.LastName
)
SELECT CustomerId, CustomerName, OrderCount
FROM CustomerOrderCounts
WHERE OrderCount > 2;
'''
st.code(code4, language="sql")
result = run_query(code4)
st.dataframe(result)

# Příklad 5
st.subheader("Příklad 5: Výpočty na úrovni faktur")
st.markdown("""
**Zadání**: Vytvořte dvě CTE – první z nich spočítá celkový výnos na každé faktuře 
a druhý vypočítá 10% slevu, která by mohla být aplikována na každou fakturu. 
Nakonec zobrazte seznam faktur s výnosem a slevou.
""")
code5 = '''
WITH InvoiceRevenue AS (
    SELECT 
        i.InvoiceId,
        SUM(il.UnitPrice * il.Quantity) AS TotalRevenue
    FROM Invoice i
    INNER JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    GROUP BY i.InvoiceId
),
InvoiceDiscount AS (
    SELECT 
        InvoiceId, 
        TotalRevenue * 0.1 AS Discount
    FROM InvoiceRevenue
)
SELECT 
    ir.InvoiceId, 
    ir.TotalRevenue, 
    id.Discount
FROM InvoiceRevenue ir
INNER JOIN InvoiceDiscount AS id ON ir.InvoiceId = id.InvoiceId
ORDER BY ir.TotalRevenue DESC;
'''
st.code(code5, language="sql")
result = run_query(code5)
st.dataframe(result)