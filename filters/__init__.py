from create_bot import dp
from .private_chat import IsPrivate

# from .is_admin import AdminFilter

dp.filters_factory.bind(IsPrivate)
if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)