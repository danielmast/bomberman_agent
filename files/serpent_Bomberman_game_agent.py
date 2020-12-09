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
        print("Start agent")

        # if self.frame_counter % 2 == 0:
        #     self.input_controller.tap_key(KeyboardKey.KEY_RIGHT)
        # else :
        #     self.input_controller.tap_key(KeyboardKey.KEY_LEFT)
        # self.frame_counter += 1

        self.click_through_menu(game_frame)


    def click_through_menu(self, game_frame):
        print('Locating SCREEN1_PLAY_BUTTON')
        sprite_locator = SpriteLocator()
        sprite = self.game.sprites['SPRITE_SCREEN1_PLAY_BUTTON']
        print(sprite)
        location = sprite_locator.locate(sprite=sprite, game_frame=game_frame)
        print(location)

        self.input_controller.click_screen_region(screen_region='SCREEN1_PLAY_BUTTON')