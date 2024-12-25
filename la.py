import streamlit as st
from datetime import timedelta

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

# Новый код для Совета от 27 ноября 2024 года
# Аутентификация пользователя

# if not st.experimental_user.is_logged_in():
#     st.warning("Пользователь не выполнил вход в приложение")
# 
# кнопка_google = st.button("Авторизация через Google", type="primary")
# 
# if кнопка_google:
#     st.experimental_user.login(provider="google")
# 
# if st.experimental_user.is_logged_in():
#     st.write(":sparkles: :rainbow[User data]")
#     st.write(st.experimental_user)
# 
#     кнопка_logout = st.button("Выход")
#     if кнопка_logout:
#         st.experimental_user.logout()

if "фамилия" not in st.session_state: 
    st.session_state.фамилия = "Котляров"
if "имя" not in st.session_state: 
    st.session_state["имя"] = "Миша"
if "соединение" not in st.session_state: 
    st.session_state.соединение = st.connection("la_sql", type="sql", 
        ttl=timedelta(minutes=0))
if "КЖП" not in st.session_state: 
    st.session_state.КЖП = st.session_state.соединение.query(
        'select * from "Книга жалоб и предложений"', ttl=timedelta(minutes=0))


МЕНЮ = st.navigation([
    st.Page("files/py/Меню/Советы.py", icon=":material/school:"),
    st.Page("files/py/Меню/Шпаргалка.py", 
            icon=":material/sticky_note_2:"),
    st.Page("files/py/Меню/Код.py", icon=":material/code:"),
    st.Page("files/py/Меню/КЖП.py", title="Книга жалоб и предложений", icon=":material/edit_square:")
])
МЕНЮ.run()

# st.secrets["Фамилия"]["Котляров"]
