a = int(input())
b = int(input())
c = int(input())
s = int(input())
if b < a and b > c and b > s:
    pred_po_maximum = b
if a < b and a > c and a > s:
    pred_po_maximum = a
if c < a and c > b and c > s:
    pred_po_maximum = c
if s < a and s > b and s > c:
    pred_po_maximum = s
print(pred_po_maximum)