import streamlit as st
import pandas as pd
import os
import time
from funcoes import *
from paginas import *

########## CONFIGURAÇÕES
st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto"
)
estilos()
titulo()

cria_sidebar()

cadastrar()

visualisar()

apagar()