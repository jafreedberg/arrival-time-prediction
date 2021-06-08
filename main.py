import sys
import os

import torch
from torch.utils.data import DataLoader
from torch import optim
from FeatureDataSet import FeatureDataSet
from tqdm import tqdm

from full_connnected_model import Net


def do_train(path,model_name):
    if not os.path.exists(path):
        os.mkdir(path)
    batch_size = 100
    learning_rate = 0.1
    epochs = 3000
    train_dataSet = FeatureDataSet()
    if torch.cuda.is_available():  
        dev = "cuda:0" 
    else:  
        dev = "cpu"  
    device = torch.device(dev) 
    

    train_size = int(0.7 * len(train_dataSet))
    test_size = len(train_dataSet) - train_size
    train_dataSet, val_db = torch.utils.data.random_split(train_dataSet, [train_size, test_size])
    print('train:', len(train_dataSet), 'validation:', len(val_db))

    train_data_loader = DataLoader(train_dataSet,
                                   batch_size=batch_size,
                                   shuffle=False,
                                   num_workers=2,
                                   drop_last=False)

    net = Net()

    criteon = torch.nn.MSELoss()
    optimizer = optim.Adam(net.parameters(), lr=learning_rate)

    best = 500000
    num_bad_epochs = 0
    for epoch in range(epochs):

        print("-----------------------------------------------------------------")
        print("Epoch: {}; Bad epochs: {}".format(epoch, num_bad_epochs))
        net.train()
        running_loss = 0
        for i, (X_batch,Y_batch) in enumerate(tqdm(train_data_loader), 0):
            # zero the parameter gradients
            optimizer.zero_grad()
            pred = net(X_batch)
            # print(X_batch)
            # print(type(X_batch))
            # print(X_batch.shape)
            loss = criteon(pred, Y_batch)
            loss.backward()
            optimizer.step()
            running_loss = loss.item()
            print(running_loss)

        print("Loss: {}".format(running_loss))
        # early stopping
        if running_loss < best:
            print("############### Saving good model ###############################")
            final_model = net.state_dict()
            best = running_loss
            torch.save(final_model, './'+path+'/'+model_name+'.pth')
            print(best)
            num_bad_epochs = 0
        else:
            num_bad_epochs = num_bad_epochs + 1


    print("Done")
    # Restore best model
    parameters = net.parameters()
    torch.save(final_model, './'+path+'/'+model_name+'.pth')
    print("best:" + str(best))


if __name__ == '__main__':
    path = "mode"
    model_name = "test"
    do_train(path,model_name)
