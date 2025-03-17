import streamlit as st

# Nadpis lekce
st.title("Použití SQL JOIN")

# 1. Co je SQL JOIN
st.write("### 1. Co je SQL JOIN?")
st.write(
    "`JOIN` v SQL slouží ke kombinování dat z více tabulek na základě společného klíče. "
    "Například pokud máte dvě tabulky, jedna s informacemi o zákaznících a druhá s jejich objednávkami, můžete je spojit pomocí příkazu `JOIN`, abyste viděli kdo objednal co."
)
st.write("Existuje několik typů `JOIN`, z nichž každý poskytuje různé výsledky na základě toho, jak data spojujeme.")

# 2. Typy JOIN operátorů
st.write("### 2. Typy JOIN operátorů")
st.image("./assets/images/joins.png")
st.write("SQL obsahuje následující typy `JOIN`:")
st.write("""
1. **INNER JOIN**  
   Spojuje pouze řádky, kde se v obou tabulkách najde shoda (překryv dat).

2. **LEFT JOIN** (neboli LEFT OUTER JOIN)  
   Vrací všechny řádky z levé tabulky a pouze odpovídající řádky z pravé tabulky.

3. **RIGHT JOIN** (neboli RIGHT OUTER JOIN)  
   Opačné od LEFT JOIN — vrací všechny řádky z pravé tabulky a odpovídající z levé tabulky.

4. **FULL JOIN** (nebo FULL OUTER JOIN)  
   Vrací všechny řádky z obou tabulek, a to i když odpovídající dvojice v druhé tabulce neexistuje.
""")

# 3. Syntaxe JOIN
st.write("### 3. Základní syntaxe")
st.write("Základní syntaxe JOIN vypadá takto:")
st.code(
    "SELECT sloupce\n"
    "FROM tabulka1\n"
    "JOIN tabulka2\n"
    "ON tabulka1.společný_klíč = tabulka2.společný_klíč;",
    language="sql"
)
st.write(
    "- `JOIN` označuje typ spojení.\n"
    "- `ON` specifikuje podmínku, která definuje propojení mezi tabulkami.\n"
    "- `společný_klíč` je sloupec, který tabulky sdílejí."
)

# 4. INNER JOIN
st.write("### 4. INNER JOIN")
st.write(
    "**INNER JOIN** kombinuje pouze ty řádky, kde tabulky mají odpovídající hodnoty ve společném klíči."
)
st.write("#### Příklad:")
st.code(
    "SELECT c.first_name, c.last_name, r.rental_date\n"
    "FROM customer c\n"
    "INNER JOIN rental r\n"
    "ON c.customer_id = r.customer_id;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí seznam zákazníků a data jejich výpůjček. Pokud zákazník nemá žádné výpůjčky, nebude zařazen do výsledku."
)

# 5. LEFT JOIN
st.write("### 5. LEFT JOIN")
st.write(
    "**LEFT JOIN** vrací všechny řádky z levé tabulky a přiřadí odpovídající data z pravé tabulky. "
    "Pokud v pravé tabulce není odpovídající řádek, jsou hodnoty nahrazeny `NULL`."
)
st.write("#### Příklad:")
st.code(
    "SELECT c.first_name, c.last_name, r.rental_date\n"
    "FROM customer c\n"
    "LEFT JOIN rental r\n"
    "ON c.customer_id = r.customer_id;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí všechny zákazníky bez ohledu na to, zda mají výpůjčky. Pokud zákazník žádnou výpůjčku nemá, `rental_date` bude `NULL`."
)

# 6. RIGHT JOIN
st.write("### 6. RIGHT JOIN")
st.write(
    "**RIGHT JOIN** vrací všechny řádky z pravé tabulky a přiřadí odpovídající data z levé tabulky. "
    "Pokud v levé tabulce není odpovídající řádek, hodnoty budou `NULL`."
)
st.write("#### Příklad:")
st.code(
    "SELECT r.rental_date, c.first_name, c.last_name\n"
    "FROM rental r\n"
    "RIGHT JOIN customer c\n"
    "ON r.customer_id = c.customer_id;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí všechny výpůjčky a informace o zákaznících. Pokud výpůjčka není spojená s žádným zákazníkem, `first_name` a `last_name` budou `NULL`."
)

# 7. FULL OUTER JOIN
st.write("### 7. FULL OUTER JOIN")
st.write(
    "**FULL JOIN** vrací všechny řádky z obou tabulek. "
    "Pokud v jedné tabulce chybí odpovídající řádek, chybějící hodnoty budou `NULL`."
)
st.write("#### Příklad:")
st.code(
    "SELECT c.first_name, c.last_name, r.rental_date\n"
    "FROM customer c\n"
    "FULL OUTER JOIN rental r\n"
    "ON c.customer_id = r.customer_id;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí seznam všech zákazníků a výpůjček. Pokud zákazník nemá výpůjčku, nebo výpůjčka není spojena se zákazníkem, chybějící hodnoty budou `NULL`."
)

# 8. Kombinované příklady
st.write("### 8. Kombinované příklady")
st.write("Příklad: Propojení zákazníků, faktur a skladeb:")
st.code("""SELECT c.CustomerId, c.FirstName, c.LastName, i.InvoiceDate, t.Name 
FROM customer AS c
    INNER JOIN Invoice AS i ON c.CustomerId = i.CustomerId
    INNER JOIN InvoiceLine AS il ON i.InvoiceId = il.InvoiceId
    INNER JOIN Track AS t ON t.TrackId = il.TrackId 
WHERE c.CustomerId = 14""", language="sql"
        )
st.write(
    "Tento příkaz vrací informace o zákaznících, filmech, které si půjčili, a datu výpůjčky."
)

# 9. Cvičení
st.write("### 9. Cvičení: Vyzkoušejte si sami")
st.write("""
1. Zobrazte seznam všech zákazníků a jména filmů, které si půjčili. Pokud zákazník žádný film nepůjčil, zobraz `NULL`.
2. Najděte kategorie (tabulka `category`) a počet filmů v každé kategorii, použijte `JOIN` s tabulkou `film_category`.
3. Spočítejte celkový obrat (`SUM(payment.amount)`) na každého zákazníka.
4. Získejte seznam všech zaměstnanců a počty výpůjček, které zprostředkovali, i když žádné výpůjčky nezprostředkovali.
""")

# Závěr
st.write("### Závěr")
st.write(
    "`JOIN` je jednou z nejdůležitějších funkcí SQL, protože umožňuje kombinovat data z více tabulek do jednoho uceleného výsledku. "
    "Pokud pochopíte rozdíly mezi `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` a `FULL OUTER JOIN`, budete schopni psát velmi výkonné dotazy a efektivně analyzovat relační data."
)
