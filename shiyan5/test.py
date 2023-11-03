fac = [1, 1, 2]
def C(n, m): # inv(x)==x
	return 0 if n<m else fac[n]*fac[m]*fac[n-m]%3
def Lucas(n, m):
	ans = 1
	while m and ans:
		ans, n, m = ans*C(n%3, m%3)%3, n//3, m//3
	return ans
def triangle(row):
	i, ans, n = 0, 0, len(row)-1
	if not n: return row
	for c in row:
		ans, i = ans+(0 if c=='R' else 1 if c=='G' else 2)*Lucas(n,i), i+1
	ans=(3-ans%3 if n&1 else ans)%3
	return 'R' if ans==0 else 'G' if ans==1 else 'B'
print(triangle('RGB'))