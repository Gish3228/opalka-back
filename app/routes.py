from flask import Blueprint

from .views import NumbersListView  #, NumberView


pig_bp = Blueprint('pig_bp', __name__)
pig_bp.add_url_rule('/numbers_list', view_func=NumbersListView.as_view('numbers_list_view'))
# pig_bp.add_url_rule('/number', view_func=NumberView.as_view('number_view'))
