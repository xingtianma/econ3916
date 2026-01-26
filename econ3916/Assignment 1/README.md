# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem  
Official inflation metrics like the Consumer Price Index (CPI) are designed to represent the “average” household, but this average often fails to capture the lived experience of students. Students spend a much larger share of their income on tuition, rent, and food away from home—categories that have historically increased faster than overall inflation—causing official CPI to understate student cost-of-living pressures.

## Methodology  
This project uses Python and the FRED API to collect CPI component data that serve as proxies for student-relevant expenses, including tuition, rent, food away from home, and streaming services. All series are normalized to a common base year (2016 = 100) to avoid misleading comparisons caused by different CPI base years. A custom **Student Spending Price Index (Student SPI)** is then constructed using a weighted Laspeyres-style index to reflect a student-specific consumption basket rather than the national average.

## Key Findings  
The analysis reveals a clear divergence between student inflation and official CPI over time. The Student SPI increases faster than national inflation, driven primarily by housing and education costs, indicating that students experience meaningfully higher effective inflation than what headline CPI suggests.
