import torch
import torch.nn as nn
import torch.nn.functional as F

class co_train_classifier(nn.Module):
    def __init__(self):
        super(co_train_classifier, self).__init__()
        self.c1 = nn.Conv2d(3, 128, kernel_size=3, padding=1)
        self.b1 = nn.BatchNorm2d(128)
        self.r1 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.c2 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.b2 = nn.BatchNorm2d(128)
        self.r2 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.c3 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.b3 = nn.BatchNorm2d(128)
        self.r3 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.m1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.d1 = nn.Dropout2d(p=0.5)

        self.c4 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.b4 = nn.BatchNorm2d(256)
        self.r4 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.c5 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.b5 = nn.BatchNorm2d(256)
        self.r5 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.c6 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.b6 = nn.BatchNorm2d(256)
        self.r6 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.m2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.d2 = nn.Dropout2d(p=0.5)

        self.c7 = nn.Conv2d(256, 512, kernel_size=3, padding=1)
        self.b7 = nn.BatchNorm2d(512)
        self.r7 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.c8 = nn.Conv2d(512, 256, kernel_size=3, padding=1)
        self.b8 = nn.BatchNorm2d(256)
        self.r8 = nn.LeakyReLU(negative_slope=0.1, inplace=False)
        self.c9 = nn.Conv2d(256, 128, kernel_size=3, padding=1)
        self.b9 = nn.BatchNorm2d(128)
        self.r9 = nn.LeakyReLU(negative_slope=0.1, inplace=False)

        self.fc = nn.Linear(128, 10)
        self.sf = nn.Softmax(dim = 1)

    def forward(self, x):
        x = self.c1(x)
        x = self.b1(x)
        x = self.r1(x)
        x = self.c2(x)
        x = self.b2(x)
        x = self.r2(x)
        x = self.c3(x)
        x = self.b3(x)
        x = self.r3(x)
        x = self.m1(x)
        x = self.d1(x)


        x = self.c4(x)
        x = self.b4(x)
        x = self.r4(x)
        x = self.c5(x)
        x = self.b5(x)
        x = self.r5(x)
        x = self.c6(x)
        x = self.b6(x)
        x = self.r6(x)
        x = self.m2(x)
        x = self.d2(x)

        x = self.c7(x)
        x = self.b7(x)
        x = self.r7(x)
        x = self.c8(x)
        x = self.b8(x)
        x = self.r8(x)
        x = self.c9(x)
        x = self.b9(x)
        x = self.r9(x)
        x = torch.mean(torch.mean(x, dim=3), dim=2)
        x_logit = self.fc(x)
        return x_logit