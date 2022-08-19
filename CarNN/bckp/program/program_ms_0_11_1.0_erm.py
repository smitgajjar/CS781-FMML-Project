import sys
sys.path.insert(0,"examples/CarNN/")
import feature_defs

def execute(inputs):
	program_nodes ={}
	program_nodes["3"]= "safety_3"
	program_nodes["2"]= "buying_4"
	program_nodes["1"]= "persons_3"
	program_nodes["0"]= "maint_4"

	program_edges ={}
	program_edges[("3",2)]= "opclass_0"
	program_edges[("3",1)]= "opclass_2"
	program_edges[("3",0)]= "opclass_2"
	program_edges[("2",3)]= "3"
	program_edges[("2",2)]= "opclass_2"
	program_edges[("2",1)]= "opclass_2"
	program_edges[("2",0)]= "opclass_2"
	program_edges[("1",3)]= "opclass_0"
	program_edges[("1",2)]= "2"
	program_edges[("1",1)]= "2"
	program_edges[("1",0)]= "2"
	program_edges[("0",3)]= "1"
	program_edges[("0",2)]= "1"
	program_edges[("0",1)]= "2"
	program_edges[("0",0)]= "2"

	features = feature_defs.retrieve_feature_defs()

	value_map = {} 
	value_map["safety_3"] = features["safety_3"]([("buying",inputs[0]),("maint",inputs[1]),("doors",inputs[2]),("persons",inputs[3]),("lug_boot",inputs[4]),("safety",inputs[5])])
	value_map["buying_4"] = features["buying_4"]([("buying",inputs[0]),("maint",inputs[1]),("doors",inputs[2]),("persons",inputs[3]),("lug_boot",inputs[4]),("safety",inputs[5])])
	value_map["persons_3"] = features["persons_3"]([("buying",inputs[0]),("maint",inputs[1]),("doors",inputs[2]),("persons",inputs[3]),("lug_boot",inputs[4]),("safety",inputs[5])])
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

