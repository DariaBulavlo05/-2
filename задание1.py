def calculate_interest(total, interest_rate):
    return total * interest_rate


def calculate_total_amount(a, years):
    total = a
    interest_rate = 0.1

    for _ in range(years):
        try:
            interest = calculate_interest(total, interest_rate)
            total += interest
            total += a
        except Exception as e:
            print(f"Произошла ошибка при расчете процентов: {e}")
            return None

    return total


def bank(a, years):
    try:
        result = calculate_total_amount(a, years)
        if result is not None:
            print(f"Сумма на счету после {years} лет: {result} рублей")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение работы функции bank.")


# Пример использования
a = 1000
years = 5
bank(a, years)