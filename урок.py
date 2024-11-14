import streamlit as st

if "самолёт_крейсерская" not in st.session_state: st.session_state.самолёт_крейсерская = 500
if "самолёт_потолок" not in st.session_state: st.session_state.самолёт_потолок = 7200
if "самолёт_расход_кглч" not in st.session_state: st.session_state.самолёт_расход_кглч = 560
if "самолёт_расход_кгкм" not in st.session_state: st.session_state.самолёт_расход_кгкм = st.session_state.самолёт_расход_кглч/st.session_state.самолёт_крейсерская
if "самолёт_масса_максимальная" not in st.session_state: st.session_state.самолёт_масса_максимальная = 23500
if "самолёт_масса_снаряжённого" not in st.session_state: st.session_state.самолёт_масса_снаряжённого = 15000
if "самолёт_масса_доступно" not in st.session_state: st.session_state.самолёт_масса_доступно = st.session_state.самолёт_масса_максимальная - st.session_state.самолёт_масса_снаряжённого
if "самолёт_салон" not in st.session_state: st.session_state.самолёт_салон = 68
if "загрузка_пассажиров" not in st.session_state: st.session_state.загрузка_пассажиров = int(st.session_state.самолёт_салон*0.7)
if "загрузка_груз" not in st.session_state: st.session_state.загрузка_груз = int((st.session_state.самолёт_масса_доступно - st.session_state.загрузка_пассажиров*100)*0.7)
if "маршрут_км" not in st.session_state: st.session_state.маршрут_км = 309
if "маршрут_откуда" not in st.session_state: st.session_state.маршрут_откуда = "UNWW"
if "маршрут_куда" not in st.session_state: st.session_state.маршрут_куда = "UNNT"
if "цена_авиатопливо" not in st.session_state: st.session_state.цена_авиатопливо = 100000

st.session_state

# слева, центр, справа = st.columns([1,1,1])

with st.popover("Самолёт", icon=":material/flight:", use_container_width=True):
    с1, с2 = st.columns([1,1])
    с1.number_input("Крейсерская скорость, км/ч", key="самолёт_крейсерская", 
                  value=st.session_state.самолёт_крейсерская,
                  min_value=10, max_value=5000)
    с2.number_input("Практический потолок, м", key="самолёт_потолок", 
                  value=st.session_state.самолёт_потолок,
                  min_value=1200, max_value=10000)



with st.popover("Маршрут", icon=":material/conversion_path:", use_container_width=True):
    с1, с2 = st.columns([1,1])
    с1.selectbox("Откуда", key="маршрут_откуда", 
                  options=[
                      "UNWW", "UNNT"
                  ])
    с2.selectbox("Куда", key="маршрут_куда", 
                  options=[
                      "UNNT", "UNWW"
                  ])



with st.popover("Загрузка", icon=":material/airline_seat_recline_extra:", use_container_width=True):
    с1, с2 = st.columns([1,1])
    с1.number_input("Пассажиров", key="загрузка_пассажиров", 
                  value=st.session_state.загрузка_пассажиров,
                  min_value=0, max_value=st.session_state.самолёт_салон)
    с2.number_input("Багаж, груз, почта, кг", key="загрузка_груз", 
                  value=st.session_state.загрузка_груз,
                  min_value=0,
                  max_value=st.session_state.самолёт_масса_доступно)



with st.popover("Стоимость", icon=":material/currency_ruble:", use_container_width=True):
    #с1, с2 = st.columns([1,1])
    st.number_input("Авиатопливо в крыло, руб/т", key="цена_авиатопливо", 
                  value=st.session_state.цена_авиатопливо,
                  min_value=0, max_value=1000000)
    
