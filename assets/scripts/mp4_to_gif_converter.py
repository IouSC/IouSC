import imageio

def mp4_to_gif(input_path, output_path, fps=10):
    """
    Convert an MP4 video to a GIF with specified frames per second.

    Parameters:
    - input_path: Path to the input MP4 file.
    - output_path: Path for the output GIF file.
    - fps: Frames per second for the output GIF.
    """
    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames[:, :, :])
    writer.close()

input_mp4 = 'assets/raw/clashbots.mp4'  # Path to MP4 file
output_gif = 'assets/gif/clashbots.gif'  # Path to output GIF file
mp4_to_gif(input_mp4, output_gif)
