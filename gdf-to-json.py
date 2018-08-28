# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 08:43:17 2018

@author: oscar
"""
import json 

def read_gdf(path):
    with open(path) as file:
        data = file.read().split(">")
        print(data)
        #deletes the first statement (since it is not needed)
        del (data[0])
        
        #data[0] contains the nodes while data[1] contains the edges
        #splits the data by each line, since each node is inserted in a new line
        data_by_lines = data[0].split("\n")
        
        #splits the data between , since , split attributes
        for x in range(len(data_by_lines)):
            data_by_lines[x] = data_by_lines[x].split(",")
        
        #stores the attributes keys, which are hold at data_by_lines[0]
        keys = data_by_lines[0]
        
        #deletes edgedef string, since it is not needed
        del (data_by_lines[-1])
        
        nodes_by_id = {}        
        attributes = {}
        
        
        #iterates throught data_by_lines and then to each node attribute to store
        #their values to their corresponding key
        for i in range(1,len(data_by_lines)):
            for j in range(1,len(keys)):
                attributes.update({keys[j]:data_by_lines[i][j]})
#            dict_to_json = json.loads(json.dumps(attributes))
            nodes_by_id.update({data_by_lines[i][0]:attributes})
        
        #this part of the code is in charge of the edgedef
        e_attributes = {}
        e_by_id = {}
        edgedef_by_lines = data[1].split("\n")
        
        for x in range(len(edgedef_by_lines)):
            edgedef_by_lines[x] = edgedef_by_lines[x].split(",")
        
        keys = edgedef_by_lines[0]
        del (edgedef_by_lines[-1])
        
        for i in range(1,len(edgedef_by_lines)):
            for j in range(0, len(keys)):
                e_attributes.update({keys[j]:edgedef_by_lines[i][j]})
            e_by_id.update({i:e_attributes})
        
        jsonfile = {"nodes" : nodes_by_id, "edgedef": e_by_id}
        file.close()
        
    with open('data.json', 'w') as outfile:
        json.dump(jsonfile, outfile)
        outfile.close()
        
read_gdf("Pittsburgh_steelers.gdf")
