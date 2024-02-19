import streamlit as st
def tela_receitas():
    # titulo com ícone de panela
    st.title(':fork_and_knife: Receitas')
    # selecionar ação CRUD - Adicionar
    selected = st.selectbox('Escolha uma ação', ['Adicionar', 'Editar', 'Excluir', 'Visualizar'])
    show = st.checkbox('Mostrar receitas')
    # se ação for Adicionar
    if selected == 'Adicionar':
        # formulário para adicionar receita
        st.subheader('Adicionar receita')
        name = st.text_input('Nome da receita')
        tags = st.text_input('Tags')
        ingredients = st.text_area('Ingredientes')
        n_ingredients = st.number_input('Número de ingredientes', min_value=1, max_value=100)
        # botão para adicionar receita
        if st.button('Adicionar'):
            st.write('Receita adicionada com sucesso')
    # se ação for Editar
    if selected == 'Editar':
        # formulário para editar receita
        st.subheader('Editar receita')
        name = st.text_input('Nome da receita')
        tags = st.text_input('Tags')
        ingredients = st.text_area('Ingredientes')
        n_ingredients = st.number_input('Número de ingredientes', min_value=1, max_value=100)
        # botão para editar receita
        if st.button('Editar'):
            st.write('Receita editada com sucesso')
    # se ação for Excluir
    if selected == 'Excluir':
        # formulário para excluir receita
        st.subheader('Excluir receita')
        name = st.text_input('Nome da receita')
        # botão para excluir receita
        if st.button('Excluir'):
            st.write('Receita excluída com sucesso')
    # se ação for Visualizar
    if selected == 'Visualizar':
        # formulário para visualizar receita
        st.subheader('Visualizar receita')
        name = st.text_input('Nome da receita')
        # botão para visualizar receita
        if st.button('Visualizar'):
            st.write('Receita visualizada com sucesso')
            