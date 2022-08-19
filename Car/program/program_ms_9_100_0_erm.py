import sys
sys.path.insert(0,"examples/Car/")
import feature_defs

def execute(inputs):
	program_nodes ={}
	program_nodes["0"]= "maint_4"

	program_edges ={}
	program_edges[("2",3)]= "opclass_3"
	program_edges[("2",2)]= "opclass_0"
	program_edges[("2",1)]= "opclass_1"
	program_edges[("2",0)]= "opclass_0"
	program_edges[("1",3)]= "opclass_3"
	program_edges[("1",2)]= "2"
	program_edges[("1",1)]= "opclass_2"
	program_edges[("1",0)]= "opclass_3"
	program_edges[("0",3)]= "opclass_2"
	program_edges[("0",2)]= "opclass_2"
	program_edges[("0",1)]= "opclass_2"
	program_edges[("0",0)]= "opclass_2"

	features = feature_defs.retrieve_feature_defs()

	value_map = {} 
	value_map["maint_4"] = features["maint_4"]([("buying",inputs[0]),("maint",inputs[1]),("doors",inputs[2]),("persons",inputs[3]),("lug_boot",inputs[4]),("safety",inputs[5])])

	flag = True
	current_node = "0"
	while flag:
		current_feature = program_nodes[current_node]
		next_node = program_edges[current_node,value_map[current_feature]]
		if next_node.isdigit():
			current_node = next_node
		else:
			current_node = next_node
			flag = False
	return current_node

