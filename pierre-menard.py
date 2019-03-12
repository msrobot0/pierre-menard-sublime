import sublime
import sublime_plugin
import datetime




class PierreEventListener(sublime_plugin.EventListener):	
	def init(self, view):
		self.fn = "%s-%s.txt" % (datetime.datetime.now().date(),"log")
		self.path = "/Users/Parmenides/projects/RC/pierre-menard-sublime/"
		self.fullpath = "%s%s" % (self.path,self.fn)
		self.f = open(self.fullpath,"a")
		self.f.write("STARTING %s" % datetime.datetime.now())
		self.f.close()
		self.f = open(self.fullpath,"a")

	def on_modified(self,view):
		try:
			if self.fullpath is None:
				self.init(view)
		except: #THIS IS TOTALLY BOGUS
			self.fullpath = ""
			self.init(view)

		regions = view.sel()

		self.f = open(self.fullpath,"a")
		for r in regions:
			row,col = view.rowcol(r.a)
			line = row + 1
			lastchar_r = sublime.Region(r.a-1,r.a)
			lastchar = view.substr(lastchar_r)
			self.f.write("%s,%s,%s,%s\n" % (datetime.datetime.now(),line,col,lastchar)) #view.text_point()))
		self.f.close()
		self.f = open(self.fullpath,"a")

	def on_load(self, view):	
		self.init(view)	

	def on_close(view):
		self.f.close()



		