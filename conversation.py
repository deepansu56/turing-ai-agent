def clear_conversation_context(messages, context_length):
    """Remove live conversation history while keeping initial context."""
    del messages[context_length:]
