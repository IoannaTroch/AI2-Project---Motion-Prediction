from ai4animation import Actor, AI4Animation, Rotation, Time, Vector3
import os, sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ASSETS_PATH = str(SCRIPT_DIR.parent / "Demos/_ASSETS_/Cranberry")

sys.path.append(ASSETS_PATH)
import Definitions

class Program:
    def Start(self):
        entity = AI4Animation.Scene.AddEntity("Actor")
        model_path = os.path.join(ASSETS_PATH, "Model.glb")
        self.Actor = entity.AddComponent(
            Actor, model_path, Definitions.FULL_BODY_NAMES, True
        )
        self.Actor.Entity.SetPosition(Vector3.Create(0, 0, 0))

    def Update(self):
        self.Actor.Entity.SetRotation(Rotation.Euler(0, 120 * Time.TotalTime, 0))
        self.Actor.SyncFromScene()


if __name__ == "__main__":
    AI4Animation(Program(), mode=AI4Animation.Mode.STANDALONE)
