import numpy as np

"""
Fake Data Helper Functions
"""
def gen_user_activity(num_users=200, num_lessons=30, thumbs_down=True):

    """
    generates fake data on user activity, 1 meaning they completed a lesson, 0 saying they did not
    
    inputs
    (the dimensions of the array)
    num_users: the rows of the returned array
    num_lessons: the columns of the returned array
    
    outputs
    user_data: a np array
    """
    lst = []

    for _ in range(num_users):
        m = np.random.randint(15,30) #number of zeros, the sparseness
        n = num_lessons - m
        a = np.ones(n+m, dtype=int)
        a[:m] = 0
        
        if thumbs_down:
            num = np.random.randint(20,30)
            td = n - num
            a[m:td] = -1 

        np.random.shuffle(a)
        lst.append(list(a))

    return np.array(lst)



def gen_lesson_tags(num_lessons=30):
    """
    produces fake lessons tags
    
    inputs
    num_lessons: number of lessons
    
    """
    lst = []
    for _ in range(num_lessons):
        m = np.random.randint(10,15)
        

        b = np.geomspace(.001,.85, num=15)
        b[:m] = 0
        np.random.shuffle(b)
        lst.append(list(np.round(b,3)))
        
    return np.array(lst)

"""
Recommender Functions
"""

# This algorithm first outlined by Simon Funk. He called it "Funk SVD" because of its superficial
# similarity to the SVD algorithm (i.e., it does matrix decomp). It does not, in fact, find singular values
# and is therefore not an SVD algorithm. Furthermore, the algorithm in use is slightly different than
# Funk's, so calling it "FunkSVD" is wrong on both counts. Alas, the name stuck, so here I'll nod to
# tradition.
class FunkSGD:
    
    def __init__(self, R, n_factors, alpha=0.03):
        # alpha is the learning rate
        
        self.R = R
        self.alpha = alpha
        
        m, n = R.shape
        self.P = np.random.normal(size=(m,n_factors))
        self.Q = np.random.normal(size=(n,n_factors))
        
    def one_iter( self ):
        m, n = self.R.shape
        
        for u in range(m): # for every user
            for i in range(n): # for every item

                if np.isnan(self.R[u,i]):         # if this user/item combo hasn't been rated, skip it!
                    continue

                reconstruction_error = self.R[u,i] - self.P[u].dot(self.Q[i])

                # get gradient of error with respect to user profile, item profile
                pu_grad = self.Q[i]*reconstruction_error
                qi_grad = self.P[u]*reconstruction_error

                # use gradient to push profiles in the right direction
                self.P[u] += self.alpha*pu_grad
                self.Q[i] += self.alpha*qi_grad
                
    def reconstruction_loss( self ):
        return np.nansum((self.R - self.P @ self.Q.T)**2)
    