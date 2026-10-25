import streamlit as st
import httpx

def init_session_states():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "message_history" not in st.session_state:
        st.session_state.message_history = []


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input():
    if prompt := st.chat_input("Talk to the JokeBot"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = httpx.post(
            "http://127.0.0.1:8000/chat",
            json={
                "question": prompt, "message_history": st.session_state.message_history
            },
        ).json()

        st.session_state.message_history = response.get("message_history")

        bot_response = response.get("response")
        st.write(bot_response)

        response = f"Ro Båt: {bot_response}"

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


def layout():
    st.markdown("# Chat with Ro Båt")
    st.write(
        "RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back."
    )

    display_chat_messages()
    handle_user_input()


if __name__ == "__main__":
    init_session_states()
    layout()
