print("Running custom program from NiFi")

def updateAttribute(flowfile):
	flowfile = session.putAttribute(flowfile, 'course', 'nifi')
	session.transfer(flowfile, REL_SUCCESS)
	session.commit()


# main
flowfile = session.get()
if flowfile is not None:
	updateAttribute(flowfile)