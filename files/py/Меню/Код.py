import streamlit as st

st.subheader("Код приложения", divider=True)
"""В разделе представлен код файлов приложения `la.py` (Lunch advice)"""

with st.expander("`la.py` - файл запуска приложения", 
                 icon=":material/code:"):
    with open("la.py", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)

with st.expander("`Код.py` - этот файл", 
                 icon=":material/code:"):
    with open("files/py/Меню/Код.py", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)

with st.expander("`Шпаргалка.py` - файл с описаниями элементов пакета :streamlit: `streamlit`", 
                 icon=":material/code:"):
    with open("files/py/Меню/Шпаргалка.py", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)

with st.expander("`Советы.py` - файл ссоветов", 
                 icon=":material/code:"):
    with open("files/py/Меню/Советы.py", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)
