import pyglet
from game import resources, physicalobject, player

# Set up a window
height, width = 1366, 768
game_window = pyglet.window.Window(height, width, caption="The Devil's Lettuce",
                                    resizable=True)
main_batch = pyglet.graphics.Batch()
background = pyglet.resource.image("background.bmp")

# Generate player sprite
player_img = player.Player(x=400, y=220, batch=main_batch)
game_window.push_handlers(player_img)
game_objects = [player_img]

# Time update function
def update(dt):
    for obj in game_objects:
        obj.update(dt)

# On window draw
@game_window.event
def on_draw():
    game_window.clear()
    background.blit(0,0)
    main_batch.draw()

def on_key_press():
    None
def on_mouse_press():
    None

# Run it
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
