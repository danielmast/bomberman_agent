from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
from serpent.input_controller import MouseButton
from serpent.sprite_locator import SpriteLocator

class SerpentBombermanGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        if self.get_current_screen(game_frame) == 'SPLASH':
            self.click_through_menu()
        else:
            self.input_controller.tap_key(KeyboardKey.KEY_RIGHT)
            self.input_controller.tap_key(KeyboardKey.KEY_LEFT)

    def get_current_screen(self, game_frame):
        sprite_locator = SpriteLocator()
        play_button = self.game.sprites['SPRITE_SPLASH_SCREEN_PLAY_BUTTON']

        if (sprite_locator.locate(sprite=play_button, game_frame=game_frame) is not None):
            return "SPLASH"
        else:
            return None


    def click_through_menu(self):
        self.game.api.Menu.click_play_button()
        self.game.api.Menu.click_1_player_button()
        self.game.api.Menu.click_1_opponent_button()
        self.game.api.Menu.click_level_1_button()