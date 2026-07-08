def create_greeting(name: str) -> str :
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not name.strip():
        raise ValueError("Name cannot be empty")
    
    return f"Hello, {name.strip()}! you're python setup is working"

def test_create_greeting_success():
    assert create_greeting("Kamal") == "Hello, Kamal! you're python setup is working"

def test_create_greeting_empty_name():
    try:
        create_greeting("")
    expect ValueError as error: 
         assert str(error) == "Name cannot be empty"
    
    
