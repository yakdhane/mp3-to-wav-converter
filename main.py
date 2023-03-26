
import os
from convert import mp3_to_wav

def main():
    input_file = input("Enter the path of the mp3 file: ")
    output_file = input("Enter the path of the output wav file: ")
    mp3_to_wav(input_file, output_file)
    print("Conversion completed successfully!")

if __name__ == "__main__":
    main()
