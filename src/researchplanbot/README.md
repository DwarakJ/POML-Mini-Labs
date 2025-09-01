# Smart Research Plan Generator from Project Options (POML + Azure OpenAI)

This mini-lab creates actionable research plans from a list of project ideas using POML, Python, and Azure OpenAI.

## Features

- Accepts multiple project options from the user
- Uses POML to apply structured, stepwise research planning
- Outputs clear, repeatable research plans with objectives, methods, criteria, and outcomes

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Set your Azure OpenAI credentials:
   ```
   export AZURE_OPENAI_API_KEY=...
   export AZURE_OPENAI_ENDPOINT=...
   export AZURE_OPENAI_DEPLOYMENT=...
   ```
3. Run the generator:
   ```
   python main.py
   ```
4. Enter project options when prompted (type 'END' to finish).

## Example Usage

```
Enter your project options (one per line). Type 'END' to finish:
> Predict equipment failure with sensor data
> Optimize warehouse layout with AI simulation
> Reduce customer churn using behavioral analytics
> END

Generating research plans...

---

### Option 1: Predict equipment failure with sensor data
- **Objectives:** Identify leading indicators of failure...
- **Data/Inputs Needed:** Historical sensor logs...
- **Research Methods:** Time-series analysis, machine learning, pilot deployment...
- **Evaluation Criteria:** Precision/recall of failure prediction, lead time improvement...
- **Expected Outcomes:** Early warning system, reduction in unplanned downtime...

### Option 2: Optimize warehouse layout with AI simulation
...

### Option 3: Reduce customer churn using behavioral analytics
...
```

---

## How POML Helps

- **Templating & Loops:** Dynamically renders research planning steps for any number of project options.
- **Stepwise Instructions:** Ensures structure and repeatability.
- **Output Format:** Guarantees consistent, actionable deliverables.

---

*Extend this project by adding output schemas, more advanced evaluation logic, or integration with project management tools!*