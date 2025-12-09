from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
import os

class dehaze_test_dataset(Dataset):
    def __init__(self, test_dir):
        self.transform = transforms.Compose([transforms.ToTensor()])
        self.list_test=[]
        for line in open(os.path.join(test_dir, 'test.txt')):
            line = line.strip('\n')
            if line!='':
                self.list_test.append(line)
        self.root_hazy = os.path.join(test_dir , 'hazy/')
        self.root_clean = os.path.join(test_dir , 'GT/')
        self.file_len = len(self.list_test)

    def __getitem__(self, index, is_train=True):
        hazy = Image.open(self.root_hazy + self.list_test[index])
        a = self.list_test[index]
        # clean=Image.open(self.root_clean + a.split('_')[0]+os.path.splitext(a)[1])
        clean = Image.open(self.root_clean + a.split('_')[0]+os.path.splitext(a)[1])
        hazy = self.transform(hazy)

        hazy_up=hazy[:,0:640,:]
        hazy_down=hazy[:,560:1200,:]
        clean = self.transform(clean)
        return hazy_up,hazy_down,hazy,clean

    def __len__(self):
        return self.file_len





