@@ -248,7 +248,7 @@ def show_cancel_generate_button_js():
    html(js, 0, 0, False)


def show_generate_chat_input_js():
def show_stop_generate_chat_input_js():
    js = """
<script>
console.log("show_generate_chat_input_js");
@@ -277,7 +277,7 @@ def set_chat_input_text(promptText: str):
    html(js, 0, 0, False)


def embed_chat_input_js():
def embed_chat_input_tokenizer():
    embed_chat_tokenizer_js('.stChatInputContainer textarea',
                            'section[tabindex="0"] textarea[aria-label="tokenizer2"]')