import streamlit as st
import pandas as pd
import os
from time import sleep

def are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
    return name and address and phone
    
def cadastrar():
    if os.path.exists('clientes.csv'):
        tabclientes = pd.read_csv('clientes.csv', sep=",")

        with st.form("configp", clear_on_submit=True):
            cidade = st.selectbox(label="Selecione a sua Cidade:", options=[
                "Condeúba",
                "Maetinga",
                "Pres. Jânio Quadros",
                "Cordeiros",
                "Piripá",
                "Mortugaba"
            ])
            nome = st.text_input("Digite seu nome", placeholder="Nome Completo")
            telefone = st.text_input("Digite seu Telefone", placeholder="(xx) xxxx-xxxx")
            rg = st.text_input("Digite seu RG", placeholder="xxxxxxxx-xx")
            cpf = st.text_input("Digite seu CPF", placeholder="xxx.xxx.xxx-xx")
            endereco_obra = st.text_input("Digite o Endereço da Obra", placeholder="Rua, nº e bairro")
            endereco_resid = st.text_input("Digite o Endereço Residencial", placeholder="Rua, nº e bairro")
            obs = st.text_area("Observação", placeholder="não obrigatório")
            
            
            btn_cadastro = st.form_submit_button("Cadastrar Dados")
    
            if btn_cadastro:
                cidadec = cidade
                cliente = nome
                fone = telefone
                rgc = rg
                cpfc = cpf
                end1 = endereco_obra
                end2 = endereco_resid
                obs1 = obs
                data2 = pd.DataFrame(tabclientes)
                d = {"Cidade": cidadec, 
                     "Nome": cliente, 
                     "Telefone": fone, 
                     "RG": rgc, 
                     "CPF": cpfc, 
                     "Endereço_Obra": end1,
                     "Endereço_Residencial": end2,
                     "Observação":obs1
                    }
                df2 = pd.DataFrame(d, index=[0])
                data2 = pd.concat([data2, df2], ignore_index=True)
                data2.to_csv('clientes.csv', index=False)
                st.success("# Cadastro Efetuado com sucesso!!!!")
                sleep(1)
            st.experimental_rerun()



    else:
        with st.form("config", clear_on_submit=True):
            cidade = st.selectbox(label="Selecione a sua Cidade:", options=[
                "Condeúba",
                "Maetinga",
                "Pres. Jânio Quadros",
                "Cordeiros",
                "Piripá",
                "Mortugaba"
            ])
            nome = st.text_input("Digite seu nome", placeholder="Nome Completo")
            telefone = st.text_input("Digite seu Telefone", placeholder="(xx) xxxx-xxxx")
            rg = st.text_input("Digite seu RG",placeholder="xxxxxxxx-xx")
            cpf = st.text_input("Digite seu CPF",placeholder="xxx.xxx.xxx-xx")
            endereco_obra = st.text_input("Digite o Endereço da Obra", placeholder="Rua, nº e bairro")
            endereco_resid = st.text_input("Digite o Endereço Residencial", placeholder="Rua, nº e bairro" )
            obs = st.text_area("Observação", placeholder="não obrigatório")
            # Mensagem de aviso
            warning_message = st.empty()

            # Desativando o botão se algum campo estiver vazio
            if not are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
                warning_message.warning("Por favor, preencha todos os campos.")
            else:
                warning_message.empty()
                
            btn_cadastro = st.form_submit_button("Cadastrar Dados")
    
            if btn_cadastro and are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
                cidadec = cidade
                cliente = nome
                fone = telefone
                rgc = rg
                cpfc = cpf
                end1 = endereco_obra
                end2 = endereco_resid
                obs1 = obs
                
                data2 = pd.DataFrame(columns=['Cidade', 
                                              'Nome', 
                                              'Telefone',
                                              'RG', 
                                              'CPF',
                                              'Endereço_Obra',
                                              'Endereço_Residencial'
                                              'Observação'
                                             ])
                d = {"Cidade": cidadec, 
                     "Nome": cliente, 
                     "Telefone": fone, 
                     "RG": rgc, 
                     "CPF": cpfc, 
                     "Endereço_Obra": end1,
                     "Endereço_Residencial": end2,
                     "Observação": obs1
                    }
                
                df2 = pd.DataFrame(d, index=[0])
                data2 = pd.concat([data2, df2], ignore_index=True)
                data2.to_csv('clientes.csv', index=False)
                st.success("# Cadastro Efetuado com sucesso!!!!")
                sleep(1)
                st.experimental_rerun()



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
    else:
        st.warning("### Nenhum Registro Encontrado")


def apagar():
    if os.path.exists('clientes.csv'):
        senha2 = st.text_input("Digite a Senha para Apagar os dados", type="password")
        btn_apagar = st.button("Apagar Dados dos Clientes", type="primary")
        if btn_apagar:
            if senha2 == "ki47trqwe":


                os.remove('clientes.csv')
                st.success("Dados Deletados com sucesso")
                sleep(0.5)
                st.experimental_rerun()
            else:
                st.error("Senha errada")






