from google_images_download import google_images_download

def download_images(query, limit=1):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": query, "limit": limit, "output_directory": "images", "format": "jpg", "no_directory": True}
    paths = response.download(arguments)
    return paths

# Example usage:
query = "Avatar"
limit = 5  # Number of images to download
downloaded_paths = download_images(query, limit)
print(downloaded_paths)
