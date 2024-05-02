from ursina import *
app = Ursina()
Sky()
camera.orthographic = True
camera.fov = 20

bird = Entity(model='cube', color=color.red, texture='white_cube', y=2
              , scale=(1.2, 1.2, 1.2), collider='box')


def update():
    bird.y -= 4 * time.dt
    for p in pipes:
        p.x -= 2 * time.dt
        if bird.intersects().hit or bird.y < -10:
            quit()


def input(key):
    if key == 'space':
        bird.y = bird.y + 2
    elif key == 'a':
        bird.x -= 3
    elif key == 'd':
        bird.y -= 3
        for p in pipes:
            p.x -= 2 * time.dt
            bird.x -= 3
    elif key == 'd':
        bird.y -= 3
        for p in pipes:
            p.x -= 2 * time.dt


pipes = []
pipe = Entity(model='quad', color=color.green, texture='white_cube', position=(20, 10)
              , scale=(3, 15, 1), collider='box')


def newPipe():
    y = random.randint(4, 12)
    new1 = duplicate(pipe, y=y)
    new2 = duplicate(pipe, y=y - 22)
    pipes.extend((new1, new2))
    invoke(newPipe, delay=5)


newPipe()
app.run()