from PIL import Image
import os
import math

def resize_image(image, target_height):
    """
    根据目标高度调整图像大小，保持 4:3 的比例
    :param image: 输入图像
    :param target_height: 目标高度
    :return: 调整后的图像
    """
    # 计算目标宽度，保持 4:3 比例
    target_width = int(target_height * 4 / 3)
    resized_image = image.resize((target_width, target_height), Image.LANCZOS)
    return resized_image

def get_target_height(original_height):
    """
    计算向上取整到16的倍数且能被3整除的目标高度
    :param original_height: 原始高度
    :return: 计算后的目标高度
    """
    # 先向上取整到16的倍数
    
    number = math.ceil(original_height / 16)
    height = number * 16

    if original_height > 480:
        return math.floor(original_height / 480) * 480
    while height < 480: # 假设最大宽度是480 
        # 确保能被3整除
        if height % 3 != 0:
            number += 1
            height = number * 16
        else:
            return height
    if height == 480:
        return height
def process_images(input_directory):
    # 创建输出文件夹
    output_directory = os.path.join(input_directory, 'resized')
    os.makedirs(output_directory, exist_ok=True)

    # 遍历输入目录下的所有图像文件
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_directory, filename)
            with Image.open(image_path) as img:
                # 获取原图的高度
                original_height = img.size[1]
                
                # 计算目标高度
                target_height = get_target_height(original_height)
                
                # 调整图像大小
                resized_image = resize_image(img, target_height)
                
                # 保存调整后的图像
                output_path = os.path.join(output_directory, filename)
                resized_image.save(output_path)
                print(f"已保存调整后的图像: {output_path}")

if __name__ == "__main__":
    input_directory = './nature_image'  # 替换为你的输入文件夹路径
    process_images(input_directory)