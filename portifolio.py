import streamlit as st

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
            <style>
                a {
                    text-decoration: none;
                }
            </style>
            
            <p>📞+55 (22) 988147990 <a href="mailto:gui.lgds2012@outlook.com">📧gui.lgds2012@outlook.com</a> <a href="https://www.linkedin.com/in/luis-guilherme-dias/">🔗Linkedin</a> <a href="https://github.com/Luiguie">🐙Github</a></p>
            <hr style="padding:0px;margin:0 0 15px 0">""",unsafe_allow_html=True)

st.markdown("""
        <h3>Skills</h3>
        <p>Python🐍 | Power BI📊 | Power Automate⚙️ | Power Apps📱 | Analise de Dados📈📊 | MongoDB🍃 | MySQL🐬 | RPA🤖 | Gestão de Projetos 📊🚀|
        🐍 : Pandas, Numpy, Plotly, Matplotlib, PyWinAuto, PyWin32, PyQt5, Pyside2, Streamlit, +</p>
        """,
        unsafe_allow_html=True)

