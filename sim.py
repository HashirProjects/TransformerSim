import matplotlib.pyplot as plt
import numpy as np


class psCurves():
	def __init__(self,lp,ls,amp,freq,eff):
		self.ratio  = lp/ls
		self.amp = amp
		self.freq = freq
		self.eff = eff

	def pfunc(self,x):
		return self.amp*np.sin(2*np.pi*self.freq * x)

	def sfunc(self,x):
		return -np.sqrt(self.eff * self.amp**2)*self.ratio*np.cos(2*np.pi*self.freq * x)

	def plotfuncs(self, startVal, endVal):
		X = np.linspace(startVal,endVal,10000)
		plt.plot(X,self.pfunc(X))
		plt.plot(X,self.sfunc(X))
		plt.plot(X,np.zeros(len(X)))
		plt.show()

he = psCurves(500,10,10,10,0.0003)
he.plotfuncs(0,1)

def pfunc(x,amp,freq):
	return amp*np.sin(2*np.pi*freq * x)

def sfunc(x,amp,freq,lp,ls):
	return amp*(lp/ls)*np.cos(2*np.pi*freq * x)

def plotfuncs():
	X = np.linspace(0,10,10000)
	plt.plot(X,pfunc(X,1,1))
	plt.plot(X,sfunc(X,1,1,5,10))
	plt.show()

plotfuncs()