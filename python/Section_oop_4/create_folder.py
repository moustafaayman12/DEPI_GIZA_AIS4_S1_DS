import os 
def create_folder(path):
    if not os.path.exists(path):
        
        os.mkdir(path)
 
    for i in range(20):
        
        inner_pathh = os.path.join(path, f"folder_{i}.txt")
        if not os.path.exists(inner_pathh):
        
            os.makedirs(inner_pathh)