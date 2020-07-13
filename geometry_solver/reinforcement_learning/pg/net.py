import torch
import torch.nn as nn


class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 16),
            nn.ReLU(),
            nn.Linear(16, 2),
            nn.Softmax(dim=0)
        ).double()

    def forward(self, x):
        if not torch.is_tensor(x):
            x = torch.tensor(x)
        x = self.net(x)
        return x

