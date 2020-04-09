from lxml import etree
import objects

def loadworld(gamefile):
        #open XML file and preparing tree element
        with open(gamefile, 'r') as file:
                xmlstring = file.read()
        tree = etree.XML(xmlstring)
        #transferring informations to objects via object's method
        world = objects.World(tree)
        #load player 
        for room in world.rooms.values():
            if hasattr(room, 'player'):
                global player
                player = room.player
                del room.player
        print("Loaded World!")
        return world, player

def saveworld(rootobj, playerobj, gamefile):
        #merger root and player
        rootobj.rooms[playerobj.inroom].player = playerobj
        tree = rootobj.save()
        xmlstring = etree.tostring(tree, pretty_print=True)
        with open(gamefile, 'wb+') as file:
                file.write(xmlstring)
        print("Saved World!")
        return
        
       
path = "game1.xml"
path2 = "test2.xml"

world, player = loadworld(path)
saveworld(world, player, path2)
