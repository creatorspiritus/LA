import streamlit as st
from datetime import datetime, timedelta
from sqlalchemy import text

ДВЮ = lambda x: x.timestamp()    # Преобразование даты и времени
                                        # в unix-формат

# Преобразование unix-формата даты и времени в текстовую строку
ЮДВС = lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')

# Преобразование unix-формата даты и времени в формат datetime
ЮДВ = lambda x: datetime.fromtimestamp(x)

@st.dialog("Добавление записи")
def Добавить_запись_в_КЖП():
    with st.form(key="добавление_записи_КЖП", border=False):
        слева, справа = st.columns([1,1])
        слева.date_input("Дата", key="КЖП_новая_запись_дата", disabled=True)
        справа.time_input("Время", key="КЖП_новая_запись_время", disabled=True)
        st.selectbox("Пользователь", key="КЖП_новая_запись_пользователь",
            options=[
                "МК",
                "Добрый пользователь",
                "Опечаленный пользователь"
            ])
        st.text_area("Текст сообщения", key="КЖП_новая_запись_текст",
            placeholder="Используйте нормативную лексику, пожалуйста")
        датавремя = datetime.combine(
            st.session_state.КЖП_новая_запись_дата,
            st.session_state.КЖП_новая_запись_время
        )
        if st.form_submit_button("Ввод"):
            with st.session_state.соединение.session as сессия:
                сессия.execute(
                    text('INSERT INTO "Книга жалоб и предложений" ("Дата и время", "Пользователь", "Текст") VALUES (:DT, :user, :текст);'),
                    params=dict(
                        DT=ДВЮ(датавремя),
                        user=st.session_state.КЖП_новая_запись_пользователь,
                        текст=st.session_state.КЖП_новая_запись_текст)
                )
                сессия.commit()
            st.session_state.КЖП = st.session_state.соединение.query(
                'select * from "Книга жалоб и предложений"', ttl=timedelta(minutes=0))
            st.rerun()


слева, справа = st.columns([3,1], vertical_alignment="bottom")
слева.header("Книга жалоб и предложений", divider=True)
if справа.button("Добавить запись"):
    Добавить_запись_в_КЖП()
    
    # st.rerun()


# таблица = st.session_state.соединение.query('select * from "Книга жалоб и предложений"')

st.dataframe(st.session_state.КЖП, key="КЖП_таблица", hide_index=True, use_container_width=True)

for _ in st.session_state.КЖП.index:
    st.write(ЮДВ(st.session_state.КЖП.loc[_]["Дата и время"]))
    st.write(f"Пользователь: {st.session_state.КЖП.loc[_]['Пользователь']}")
    st.write(st.session_state.КЖП.loc[_]['Текст'])
    st.divider()
