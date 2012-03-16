# hungary.py

# hungary algorithm using bfs method
def hungary_bfs(m,n,mat):
	s = [-1]*(m+1)
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
						
# hungary algorithm using dfs recursive method
def dfs(m,n,k,t,mat,match1,match2):
	
	for j in range(n):
		if mat[k][j] == 1 and t[j] < 0:
			t[j] = k
			if match2[j] == -1 or dfs(m,n,match2[j],t,mat,match1,match2) == True:
				match1[k] = j
				match2[j] = k
				return True
	return False
	
def hungary_dfs_rec(m,n,mat):
	match1 = [-1]*m
	match2 = [-1]*n
	ret = 0
	
	for i in range(m):
		t = [-1]*n
		if dfs(m,n,i,t,mat,match1,match2) == True:
			ret += 1
			
	return ret,match1

# hungary algorithm using dfs unrecursive method
def hungary_dfs_unrec(m,n,mat):
	stack = [0]*(m+2)
	ind = [-1]*m
	
	match1 = [-1]*m
	match2 = [-1]*n
	
	ret = 0
	
	for i in range(m):
		t = [-1]*n
		top = 0
		stack[top] = i
		ind[top] = 0
		top+=1
#		print match1
		while True:
			if match1[i] >= 0 or top == 0: break
			k = stack[top-1]
			j = ind[top-1]
			while True:
				if j == n : 
					top -= 1
					break
				if mat[k][j] == 1 and t[j] < 0:
					t[j] = k
					if match2[j] == -1:
						p = j
						while True:
							if p < 0: break
							match2[j] = t[j]
							k = t[j]
							p = match1[k]
							match1[k] = j
							j = p
						break
					else:
						stack[top] = match2[j]
						ind[top] = 0
						top+=1
						break
				j+=1
		if match1[i] >=0:
			ret += 1
	
	return ret,match1
	

if __name__ == '__main__':
	mat = [[0,1,1],[1,0,0],[0,1,0]]
#	(res,match1) = hungary_dfs_rec(3,3,mat)
#	print res
#	print match1
	(res,match1) = hungary_dfs_unrec(3,3,mat)
	print res
	print match1