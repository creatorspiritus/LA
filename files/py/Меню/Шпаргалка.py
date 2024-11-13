import streamlit as st


st.subheader("Шпаргалка", divider=True)

"""В этом разделе представлены элементы пакета :streamlit: streamlit.
В начале каждого раздела представлено краткое описание элемена, затем
примеры его использования и рекомендации по применению.

В конце раздела ссылка на официальное описание элемента на сайте
разработчика."""

with st.expander("Текст и волшебство", icon=":material/edit_note:"):
    """
    Зарезервировано
    """
    st.link_button("Описание элемента `st.write` на странице разработчика", 
                   url="https://docs.streamlit.io/develop/api-reference/write-magic/st.write",
                   use_container_width=True)

with st.expander("Элементы текста", icon=":material/format_align_justify:"):
    """
    Зарезервировано
    """

with st.expander("Элементы данных", icon=":material/storage:"):
    """
    Зарезервировано
    """

with st.expander("Карты и диаграммы", icon=":material/monitoring:"):
    """
    Зарезервировано
    """

with st.expander("Элементы ввода данных", icon=":material/keyboard_keys:"):
    """
    Зарезервировано
    """

with st.expander("Видео, аудио, рюшечки", icon=":material/smart_display:"):
    """
    Зарезервировано
    """

with st.expander("Макеты и контейнеры", icon=":material/calendar_view_month:"):
    """
    Зарезервировано
    """

with st.expander("Переписка", icon=":material/forum:"):
    """
    Зарезервировано
    """

with st.expander("Статусы и состояния", icon=":material/person_celebrate:"):
    """
    Зарезервировано
    """

with st.expander("Меню и настройка", icon=":material/construction:"):
    """
    Зарезервировано
    """
