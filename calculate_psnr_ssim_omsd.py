import os
import cv2
from metrics import calculate_psnr, calculate_ssim
import PIL
# Sample script to calculate PSNR and SSIM metrics from saved images in two directories
# using calculate_psnr and calculate_ssim functions from: https://github.com/JingyunLiang/SwinIR

gt_path = '../data/OMSD/test/GT'
# results_path = '/data/stu/lijunjie/WeatherDiffusion/results/images/AllWeather/Haze1k/fft-diffusion-640000/'
results_path = './results/omsd'
# results_path = '/data/gh/ljj/WeatherDiffusion/results/images/Rurs/rurs/rurs_415000'
# results_path = '/data/gh/ljj/WeatherDiffusion/results/images/AllWeather/rshaze/rshaze_700000'
# results_path = '/data/stu/lijunjie/WeatherDiffusion/results/images/AllWeather/Haze1k/64-data-fft-diffusion-795000/'
# results_path = '/data/stu/lijunjie/code/ours_WeatherDiffusion/results/images/AllWeather/Haze1k_ch128-11234/'

imgsName = sorted(os.listdir(results_path))
gtsName = sorted(os.listdir(gt_path))
# assert len(imgsName) == len(gtsName)

cumulative_psnr, cumulative_ssim = 0, 0
name_recode = []
de_number = 0
none_image = 0
for i in imgsName:
    # gt_name = i[2:-13] + '.'
    gt_name = i.split('_')[0] + '.'
    gt_name += 'png' if os.path.exists(os.path.join(gt_path, gt_name + 'png')) else 'jpg'
    # print('Processing image: %s' % (i))
    if os.path.exists(os.path.join(gt_path, gt_name)):
        res = cv2.imread(os.path.join(results_path, i), cv2.IMREAD_COLOR)
        gt = cv2.imread(os.path.join(gt_path, gt_name), cv2.IMREAD_COLOR)
        cur_psnr = calculate_psnr(res, gt, test_y_channel=True)
        cur_ssim = calculate_ssim(res, gt, test_y_channel=True)
        recode = 'image %s, PSNR is %.4f and SSIM is %.4f' % (i, cur_psnr, cur_ssim)
        print(recode)
        if cur_psnr < 0:
            name_recode.append(recode)
            de_number += 1
        else:
            cumulative_psnr += cur_psnr
            cumulative_ssim += cur_ssim
    else:
        none_image += 1
print(none_image)
print('Total %s Testing set, %s less than 25, else %s images, PSNR is %.4f and SSIM is %.4f' % (len(imgsName), str(de_number), str(len(imgsName)-de_number-none_image), cumulative_psnr / (len(imgsName)-de_number-none_image), cumulative_ssim / (len(imgsName)-de_number-none_image)))
print(results_path)
print('\n'.join(name_recode))
print("len:", len(name_recode))
print('%.4f' % (cumulative_psnr / (len(imgsName)-de_number-none_image)))
