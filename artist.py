

class Artist(object):

	def __init__(self, name=None, label=None, sisy_time= None, time=None):
		self.name = name
		self.name_utf = unicode(name, "utf-8")
		self.label = label
		self.sisy_time = sisy_time
		self.time = time

	def print_me(self):
		print("'{}' from '{}' plays {}".format(self.name, self.label, self.sisy_time))