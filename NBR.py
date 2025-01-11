import iteration
import numpy as np


def decode(H,ep):
    """
    :param H:  lower-triangular generator matrices
    :param x:
    :return: the closest point of x, (1,n)
    """
    n = H.shape[0]  # Matrix dimension
    bestdist = np.inf
    k = n - 1
    dist = np.zeros(n)
    e = np.zeros((n, n))
    u = np.zeros(n)
    step = np.zeros(n)
    u_hat = []
    dist[k] = 0
    # e[k] = 0
    u[k] = np.round(e[k][k]).astype(int)
    y = (e[k][k] - u[k]) / H[k][k]

    step[k] = iteration.sign(y)

    while True:
        newdist = dist[k] + y ** 2

        if newdist < (1 + ep) * bestdist:
            if k != 0:
                for i in range(0, k):
                    e[k - 1][i] = e[k][i] - y * H[k][i]
                k -= 1
                dist[k] = newdist
                u[k] = np.round(e[k][k]).astype(int)
                y = (e[k][k] - u[k]) / H[k][k]
                step[k] = iteration.sign(y)
            else:
                if newdist != 0:
                    if not any(np.array_equal(u,x) for x in u_hat):
                        # print(u_hat)
                        u_hat.append(u.copy())
                        # print(u_hat)
                    bestdist = min(bestdist, newdist)
                # k += 1
                u[k] = u[k] + step[k]
                y = (e[k][k] - u[k]) / H[k][k]
                step[k] = -step[k] - iteration.sign(step[k])
        else:
            if k == n - 1:
                return u_hat
            else:
                k += 1
                u[k] = u[k] + step[k]
                y = (e[k][k] - u[k]) / H[k][k]
                step[k] = -step[k] - iteration.sign(step[k])

# 调用decode时选择的ep参数应该根据B和r的大小更改。此函数在维度大或者ep参数选择不当时只能计算出下界或计算时间过长。
def compute_NBR(B, r):
    U = decode(np.linalg.inv(B),4)
    x=np.zeros(np.array(B).shape[0])
    if not any(np.array_equal(u, x) for u in U):
        U.append(x.copy())
    print(U)
    count=0
    for u in U:
        lattice_point=u@B
        norm=np.linalg.norm(lattice_point)
        if norm<=r:
            count+=1
    return count
B2=[[ 1.07721641,  0.        ],
 [-0.53500698,  0.92831857]]
B3=[[ 1.08992131,  0.,          0.        ],
 [ 0.36251462,  1.02788321,  0.        ],
 [-0.36623167,  0.50961007,  0.89260864]]
B4=[[ 1.18573867,  0.,          0.,          0.        ],
 [-0.00479878,  1.18744622,  0.,          0.        ],
 [-0.58810547, -0.59206649,  0.84311786,  0.        ],
 [ 0.58704406,  0.59144237,  0.00314032,  0.84238142]]
B10=[[ 1.58587605,  0.,          0.,          0.,          0.,          0.,
   0.,          0.,          0.,          0.,        ],
 [ 0.30095661,  1.52365335,  0.,          0.,          0.,          0.,
   0.,          0.,          0.,          0.,        ],
 [-0.31714584,  0.35264529,  1.50624341,  0.,          0.,          0.,
   0.,          0.,          0.,          0.,        ],
 [ 0.63744095, -0.11461431, -0.50501253,  1.14413832,  0.,          0.,
   0.,          0.,          0.,          0.,        ],
 [-0.63630001,  0.14435027, -0.17027073,  0.2931415,   1.21331243,  0.,
   0.,          0.,          0.,          0.,        ],
 [-0.63878841,  0.75086317,  0.33023462,  0.56996207, -0.50523365,  0.55419282,
   0.,          0.,          0.,          0.,        ],
 [ 0.01058537, -0.61279179, -0.49692751, -0.25633563,  0.07448787, -0.2464173,
   1.10334554,  0.,          0.,          0.        ],
 [-0.63944409,  0.7579534,   0.33250649, -0.26900993, -0.28885689, -0.16873019,
   0.52419624,  0.65203941,  0.,          0.        ],
 [ 0.65585338, -0.74530601, -0.34284773,  0.29543685,  0.30149274,  0.17603913,
   0.40531285,  0.16647994,  0.70586947,  0.        ],
 [-0.63984878, -0.4853407,  -0.66309563,  0.02096227, -0.37339316,  0.06958645,
   0.35344802, -0.08619032, -0.35154403,  0.70327887]]

count=compute_NBR(B10,np.sqrt(2))
print(count)

"""print("请输入想要求解生成矩阵的维度：")
n = int(input())
B, nsm = iteration.iterative_lattice_construction(n)"""

