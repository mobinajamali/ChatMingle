from types import SimpleNamespace
from src.utils.keyboard import create_keyboard
import emoji

# building keys and keyboards
keys = SimpleNamespace(settings=emoji.emojize(':gear: Settings'), exit=emoji.emojize(':cross_mark: Exit'))

keyboards = SimpleNamespace(main=create_keyboard(keys.settings, keys.exit))