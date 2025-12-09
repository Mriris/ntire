import os

def rename_images_in_order(directory):
    # 获取目录下所有图像文件
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    # 按文件名排序
    image_files.sort()

    # 重命名文件
    for index, filename in enumerate(image_files):
        # 生成新的文件名，使用三位数字格式
        new_filename = f"{index + 1:03d}.jpg"  # 这里将文件扩展名设置为 .jpg，可以根据需要调整
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} to {new_file_path}")

# 使用示例
directory_path = './nature_image'  # 替换为你的文件夹路径
rename_images_in_order(directory_path)