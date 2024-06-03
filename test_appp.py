@@ -54,10 +54,9 @@ def test_chat_strated():
    send_button.click().run()
    assert len(app_test.button) == 3, "Button list does not contain 3 elements"
    assert app_test.button[0].label == 'Delete Chat', "First button is not 'Delete Chat'"
    assert app_test.button[1].label == 'Cancel generation', "Second button is not 'Cancel generation'"
    assert app_test.button[2].key == 'FormSubmitter:hidden-Submit', "Third button key is not 'FormSubmitter:hidden-Submit'"
    assert app_test.button[2].label == 'Submit', "Third button label is not 'Submit'"
    assert app_test.button[2].form_id == 'hidden', "Third button form_id is not 'hidden'"
    assert app_test.button[1].label == 'Submit', "2nd button label is not 'Submit'"
    assert app_test.button[2].label == 'Cancel generation', "3rd button is not 'Cancel generation'"

    # print_debug(app_test)
