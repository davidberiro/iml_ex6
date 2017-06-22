import numpy as np
import matplotlib.pyplot as plt
import valueIteration

#assuming symettrically that | $|s_0|  |  |  |  |$$$|


class State:
	def __init__(self):
		self.actions = {}
		self.gainFromAction={}

	def setActions(self, r, l, rvalue, lvalue):
		self.actions = {"right": r, "left": l}
		self.gainFromAction={"right": rvalue, "left": lvalue}

A = ["right", "left"]

states = [State() for i in range(5)]
states[0].setActions(1, 0, 0, 1)
states[1].setActions(2, 0, 0, 0)
states[2].setActions(3, 1, 0, 0)
states[3].setActions(4, 2, 0, 0)
states[4].setActions(0, 3, 6, 0)

tau = np.zeros((5, 2, 5))
rho = np.zeros((5, 2))

for i in range(5):
	for j in range(len(A)):
		rho[i,j]=states[i].gainFromAction[A[j]]
		for k in range(5):
			tau[i,j,k]=1 if states[i].actions[A[j]]==k else 0


def q1():
	print(valueIteration.valueIteration(5, 2, tau, rho, 0.75))

def q2():
	print(valueIteration.valueIteration(5, 2, tau, rho, 0.5))
	print(valueIteration.valueIteration(5, 2, tau, rho, 0.75))
	print(valueIteration.valueIteration(5, 2, tau, rho, 0.85))

def q3():
	gamma=0.5
	gamma_values = []
	s_0 = []
	for i in range(50):
		gamma_values.append(gamma)
		s_0.append(valueIteration.valueIteration(5, 2, tau, rho, gamma)[0])
		gamma+=0.01
	plt.plot(gamma_values, s_0, 'r-')
	plt.show()

q3()



