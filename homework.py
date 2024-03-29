from typing import Dict, Type


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        """Вернёт сообщение в виде строки с данными о тренировке."""

        info_message: str = (f'Тип тренировки: {self.training_type}; '
                             f'Длительность: {self.duration:.3f} ч.; '
                             f'Дистанция: {self.distance:.3f} км; '
                             f'Ср. скорость: {self.speed:.3f} км/ч; '
                             f'Потрачено ккал: {self.calories:.3f}.')
        return info_message


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: float = 1000
    MIN_IN_HOUR: float = 60
    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""

    CALORIES_RUN_MULTIPLIER_1: float = 18
    CALORIES_RUN_MULTIPLIER_2: float = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        return (self.weight * (self. CALORIES_RUN_MULTIPLIER_1
                * self.get_mean_speed()
                - self.CALORIES_RUN_MULTIPLIER_2)
                / self.M_IN_KM * (self.duration
                * self.MIN_IN_HOUR))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_SPORTWALK_MULTIPLIER_1: float = 0.035
    CALORIES_SPORTWALK_MULTIPLIER_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return (self.weight * (self.CALORIES_SPORTWALK_MULTIPLIER_1
                + (self.get_mean_speed()**2 // self.height)
                * self.CALORIES_SPORTWALK_MULTIPLIER_2)
                * (self.duration * self.MIN_IN_HOUR))


class Swimming(Training):
    """Тренировка: плавание."""

    CALORIES_SWIM_MULTIPLIER_1: float = 1.1
    CALORIES_SWIM_MULTIPLIER_2: float = 2
    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = length_pool  # длинна бассейна в метрах
        self.count_pool = count_pool  # сколько раз проплыл бассейн

    def get_mean_speed(self) -> float:
        return (self.lenght_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.CALORIES_SWIM_MULTIPLIER_1)
                * self.CALORIES_SWIM_MULTIPLIER_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    sport_dict: Dict[str, Type[Training]] = {'SWM': Swimming,
                                             'RUN': Running,
                                             'WLK': SportsWalking}
    return sport_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""

    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training: Training = read_package(workout_type, data)
        main(training)
