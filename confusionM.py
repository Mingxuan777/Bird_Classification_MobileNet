import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import numpy as np
import torchvision.models as model
import torch
from torch.utils.data import DataLoader
from main import setups
import load_data

args = setups()

# Function to plot the confusion matrix:
def plot_confusion_matrix(gt, pred, classes=0, normalize=False, title='Confusion Matrix', cmap=plt.cm.Blues):

    cm = metrics.confusion_matrix(gt, pred)
    np.set_printoptions(precision=2)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))

    plt.xticks(tick_marks, fontsize=3)
    plt.yticks(tick_marks, fontsize=3)

    plt.grid(True)

    plt.ylabel('Ground Truth')
    plt.xlabel('Predictions')
    plt.tight_layout()
    plt.savefig(f"cm.pdf", bbox_inches='tight')
    plt.show()
    plt.close()
