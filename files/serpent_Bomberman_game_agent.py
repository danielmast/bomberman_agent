from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
from serpent.input_controller import MouseButton
from serpent.sprite_locator import SpriteLocator
import random

class SerpentBombermanGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        current_screen = self.get_current_screen(game_frame)
        print ('current_screen = ', current_screen)
        if current_screen == 'SPLASH':
            self.game.api.Menu.click_play_button()
        elif current_screen == 'PLAYER_MENU':
            self.game.api.Menu.click_1_player_button()
            self.game.api.Menu.click_1_opponent_button()
            self.game.api.Menu.click_level_1_button()
        elif current_screen == 'END OF ROUND':
            self.game.api.Menu.click_play_now_button()
        elif current_screen == 'END OF GAME':
            self.game.api.Menu.click_play_again_button()
        else:
            action = random.randint(0, 5)
            if action == 0:
                self.input_controller.tap_key(KeyboardKey.KEY_LEFT)
            elif action == 1:
                self.input_controller.tap_key(KeyboardKey.KEY_RIGHT)
            elif action == 2:
                self.input_controller.tap_key(KeyboardKey.KEY_UP)
            elif action == 3:
                self.input_controller.tap_key(KeyboardKey.KEY_DOWN)
            elif action == 4:
                self.input_controller.tap_key(KeyboardKey.KEY_SPACE)


    def get_current_screen(self, game_frame):
        if self.is_located(self.game.sprites['SPRITE_SPLASH_SCREEN_PLAY_BUTTON'], game_frame):
            return "SPLASH"
        elif self.is_located(self.game.sprites['SPRITE_PLAYER_MENU_1_PLAYER_BUTTON'], game_frame):
            return "PLAYER_MENU"
        elif self.is_located(self.game.sprites['SPRITE_END_OF_ROUND_PLAY_NOW_BUTTON'], game_frame):
            return "END OF ROUND"
        elif self.is_located(self.game.sprites['SPRITE_END_OF_GAME_PLAY_AGAIN_BUTTON'], game_frame):
            return "END OF GAME"
        else:
            return None

    def is_located(self, sprite, game_frame):
        return SpriteLocator().locate(sprite=sprite, game_frame=game_frame) is not None

    def click_through_menu(self):
        self.game.api.Menu.click_play_button()
        self.game.api.Menu.click_1_player_button()
        self.game.api.Menu.click_1_opponent_button()
        self.game.api.Menu.click_level_1_button()