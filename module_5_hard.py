import time


class User: # создаются пользователи
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def hash(self):
        return self.password

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'Пользователь: {self.nickname} {self.password}'


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    # def __repr__(self):
    #     return f'{self.title}, {self.duration}, {self.adult_mode}'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print(f'Неверный логин или пароль')

    def register(self, nickname, password, age):
        for uu in self.users:
            if uu.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.current_user = new_user
        self.users.append(new_user)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for film in videos:
            if not any(vd.title == film.title for vd in self.videos):
                self.videos.append(film)

    def get_videos(self, search_word):
        search_word_low = search_word.lower()
        return [video.title for video in self.videos if search_word_low in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = next((vid for vid in self.videos if vid.title == title), None)
        if not video:
            print('Такого видео нет!')
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, покиньте страницу!")
            return
        for seconds in range(video.time_now, video.duration):
            time.sleep(1)
        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



