import streamlit as st

st.subheader("Советы", divider=True)

with st.expander("13 ноября 2024 года | Применение переменных сессии `st.session_state`", icon=":material/school:"):
    st.divider()
    """Метод `session_state` позволяет обмениваться переменными между 
повторными запусками кода файлов приложения для каждой 
пользовательской сессии. 

В дополнение к возможности сохранять значения переменных, Streamlit 
также предоставляет возможность манипулировать состоянием с помощью 
функций обратного вызова.

##### Инициализация значений в API 
API позволяет создавать переменные и присваивать им значения на основе 
полей, очень похожих на словари Python:
"""



    st.code("""# Инициализация (создание переменной и присваивание её значения)
# В нашем случае имя переменной - имя, а значение - Миша
if 'имя' not in st.session_state:
    st.session_state['имя'] = 'Миша'

# Поддерживается синтаксис, основанный на атрибутах
if 'имя' not in st.session_state:
    st.session_state.key = 'Миша'""")


    """Все значения переменных сеанса хранятся в структуре, похожей
на словарь. Соответственно и получение значений производится по ключам
или через атрибуты.
"""

    st.code("""# Просмотр всех пар (ключ-значение)
            
st.session_state # Волшебный вариант вывода на экран всех созданных пар
            
st.write(st.session_state) # Классический, через вызов функции отображения

# Получение значения по указанному ключу 

st.session_state.имя # Получим Миша
st.session_state['имя'] # Тоже получим Миша
st.write(st.session_state.имя) # И здесь получим Миша
st.write(st.session_state['имя']) # Тоже Миша в результате
            """)
    
    """Значения переменных сессии можно изменять простым присваиванием."""

    st.code("""
# Был Миша
st.session_state.имя = "Вася" # Стал Вася
        """)

    """
    Ссылка на видеоурок: https://youtu.be/92jUAXBmZyU?list=TLGGYqrRVqMdT0wxMzExMjAyNA
    """

with st.expander("27 ноября 2024 года | Аутентификация пользователей", icon=":material/school:"):

    with open("files/md/Streamlit Аутентификация без SSO.md", 'r', encoding='utf8') as файл:
        текст =  файл.read()
    
    st.markdown(текст)
    """
    Streamlit Authenticator: https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/

    Аутентификация через Google: https://github.com/kajarenc/stauthlib.git
    """


with st.expander("25 декабря 2024 года | Работа с базами данных", icon=":material/school:"):

    with open("files/md/Работа с базами данных.md", 'r', encoding='utf8') as файл:
        текст =  файл.read()
    
    st.markdown(текст)
    """
    Подключение к базам данных: https://docs.streamlit.io/develop/api-reference/connections

    """