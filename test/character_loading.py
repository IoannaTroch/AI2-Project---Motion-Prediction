from ai4animation import Actor, AI4Animation, Rotation, Time, Vector3
import os

class Program:
    def Start(self):
        entity = AI4Animation.Scene.AddEntity("Actor")
        model_path = os.path.join("Demos", "Actor", "Biped.txt")
        self.Actor = entity.AddComponent(
            Actor, model_path
        )
        self.Actor.Entity.SetPosition(Vector3.Create(0, 0, 0))

    def Update(self):
        self.Actor.Entity.SetRotation(Rotation.Euler(0, 120 * Time.TotalTime, 0))
        self.Actor.SyncFromScene()


if __name__ == "__main__":
    AI4Animation(Program(), mode=AI4Animation.Mode.STANDALONE)

# from ai4animation import AI4Animation, Vector3, Rotation, Time

# class Program:
#     def Start(self):
#         print("Initializing Scene...")
#         # Create a generic scene entity wrapper without needing an external asset file!
#         self.ActorEntity = AI4Animation.Scene.AddEntity("Generic_Actor_Pivot")
#         self.ActorEntity.SetPosition(Vector3.Create(0, 0, 0))

#     def Update(self):
#         # Rotate our phantom placeholder over time to verify the lifecycle loop works
#         self.ActorEntity.SetRotation(Rotation.Euler(0, 120 * Time.TotalTime, 0))
#         print(f"Actor Position Tracking Active - Rotation Angle: {120 * Time.TotalTime:.2f}°")

#     def Draw(self): pass
#     def GUI(self): pass

# if __name__ == "__main__":
#     # Using HEADLESS mode so it prints output directly into your VS Code terminal window
#     AI4Animation(Program(), mode=AI4Animation.Mode.STANDALONE)