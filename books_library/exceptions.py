from fastapi import HTTPException, status

RecordNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запись не найден"
)
NotValidBirthday = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не верная дата рождения"
)
NotValidName = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Введены некорректные данные")
BorrowIDNotFound = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Выдача с таким ID отсутствует"
)
BooksAuthorNotFound = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Автор отсутствует"
)
BookNotFound = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Книга отсутствует"
)

BookReturn = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Книга уже возвращена"
)

NotValidID = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Параметр id должен быть больше 0"
)
NotValidBirthday = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Дата рождения должна быть раньше сегодняшнего числа"
)

WrongQuantity = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Нет на складе"
)

WrongeDate = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Неверная дата"
)
ExceptionQuantity = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Количество экземпляров не должно быть меньше 0"
)