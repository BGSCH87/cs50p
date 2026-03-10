def main():

    # prompt  user for input
    filename = input("File name: ").strip().lower()

    # create dict for mapping
    extensions = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # check if user input is in dict
    for extension, media_type in extensions.items():
        if filename.endswith(extension):
            print(media_type)
            return
    # fallback
    print("application/octet-stream")


main()
