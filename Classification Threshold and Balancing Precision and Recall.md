Continues [[Classifier Evaluation]]
# Classification Threshold
- The output of the probabilistic (logistic) classifier

For class #intro-ML


$\text{Precision} = \frac{TP}{TP+FP}$
$1-\frac{TP}{TP+FP}=\frac{TP+FP}{TP+FP}-\frac{TP}{TP+FP}$

$=\frac{FP}{TP+FP}$

$\text{Recall} = \frac{TP}{TP+FN}$
$1-\frac{TP}{TP+FN}=\frac{TP+FN}{TP+FN}-\frac{TP}{TP+FN}$

$=\frac{FN}{TP+FP}$


|        | True 1 | True 0 |
| ------ | ------ | ------ |
| Pred 1 | TP     | FP     |
| Pred 0 | FN     | TN     |

$TNR=\frac{TN}{TN+FP}$
$FNR=\frac{FN}{FN+TP}$
$FPR = \frac{FP}{FP+TN}$



| TP  | FP  |
| --- | --- |
| FN  | TN  |
     |
