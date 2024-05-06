from PIL import Image, ImageSequence

def extend_last_frame_duration(input_gif_path, output_gif_path, last_frame_duration_seconds):
    with Image.open(input_gif_path) as img:
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        
        durations = [frame.info['duration'] for frame in frames[:-1]]
        
        last_frame_duration_ms = last_frame_duration_seconds * 1000
        durations.append(last_frame_duration_ms)
        
        first_frame = frames[0]
        additional_frames = frames[1:]
        
        first_frame.save(
            output_gif_path,
            save_all=True,
            append_images=additional_frames,
            loop=0,
            duration=durations
        )

input_gif_path = 'assets/gif/rdkdc_imagedrawing.gif'
output_gif_path = 'assets/gif/rdkdc_imagedrawing.gif'
last_frame_duration_seconds = 1

extend_last_frame_duration(input_gif_path, output_gif_path, last_frame_duration_seconds)
