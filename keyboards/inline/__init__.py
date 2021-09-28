from . import callback_datas
from . import inline_main_menu
from . import result_menu
from . import subscriptions_menu
from . import subs_team

# TODO: Разобраться в первую очередь
    # ImportError: 
    # cannot import name 'get_items_kb' from partially initialized module 'keyboards.inline' 
    # (most likely due to a circular import) (C:\code\py\svarog2022_Tbot\tbot\keyboards\inline\__init__.py)
    # https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python
# from . import get_items_kb 