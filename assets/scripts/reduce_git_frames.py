from PIL import Image, ImageSequence

def reduce_and_extend_gif_duration(input_gif_path, output_gif_path, reduction_factor, total_duration_seconds):
    with Image.open(input_gif_path) as img:
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        
        reduced_frames = frames[::reduction_factor]
        
        total_duration_ms = total_duration_seconds * 1000
        new_frame_duration = total_duration_ms // len(reduced_frames)
        
        reduced_frames[0].save(
            output_gif_path,
            save_all=True,
            append_images=reduced_frames[1:],
            loop=0,
            duration=new_frame_duration
        )

input_gif_path = 'assets/gif/clashbots.gif'
output_gif_path = 'assets/gif/clashbots_test.gif'
reduction_factor = 5
total_duration_seconds = 60

reduce_and_extend_gif_duration(input_gif_path, output_gif_path, reduction_factor, total_duration_seconds)
