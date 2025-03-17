import streamlit as st
import reveal_slides as rs


def home():
    st.title('O kurzu')
    # x = rs.slides("""**Test**""")
    st.write("## Zaměření")
    st.markdown(
        """<p style="text-align: justify;">Tento kurz je zaměřen na základy SQL, tedy na klíčový jazyk pro práci s relačními databázemi. Naučíte se, jak dotazovat data pomocí různých příkazů, jako je SELECT, WHERE, ORDER BY, nebo GROUP BY. V průběhu kurzu budete pracovat se skutečnými daty a vyzkoušíte si základní analýzu, manipulaci s daty a optimalizaci dotazů. Kurz je ideální pro začátečníky, kteří chtějí získat pevné základy, a zároveň připravuje na pokročilejší práci s databázemi. Nepotřebujete předchozí zkušenosti – krok za krokem vás provedeme celým procesem.</p>""",
        unsafe_allow_html=True)
    st.write("## SQLite")
    st.markdown(
        """<p style="text-align: justify;">SQLite je lehká a vestavěná relační databáze, která je skvělá pro výuku základů SQL. Její hlavní výhodou je jednoduchost – nevyžaduje složitou instalaci ani konfiguraci, protože celé databázové úložiště se ukládá do jednoho souboru. V tomto kurzu si ukážeme klíčové vlastnosti a schopnosti SQL pomocí SQLite, jako je vytváření tabulek, vkládání dat, filtrování záznamů, práce s daty, řazení a základní agregace. SQLite je ideálním nástrojem, pokud chcete začít s SQL od začátku a přitom pracovat s databází, která je široce využívaná v praxi.</p>""",
        unsafe_allow_html=True)
    st.write("## DB Chinook")

    st.markdown(
        """<p style="text-align: justify;">Databáze Chinook je ukázková relační databáze, která je často používána k výuce a demonstraci práce s SQL. Je inspirována databázemi s multimediálním obsahem a obsahuje data spojená s digitálním obchodem na prodej hudby. Databáze zahrnuje tabulky jako zákazníci, alba, interpreti, skladby, faktury, zaměstnanci nebo žánry, což umožňuje reálné simulace práce s daty. Díky svému přehlednému a praktickému uspořádání se skvěle hodí pro procvičování základních i pokročilých SQL dotazů. Chinook je dostupná ve formátech pro různé databázové systémy, včetně SQLite, a je ideálním nástrojem pro výuku a testování vašich dovedností v práci s relačními databázemi.</p>""",
        unsafe_allow_html=True)

    # code = '''
    # import streamlit as st
    #
    # st.title('O projektu')
    # '''
    #
    # st.code(code, language='python')


def contact():
    st.title('Kontaktní informace')
    col1, col2 = st.columns(2)

    with col1:
        st.info('Luděk Reif', icon=":material/signature:")
        st.info('+420 720 116 008', icon=":material/call:")
        st.info('luipenox@gmail.com', icon=":material/mail:")
        st.info('https://www.linkedin.com/in/luipenox/', icon=":material/link:")

    with col2:
        st.image('assets/images/luipenox.png', width=272)


def download():
    st.title("Soubory ke stažení")
    st.markdown('<a href="assets/downloads/dta_chinook.sqlite" download>Upravená Chinook SQLite DB</a> - ukázková upravená databáze pro potřeby kurzu', unsafe_allow_html=True)
    st.write(
        "[Chinook SQLite DB](https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite) - ukázková neupravená databáze, která simuluje obchod s digitální hudbou, obsahující data o skladbách, umělcích, albech, zákaznících, objednávkách a zaměstnancích")
    st.write(
        "[DBeaver](https://dbeaver.io/download/) - univerzální databázový nástroj pro správu, který nabízí grafické rozhraní pro práci s různými relačními i nerelačními databázemi, včetně vizualizace dat a vytváření SQL dotazů")
    st.write(
        "[DB Browser for SQLite](https://sqlitebrowser.org/dl/) - uživatelsky přívětivá aplikace s grafickým rozhraním, která umožňuje snadné vytváření, prohlížení a správu SQLite databází bez nutnosti psaní SQL příkazů (alternativa k DBeaver)")


introduction = st.Page(
    "sql/chapters/introduction.py",
    title="Úvod do SQL",
    icon=":material/counter_0:")

select = st.Page(
    "sql/chapters/select.py",
    title="První krůčky (SELECT)",
    icon=":material/counter_1:")

where = st.Page(
    "sql/chapters/where.py",
    title="Podmínky (WHERE)",
    icon=":material/counter_2:")

dates = st.Page(
    "sql/chapters/dates.py",
    title="Formát data (DATE)",
    icon=":material/counter_2:")

joins = st.Page(
    "sql/chapters/joins.py",
    title="Propojení (JOIN)",
    icon=":material/counter_4:")

union = st.Page(
    "sql/chapters/union.py",
    title="Spojení (UNION)",
    icon=":material/counter_3:")

sql_02 = st.Page(
    "sql/02.py",
    title="DATE",
    icon=":material/counter_2:")

sql_03 = st.Page(
    "sql/03.py",
    title="GROUP BY",
    icon=":material/counter_3:")


sql_06 = st.Page(
    "sql/06.py",
    title="Poddotazy",
    icon=":material/counter_6:")

keys_sql = st.Page(
    "sql/additionals/keys_sql.py",
    title="Klíče v SQL",
    icon=":material/key:")

datatypes_sqlite = st.Page(
    "sql/additionals/datatypes_sqlite.py",
    title="Datové typy SQLite",
    icon=":material/flag:")

chinook_structure = st.Page(
    "sql/additionals/chinook_structure.py",
    title="Struktura DB Chinook",
    icon=":material/database:")

home_page = st.Page(home, title="O kurzu", icon=":material/info:")
download_page = st.Page(download, title="Ke stažení", icon=":material/download:")
contact_page = st.Page(contact, title="Kontakt", icon=":material/import_contacts:")


account_pages = [home_page, download_page, contact_page]

page_dict = {'Kapitoly': [
    introduction,
    select,
    where,
    dates,
    joins,
    union
], 'Doplňující materiály': [
    keys_sql,
    datatypes_sqlite,
    chinook_structure
]}

pg = st.navigation({"Informace": account_pages} | page_dict)



pg.run()
