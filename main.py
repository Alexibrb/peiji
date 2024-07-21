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
tab1, tab2 = st.tabs(["Cadastrar Dados", "Visualizar Dados(Só admin)"])
with tab1:
    cadastrar()
 
with tab2:
    visualisar()
    apagar()
