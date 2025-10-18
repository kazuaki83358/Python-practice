import argparse
import os
import requests

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully and saved to '{save_path}'")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="Download an image from a URL.")
    parser.add_argument("url", type=str, help="The URL of the image to download.")
    parser.add_argument("save_path", type=str, help="The path where the image will be saved.")

    args = parser.parse_args()

    download_image(args.url, args.save_path)

if __name__ == "__main__":
    main()