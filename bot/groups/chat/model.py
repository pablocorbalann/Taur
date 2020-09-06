# In this file we store the classes that we need to create connections in the Net()
# class with other modules

#imports
import torch
import torch.nn as nn


class Net(nn.Module):
    """
    The Net() class is used to manage a neural net implemented from 
    pytorch.nn.Module that contains three layers (l1, l2, l3)
    """
    def __init__(self, input_size, hidden_size, out_size):
        """
        The __init__ method of the Net() class (Net().__init__())
        uses three parameters:

            p:input_size => the size of the input in the net 
            p:hidden_size => the size of the hidden size.
            p:out_size => the size of the output size of the net

        To generate three diferent layers (l1, l2, l3) and a ReLU instance
        """
        super(Net, self).__init__()
        # create the three layers
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, out_size)
        # create the relu
        self.relu = nn.ReLU()
    
    def forward(self, x):
        """
        The .forward() method recibes a parameter p:x and uses the
        three layers to evaluate its output using the self.relu attribute.
        Then it returns the output.
        """
        output = self.l1(x)
        output = self.relu(output)
        output = self.l2(output)
        output = self.relu(output)
        output = self.l3(output)
        # no activation and no softmax at the end
        return output