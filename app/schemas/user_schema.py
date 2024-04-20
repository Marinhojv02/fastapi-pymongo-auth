def user_individual_serial(user) -> dict:
    return {
        "_id": str(user['_id']),
        "nome": str(user["nome"]),
        "cpf": str(user["cpf"]),
        "username": str(user["username"]),
        "password": str(user["password"]),
        "email": str(user["email"]),
        "celular": str(user["celular"]),
        "funcao": str(user["funcao"]),
    }
    
def user_list_serial(users) -> list:
    return [user_individual_serial(user) for user in users]