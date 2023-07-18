from types import SimpleNamespace
from src.utils.keyboard import create_keyboard
import emoji


keys = SimpleNamespace(
    random_connect=emoji.emojize(':handshake: Random Connect'),
    settings=emoji.emojize(':gear: Settings'),
    exit=emoji.emojize(':cross_mark: Exit'),
)

keyboards = SimpleNamespace(
    exit=create_keyboard(keys.exit),
    main=create_keyboard(keys.random_connect, keys.settings),
)

states = SimpleNamespace(
    random_connect='RANDOM_CONNECT',
    main='MAIN',
    connected='CONNECTED',
)