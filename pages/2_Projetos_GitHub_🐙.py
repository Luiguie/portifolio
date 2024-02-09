import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center;'>Projetos GitHub</h1><hr>", unsafe_allow_html=True)

    st.markdown("""
                <h3>Introdução</h3>
                <p>Nesta página se encontram projetos que somente existem no github, sem uma interface web por não estar no escopo
                deste tipo de aplicação. Em cada um ficará uma breve explicação e um link para o repositório.</p>
                """,unsafe_allow_html=True)
    
    st.markdown("""
                <h3>MP3 Youtube Converter ▶️ ->🎵 </h3>
                <ul>
                    <li>Feito com Python. Utilizando Tkinter e Pytube</li>
                    <li>Realiza a conversão e download de videos do Youtube para o formato MP3. Possui uma interface simples e de fácil entendimento,
                    permite a conversão de vários videos ao mesmo tempo.</li>
                    <li><a href="https://github.com/Luiguie/Mp3YoutubeImporter">GitHub Repo</a></li>
                </ul>
                """,unsafe_allow_html=True)
    
    st.markdown("""
                <h3>PDF Keyterm Searcher 📄🔍 </h3>
                <ul>
                    <li>Feito com Python. Utilizando Tkinter e PyPDF2</li>
                    <li>Permite a busca de uma palavra em um conjunto de PDFs selecionados em determinada pasta. Em cada PDF será buscado a palavra chave
                    e o programa irá retornar a lista de PDFs que contém essa palavra chave, dando a opção de abri-los para análise.</li>
                    <li><a href="https://github.com/Luiguie/KeytermPDFSearcher">GitHub Repo</a></li>
                </ul>
                """,unsafe_allow_html=True)
    
    st.markdown("""
                <h3>QR Code Generator 🏁🛠️ </h3>
                <ul>
                    <li>Feito com Python. Utilizando Pyqt5 e qrcode</li>
                    <li>Gera QR Codes a partir de links ou texto. Os QR Code Gerados não expiram.</li>
                    <li><a href="https://github.com/Luiguie/qr_code_generator">GitHub Repo</a></li>
                </ul>
                """,unsafe_allow_html=True)
    
    st.sidebar.title("Portifólio e Currículo")
    st.sidebar.markdown("""
                        <p>📞+55 (22) 988147990 <br>
                        <a href="mailto:gui.lgds2012@outlook.com">📧gui.lgds2012@outlook.com</a> <br>
                        <a href="https://www.linkedin.com/in/luis-guilherme-dias/">🔗Linkedin</a> <br>
                        <a href="https://github.com/Luiguie">🐙Github</a></p>
                        """,
                        unsafe_allow_html=True)
    

if __name__ == "__main__":
    st.set_page_config(page_title="Projetos GitHub")
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