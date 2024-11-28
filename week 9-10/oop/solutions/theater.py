class Movie:
    def __init__(self, title: str, duration: int) -> None:
        self._title = title
        self._duration = duration

    def get_title(self) -> str:
        return self._title

    def get_duration(self) -> int:
        return self._duration

    # dunder (double under) method
    def __str__(self) -> str:  # текстовое описание класса
        return f"Фильм: {self.get_title()}"


class Ticket:  # Билет
    def __init__(self, movie: Movie, seat_number: int):
        self._movie = movie
        self._seat_number = seat_number

    def __str__(self) -> str:
        return f"Билет на фильм {self._movie.get_title()}, место {self._seat_number}"


class Theater:
    def __init__(self, name, movies: list = [], seats: list = []) -> None:
        self._name = name
        self._movies = movies
        self._seats = seats

    def add_movie(self, movie) -> None:
        self._movies.append(movie)

    def show_movies(self) -> None:
        for num, movie in enumerate(self._movies, start=1):
            print(f"{num}: {movie}")

    def book_seat(self, movie: Movie, seat_number: int) -> Ticket | str:
        if movie not in self._movies:
            return "Данный фильм не показывается в кинотеатре"

        if seat_number in self._seats:
            return "Место занято"

        return Ticket(
            movie=movie,
            seat_number=seat_number,
        )


theater = Theater("Кинотеатр 'Алем'")

titanik = Movie(title="Титаник", duration=150)
startrek = Movie(title="Стартрек", duration=120)

theater.add_movie(titanik)
theater.add_movie(startrek)
theater.show_movies()


startrek_ticket = theater.book_seat(startrek, 1)
print(startrek_ticket)

titanik_ticket = theater.book_seat(titanik, 1)
print(titanik_ticket)
