# streamlit_app.py
import hmac
import streamlit as st

def check_password():
    """Возвращает `True`, если пользователь ввел правильный пароль."""

    def password_entered():
        """Проверяет правильность введенного пользователем пароля."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Пароль не хранить!
        else:
            st.session_state["password_correct"] = False

    # Возвращает True, если пароль подтвержден.
    if st.session_state.get("password_correct", False):
        return True

    # Поле для ввода пароля
    st.text_input(
        "Пароль", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Сорян, Братан! Кривой пароль")
    return False


if not check_password():
    st.stop()  # Не продолжать, если check_password не True.

# Основной код приложения начинается здесь
st.write("Начало выполнения основного кода приложения...")
st.button("Жми!")