from streamlit_option_menu import option_menu
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
# horizontal Menu
selected2 = option_menu(None, ["Cadastrar", "Visualizar"],
                            icons=['cloud-upload', "list-task"],
                            menu_icon="cast", default_index=0, orientation="horizontal")
st.write(f"# Página/{selected2}")
if selected2 == "Cadastrar":
    cadastrar()
if selected2 == "Visualizar":
    visualisar()
    apagar()
