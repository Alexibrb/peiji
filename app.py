import streamlit as st
import pandas as pd
import os
from time import sleep


def visualisar():
    if os.path.exists('clientes.csv'):
        tabclientes = pd.read_csv('clientes.csv', sep=",")
        senha = st.text_input("Digite a senha para visualizar os dados", type="password")
        btn_visualizar = st.button("Visualizar")
        if btn_visualizar:
            if senha == "ki47trqwe":

                st.table(tabclientes)

            else:
                st.error("Senha errada")



def apagar():
    if os.path.exists('clientes.csv'):
        senha2 = st.text_input("Digite a senha para Apagar os dados", type="password")
        btn_apagar = st.button("Apagar Dados dos Clientes", type="primary")
        if btn_apagar:
            if senha2 == "ki47trqwe":


                os.remove('clientes.csv')
                st.success("Dados Deletados com sucesso")
                sleep(2)
                st.experimental_rerun()
            else:
                st.error("Senha errada")







