import os

IMAGE_EXTENSION = ".jpg"
TEXT_EXTENSION = ".txt"

if __name__ == "__main__":
    current_path = os.getcwd()
    file_list = list(filter(lambda k: "untagged_img_cleaner" not in k and "classes" not in k, os.listdir(current_path)))
    image_list = list(filter(lambda k: IMAGE_EXTENSION in k, file_list))
    text_list = list(filter(lambda k: TEXT_EXTENSION in k, file_list))

    print("TOTAL FILE COUNT (without classes.txt and the exe itself): " + str(len(file_list)))
    print("IMAGE FILE COUNT: " + str(len(image_list)))
    print("TEXT FILE COUNT (without classes.txt): " + str(len(text_list)))

    for img in image_list:
        image_file_name = img.split(IMAGE_EXTENSION)[0]
        text_file = image_file_name + TEXT_EXTENSION
        if text_file not in text_list:
            print(f"{img} does not have a tag so it is deleted")
            os.remove(img)
