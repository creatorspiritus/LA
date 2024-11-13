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

with st.expander("`Советы.py` - файл советов", 
                 icon=":material/code:"):
    with open("files/py/Меню/Советы.py", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)

with st.expander("`README.md` - файл описания приложения", 
                 icon=":material/code:"):
    "Код файла:"
    with open("README.md", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)
    """И его правильное отображение 👇👇👇"""
    st.markdown(t)

with st.expander("`config.toml` - файл настройки приложения", 
                 icon=":material/code:"):
    with open(".streamlit/config.toml", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)
    """Здесь указана команда перезапуска приложения после внесения
изменений в код любого файла приложения и его последующего сохранения."""

with st.expander("`requirements.txt` - необходимые пакеты", 
                 icon=":material/code:"):
    with open("requirements.txt", 'r', encoding='utf8') as f: t = f.read()
    st.code(t)
    """В данном файле указаны дополнительные пакеты, установленные
в виртуальное окружение Python для нормальной работы приложения"""

