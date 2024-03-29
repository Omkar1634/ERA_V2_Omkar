import torch.utils.data
from torchvision import datasets, transforms

def load_data():


     # Train data transformations
    train_transforms = transforms.Compose([
        transforms.RandomApply([transforms.CenterCrop(32), ], p=0.1),
        transforms.RandomRotation((-15., 15.), fill=0), # Rotate the image by angle.
        transforms.ToTensor(),# Convert images to PyTorch tensors
        transforms.Normalize((0.49139968, 0.48215827 ,0.44653124), (0.24703233, 0.24348505, 0.26158768)), # Normalize images
        ])

    # Test data transformations
    test_transforms = transforms.Compose([
        transforms.ToTensor(), # Convert images to PyTorch tensors
        transforms.Normalize((0.49139968, 0.48215827 ,0.44653124), (0.24703233, 0.24348505, 0.26158768)) # Normalize images
        ])


    
    kwargs = {'batch_size': 512, 'shuffle': True, 'num_workers': 2, 'pin_memory': True}
    
    train_data = datasets.CIFAR10('../data', train=True, download=True, transform=train_transforms)
    test_data = datasets.CIFAR10('../data', train=False, download=True, transform=test_transforms)

    test_loader = torch.utils.data.DataLoader(test_data, **kwargs)

    train_loader = torch.utils.data.DataLoader(train_data, **kwargs)

    return train_loader,test_loader


def load_data_LN():


    # Train data transformations
    train_transforms = transforms.Compose([
        transforms.Resize((28,28)), # Resize image at (32,32)
        transforms.ToTensor(),# Convert images to PyTorch tensors
        transforms.Normalize((0.1307,), (0.3081,)), # Normalize images
        ])

    # Test data transformations
    test_transforms = transforms.Compose([
        transforms.Resize((28,28)),
        transforms.ToTensor(), # Convert images to PyTorch tensors
        transforms.Normalize((0.1307,), (0.3081,)) # Normalize images
        ])


    
    kwargs = {'batch_size': 64, 'shuffle': True, 'num_workers': 2, 'pin_memory': True}
    
    train_data = datasets.CIFAR10('../data', train=True, download=True, transform=train_transforms)
    test_data = datasets.CIFAR10('../data', train=False, download=True, transform=test_transforms)

    test_loader = torch.utils.data.DataLoader(test_data, **kwargs)

    train_loader = torch.utils.data.DataLoader(train_data, **kwargs)

    return train_loader,test_loader