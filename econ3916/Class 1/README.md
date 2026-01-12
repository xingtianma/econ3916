\## 🌍 Global Purchasing Power Parity Analysis via the Big Mac Index

### Objective
This project evaluates the **Law of One Price** by using the Big Mac Index as an informal measure of **Purchasing Power Parity (PPP)**, assessing whether identical goods cost the same across countries once prices are expressed in a common currency.

---

### Methodology
- Constructed a cross-country dataset using **The Economist’s 2015 Big Mac Index**, manually encoding price data to reinforce data-structuring fundamentals.
- Calculated **implied PPP exchange rates** by comparing local Big Mac prices to the U.S. benchmark.
- Measured **currency misalignment** by computing the percentage deviation between implied PPP rates and observed market exchange rates.
- Interpreted results through an economic lens, emphasizing price dispersion, market frictions, and deviations from arbitrage conditions.

---

### Key Findings
The analysis reveals substantial deviations from Purchasing Power Parity across countries, indicating that many currencies are either **overvalued or undervalued** relative to the U.S. dollar. These misalignments suggest the presence of **transaction costs, non-tradable inputs, and market rigidities** that prevent full arbitrage and violate the Law of One Price in practice. Overall, the findings reinforce the view that PPP is a useful long-run benchmark but an imperfect predictor of short-run exchange rates.

---

### Tools & Concepts
- Economic theory: Law of One Price, Purchasing Power Parity, arbitrage
- Data analysis: structured data ingestion, ratio-based metrics, percentage deviations
- Libraries: Python, Pandas
