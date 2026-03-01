import matplotlib.pyplot as plt
import numpy as np
import math


#task1: build plot of density propability
def task1():
    mu = 5
    sigma = 1.5
    dx = 0.01
    
    x = np.arange(-10, 10, dx)
    
    func = 1/(np.sqrt(2*np.pi) * sigma)*np.exp((-(x - mu)**2) / (2*sigma))
    
    plt.plot(x, func)
    plt.xlabel("x")
    plt.ylabel("d(x)")
    plt.title("Density distribution")
    plt.show()

#task2: hist of normal distribution
def task2():
    mu = 7
    sigma = 25
    sko = np.sqrt(sigma)
    
    t = np.linspace(0, 3, 10000000)
    x = np.random.normal(mu, sko, len(t))
    
    plt.subplot(1, 2, 1)   
    plt.plot(t, x)
    plt.xlabel("x")
    plt.ylabel("N(x)")
    plt.title("Random value")
    
    plt.subplot(1, 2, 2)   
    plt.hist(x, 120)
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.title("Hist of density distribution")
    
    plt.show()

def task3():
    mu = 7
    sigma = 25
    sko = np.sqrt(sigma)

    t = np.linspace(0, 3, 10000000)
    x = np.random.normal(mu, sko, len(t))  
    
    emperical_mu = np.sum(x) / len(x)
    emperical_sigma = np.sum(x**2) / len(x) - emperical_mu**2
    
    print("M:", emperical_mu)
    print("D:",emperical_sigma) 
    
task3()