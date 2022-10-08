file = input("Insert file name: ").lower().strip()

# the last element of the split
extension = file.split(".")[-1]

match extension:
    case "gif" | "png":
        print(f"image/{extension}")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
