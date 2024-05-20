import requests
from datetime import datetime
from access_token import TOKEN

domain = "https://api.vk.com/method"

def get_friends(user_id):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    
    url = f"{domain}/friends.get?&user_id={user_id}&fields=bdate&access_token={TOKEN}&v=5.199"
    response = requests.get(url) # Ответ сервера на посланный нами запрос
    src = response.json()

    return src["response"]["items"]

def age_predict(users):
    average_age = 0
    users_count = 0

    for user in users:
        try:
            birthdate = datetime.strptime(user["bdate"], "%d.%m.%Y")
            age = datetime.now().year - birthdate.year - ((datetime.now().month, datetime.now().day) < (birthdate.month, birthdate.day))

            print(f"{user["first_name"]} {user["last_name"]}: {age} лет")

            users_count += 1
            average_age += age
        except:
            pass
    
    return average_age/users_count


user_id = 513939745
friends = get_friends(user_id)
print(f"\nСредний возраст id{user_id}: {age_predict(friends)}")