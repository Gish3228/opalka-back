from flask.views import MethodView
from flask import request

from .models import Numbers, db
from config import MiscParams


class NumbersListView(MethodView):
    """
    Работа со списком чисел
    """

    @staticmethod
    def get():
        """
        Получить список чисел и цветов
        :returns: Список чисел в заданном количестве и офсетом
        """
        limit = request.values.get('limit')
        query = db.session.query(Numbers.id, Numbers.font_color, Numbers.background_color,
                                 Numbers.author, Numbers.message). \
            order_by(Numbers.id)
        if limit:
            limit = int(limit)
            offset = (int(request.values.get('page', MiscParams.default_page)) - 1) * limit
            query = query.limit(limit).offset(offset)
        result = [dict(item) for item in query.all()]
        return result

    @staticmethod
    def post():
        """
        Добавить новую запись (цвета, автор, сообщение)
        :returns: json с выданным числом
        """
        author = request.json['author']
        message = request.json.get('message')
        font_color = request.json.get('font_color')
        background_color = request.json.get('background_color')
        new_number = Numbers(author=author, message=message, font_color=font_color, background_color=background_color)
        db.session.add(new_number)
        db.session.commit()
        return {'id': new_number.id}


# class NumberView(MethodView):
#     """
#     Работа с конкретным числом
#     """
#
#     @staticmethod
#     def get():
#         """
#         Получить данные по числу
#         :returns: Данные по числу
#         """
#         pass
