class InfoMessage:
    """Информационное сообщение о тренировке."""
    
    def show_training_info(Training):
        def __init__(self,
                     traibibg_tupe,
                     duration,
                     distance,
                     speed,
                     calories,
                     )


class Training:
    """Базовый класс тренировки."""

    M_IN_KM = 1000
    MIN_IN_HOUR = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        if Training == 'SWM':
            LEN_STEP = 1.38
        else:
            LEN_STEP = 0.65

        return self.action * LEN_STEP / self.M_IN_KM
        

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration
    

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage


class Running(Training):
    """Тренировка: бег."""
    
    coef_calories_1: float = 18
    coef_calories_2: float = 20

    def __init__(self, 
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        
        return self.weight * (self.coef_calories_1 * self.get_mean_speed() - self.coef_calories_2) / self.M_IN_KM * (self.duration * self.MIN_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coef_calories_1: float = 0.035
    coef_calories_2: float = 0.029

    def __init__(self, 
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return self.weight (self.coef_calories_1 + (self.get_mean_speed()**2 // self.height) * self.coef_calories_2 ) * (self.duration * self.MIN_IN_HOUR) 


class Swimming(Training):
    """Тренировка: плавание."""

    coef_calories_1: float = 1.1
    coef_calories_2: float = 2

    def __init__(self,action: int,
                 duration: float,
                 weight: float,
                 length_pool: int, 
                 count_pool: int, 
                ) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = length_pool #длинна бассейна в метрах
        self.count_pool = count_pool #сколько раз пользователь проплыл бассейн  

    def get_mean_speed(self) -> float:
        return self.lenght_pool * self.count_pool / self.M_IN_KM / self.duration 
    
    def get_spent_calories(self) -> float:
        return (self.get_mean_speed + self.coef_calories_1) * self.coef_calories_2 * self.weight 


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

