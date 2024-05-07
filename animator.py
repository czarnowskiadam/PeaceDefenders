from imports import *

def animate_sprites(sprite, frame_w, frame_h, rows, cols, ):
    rows = 1
    cols = 8
    total_frames = rows * cols

    frame_index = 0
    frame_countdown = 5

    frames = []
    for i in range(rows):
        for j in range(cols):
            frame = sprite.subsurface(pygame.Rect(j * frame_w, i * frame_w, frame_w, frame_h))
            frames.append(frame)

    return frames, total_frames, frame_index, frame_countdown

def update_sprites(screen, frames, total_frames, frame_index, frame_countdown):
    screen.blit(frames[frame_index], (450, 550))
    frame_countdown -= 1
    if frame_countdown == 0:
        frame_index = (frame_index + 1) % total_frames
        frame_countdown = 5

    return frame_index, frame_countdown
