signals = input() 
weights = input() 

signals_list = signals[1:-1].split(",")
weights_list = weights[1:-1].split(",")

modified_signals = []
for signal,weight in zip(signals_list, weights_list):
    modified_signals.append(int(signal)*int(weight))

max_product = 1
min_product = 1
result = float('-inf')

for signal in modified_signals:
    if signal < 0:
        max_product, min_product = min_product, max_product
    max_product = max(signal,max_product*signal )
    min_product = min(signal, min_product*signal )
    result = max(result,max_product)

print(result)