full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return("The character name should be a string")
    
    if name == "":
        return("The character should have a name")
    
    if len(name) > 10:
        return("The character name is too long")
    
    if " " in name:
        return("The character name should not contain spaces")

    if not (isinstance(strength, int) and not isinstance(strength, bool)
            and isinstance(intelligence, int) and not isinstance(intelligence, bool)
            and isinstance(charisma, int) and not isinstance(charisma, bool)):
        return("All stats should be integers")
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return("All stats should be no less than 1")
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return("All stats should be no more than 4")
    
    if strength + intelligence + charisma != 7:
        return("The character should start with 7 points")
    
    def render(n):
        return full_dot * n + empty_dot * (10 - n)
    
    return f"{name}\nSTR {render(strength)}\nINT {render(intelligence)}\nCHA {render(charisma)}"

if __name__ == "__main__":
    print(create_character("Aragorn", 3, 2, 2))
    print(create_character("", 3, 2, 2))
    print(create_character("Legolas", 5, 1, 1))
    print(create_character("Gimli", 3, 3, 3))
    print(create_character("Frodo", 2, 2, 3))
    