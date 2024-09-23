import os


def saveResourceAtDirectory(resources:list):
    try:
        for resource in resources:
            path=f"Temp/{resource.name}"
            with open(path, "wb") as file:
                file.write(resource.file.read())
    except Exception as e:
        print(e)
        
        
def saveResourceToDatabase(resources:list):
    pass
                    
        