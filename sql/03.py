import streamlit as st

# Nadpis lekce
st.title("Použití GROUP BY v SQL")

# 1. Co je GROUP BY
st.write("### 1. Co je GROUP BY?")
st.write(
    "`GROUP BY` je SQL příkaz, který se používá ke seskupení dat v tabulce na základě jedné nebo více hodnot sloupců. "
    "To umožňuje provádět agregace, jako jsou výpočty součtů, průměrů, maximálních a minimálních hodnot pro jednotlivé skupiny."
)
st.write(
    "Například: Pokud chcete seskupit zaměstnance podle jejich oddělení a spočítat průměrné platy v každém oddělení, příkaz `GROUP BY` je ideálním řešením.")

# 2. Základní syntaxe
st.write("### 2. Základní syntaxe")
st.write(
    "Základní syntaxe příkazu `GROUP BY` vypadá takto:"
)
st.code(
    "SELECT sloupec1, agregační_funkce(sloupec2) \n"
    "FROM název_tabulky \n"
    "GROUP BY sloupec1;",
    language="sql"
)
st.write(
    "- `sloupec1`: Sloupec, podle kterého chcete data seskupit.\n"
    "- `agregační_funkce`: Funkce, která se aplikuje na seskupená data, např. `SUM`, `COUNT`, `AVG`, `MAX`, `MIN`."
)

# 3. Příklad 1: Počítání řádků ve skupině
st.write("### 3. Příklad 1: Počítání řádků ve skupině")
st.write(
    "Chcete-li zjistit, kolik zaměstnanců je v každém oddělení, použijte příkaz `COUNT` v kombinaci s `GROUP BY`."
)
st.code(
    "SELECT department, COUNT(*) AS num_employees \n"
    "FROM employees \n"
    "GROUP BY department;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí jednotlivá oddělení (`department`) a počet zaměstnanců (`num_employees`) v každém z nich."
)

# 4. Příklad 2: Průměrné platy podle oddělení
st.write("### 4. Příklad 2: Průměrné platy podle oddělení")
st.write(
    "Můžete také použít agregační funkci `AVG`, abyste spočítali průměrné platy zaměstnanců v každém oddělení."
)
st.code(
    "SELECT department, AVG(salary) AS avg_salary \n"
    "FROM employees \n"
    "GROUP BY department;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí oddělení a průměrný plat zaměstnanců v daném oddělení."
)

# 5. Použití GROUP BY s HAVING
st.write("### 5. Použití GROUP BY s HAVING")
st.write(
    "`HAVING` se používá k filtrování seskupených dat poté, co byla provedena agregace. "
    "Je podobný příkazu `WHERE`, ale zatímco `WHERE` filtruje řádky před seskupením, `HAVING` filtruje výsledky po seskupení."
)
st.write("#### Příklad: Zobrazení oddělení s více než 5 zaměstnanci:")
st.code(
    "SELECT department, COUNT(*) AS num_employees \n"
    "FROM employees \n"
    "GROUP BY department \n"
    "HAVING COUNT(*) > 5;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí pouze ta oddělení, která mají více než 5 zaměstnanců."
)

# 6. Kombinace ORDER BY s GROUP BY
st.write("### 6. Kombinace ORDER BY s GROUP BY")
st.write(
    "`ORDER BY` se používá k řazení seskupených dat podle jednoho nebo více sloupců."
)
st.write("#### Příklad: Seřazení oddělení podle počtu zaměstnanců v sestupném pořadí:")
st.code(
    "SELECT department, COUNT(*) AS num_employees \n"
    "FROM employees \n"
    "GROUP BY department \n"
    "ORDER BY num_employees DESC;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí seznam oddělení seřazených podle počtu zaměstnanců, od největšího k nejmenšímu."
)

# 7. Příklad 3: Spojení GROUP BY a více agregačních funkcí
st.write("### 7. Příklad 3: Spojení GROUP BY a více agregačních funkcí")
st.write(
    "Ve stejném dotazu můžete použít více agregačních funkcí pro různé výpočty."
)
st.write("#### Příklad: Zobrazení počtu zaměstnanců, průměrného a maximálního platu podle oddělení:")
st.code(
    "SELECT department, COUNT(*) AS num_employees, AVG(salary) AS avg_salary, MAX(salary) AS max_salary \n"
    "FROM employees \n"
    "GROUP BY department;",
    language="sql"
)
st.write(
    "Tento příkaz zobrazí oddělení, počet zaměstnanců, průměrný plat a nejvyšší plat v každém oddělení."
)

# 8. Cvičení
st.write("### 8. Cvičení: Vyzkoušejte si sami")
st.write(
    "1. Spočítejte počet produktů v každé kategorii z tabulky `products`.\n"
    "2. Zobrazte celkový obrat (`SUM(price)`) dle regionu z tabulky `sales`.\n"
    "3. Najděte oddělení s průměrným platem vyšším než 50 000.\n"
    "4. Seřaďte skupiny (např. oddělení) podle průměrného platu v sestupném pořadí.\n"
    "5. Zobrazte město a počet zákazníků, kteří tam bydlí, pouze pokud je počet zákazníků větší než 10."
)

# Závěr
st.write("### Závěr")
st.write(
    "`GROUP BY` je klíčový nástroj v SQL pro organizaci dat do skupin a provádění analýz. "
    "S využitím agregačních funkcí, jako jsou `COUNT`, `SUM`, `AVG`, `MAX` a `MIN`, můžete z tabulek snadno extrahovat užitečné informace. "
    "Pokud potřebujete pokročilejší analýzy, kombinace `GROUP BY` s příkazy `HAVING`, `ORDER BY` a více agregačními funkcemi výrazně rozšiřuje jeho možnosti."
)
