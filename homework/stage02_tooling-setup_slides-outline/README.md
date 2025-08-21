# Dividend Index Strategy and Yield Spread Analysis

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Dividend equity indices are often treated as stable, income-generating investments, but their relative performance is tightly linked to macroeconomic conditions, particularly interest rate movements and yield spreads. When bond yields rise, dividend-paying equities can become less attractive compared to fixed income; conversely, during low-rate environments, dividend indices often outperform as investors search for yield.

This project seeks to quantify the relationship between yield spreads (e.g., 10Y–2Y Treasury spread, credit spreads) and the performance of dividend equity indices. By analyzing historical spread regimes and dividend index returns, the project will identify conditions under which dividend strategies outperform or underperform. The goal is to provide investors and asset managers with a systematic framework to time exposures and manage risk more effectively.

## Stakeholder & User

- **Primary Stakeholder:** Portfolio managers and factor strategy designers at asset management firms.
- **End Users:** Quantitative researchers and investment analysts who need evidence-based tools to evaluate when dividend index allocations are advantageous or risky.

## Useful Answer & Decision

- **Type:** Predictive (forecast future dividend index performance based on spread regimes) & Descriptive (summarize historical spread–return sensitivities).
- **Metrics:** Dividend index excess return forecasts, spread beta coefficients, drawdown probabilities.
- **Artifacts:**
  - Scenario-based dashboard showing expected index performance under different yield curve shapes.
  - Summary reports highlighting stress-test results.
  - Decision trigger guide for overweight/underweight calls.

## Assumptions & Constraints

- Historical spread–return relationships are sufficiently stable to provide predictive value.
- Data is sourced from public and reliable databases (FRED, Bloomberg, MSCI indices).
- Limited access to proprietary transaction-level data; dependent on daily/weekly resolution instead of intraday.
- Compliance restrictions prevent use of certain alternative datasets.

## Known Unknowns / Risks

- Structural changes in monetary policy may reduce the relevance of historical spread–dividend relationships.
- Dividend strategies may behave differently in volatile vs. calm macro environments, introducing non-linearities.
- Sudden policy shocks (e.g., emergency Fed cuts, rapid tightening) could invalidate forecast models in real time.

## Lifecycle Mapping

Goal → Stage → Deliverable

- Define spread metrics and collect index data → Problem Framing & Scoping (Stage 01) → Project plan and scoping document
- Run regression and scenario analysis linking spreads to dividend index returns → Data Processing & Analysis (Stage 02) → Clean dataset and model results
- Build interactive tools and stakeholder memo → Visualization & Reporting (Stage 03) → Dashboard + summary report

## Repo Plan

- `/data/` : Treasury yields, credit spreads, dividend index returns
- `/src/` : Functions for spread calculations, regressions, scenario analysis
- `/notebooks/` : Exploratory data analysis, model testing, visualizations
- `/docs/` : Stakeholder memo, reports, slides for presentation
