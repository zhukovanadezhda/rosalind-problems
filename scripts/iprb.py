import sys

def calculate_dominant_proba(k, m, n):
    sum = k + m + n
    AA = k/sum * ((k-1)/(sum-1) + m/(sum-1) + n/(sum-1))
    Aa = m/sum * (0.75*(m-1)/(sum-1) + k/(sum-1) + 0.5*n/(sum-1))
    aa = n/sum * (0*(n-1)/(sum-1) + 0.5*m/(sum-1) + k/(sum-1))
    return AA+Aa+aa

print(calculate_dominant_proba(*[int(x) for x in sys.argv[1:]]))