import torch as T
from torch import nn
from torch.nn import functional as F


class Net_FlappyBird(nn.Module):
    """Red neuronal utilizada para tomar decisiones en Flappy Bird."""

    def __init__(self, input_size=5):
        super(Net_FlappyBird, self).__init__()

        # Arquitectura de la red
        self.l1 = nn.Linear(input_size, 32)
        self.l2 = nn.Linear(32, 1)

        # Inicialización de pesos para mejorar la estabilidad del entrenamiento
        nn.init.xavier_uniform_(self.l1.weight)
        nn.init.xavier_uniform_(self.l2.weight)

        # Dispositivo: usa GPU si está disponible, de lo contrario CPU
        self.device = T.device("cuda" if T.cuda.is_available() else "cpu")
        self.to(self.device)

    def forward(self, x):
        """Propagación hacia adelante."""
        x = x.to(self.device)
        x = F.relu(self.l1(x))
        return T.sigmoid(self.l2(x))

    def save_model(self, path):
        """Guarda el modelo en la carpeta 'models'."""
        T.save(self.state_dict(), f'models/{path}.pkl')

    def load_model(self, path):
        """Carga un modelo desde un archivo."""
        self.load_state_dict(T.load(path, map_location=self.device))
