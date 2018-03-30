import pip

class install_packages:
	def __init__(self):
		self.data = {
		  "Dependencies":[
			"alabaster==0.7.10",
			"appdirs==1.4.3",
			"astroid==1.6.1",
			"attrs==16.3.0",
			"Automat==0.3.0",
			"Babel==2.5.3",
			"backports-abc==0.5",
			"backports.functools-lru-cache==1.5",
			"backports.shutil-get-terminal-size==1.0.0"
		  ]
		}
	def install_packages_using_python(self):
		failed_packages = []
		for package in self.data["Dependencies"]:
			data = pip.main(['install', package])
			if data != 0:
				failed_packages.append(package)
				print package, "------------------Failed to install"
				print "1 for continue"
				ch = input()
				if ch == 1:
					continue
				else:
					break
		print '---------------------Status--------------------------'
		if not failed_packages:
			print "Sucess"
		else:
			print "----------------Failed Packages------------------"
			for packg in failed_packages:
				print packg

obj = install_packages()
obj.install_packages_using_python()