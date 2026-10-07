from conversation import clear_conversation_context


def test_clear_conversation_context_keeps_initial_context():
    messages = [
        {"role": "system", "content": "instructions"},
        {"role": "system", "content": "persistent memories"},
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"},
    ]

    clear_conversation_context(messages, 2)

    assert messages == [
        {"role": "system", "content": "instructions"},
        {"role": "system", "content": "persistent memories"},
    ]


def test_clear_conversation_context_when_history_is_empty():
    messages = [
        {"role": "system", "content": "instructions"},
        {"role": "system", "content": "persistent memories"},
    ]

    clear_conversation_context(messages, 2)

    assert len(messages) == 2
