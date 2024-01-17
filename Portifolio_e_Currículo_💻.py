import streamlit as st
from st_pages import Page, show_pages

def main():
    
#Pagina Principal
    pfp_col_1, pfp_col_2 = st.columns(2,gap="small")
    pfp_col_2.image('pfp.png',width=260,caption="Eu")

    pfp_col_1.markdown("""<h1>Luis Guilherme Dias de Souza</h1>
            <p>Programador Python | Analista de Dados <br>
            21 Anos <br>
            Macaé - Rio de Janeiro <br>
            🐍📊⚙️🍃🐬🚀🚀</p>
            """
            , unsafe_allow_html=True)

    st.markdown("""
                <p>📞+55 (22) 988147990 <a href="mailto:gui.lgds2012@outlook.com">📧gui.lgds2012@outlook.com</a> <a href="https://www.linkedin.com/in/luis-guilherme-dias/">🔗Linkedin</a> <a href="https://github.com/Luiguie">🐙Github</a></p>
                <hr style="padding:0px;margin:0 0 15px 0">""",unsafe_allow_html=True)

    st.markdown("""
            <h3>Skills</h3>
            <h4>Hard Skills 🛠️</h4>
            <p>Python🐍 | Power BI📊 | Power Automate⚙️ | Power Apps📱 | Analise de Dados📈📊 | MongoDB🍃 | MySQL🐬 | RPA🤖 | Gestão de Projetos 📊🚀|
            🐍 : Pandas, Numpy, Plotly, Matplotlib, PyWinAuto, PyWin32, PyQt5, Pyside2, Streamlit, +</p>
            
            <h4>Soft Skills 🤝</h4>
            <p>Comunicação | Aprendizado Rápido | Motivado | Trabalho Sobre Pressão | Organização | Orientado a Resultados | Trabalho em Equipe | Resolução de Problemas
            """,
            unsafe_allow_html=True)

    st.markdown("""
            <h3>Sobre Mim 🧑‍💼</h3>
            <p>Meu objetivo é desenvolver e automatizar sistemas cada vez mais eficientes, 
            adquirindo experiência e habilidades ao longo do caminho. Eu sou apaixonado por programação e gosto de colaborar 
            com outros para solucionar problemas complexos.</p>
            """,
            unsafe_allow_html=True)

    st.markdown("""
                <h3>Experiências Profissionais 🏢</h3>
                <h4>Estagiário em Automação de Sistemas</h4>
                <p>Baker Hughes 08/23 - Atualmente</p>
                <li>Utilizei Python e suas bibliotecas para automatizar fluxos internos, otimizando operações;</li>
                <li>Projetei e implementei flows para otimização de tarefas com o Power Automate, reduzindo o esforço manual e aumentando a eficiência;</li>
                <li>Empreguei Python e VBA para automatizar planilhas do Excel, resultando em maior precisão dos dados e redução nos prazos de entrega;</li>
                <li>Desenvolvi dashboards de controle de KPIs com o Power BI, facilitando a tomada de decisões baseada em dados;</li>
                <li>Implementei técnicas de extração de dados em sistemas SAP usando Python;</li>
                <li>Integrei SharePoint com o Power Apps e o Power Automate para criar formulários e listas personalizadas, aprimorando a colaboração e a gestão de dados.</li>
                
                <h4>Aprendiz em Gestão de Projetos</h4>
                <p>SpeedCast 06/22 - 05/23</p>
                <li>Participação em reuniões de escopo de projetos;</li>
                <li>Gestão de Projetos em conjunto ao PM;</li>
                <li>Automação de planilhas e tarefas com Python e VBA;</li>
                <li>DAbertura de SCs;</li>
                <li>Tratamento de documentação;</li>
                <li>Emissão de relatórios financeiros/de operação para clientes.</li>
                
                """,
                unsafe_allow_html=True)

    #side bar
    st.sidebar.title("Portifólio e Currículo")
    st.sidebar.markdown("""
                        <p>📞+55 (22) 988147990 <br>
                        <a href="mailto:gui.lgds2012@outlook.com">📧gui.lgds2012@outlook.com</a> <br>
                        <a href="https://www.linkedin.com/in/luis-guilherme-dias/">🔗Linkedin</a> <br>
                        <a href="https://github.com/Luiguie">🐙Github</a></p>
                        """,
                        unsafe_allow_html=True)
                        

if __name__ == "__main__":
    st.set_page_config(page_title="Portifolio")
    st.markdown(
        """
        <style>
        a {
            text-decoration: none;
        }
        </style>
        """,
    unsafe_allow_html=True,
    )
    
    
    main()