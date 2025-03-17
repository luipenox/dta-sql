import streamlit as st

# Nadpis lekce
st.title("Práce s datumy v SQL")

# 1. Co jsou datumy v SQL
st.write("### 1. Co jsou datumy v SQL?")
st.write(
    "V SQL existují speciální datové typy pro reprezentaci datumu a času. "
    "Nejběžnější datové typy jsou `DATE`, `DATETIME`, `TIMESTAMP`, `TIME` a `YEAR`. "
    "Pomocí těchto typů lze uložit informace o datu, čase nebo kombinaci obojího, což je velmi užitečné v databázích sledování událostí, rezervací, transakcí apod."
)
st.write("Příklady datových typů:")
st.write("- `DATE`: Ukládá pouze datum (např. '2023-10-15').")
st.write("- `DATETIME`: Ukládá datum a čas (např. '2023-10-15 14:30:00').")
st.write("- `TIMESTAMP`: Podobný jako `DATETIME`, ale používá časové zóny.")
st.write("- `TIME`: Ukládá pouze čas (např. '14:30:00').")
st.write("- `YEAR`: Ukládá pouze rok (např. '2023').")

# 2. Vkládání datumu a času
st.write("### 2. Vkládání datumu a času")
st.write("Pro vložení záznamu s datumy a časy používejte `INSERT INTO`. Formát závisí na zvoleném datovém typu.")
st.write("#### Příklad:")
st.code(
    "INSERT INTO events (event_name, event_date) \n"
    "VALUES ('Setkání', '2023-12-01');",
    language="sql"
)
st.write("V tomto případě je `event_date` sloupec typu `DATE`.")

# 3. Výběr datumu a času
st.write("### 3. Výběr datumu a času")
st.write("Pro zobrazení sloupců obsahujících datum nebo čas použijte standardní příkaz `SELECT`.")
st.write("#### Příklad:")
st.code(
    "SELECT event_name, event_date \n"
    "FROM events;",
    language="sql"
)
st.write("Tento dotaz zobrazí názvy událostí a jejich datum.")

# 4. Filtrování podle datumu
st.write("### 4. Filtrování podle datumu")
st.write("Pomocí `WHERE` můžete filtrovat řádky podle hodnot v datech.")
st.write("#### Příklad 1: Filtr na konkrétní datum:")
st.code(
    "SELECT event_name \n"
    "FROM events \n"
    "WHERE event_date = '2023-12-01';",
    language="sql"
)
st.write("Tento příkaz zobrazí události, které probíhají přesně 1. prosince 2023.")
st.write("#### Příklad 2: Rozsah dat pomocí `BETWEEN`:")
st.code(
    "SELECT event_name \n"
    "FROM events \n"
    "WHERE event_date BETWEEN '2023-01-01' AND '2023-12-31';",
    language="sql"
)
st.write("Tento příkaz zobrazí události probíhající v roce 2023.")

# 5. Práce s datem a časem - Funkce SQL
st.write("### 5. Práce s datem a časem - Funkce SQL")
st.write("SQL obsahuje užitečné funkce pro manipulaci s daty. Zde jsou některé z nich:")
st.write("- `NOW()`: Vrátí aktuální datum a čas.")
st.write("- `CURDATE()`: Vrátí aktuální datum (bez času).")
st.write("- `CURTIME()`: Vrátí aktuální čas.")
st.write("- `DATEADD()`: Přidává k datům určitý počet dnů, měsíců nebo let (funkce dostupná v některých DBMS).")
st.write("- `DATEDIFF()`: Vrátí rozdíl mezi dvěma daty ve dnech.")
st.write("- `YEAR()`, `MONTH()`, `DAY()`: Extrahuje část data.")

st.write("#### Příklad 1: Získat aktuální datum a čas")
st.code(
    "SELECT NOW();",
    language="sql"
)
st.write("Výstup: například `2023-10-15 14:30:00`.")

st.write("#### Příklad 2: Přidání 7 dní k datu")
st.code(
    "SELECT DATE_ADD('2023-10-15', INTERVAL 7 DAY);",
    language="sql"
)
st.write("Výstup: `2023-10-22`.")

st.write("#### Příklad 3: Rozdíl mezi dvěma daty")
st.code(
    "SELECT DATEDIFF('2023-12-31', '2023-01-01');",
    language="sql"
)
st.write("Výstup: `364` (počet dnů mezi začátkem a koncem roku 2023).")

# 6. Třídění podle datumu
st.write("### 6. Třídění podle datumu")
st.write("Data mohou být tříděna pomocí příkazu `ORDER BY`.")
st.write("#### Příklad:")
st.code(
    "SELECT event_name, event_date \n"
    "FROM events \n"
    "ORDER BY event_date ASC;",
    language="sql"
)
st.write("Tento příkaz zobrazí události seřazené podle datumu od nejstaršího po nejnovější.")

# 7. Cvičení
st.write("### Cvičení: Vyzkoušejte si sami")
st.write(
    "1. Zobrazte všechny události, které se uskuteční v budoucnosti (datumy větší než dnešní datum).\n"
    "2. Najděte všechny události, které se konaly mezi 1. lednem 2022 a 31. prosincem 2022.\n"
    "3. Spočítejte počet dnů mezi datem '2023-10-01' a dnešním datem.\n"
    "4. Přidejte 30 dní k datu '2023-11-01' a zobrazte výsledek.\n"
    "5. Zobrazte všechny události, seřazené podle datumu v sestupném (DESC) pořadí."
)

# Závěr
st.write("### Závěr")
st.write(
    "Práce s datumy a časy v SQL je základní dovednost při správě databází. "
    "Díky funkcím SQL můžete snadno filtrovat události dle datumu, vypočítávat rozdíly mezi daty nebo manipulovat s datovými hodnotami. "
    "V každodenní praxi se tento přístup hojně využívá v plánování, analýze a sledování informací spojených s časem."
)