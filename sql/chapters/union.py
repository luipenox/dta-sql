import streamlit as st

# Nadpis lekce
st.write("## Lekce: Použití SQL UNION")

# 1. Co je SQL UNION
st.write("### 1. Co je SQL UNION?")
st.write(
    "`UNION` je SQL operátor, který se používá ke kombinování výsledků dvou nebo více `SELECT` dotazů do jednoho výsledku. "
    "Sloupce v obou dotazech musí mít stejný datový typ a stejný počet, aby mohly být kombinovány."
)
st.write(
    "Například pokud máte dvě tabulky a chcete vytvořit seznam všech unikátních záznamů z obou, použijete `UNION`."
)

# 2. Syntaxe UNION
st.write("### 2. Syntaxe UNION")
st.write("Základní syntaxe operátoru `UNION` vypadá takto:")
st.code(
    "SELECT sloupce FROM tabulka1\n"
    "UNION\n"
    "SELECT sloupce FROM tabulka2;",
    language="sql"
)
st.write(
    "- Každý `SELECT` dotaz musí vracet stejný počet sloupců.\n"
    "- Sloupce na odpovídajících pozicích musí mít stejný nebo kompatibilní datový typ.\n"
    "- Výsledný dotaz automaticky odstraní duplicitní řádky. Pokud chcete zachovat duplicity, použijte `UNION ALL`."
)

# 3. Rozdíl mezi UNION a UNION ALL
st.write("### 3. Rozdíl mezi UNION a UNION ALL")
st.write("SQL umožňuje dva způsoby operace `UNION`:")
st.write("""
1. **UNION**  
   - Kombinuje výsledky z více dotazů a odstraňuje duplicity.  
   - Pomalejší, protože vyžaduje zpracování pro odstranění duplicit.

2. **UNION ALL**  
   - Kombinuje výsledky z více dotazů, bez odstranění duplicit.  
   - Rychlejší, pokud neřešíte duplicitní řádky.
""")

# 4. Příklad použití UNION (unikátní výsledky)
st.write("### 4. Příklad: Unikátní výsledky")
st.write(
    "Předpokládejme následující situaci: Máte dvě tabulky, `old_customers` a `new_customers`, a chcete vytvořit seznam všech jedinečných zákazníků."
)
st.code(
    "SELECT first_name, last_name FROM old_customers\n"
    "UNION\n"
    "SELECT first_name, last_name FROM new_customers;",
    language="sql"
)
st.write(
    "Tento příkaz kombinuje všechny zákazníky z obou tabulek a odstraní duplicitní záznamy (stejná jména a příjmení)."
)

# 5. Příklad použití UNION ALL (zachování duplicit)
st.write("### 5. Příklad: Zachování duplicit")
st.write(
    "Pokud chcete vrátit všechny záznamy bez odstranění duplicit, použijte `UNION ALL`."
)
st.code(
    "SELECT first_name, last_name FROM old_customers\n"
    "UNION ALL\n"
    "SELECT first_name, last_name FROM new_customers;",
    language="sql"
)
st.write(
    "Tento příkaz vrátí všechny zákazníky (včetně duplicitních záznamů, pokud jsou stejní zákazníci v obou tabulkách)."
)

# 6. Kombinace UNION s filtrováním
st.write("### 6. Kombinace UNION s filtrováním")
st.write(
    "Můžete použít různé `WHERE` podmínky v každém `SELECT` dotazu, než je zkombinujete pomocí `UNION`."
)
st.write("#### Příklad: Zákazníci podle registrace:")
st.code(
    "SELECT first_name, last_name FROM old_customers\n"
    "WHERE register_date < '2023-01-01'\n"
    "UNION\n"
    "SELECT first_name, last_name FROM new_customers\n"
    "WHERE register_date >= '2023-01-01';",
    language="sql"
)
st.write(
    "Tento dotaz vrátí unikátní seznam zákazníků. Zákazníci z tabulky `old_customers` byli zaregistrováni před rokem 2023, a ti z `new_customers` po roce 2023."
)

# 7. Kombinace UNION s více sloupci
st.write("### 7. Kombinace UNION s více sloupci")
st.write(
    "Pamatujte, že počet sloupců a jejich datové typy musí být shodné. Pokud je například jedna tabulka s názvy zákazníků a druhá s produkty, můžete je spojit takto:"
)
st.code(
    "SELECT 'Customer' AS type, first_name, last_name FROM customers\n"
    "UNION ALL\n"
    "SELECT 'Product' AS type, product_name, NULL AS placeholder FROM products;",
    language="sql"
)
st.write(
    "V tomto příkladu sloupec `type` označuje, odkud data pocházejí (zákazníci nebo produkty)."
)

# 8. Příklad: Sjednocení dat z JOIN dotazů
st.write("### 8. Příklad: Sjednocení dat z JOIN dotazů")
st.write("Můžete také spojovat výsledky složitějších dotazů:")
st.code(
    "SELECT c.first_name, c.last_name, r.rental_date\n"
    "FROM customer c\n"
    "JOIN rental r ON c.customer_id = r.customer_id\n"
    "WHERE r.rental_date < '2023-01-01'\n"
    "UNION\n"
    "SELECT s.first_name, s.last_name, p.payment_date\n"
    "FROM staff s\n"
    "JOIN payment p ON s.staff_id = p.staff_id\n"
    "WHERE p.payment_date >= '2023-01-01';",
    language="sql"
)
st.write(
    "Tento příklad sjednocuje informace o zákaznících, kteří si půjčovali filmy před rokem 2023, a zaměstnancích, kteří přijímali platby po roce 2023."
)

# 9. Cvičení
st.write("### 9. Cvičení: Vyzkoušejte si sami")
st.write("""
1. Spojte tabulky `staff` a `customers` pomocí `UNION`, tak aby se zobrazil seznam všech unikátních osob (zákazníků i zaměstnanců) a jejich e-maily.
2. Získejte seznam jedinečných kategorií filmů z tabulek `film` a `inventory` pomocí `UNION`.
3. Spojte data o filmech (`film.title`) z tabulek `film` a `old_film` (předchozí databáze).
4. Použijte `UNION ALL`, abyste zobrazili kompletní seznam všech řádků z tabulek `rental` a `old_rental`, zachovávající duplicity.
""")

# Závěr
st.write("### Závěr")
st.write(
    "`UNION` je užitečný nástroj pro slučování dat z různých tabulek nebo dotazů do jednoho výsledku. "
    "Použitím `UNION` získáte unikátní záznamy, zatímco `UNION ALL` zachová všechny řádky, včetně duplicit."
)
st.write("Nezapomeňte, že všechny `SELECT` dotazy musí vracet stejný počet sloupců a odpovídající datové typy.")
