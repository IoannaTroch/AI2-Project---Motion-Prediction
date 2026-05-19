import numpy as np
import torch
from ai4animation import MLP, Tensor, Plotting, AI4Animation
from ai4animation.AI.Optimizers.AdamWR.AdamW import AdamW
from ai4animation.AI.Optimizers.AdamWR.CyclicScheduler import CyclicScheduler

class Program:
    def Start(self):
        self.EpochCount = 150
        self.BatchSize = 32
        self.BatchCount = 10
        self.SampleCount = self.BatchSize * self.BatchCount

        self.Network = Tensor.ToDevice(
            MLP.Model(input_dim=1, output_dim=100, hidden_dim=128, dropout=0.1)
        )
        self.Optimizer = AdamW(
            self.Network.parameters(), lr=1e-4, weight_decay=1e-4
        )
        self.Scheduler = CyclicScheduler(
            optimizer=self.Optimizer,
            batch_size=self.BatchSize,
            epoch_size=self.SampleCount,
            restart_period=10,
            t_mult=2,
            policy="cosine",
            verbose=True,
        )
        self.LossHistory = Plotting.LossHistory(
            "Loss History", drawInterval=500, yScale="log"
        )
        self.Trainer = self.Training()

    def Update(self):
        try:
            next(self.Trainer)
        except StopIteration:
            pass

    def Training(self):
        for e in range(1, self.EpochCount + 1):
            print("Epoch", e)
            for _ in range(self.BatchCount):
                x = self.GetInput()
                y = self.GetOutput(x)
                xBatch = Tensor.ToDevice(torch.tensor(x, dtype=torch.float32))
                yBatch = Tensor.ToDevice(torch.tensor(y, dtype=torch.float32))

                losses = self.Network.learn(xBatch, yBatch, e == 1)
                self.Optimizer.zero_grad()
                sum(losses.values()).backward()
                self.Optimizer.step()
                self.Scheduler.batch_step()

                for k, v in losses.items():
                    self.LossHistory.Add((Plotting.ToNumpy(v), k))

                yield

            self.Scheduler.step()
            self.LossHistory.Print()

    def GetInput(self):
        x = np.random.uniform(0, 1, self.BatchSize)
        return x.reshape(self.BatchSize, 1)

    def GetOutput(self, x):
        y = np.linspace(-1, 1, 100)
        y = np.power(y, 2)
        y = y.reshape(1, -1).repeat(self.BatchSize, axis=0)
        return y * x


if __name__ == "__main__":
    AI4Animation(Program(), mode=AI4Animation.Mode.HEADLESS)