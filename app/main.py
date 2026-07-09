class Person:
    # atributo de classe para armazenar todas as instâncias
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # adiciona a instância ao dicionário de pessoas
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    # primeiro cria todas as instâncias sem relacionamentos
    person_list = []
    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    # depois conecta marido/esposa
    for person_dict in people_data:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]

    return person_list
