from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from panda3d.core import DirectionalLight, AmbientLight

loadPrcFileData('settings.prc')

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        grassBlock = loader.loadModel('grass-block.glb')
        grassBlock.reparentTo(render)

        dirtBlock = loader.loadModel('dirt-block.glb')
        dirtBlock.setPos(0, 2, 0)
        dirtBlock.reparentTo(render)

        sandBlock = loader.loadModel('sand-block.glb')
        sandBlock.setPos(0, 4, 0)
        sandBlock.reparentTo(render)

        stoneBlock = loader.loadModel('stone-block.glb')
        stoneBlock.setPos(0, 6, 0)
        stoneBlock.reparentTo(render)

        mainLight = DirectionalLight('mainLight')
        mainLightNodePath = render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)
        render.setLight(mainLightNodePath)

        ambientLight = AmbientLight('ambientLight')
        ambientLight.setColor((0.3, 0.3, 0.3, 1))
        ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNodePath)

game = MyApp()
game.run()