# program template based on AI4AnimationPy's documentation
from ai4animation import AI4Animation
from ai4animation import Time # provides frame timing globals

class Program:
    def Start(self):
        # Called once at initialization
        # Create entities, load models, set up data
        pass

    def Standalone(self):
        # Called once after Start (standalone only)
        # Configure camera, create GUI elements
        pass

    def Update(self):
        # Called every frame
        # Game logic, animation, input handling
        # speed = 2.0
        # distance = speed * Time.DeltaTime  # Frame-rate independent movement
        # angle = 120 * Time.TotalTime       # Continuous rotation
        pass

    def Draw(self):
        # Called every frame (standalone only, inside render pass)
        # Debug visualization, shape drawing
        pass

    def GUI(self):
        # Called every frame (standalone only, after render)
        # UI overlays, handles, text
        pass


if __name__ == "__main__":
    AI4Animation(Program(), mode=AI4Animation.Mode.STANDALONE)
    # # Run headless - no GUI
    # AI4Animation(Program(), mode=AI4Animation.Mode.HEADLESS)
    
    # # Run manually
    # engine = AI4Animation(Program(), mode=AI4Animation.Mode.MANUAL)

    # # Drive the update loop externally
    # for i in range(1000):
    #     AI4Animation.Update(deltaTime=1.0/60.0)