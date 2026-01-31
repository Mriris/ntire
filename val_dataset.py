from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
import os

class dehaze_val_dataset(Dataset):
    def __init__(self, test_dir, img_size=(480, 640)):
        self.img_size = img_size  # (H, W)
        self.transform = transforms.Compose([
            transforms.Resize(img_size),
            transforms.ToTensor()
        ])
        self.list_test = os.listdir(test_dir)
        self.list_test.sort()
        self.root_hazy = test_dir
        self.file_len = len(self.list_test)
        # print(self.list_test)

    def __getitem__(self, index, is_train=True):
        hazy = Image.open(self.root_hazy +'/'+ self.list_test[index]).convert('RGB')
        orig_size = (hazy.height, hazy.width)  # (H, W)
        hazy = self.transform(hazy)

        return (hazy, self.list_test[index], orig_size)

    def __len__(self):
        return self.file_len

