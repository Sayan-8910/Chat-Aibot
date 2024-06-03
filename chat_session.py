@@ -3,7 +3,7 @@
import logic.utility as util
from ui.ui_helpers import (chat_bottom_padding, chat_collapse_markdown_hidden_elements, right_align_2nd_col_tokenizer,
                           show_cancel_generate_button_js, set_chat_input_text,
                           embed_chat_input_js, hide_tokinzer_workaround_form,
                           embed_chat_input_js, hide_tokenzer_workaround_form,
                           show_generate_chat_input_js, cancel_generation_button_styles)


@@ -19,43 +19,14 @@ def show_chat_session(chat_session: state.ChatSession, model: state.Model):
    if 'get_and_display_ai_reply_BREAK' not in st.session_state:
        st.session_state['get_and_display_ai_reply_BREAK'] = False

    hide_tokinzer_workaround_form()
    hide_tokenzer_workaround_form()
    chat_bottom_padding()
    chat_collapse_markdown_hidden_elements()
    cancel_generation_button_styles()
    right_align_2nd_col_tokenizer()

    # Hidden elements to trigger server side counting of token in chat input
    with st.form("hidden"):
        txt = st.text_area("tokenizer2").strip()
        st.form_submit_button("Submit")
        if txt != st.session_state['prompt_for_tokenizer'] \
                and not (txt == '' and st.session_state['prompt_for_tokenizer'] is None):
            st.session_state['prompt_for_tokenizer'] = None if txt == '' else txt
            st.rerun()

    # Chat header
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Delete Chat'):
            state.session_manager.delete(chat_session.session_id)
            st.session_state['get_and_display_ai_reply_BREAK'] = True
            st.session_state['generating'] = False
            st.rerun()
    with col2:
        if chat_session is not None:
            model_alias = model.alias if model else "No Model"
            if st.session_state['token_count'] is None:
                st.session_state['token_count'] = util.num_tokens_from_messages(chat_session.messages)
            if 'prompt_for_tokenizer' in st.session_state and st.session_state['prompt_for_tokenizer']:
                prompt_tokens = util.num_tokens_from_messages(
                    [{'role': 'User', 'content': st.session_state['prompt_for_tokenizer']}])
            else:
                prompt_tokens = 0
            if prompt_tokens > 0:
                st.write(f"{model_alias} / {st.session_state['token_count'] } +{prompt_tokens}")
            else:
                st.write(f"{model_alias} / {st.session_state['token_count'] }")

    try:
        if chat_session is not None:
@@ -110,17 +81,48 @@ def show_chat_session(chat_session: state.ChatSession, model: state.Model):

    except Exception as e:
        st.session_state['generating'] = False
        st.session_state['get_and_display_ai_reply_BREAK'] = False
        with st.container():
            st.write('An error occurred while sending Chat API request')
            st.write(e)

    # Hidden elements to trigger server side counting of token in chat input
    with st.form("hidden"):
        txt = st.text_area("tokenizer2").strip()
        st.form_submit_button("Submit")
        if txt != st.session_state['prompt_for_tokenizer'] \
                and not (txt == '' and st.session_state['prompt_for_tokenizer'] is None):
            st.session_state['prompt_for_tokenizer'] = None if txt == '' else txt
            st.rerun()

    embed_chat_input_js()
    show_generate_chat_input_js()
    # Cancelation happened, fill in chat input with past prompt
    if st.session_state['canceled_prompt'] not in (None, ''):
        set_chat_input_text(st.session_state['canceled_prompt'])
        st.session_state['canceled_prompt'] = None

    with col1:
        if st.button('Delete Chat'):
            state.session_manager.delete(chat_session.session_id)
            st.session_state['get_and_display_ai_reply_BREAK'] = True
            st.session_state['generating'] = False
            st.rerun()
    with col2:
        if chat_session is not None:
            model_alias = model.alias if model else "No Model"
            if st.session_state['token_count'] is None:
                st.session_state['token_count'] = util.num_tokens_from_messages(chat_session.messages)
            if 'prompt_for_tokenizer' in st.session_state and st.session_state['prompt_for_tokenizer']:
                prompt_tokens = util.num_tokens_from_messages(
                    [{'role': 'User', 'content': st.session_state['prompt_for_tokenizer']}])
            else:
                prompt_tokens = 0
            if prompt_tokens > 0:
                st.write(f"{model_alias} / {st.session_state['token_count'] } +{prompt_tokens}")
            else:
                st.write(f"{model_alias} / {st.session_state['token_count'] }")


def get_and_display_ai_reply(client, model: state.Model,
                             chat_session: state.ChatSession) -> None:
@@ -130,6 +132,7 @@ def get_and_display_ai_reply(client, model: state.Model,
    try:
        message_placeholder = st.empty()
        full_response = ''
        message_placeholder.markdown('...')

        for response in client.chat.completions.create(
                    model=model.model_or_deployment_name,
