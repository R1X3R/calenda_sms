import streamlit as st

def main():
    st.title("Calendário do Google - SMS/Assis")

    # Inserir o código HTML do calendário do Google
    st.markdown(
        """
        <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%234285F4&ctz=America%2/Sao_Paulo&showTz=0&showTabs=1&src=ZWR1Y2FjYW9jb250aW51YWRhc21zYXNzaXNAZ21haWwuY29t&src=MTk1OGQ2MDhhMjYzMzUyMzY0NmQ4Zjk5MWU5YzQwYjcyZWM2ZThiMzkyY2U2ZWU1MzliZDlhM2IwMmI0MGJkZTUwYkBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=YWYwNmM3NGE4N2JlZjQ3ODBlYTBlNWYxDlmMzIwM2JhMjBmNzUyMjM2NDcwOThiNzY0MWU1ZGJahZDA0ZWM4MkBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=NTA4NGMyMTc4YzYzYTM3YjZlNTFjOGFmMWE4YzEyM2E0YTg1ZTI4YzE3MWVkNGMyZWQwYmIyNTRjMmExYzk5YkBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23039BE5&color=%23F4511E&color=%238E24AA&color=%23AD1457" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
