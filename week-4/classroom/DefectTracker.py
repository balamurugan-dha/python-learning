import pandas as pd
import numpy as np

defect_ids = np.array(['D1', 'D2', 'D3', 'D4', 'D5'])
modules = np.array(['Login', 'Payment', 'Reports', 'Login', 'Payment'])
severities = np.array(['High', 'Medium', 'Low', 'High', 'Medium'])
statuses = np.array(['Open', 'Closed', 'Open', 'Closed', 'Open'])
df = pd.DataFrame({'DefectID': defect_ids,'Module': modules,'Severity': severities,'Status': statuses})
print("\n", df)

open_defects = df[df['Status'] == "Open"]
print("\nAll Open Defects:\n", open_defects)

high_severity_defects = df[df['Severity'] == "High"]
print("\nAll High Severity Defects:\n", high_severity_defects)

status_counts = df.groupby("Status")["DefectID"].count()
print("\nDefect Count by Status:\n", status_counts)
