# Import your libraries
import pandas as pd

# Start writing code
worker
title

df1 = pd.merge(worker, title, how = 'left', left_on = 'worker_id', right_on = 'worker_ref_id').sort_values('salary', ascending = False)

df2 = df1.query('salary == salary.max()')['worker_title']
df1[df1.salary == df1.salary.max()]['worker_title']
