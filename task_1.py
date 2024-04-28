import queue
import time


# Створення черги заявок
request_queue = queue.Queue()
request_count = 0


def generate_request():
    """Генерує нові заявки та додає їх до черги."""
    global request_count
    request_count += 1

    request_id = request_count
    print(f"Згенеровано нову заявку з ID: {request_id}")
    request_queue.put(request_id)


def process_request():
    """Видаляє заявку з черги та обробляє її."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробляємо заявку з ID: {request_id}")
    else:
        print("Черга пуста")


def main():
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Програма завершена користувачем")


if __name__ == "__main__":
    main()
