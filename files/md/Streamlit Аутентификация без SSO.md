# Аутентификация без SSO



## Введение

Этот совет поможет Вам организовать вход в приложение через имя пользователя и пароль. Здесь представлены два простых способа добавления базовой аутентификации.

П р и м е ч а н и е: Представленные алгоритмы добавляют защиту входа в приложение, но они не обеспечивают уровень безопасности провайдера SSO.

> **SSO-провайдер** — это программный компонент, который предоставляет единый способ аутентификации и входа в приложения. Он содержит учётные данные пользователей приложения и предоставляет различные уровни доступа.
>
> SSO позволяет пользователям получать доступ к разным системам и приложениям, используя один и тот же набор учётных данных (имя пользователя и пароль). 



## Вариант 1: Один пароль для всех пользователей

Cамый простой вариант. Приложение будет запрашивать пароль, который будет общим для всех пользователей. Он будет храниться в файле `.streamlit/secrets.toml`. При изменении пароля, параметры входа изменятся для всех. Для индивидуального входа каждого пользователя использовать второй вариант (см. ниже).



### Шаг 1: Добавить пароль в файл `secrets.toml`

Прорграмма будет запрашивать данные из файла `.streamlit/secrets.toml` в корневом каталоге приложения. Для этого необходимо создать этот файл, если он еще не существует, и добавить в него свой пароль, как показано ниже:

```toml
password = "streamlit123" 
```



> #### Важно
>
> Если для разработки применяется `GitHub` или другой аналогичный сервис совместной работы с приложением, обязательно добавьте этот файл в `.gitignore`, чтобы не распространять конфиденциальную информацию.



### Шаг 2: Скопируйте секреты приложения в облако

Поскольку файл `secrets.toml` не отправляется в `GitHub`, потребуется ручной перенос этого файла в развернутое приложение отдельно. Для этого необходимо перейти в экран настройки приложения и в выпадающем меню нажать `Edit Secrets`. Скопировать содержимое файла `secrets.toml` в текстовую область. Дополнительную информацию можно найти в разделе **Управление доступом** (Secrets managements).

![Secrets manager screenshot](https://docs.streamlit.io/images/databases/edit-secrets.png)



### Шаг 3: Запросить пароль в приложении Streamlit

Скопировать приведенный ниже код в свое приложение, вставить основной код приложения ниже вызова функции `check_password()` в самом низу и запустить:

```python
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
```

Окно входа в приложение:

![Global passwords](https://docs.streamlit.io/images/streamlit-community-cloud/auth-without-sso-global.png)



## Вариант 2: Индивидуальный вход для каждого пользователя

Этот способ позволяет задать имя и пароль для каждого пользователя приложения. Как и в первом варианте, оба значения будут храниться в файле `.streamlit/secrets.toml`.

### Шаг 1: Добавить имена пользователей и пароли в `secrets.toml`

Программа будет сравнивать вводимые пользователями данные из файла `.streamlit/secrets.toml`, расположенного в подкаталоге `.streamlit` корневого каталога приложения. Для этого необходимо создать файл `.streamlit/secrets.toml`, если он еще не существует, и добавить в него имена пользователей и пароли, как показано ниже:

```toml
# .streamlit/secrets.toml

[passwords]
# Следовать правилу: "имя_пользователя" = "пароль"
# Английский текст в именах и значениях могут набираться без кавычек
alice_foo = "streamlit123"
bob_bar = "mycrazypw"
# При использовании кириллицы имена и значения заключать в кавычки
["пароли"]
"Миша" = "Техпис248"
"Паша" = "главный"
"админ" = "админ"
```

> #### Важно
>
> Обязательно добавить `s.streamlit/ecrets.toml` в `.gitignore`, чтобы не распространять конфиденциальную информацию.

В качестве альтернативы можно настроить и управлять именами пользователей и паролями с помощью электронных таблиц или базы данных. Чтобы использовать ключевую информацию для безопасного подключения к Google Sheets, AWS и другим поставщикам данных, необходимо ознакомиться с руководством по [подключению Streamlit к источникам данных](https://docs.streamlit.io/develop/tutorials/databases).



### Шаг 2: Перенос ключевой информации в облако

Поскольку файл `secrets.toml` не хранится на `GitHub`, требуется перенос его содержимого в развернутое приложение (на Streamlit Community Cloud) отдельно. Для этого необходимо перейти в экран настроек и в выпадающем меню приложения нажать **Edit Secrets** и перенести содержимое файла `secrets.toml` в текстовую область. Дополнительную информацию можно найти в разделе **Управление доступом** (Secrets manegement).

![Secrets manager screenshot](https://docs.streamlit.io/images/databases/edit-secrets.png)



### Шаг 3: Кодирование доступа

Скопировать приведенный ниже код в свое приложение. Основной код приложения должен находиться ниже вызова функции `check_password()`:

```python
#  streamlit_app.py

import hmac
import streamlit as st

def check_password():
    """Возвращает `True`, если пользователь ввел правильный пароль."""

    def login_form():
        """Форма с элементами ввода информации о пользователе"""
        with st.form("Credentials"):
            st.text_input("Пользователь", key="username")
            st.text_input("Пароль", type="password", key="password")
            st.form_submit_button("Вход", on_click=password_entered)

    def password_entered():
        """Проверка введённой ключевой информации"""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"] # Удалить пароль
            del st.session_state["username"] # Удалить имя пользователя
        else:
            st.session_state["password_correct"] = False

    # Возвращает True, если имя пользователя и пароль подтверждены
    if st.session_state.get("password_correct", False):
        return True

    # Вывод на экран формы для ввода имени пользователя и пароля
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 Пользователь мне не знаком или пароль его неверен")
    return False


if not check_password():
    st.stop()

# Основной код приложения начинается здесь
st.write("Здесь начинается основной код приложения...")
st.button("Жми!")
```

Вход в приложение должен выглядеть так:

![Individual passwords](https://docs.streamlit.io/images/streamlit-community-cloud/auth-without-sso-individual.png)