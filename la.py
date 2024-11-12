import streamlit as st

st.title(":streamlit: Совет в обед")
# st.header("Шпаргалка", divider=True)
# st.subheader("Новое в версии 1.40", divider=True)
# """Зарезервировано"""
# st.subheader("Применение переменных сессии `st.session_state`", divider=True)
# """Зарезервировано"""


МЕНЮ = st.navigation([
    st.Page("files/py/Меню/Советы.py"),
    st.Page("files/py/Меню/Шпаргалка.py")
])

МЕНЮ.run()


