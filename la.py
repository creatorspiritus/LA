import streamlit as st

st.set_page_config("Совет в обед", 
page_icon="files/ico/DISg_colored.ico", menu_items={
    'Get Help': 'https://dis-group.ru/',
    'Report a bug': "https://data-innovations.ru/",
    'About': """#### Совет в обед
Разработано МК в 2024 году"""
})

st.logo(image="files/png/1_Data_Innovations_RU_grad.png", 
        size="large", link="https://data-innovations.ru/", 
        icon_image="files/ico/DISg_colored.ico")

st.title(":streamlit: Совет в обед")

if "фамилия" not in st.session_state: st.session_state.фамилия = "Котляров"
if "имя" not in st.session_state: st.session_state["имя"] = "Миша"

МЕНЮ = st.navigation([
    st.Page("files/py/Меню/Советы.py", icon=":material/school:"),
    st.Page("files/py/Меню/Шпаргалка.py", 
            icon=":material/sticky_note_2:"),
    st.Page("files/py/Меню/Код.py", icon=":material/code:")
])

МЕНЮ.run()


