# Outliers + Risk Assumptions (Stage 07)

For this assignment I used both the **IQR rule** and the **z-score method** to detect outliers.

- For IQR, I used the standard threshold of 1.5×IQR beyond Q1 and Q3.
- For z-scores, I set the cutoff at 3.0.

**Assumptions:**

- The data distribution is approximately continuous and not highly skewed, so median and IQR provide a stable view of “typical” values.
- Outliers reflect noise or unusual errors rather than meaningful rare events.
- Linear regression is sensitive to extreme points, so trimming them is justified to improve model stability.

**Impacts observed:**

- Summary statistics (mean and standard deviation) shifted noticeably after removing outliers, while medians remained stable, confirming that outliers had a strong effect on averages.
- In the regression, the version with outliers produced inflated coefficients and higher error. After filtering, coefficients aligned more closely with expectations and R² improved modestly.
- Winsorizing (as a stretch) reduced the influence of outliers while still keeping all rows, leading to intermediate results between full removal and keeping everything.

**Risks:**

- If the extreme values are actually **real signals** (e.g., rare but important cases), removing or shrinking them could discard valuable information.
- Default thresholds (1.5 IQR or z=3) may not fit every dataset; applying them blindly could bias results.
- In financial or risk contexts, tail events are especially meaningful; treating them as “noise” could understate volatility or risk exposure.
