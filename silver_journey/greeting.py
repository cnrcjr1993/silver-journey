"""Greeting helpers."""


def build_greeting(name: str) -> str:
    """Return a friendly greeting for a non-empty name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")
    return f"Welcome aboard, {cleaned_name}!"
