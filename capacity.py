
import cvxpy as cp
import numpy as np
def channel_capacity(n, m, P, sum_x=1):
    '''
    Boyd and Vandenberghe, Convex Optimization, exercise 4.57 page 207
    Capacity of a communication channel.

    We consider a communication channel, with input X(t)∈{1,..,n} and
    output Y(t)∈{1,...,m}, for t=1,2,... .The relation between the
    input and output is given statistically:
    p_(i,j) = ℙ(Y(t)=i|X(t)=j), i=1,..,m  j=1,...,m

    The matrix P ∈ ℝ^(m*n) is called the channel transition matrix, and
    the channel is called a discrete memoryless channel. Assuming X has a
    probability distribution denoted x ∈ ℝ^n, i.e.,
    x_j = ℙ(X=j), j=1,...,n

    The mutual information between X and Y is given by
    ∑(∑(x_j p_(i,j)log_2(p_(i,j)/∑(x_k p_(i,k)))))
    Then channel capacity C is given by
    C = sup I(X;Y).
    With a variable change of y = Px this becomes
    I(X;Y)=  c^T x - ∑(y_i log_2 y_i)
    where c_j = ∑(p_(i,j)log_2(p_(i,j)))
    '''

    # n is the number of different input values
    # m is the number of different output values
    if n*m == 0:
        print('The range of both input and output values must be greater than zero')
        return 'failed', np.nan, np.nan

    # x is probability distribution of the input signal X(t)
    x = cp.Variable(shape=n)

    # y is the probability distribution of the output signal Y(t)
    # P is the channel transition matrix
    y = P*x

    # I is the mutual information between x and y
    c = np.sum(P*np.log2(P),axis=0)
    I = c*x + cp.sum(cp.entr(y))
   
    # Channel capacity maximised by maximising the mutual information
    obj = cp.Minimize(-I)
    constraints = [cp.sum(x) == sum_x,x >= 0]

    # Form and solve problem
    prob = cp.Problem(obj,constraints)
    prob.solve()
    if prob.status=='optimal':
        return prob.status, prob.value, x.value
    else:
        return prob.status, np.nan, np.nan
        
np.set_printoptions(precision=5)
n = 3
m = 3
P = np.array([[0.1616880539,0.4343575576,0.4039543886],
             [0.3085662296,0.4748585777,0.2165751927],
             [0.5297457166,0.09078386473,0.3794704187]])
A = np.transpose(P)
stat, C, x = channel_capacity(n, m, np.transpose(P))
print('Problem status: ',stat)
print('Optimal value of C = {:.4g}'.format(C))
print('Optimal variable x = \n', x)
