import configuration
import requests
import data

# Функция для создания заказа
def create_order(order_data):
    url = f"{configuration.URL_SERVICE}{configuration.CREAT_ORDERS}"
    response = requests.post(url, json=order_data)
    return response

# Функция для получения заказа по номеру трекера
def fetch_order_by_tracker(tracker_id):
    url = f"{configuration.URL_SERVICE}/api/v1/orders/track"
    params = {"t": tracker_id}
    response = requests.get(url, params=params)
    return response

# Автотест: Создание и получение заказа
def test_create_and_fetch_order():
    # Создание нового заказа
    create_response = create_order(data.order_body)

    if create_response.status_code == 201:
        tracker_id = create_response.json().get("track")
        print(f"Заказ успешно создан. Номер трекера: {tracker_id}")
    else:
        print(f"Ошибка при создании заказа: {create_response.status_code}")
        return

    # Получение информации о заказе по трекеру
    fetch_response = fetch_order_by_tracker(tracker_id)

    assert fetch_response.ok, f"Ошибка при получении данных заказа: {fetch_response.status_code}"
    order_details = fetch_response.json()
    print("Информация о заказе:")
    print(order_details)
