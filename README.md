# Split Video

This project provides a script to cut sections from a video file based on time intervals specified in a text file. It leverages `ffmpeg` to handle the video processing.

## Features

- Extracts multiple segments from a video file.
- Uses time intervals specified in an external text file.
- Saves each segment as a separate video file.

## Requirements

- Python 3.6+
- ffmpeg

## Installation

### Python Libraries

This script uses standard Python libraries (`subprocess`, `os`, `cmd`). No additional Python libraries are required.

### ffmpeg

#### For Windows:

1. Download ffmpeg from [here](https://ffmpeg.org/download.html).
2. Extract the downloaded ZIP file.
3. Add the `bin` folder from the extracted files to your system's PATH.

#### For Linux:

Use your package manager to install ffmpeg:

```sh
sudo apt-get install ffmpeg
```

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/video-cutter.git
    cd video-cutter
    ```

2. Prepare the `cuts.txt` file:
    - Create a file named `cuts.txt` in the same directory as your script.
    - Each line in `cuts.txt` should follow the format: `output_filename start_time end_time`
    - Example:
        ```
        clip1.mp4 00:00:00 00:01:00
        clip2.mp4 00:02:00 00:03:00
        ```

3. Run the script:

    ```sh
    python video_cutter.py
    ```

4. Follow the prompt to enter the path to your video file.

### Example

Here’s an example of running the script:

```sh
Enter Your Video Path: Q:\Web\VIDEO\input.mp4
```

The script will read the time intervals from `cuts.txt`, extract the specified segments from `input.mp4`, and save them in the same directory as the original video file.

## Script Details

### Input and Output

- **Input**: The script prompts the user to input the path to the video file.
- **Output**: The extracted video segments are saved with the filenames specified in `cuts.txt`.

### Main Function

- Reads the video path from the user.
- Reads the time intervals and output filenames from `cuts.txt`.
- Uses `ffmpeg` to extract the specified segments from the video file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [ffmpeg](https://ffmpeg.org/)

---

Feel free to customize this README to better suit your project's details and needs!

## Script Code

Here is the code for the script for reference:

```python
import cmd
import subprocess, os

VideoPath = input("\n\n\tEnter Your Video Path:\t")
folder = os.path.basename(VideoPath)
folder = folder.replace('.mp4', '')
VideoPath = VideoPath.replace('"', '')

with open("cuts.txt") as f:
    for line in f.readlines():
        filename, start, end = line.strip().split(' ')
        cmd = ["ffmpeg", "-i", VideoPath, "-ss", start, "-to", end, "-c", "copy", f"{folder}\\{filename}"]
        subprocess.run(cmd, stderr=subprocess.STDOUT)
```