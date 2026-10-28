
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataQualityPreset

# Sample reference data
reference_data = pd.DataFrame({
    "age": [22, 25, 30, 28, 35],
    "salary": [25000, 30000, 45000, 40000, 50000]
})

# New data received by the application
current_data = pd.DataFrame({
    "age": [23, 26, 31, 29, 36],
    "salary": [26000, 31000, 46000, 41000, 51000]
})

# Generate a data quality report
report = Report(metrics=[
    DataQualityPreset()
])

report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save the report as an HTML file
report.save_html("data_quality_report.html")

print("Data quality report generated successfully!")
