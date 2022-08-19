import sys
import os
import csv

outputclasslist = ['acc', 'good', 'unacc', 'vgood']

#Generated file 
def check_num_of_inputs(inputs):
	return len(inputs)==6

# buying_4:4:1,  maint_4:4:1,  doors_4:4:1, persons_3:4:1, lug_boot_3:3:1, safety_3:3:1

def buying_4(inputs):
	assert(check_num_of_inputs(inputs))
	return inputs[0][1]

def maint_4(inputs):
	assert(check_num_of_inputs(inputs))
	return inputs[1][1]

def doors_4(inputs):
	assert(check_num_of_inputs(inputs))
	return inputs[2][1]

def persons_3(inputs):
	assert(check_num_of_inputs(inputs))
	return inputs[3][1]

def lug_boot_3(inputs):
	assert(check_num_of_inputs(inputs))
	return inputs[4][1]

def safety_3(inputs):
	assert(check_num_of_inputs(inputs))
	return inputs[5][1]


def opclass(outputs):
	value = outputs[0][1]
	# index = outputclasslist.index(value)
	print ("featuredefs.py value:",value)
	return value

def retrieve_feature_defs(): 
	feature_defs = {} 
	feature_defs["buying_4"] = buying_4
	feature_defs["maint_4"] = maint_4
	feature_defs["doors_4"] = doors_4
	feature_defs["persons_3"] = persons_3
	feature_defs["lug_boot_3"] = lug_boot_3
	feature_defs["safety_3"] = safety_3
	feature_defs["opclass"] = opclass
	return feature_defs 


def fix_nulls(s):
    for line in s:
        yield line.replace('\0', "")

def bucketize():

	file_name = sys.argv[1]
	oFile_name =  os.path.splitext(file_name)[0]+'.minds.csv'
	i_file = open(file_name, 'r') 
	o_file = open(oFile_name, 'w')

	csv_reader = csv.reader(fix_nulls(i_file), delimiter=',')
	csv_writer = csv.writer(o_file, delimiter=',')
    
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			#csv_writer.writerow(["Age_1", "Age_2", "Monthly_Income", row[2], "Credit_Score_1", "Credit_Score_2", row[4]])
#            print(f'Column names are {", ".join(row)}')
			# new_header = ["clouds_3", "clouds_6", "day_time_3","daytime_4", "init_pos_4", "alert"]
			new_header = ["buying_4", "maint_4", "doors_4","persons_3", "lug_boot_3", "safety_3","opclass"]
			csv_writer.writerow(new_header)
			line_count += 1
		else:
			inputs = [("",float(row[0])), ("",float(row[1])), ("", float(row[2])), ("", float(row[3])), ("", float(row[4])),
			("", float(row[5]))]
			outputs = [("", float(row[6]))]
			col1 = buying_4(inputs)
			col2 = maint_4(inputs)
			col3 = doors_4(inputs)
			col4 = persons_3(inputs)
			col5 = lug_boot_3(inputs)
			col6 = opclass(outputs)
			new_row = [col1,col2,col3,col4,col5,col6]
			csv_writer.writerow(new_row)
			line_count += 1
	print(f'Processed {line_count} lines.')


# bucketize()

	