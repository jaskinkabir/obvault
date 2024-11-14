# Part A
## 1 Core
$\left( 2.56 \times 10^{9} \text{ instructions} * 1 \frac{\text{cycles}}{instruction} + 1.28 \times 10^{9} \text{ instructions} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large9.6 sec$
## 2 Cores
$\left( \frac{2.56 \times 10^{9} \text{ instructions}}{0.7 \times 2} * 1 \frac{\text{cycles}}{instruction} + \frac{1.28 \times 10^{9} \text{ instructions}}{0.7 \times 2} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large7.04 sec$
$1-\frac{7.04}{9.6} =26.67$% Faster
## 4 Cores
$\left( \frac{2.56 \times 10^{9} \text{ instructions}}{0.7 \times 4} * 1 \frac{\text{cycles}}{instruction} + \frac{1.28 \times 10^{9} \text{ instructions}}{0.7 \times 4} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large 3.84 sec$
$1-\frac{3.84}{9.6} =60$% Faster
## 8 Cores
$\left( \frac{2.56 \times 10^{9} \text{ instructions}}{0.7 \times 8} * 1 \frac{\text{cycles}}{instruction} + \frac{1.28 \times 10^{9} \text{ instructions}}{0.7 \times 8} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large 2.24 sec$
$1-\frac{2.24}{9.6} =76.7$% Faster

# Part B
## 1 Core
$\left( 2.56 \times 10^{9} \text{ instructions} * 2 \frac{\text{cycles}}{instruction} + 1.28 \times 10^{9} \text{ instructions} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large 10.88 sec$
$\frac{10.88}{9.6}-1 = 13.3$% slower
## 2 Cores
$\left( \frac{2.56 \times 10^{9} \text{ instructions}}{0.7 \times 2} * 2 \frac{\text{cycles}}{instruction} + \frac{1.28 \times 10^{9} \text{ instructions}}{0.7 \times 2} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large 7.95 sec$
$\frac{7.95}{7.04}-1 = 13$% slower
## 4 Cores
$\left( \frac{2.56 \times 10^{9} \text{ instructions}}{0.7 \times 4} * 2 \frac{\text{cycles}}{instruction} + \frac{1.28 \times 10^{9} \text{ instructions}}{0.7 \times 4} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large 4.3 sec$
$\frac{4.3}{3.84} =11.9$% Slower
## 8 Cores
$\left( \frac{2.56 \times 10^{9} \text{ instructions}}{0.7 \times 8} * 2 \frac{\text{cycles}}{instruction} + \frac{1.28 \times 10^{9} \text{ instructions}}{0.7 \times 8} \times 12 \frac{\text{cycles}}{instruction} + 2.56 \times 10^{8} \text{ instructions} \times 5 \frac{\text{cycles}}{instruction} \right) * \frac{1}{2 \times 10^ {9}} \frac{\text{sec}}{\text{cycle}}=\Large 2.47 sec$
$\frac{2.47}{2.24} =10.2$% Slower
