import math

def hinh_lap_phuong(s):
    V = s**3
    return V

def hop_chu_nhat(l,w,h):
    V = l*w*h
    return V

def hinh_tru_tron(r,h):
    V = (math.pi)*(r**2)*h
    return V

def hinh_cau(r):
    V = (4/3)*(math.pi)*(r**3)
    return V

print('so pi co gia tri la',math.pi)
print('the tich cua hinh cau la',hinh_cau(1.3))
print('the tich cua hinh hop chu nhat la', hop_chu_nhat(1,2,3))
print('the tich cua hinh tru tron la', hinh_tru_tron(1.2,4))
print('the tich cua hinh lap phuong la', hinh_lap_phuong(3))