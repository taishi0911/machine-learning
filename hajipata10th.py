#coding:utf-8
import numpy as np
import math
import matplotlib.pyplot as plt

#多次元正規分布の実装
def mnd(x, mu, sigma):
	norm1 = 1 / (math.pow(2 * math.pi, len(x)/2.0) * math.pow(np.linalg.det(sigma), 1.0/2.0))
	x_mu = np.matrix(x-mu)
	sigma = np.matrix(sigma)
	norm2 = np.exp(-0.5 * x_mu * sigma.I * x_mu.T)
	return float(norm1 * norm2)

#EMアルゴリズムのEステップ関数
def estep(data, K, mu, sigma, pi_k):
	"""
	このEstimationステップでは現在のパラメータを用いて負担率を計算し、負担率の行列を返す
	負担率はこのパラメータの確率分布においてクラスタKに所属する確率を表す
	クラスタ数Kはk-meansと同様、あらかじめクラスタ数を決めておく必要がある
	"""
	N = len(data)						#データ数
	
	likelihood = np.zeros((N,K))
	gamma_nk = np.zeros((N,K))

	#負担率の分子を算出
	for k in range(K):
		likelihood[:,k] = [pi_k[k] * mnd( d, mu[k], sigma[k]) for d in data]

	#負担率を算出
	for n in range(N):
		gamma_nk[n,:] = likelihood[n,:] / sum(likelihood[n,:])

	return (gamma_nk, likelihood)

#EMアルゴリズムのMステップ関数
def mstep(data, gamma_nk, K):
	"""
	このMaximizationステップでは、現在の負担率を用いてパラメータの更新を行う
	尤度関数、対数尤度関数、Ｑ関数を最大化するパラメータを求める
	"""
	N = len(data)

	N_k = np.array([sum(gamma_nk[:,k]) for k in range(K)])
	pi_k = N_k / sum(N_k)
	mu = np.dot(gamma_nk.T, data)/N_k
	for k in range(K):
		sig = 0

		for n in range(N):
			x_mu = data[n,:] - mu[:,k]
			sig += gamma_nk[n,k] * np.outer(x_mu, x_mu.T)
		sigma[k] = np.array(sig/N_k[k])
	
	return (mu, sigma, pi_k)



#test_dataの生成
d1 = np.random.randn(1000,2)				#平均(0,0)で分散1
d2 = np.random.randn(1000,2)*2+ [5,4]		#平均(5,4)で分散4(標準偏差が2)

data = np.r_[d1, d2]

plt.scatter(d1[:,0], d1[:,1], c="red", marker="o")
plt.scatter(d2[:,0], d2[:,1], c="yellow", marker="o")
plt.show()


#平均、分散、混合率を初期化する
mu = [np.array([0,0]), np.array([1,0])]		#平均値μをクラスタ数分生成
sigma = [np.eye(2), np.eye(2)]				#単位行列をクラスタ数分生成
pi_k = [0.5, 0.5]							#混合比π

#クラスタ数の設定
K =	2

#対数尤度とその変化度の初期化
L = []										#対数尤度を格納する
diff = 1 									#対数尤度の変化度の初期化

"""
while文を使ってdiffが0.01以下になるまでループを繰り返しましょう
対数尤度を計算し、パラメータと対数尤度の値から収束性を判断

（もしくはfor文で10ループくらいまわしてもそれなりの答えがでます）
"""

# for var in range(0,10):
while diff<0.01:
	gamma_nk, likelihood = estep(data, K, mu, sigma, pi_k)
	mu, sigma, pi_k = mstep(data, gamma_nk, K)
	
#	L1 = sum(likelihood)
#	L.append(math.log(L1))
#	diff = 
	N = len(data)
	l=sum(map(np.log, [sum(likelihood[n,:]for n in range(N))]))
	if L:
		diff = math.fabs(L[-1],1)
		L.append(l)
	else:
		L.append(l)

print gamma_nk

