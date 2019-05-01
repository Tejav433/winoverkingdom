def solution(n,a,p,q):
	start_range = []
 	end_range = []
 	for i in range(0,n):
 		start_range.append(a[i]-q[i])
 		end_range.append(a[i]+p[i])
 	return (min(end_range)-max(start_range)+1)
 	
t  = input()
for i in range(0,t):
	n = input()
 	a = map(int,raw_input().split())
 	p = map(int,raw_input().split())
 	q = map(int,raw_input().split())
 	print solution(n,a,p,q)
