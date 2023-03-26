Sure, here is the README.md file:

# MP3 to WAV Converter

This is a Python application that converts MP3 files to WAV format using the Pydub library.

## Files

- `convert.py`: Contains the `mp3_to_wav` function that converts an MP3 file to WAV format.
- `main.py`: Contains the main function that prompts the user for the input and output file paths and calls the `mp3_to_wav` function to perform the conversion.
- `Dockerfile`: Contains the instructions to build a Docker image for the application.

## Installation

1. Clone the repository:

```
git clone https://github.com/username/mp3-to-wav-converter.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the application:

```
python main.py
```

2. Enter the path of the MP3 file and the output WAV file when prompted.

## Docker

1. Build the Docker image:

```
docker build -t mp3-to-wav-converter .
```

2. Run the Docker container:

```
docker run -it --rm -v /path/to/mp3/files:/app mp3-to-wav-converter
```

Replace `/path/to/mp3/files` with the path to the directory containing the MP3 files you want to convert.

## Credits

- Pydub library: https://github.com/jiaaro/pydub

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.