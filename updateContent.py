import csv
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback

class updateContent(StreamCallback):
	def __init__(self):
		pass
		
	def process(self, input, output):
		data = IOUtils.toString(input, StandardCharsets.UTF_8)
		record = data.split(",")
		id = str(record[0])
		name = str(record[1])
		dept = str(record[2])
		salary = int(record[3])
		
		salary = salary + 99
		
		## write output to flowfile
		converted_output = id + "," + name.lower() + "," + dept.lower() + "," + str(salary)
		output.write(converted_output)
		

# main

flowfile = session.get()
if flowfile is not None:
	flowfile = session.write(flowfile, updateContent())
	session.transfer(flowfile, REL_SUCCESS)
	session.commit()
	

		