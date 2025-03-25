import pandas as pd

# Load the data
df = pd.read_excel('fitness_exercises_final1.xlsx')

# Standardize text fields
df['Primary Muscle Group'] = df['Primary Muscle Group'].str.title()
df['Equipment Required'] = df['Equipment Required'].str.lower()
df['Category'] = df['Category'].str.title()

# Fix common inconsistencies
df['Equipment Required'] = df['Equipment Required'].replace({
    'bodyweight': 'body weight',
    'barbell': 'barbell',
    'dumbbell': 'dumbbell'
})

df['Primary Muscle Group'] = df['Primary Muscle Group'].replace({
    'Abs': 'Rectus Abdominis',
    'Lats': 'Latissimus Dorsi',
    'Delts': 'Deltoids'
})

# Fill empty secondary muscle groups with "None"
df['Secondary Muscle Group'] = df['Secondary Muscle Group'].fillna('None')

# Save cleaned data
df.to_excel('cleaned_fitness_exercises.xlsx', index=False)