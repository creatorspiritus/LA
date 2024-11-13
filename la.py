import streamlit as st

st.title(":streamlit: Совет в обед")
# st.header("Шпаргалка", divider=True)
# st.subheader("Новое в версии 1.40", divider=True)
# """Зарезервировано"""
# st.subheader("Применение переменных сессии `st.session_state`", divider=True)
# """Зарезервировано"""

if "фамилия" not in st.session_state: st.session_state.фамилия = "Котляров"

МЕНЮ = st.navigation([
    st.Page("files/py/Меню/Советы.py", icon=":material/school:"),
    st.Page("files/py/Меню/Шпаргалка.py", icon=":material/sticky_note_2:"),
    st.Page("files/py/Меню/Код.py", icon=":material/code:")
])

МЕНЮ.run()


