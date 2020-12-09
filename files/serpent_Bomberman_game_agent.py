from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
from serpent.sprite_locator import SpriteLocator
import random
from time import sleep

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

        if current_screen != 'GAMEPLAY':
            self.handle_menu(current_screen)
            return

        game_state = self.get_game_state(game_frame)

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

    def get_game_state(self, game_frame):
        player_1_location = self.get_player_1_location(game_frame)
        print('Location player 1: ', player_1_location)

        # todo

        return None

    def get_player_1_location(self, game_frame):
        region = SpriteLocator().locate(sprite=self.game.sprites['SPRITE_PLAYER_1'], game_frame=game_frame)
        x = round((region[1] - 295) / 34.4)
        y = round((region[0] - 220) / 34.4)
        return (x, y)

    def handle_menu(self, current_screen):
        if current_screen == 'SPLASH':
            self.game.api.Menu.click_play_button()
            sleep(0.5)
        elif current_screen == 'PLAYER_MENU':
            self.game.api.Menu.click_1_player_button()
            self.game.api.Menu.click_1_opponent_button()
            self.game.api.Menu.click_level_1_button()
            sleep(0.5)
        elif current_screen == 'END OF ROUND':
            self.game.api.Menu.click_play_now_button()
            sleep(0.5)
        elif current_screen == 'END OF GAME':
            self.game.api.Menu.click_play_again_button()
            sleep(0.5)


    def get_current_screen(self, game_frame):
        if self.is_located(self.game.sprites['SPRITE_GAMEPLAY_WALL'], game_frame):
            return "GAMEPLAY"
        elif self.is_located(self.game.sprites['SPRITE_SPLASH_SCREEN_AVATAR_BELLY'], game_frame):
            return "SPLASH"
        elif self.is_located(self.game.sprites['SPRITE_PLAYER_MENU_1_PLAYER_BUTTON'], game_frame):
            return "PLAYER_MENU"
        elif self.is_located(self.game.sprites['SPRITE_END_OF_ROUND_GAME_LABEL'], game_frame):
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