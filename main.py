from funcoes import *
from paginas import *

########## CONFIGURAÇÕES
st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto"
)
estilos()
titulo()
cadastrar()
tab1, tab2 = st.tabs(["Cadastar", "Visualizar"])
with tab1:
    visualisar()
with tab2:
    apagar()
