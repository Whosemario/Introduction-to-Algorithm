# hungary.py

def hungary(m,n,mat,match1,match2):
	s = [-1]*m
	match1 = [-1]*n
	match2 = [-1]*m
	ret = 0
	
	for i in range(m):
		t = [-1]*n
		p=q=0
		s[0] = i
		while True:
			if match1[i] >=0 or p > q: break
			k = s[p]
			for j in range(n):
				if match1[i] >=0: break
				if mat[k][j] != 0 and t[j] < 0:
					q+=1
					s[q] = match2[j]
					t[j] = k
					if s[q] < 0:
						p = j
						while True:
							if p<0: break
							match2[j] = t[j]
							k = t[j]
							p = match1[k]
							match1[k] = j
							j = p
			p+=1
		
		if match1[i] >=0 : ret += 1
	
#	print match1
	return ret,match1
						
	
if __name__ == '__main__':
	mat = [[0,1,1],[1,0,0],[0,1,0]]
	match1 = []
	match2 = []
	(res,match1) = hungary(3,3,mat,match1,match2)
	print res
	print match1