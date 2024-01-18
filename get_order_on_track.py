import sender_stend_request

# Функция для позитивной проверки
def positive_assert(track_order):
    # Сохраняется результат запроса на получение заказа по трек номеру
    order_response = sender_stend_request.get_order_track(track_order)
    # Проверка, что код ответа  200
    assert order_response.status_code == 200


# Тест на получение трек номера:
def test_get_order_track_success_response():
    positive_assert(sender_stend_request.track_order)
