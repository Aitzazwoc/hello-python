def make_greeting(name: str) -> str:
    cleaned_name = name.strip()
    if not cleaned_name:
        return "Hello, there!"
    return f"Hello, {cleaned_name}!"

if __name__ == "__main__":
    user_name = input("What is your name? ")
    print(make_greeting(user_name))