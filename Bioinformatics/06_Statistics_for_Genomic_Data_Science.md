# Statistics for Genomic Data Science

1- Exploratory Data Analysis (EDA), Linear Modeling, and Testing / Multiple Testing
2- Preprocessing, Linear Modeling, and batch effects.
3- Modeling Non-continuous Outcomes, Hypothesis Testing, and Multiple Hypothesis Testing
4- General Pipelines for Genomic Data Analysis


## 1- Exploratory Data Analysis (EDA), Linear Modeling, and Testing / Multiple Testing

"Statistics is the science of learning generalizable knowledge from data."

![alt text](image-42.png)

Sources of statistics packages and tools: blogs, github, cran, bioconductor, etc.

"Data are values of qualitative or quantitative variables, belonging to a set of items."

![alt text](image-43.png)

Raw data = no computations
Processed data = final, tidy dataset

![alt text](image-44.png)

![alt text](image-45.png)


Reproducible Research:

Reproducible research means that you can take someone's data and their code, rerun it and get the same answer exactly the same every time that that code and data are run. 


Achieving Reproducibility:

![alt text](image-46.png)

![alt text](image-47.png)

![alt text](image-48.png)


R Markdown:


The Three Tables in Genomics:

![alt text](image-49.png)

![alt text](image-50.png)


Experimental Design - Variability, Replication, and Power:

![alt text](image-51.png)

![alt text](image-52.png)

![alt text](image-53.png)

![alt text](image-54.png)

![alt text](image-55.png)

![alt text](image-56.png)


Experimental Design - Confounding and Randomization:

![alt text](image-57.png)

![alt text](image-58.png)

![alt text](image-59.png)

![alt text](image-60.png)

![alt text](image-61.png)

![alt text](image-62.png)

![alt text](image-63.png)

![alt text](image-64.png)


Exploratory Analysis:

![alt text](image-65.png)

![alt text](image-66.png)

![alt text](image-67.png)

![alt text](image-68.png)

![alt text](image-69.png)


in R:

![alt text](image-73.png)

![alt text](image-70.png)

![alt text](image-71.png)

![alt text](image-72.png)

![alt text](image-74.png)

![alt text](image-75.png)

![alt text](image-76.png)

![alt text](image-77.png)

![alt text](image-78.png)

![alt text](image-79.png)

![alt text](image-80.png)

![alt text](image-81.png)

![alt text](image-82.png)

![alt text](image-83.png)

![alt text](image-84.png)

![alt text](image-85.png)

![alt text](image-86.png)


Data Transforms:

![alt text](image-87.png)

![alt text](image-88.png)

![alt text](image-89.png)

![alt text](image-90.png)

![alt text](image-91.png)


Clustering:

Hierrarchichal Clustering

![alt text](image-93.png)

![alt text](image-94.png)

![alt text](image-92.png)

K-means Clustering

![alt text](image-95.png)

![alt text](image-96.png)

in R:

![alt text](image-97.png)

![alt text](image-98.png)

![alt text](image-99.png)

![alt text](image-100.png)

![alt text](image-101.png)


Study Reproducibility vs Replicability:

- Reproducibility: The ability to reanalyze the same data and methods from the study and get the same results.

- Replicability: The ability to conduct a new study that is similar to the original study but with new data and maybe new similar methods and get the same results.



## 2- Preprocessing, Linear Modeling, and batch effects.

Quantile normalization example

![alt text](image-102.png)


Dimension Reduction:

![alt text](image-103.png)

![alt text](image-104.png)

![alt text](image-105.png)

![alt text](image-106.png)

![alt text](image-107.png)

![alt text](image-108.png)

in R:

![alt text](image-109.png)

![alt text](image-110.png)

![alt text](image-111.png)


Pre-processing and Normalization

![alt text](image-112.png)

![alt text](image-113.png)

![alt text](image-114.png)

![alt text](image-115.png)

![alt text](image-116.png)

![alt text](image-117.png)

![alt text](image-118.png)

![alt text](image-119.png)

![alt text](image-120.png)

![alt text](image-121.png)


Quanitle Normalization (in R):

![alt text](image-122.png)

![alt text](image-123.png)

![alt text](image-124.png)

![alt text](image-125.png)

![alt text](image-126.png)

![alt text](image-127.png)


The Linear Model:

![alt text](image-128.png)

![alt text](image-129.png)


Linear Models with Categorical Covariates:

![alt text](image-130.png)

![alt text](image-131.png)

![alt text](image-132.png)

![alt text](image-133.png)

![alt text](image-134.png)


Adjusting for Covariates:

![alt text](image-135.png)

![alt text](image-136.png)

![alt text](image-137.png)

![alt text](image-138.png)


Linear Regression in R:

![alt text](image-139.png)

![alt text](image-140.png)

![alt text](image-141.png)

![alt text](image-142.png)

![alt text](image-143.png)

![alt text](image-144.png)

![alt text](image-145.png)

![alt text](image-146.png)

![alt text](image-147.png)


Many Regressions Simultaneously:

![alt text](image-148.png)

![alt text](image-149.png)

![alt text](image-150.png)

![alt text](image-151.png)

![alt text](image-152.png)

![alt text](image-153.png)

![alt text](image-154.png)

in R:

![alt text](image-155.png)

![alt text](image-156.png)

![alt text](image-157.png)

![alt text](image-158.png)

![alt text](image-159.png)

![alt text](image-160.png)


Batch Effects and Confounders:

![alt text](image-161.png)

![alt text](image-162.png)

![alt text](image-163.png)

![alt text](image-164.png)

![alt text](image-165.png)

![alt text](image-166.png)

![alt text](image-167.png)

![alt text](image-168.png)

Surrogate Variable Analysis (SVA) is a method to identify and estimate hidden sources of variation in high-dimensional data sets. It can be used to identify and adjust for confounding factors in high-dimensional data sets, such as those from microarray or RNA-seq experiments.
![alt text](image-169.png)


Batch Effects in R:

![alt text](image-170.png)

![alt text](image-171.png)

![alt text](image-172.png)

![alt text](image-173.png)

![alt text](image-174.png)

![alt text](image-175.png)

![alt text](image-176.png)

![alt text](image-177.png)

![alt text](image-178.png)

![alt text](image-179.png)

![alt text](image-180.png)



## 3- Modeling Non-continuous Outcomes, Hypothesis Testing, and Multiple Hypothesis Testing

![alt text](image-181.png)

![alt text](image-182.png)


Logistic Regression:

![alt text](image-183.png)

![alt text](image-184.png)

![alt text](image-187.png)

![alt text](image-188.png)

![alt text](image-189.png)

![alt text](image-190.png)

![alt text](image-191.png)

![alt text](image-192.png)


Regression for Counts:

![alt text](image-193.png)

![alt text](image-194.png)

![alt text](image-195.png)

![alt text](image-196.png)

![alt text](image-197.png)

![alt text](image-198.png)

![alt text](image-199.png)

![alt text](image-200.png)


GLMs in R:

![alt text](image-201.png)

![alt text](image-202.png)

![alt text](image-203.png)

![alt text](image-204.png)

![alt text](image-205.png)

![alt text](image-206.png)

![alt text](image-207.png)

![alt text](image-208.png)

![alt text](image-209.png)


Inference:

![alt text](image-210.png)

![alt text](image-211.png)


Null and Alternative Hypotheses:

![alt text](image-212.png)

![alt text](image-213.png)

![alt text](image-214.png)


Calculating statistics:

![alt text](image-215.png)

![alt text](image-216.png)

![alt text](image-217.png)

![alt text](image-218.png)

![alt text](image-219.png)


Comparing Models:

![alt text](image-220.png)

![alt text](image-221.png)

![alt text](image-222.png)

![alt text](image-223.png)

![alt text](image-224.png)

![alt text](image-225.png)

![alt text](image-226.png)

![alt text](image-227.png)


Calculating Statistics in R:

![alt text](image-228.png)

![alt text](image-229.png)







