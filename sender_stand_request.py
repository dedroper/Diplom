# Дмитрий 20 когорта
import requests
import configuration


# Функция для создания заказа
def create_order(order_data):
    url = f"{configuration.URL_SERVICE}{configuration.CREATE_ORDERS}"
    response = requests.post(url, json=order_data)
    return response

# Функция для получения заказа по номеру трекера
def fetch_order_by_tracker(tracker_id):
    url = f"{configuration.URL_SERVICE}{configuration.FETCH_ORDER_TRACK}"
    params = {"t": tracker_id}
    response = requests.get(url, params=params)
    return response
