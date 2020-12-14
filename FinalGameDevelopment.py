Game Development Final Project Julie Kiehne Lamkin
# Why should gems and coins wait while you are collecting them?

# First, spawn the top, bottom, and sides forest borders.
game.spawnXY("forest", -4, 64)
game.spawnXY("forest", 4, 64)
game.spawnXY("forest", 12, 64)
game.spawnXY("forest", 20, 64)
game.spawnXY("forest", 28, 64)
game.spawnXY("forest", 36, 64)
game.spawnXY("forest", 44, 64)
game.spawnXY("forest", 52, 64)
game.spawnXY("forest", 60, 64)
game.spawnXY("forest", 68, 64)
game.spawnXY("forest", 76, 64)
game.spawnXY("forest", -4, 4)
game.spawnXY("forest", 4, 4)
game.spawnXY("forest", 12, 4)
game.spawnXY("forest", 20, 4)
game.spawnXY("forest", 28, 4)
game.spawnXY("forest", 36, 4)
game.spawnXY("forest", 44, 4)
game.spawnXY("forest", 52, 4)
game.spawnXY("forest", 60, 4)
game.spawnXY("forest", 68, 4)
game.spawnXY("forest", 76, 4)
game.spawnXY("forest", 4, 10)
game.spawnXY("forest", 4, 18)
game.spawnXY("forest", 4, 26)
game.spawnXY("forest", 4, 34)
game.spawnXY("forest", 4, 42)
game.spawnXY("forest", 4, 50)
game.spawnXY("forest", 4, 58)
game.spawnXY("forest", 4, 64)
game.spawnXY("forest", 71, 8)
game.spawnXY("forest", 71, 16)
game.spawnXY("forest", 71, 24)
game.spawnXY("forest", 71, 32)
game.spawnXY("forest", 71, 40)
game.spawnXY("forest", 71, 48)
game.spawnXY("forest", 71, 56)
game.spawnXY("forest", 71, 64)

# This spawns a gem at a random point with random directions
def spawnRandomGem():
    x = game.randomInteger(10, 70)
    y = game.randomInteger(10, 58)
    gem = game.spawnXY("gem", x, y)
    # This defines the direction along the X axis. 1 means move to the right. -1 means move to the left. Zero means don't move horizontally.
    gem.dirX = game.randomInteger(-1, 1)
    # This defines the direction along the Y axis. 1 means move up, -1 means move down. Zero means don't move vertically.
    gem.dirY = game.randomInteger(-1, 1)
    gem.scale = 1.5

# Spawn as many gems as you want.
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()
spawnRandomGem()

gemSpeed = 0.6

# This handler moves gems.
def onUpdate(event):
    item = event.target
    # There are two parts of moving: X and Y.
    diffX = item.dirX * gemSpeed
    diffY = item.dirY * gemSpeed
    # Increase item.pos.x by diffX:
    item.pos.x += diffX
    # Increase item.pos.y by diffY:
    item.pos.y += diffY
    # If the item is out of boundd by the X coordinate.
    if item.pos.x > 70 or item.pos.x < 10:
        # Then we change X direction for the item.
        item.dirX *= -1
    # If item.pos.y greater than 58 or less than 10:
    if item.pos.y > 58 or item.pos.y < 10:
        # Multiply item.dirY by -1:
        item.dirY *= -1
        
# This spawns a coin at a random point with random directions
def spawnRandomCoin():
    x = game.randomInteger(12, 72)
    y = game.randomInteger(12, 56)
    gem = game.spawnXY("coin", x, y)
    # This defines the direction along the X axis. 1 means move to the right. -1 means move to the left. Zero means don't move horizontally.
    gem.dirX = game.randomInteger(-1, 1)
    # This defines the direction along the Y axis. 1 means move up, -1 means move down. Zero means don't move vertically.
    coin.dirY = game.randomInteger(-1, 1)
    coin.scale = 1.5

# Spawn as many gems as you want.
spawnRandomCoin()
spawnRandomCoin()
spawnRandomCoin()
spawnRandomCoin()

coinSpeed = 0.2


game.setActionFor("coin" and "gem", "update", onUpdate)

player = game.spawnPlayerXY("captain", 40, 34)
player.maxSpeed = 20
game.addCollectGoal()
ui.track(game, "time")
