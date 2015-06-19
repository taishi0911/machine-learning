#coding:utf-8
import numpy as np
import math
import matplotlib.pyplot as plt

#多次元正規分布の実装
def mnd2(_x, _mu, _sig):
    x = np.matrix(_x)
    mu = np.matrix(_mu)
    sig = np.matrix(_sig)
    a = np.sqrt(np.linalg.det(sig)*(2*np.pi)**sig.ndim)
    b = np.linalg.det(-0.5*(x-mu)*sig.I*(x-mu).T)
    return np.exp(b)/a

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
d1 = np.random.randn(1000,2)			#平均(0,0)で分散1
d2 = np.random.randn(1000,2)*2+ [5,4]	#平均(6,6)で分散4(標準偏差が2)

data = np.r_[d1, d2]

plt.scatter(d1[:,0], d1[:,1], c="red", marker="o")
plt.scatter(d2[:,0], d2[:,1], c="yellow", marker="o")
plt.show()


#平均、分散、混合率の初期値
mu = [np.array([0,0]), np.array([1,0])]		#平均値μをクラスタ数分生成
sigma = [np.eye(2), np.eye(2)]				#単位行列をクラスタ数分生成
pi_k = [0.5, 0.5]							#混合比π

K =	2	#クラスタ数

L = []
mu_iter = []
sigma_iter = []
pi_k_iter = []
diff = 1

step = 1

#収束するまで繰り返し
#対数尤度を計算し、パラメータと対数尤度の値から収束性を判断
while diff > 0.01:

	print "step : ", step

	gamma_nk, likelihood = estep(data, K, mu, sigma, pi_k)
	mu, sigma, pi_k = mstep(data, gamma_nk, K)

	mu_iter.append(mu)
	sigma_iter.append(sigma)
	pi_k_iter.append(pi_k)

	N = len(data)

	l = sum(map(np.log, [sum(likelihood[n,:]) for n in range(N)])) / N
	"""
	mapはすべての要素を関数の引数として実行し、その実行結果から新しいlistを作成する。
	ここでは
	[sum(likelihood[n,:]) for n in range(N)]
	のすべての要素に対して対数をとっている
	"""
	print "log-likelihood : ", l
	step += 1
	if L:
		diff = math.fabs(L[-1] - l)		#fabsは絶対値を返す。一つ前のlとくらべて差が0.1以下になるまで繰り返す。
		L.append(l)
	else:
		L.append(l)


result = u"""
****RESULT****
---Log-likelihood---
%s

---μ---
%s

---Σ1---
%s

---Σ2---
%s

---π---
%s

---γ---
%s
accuracy rate of data1 : %s

%s
accuracy rate of data2 : %s
""" %(L, mu, sigma[0], sigma[1], pi_k, gamma_nk[:N/2-1], sum(gamma_nk[:N/2-1,0])/(N/2), gamma_nk[N/2:N-1], sum(gamma_nk[N/2:N-1,1])/(N/2))

print result