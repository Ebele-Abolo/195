diabetic_patient = df.loc[df['diabetes'] == 1]
groupby_age_diabetes= diabetic_patient.groupby('age')['diabetes'].count().reset_index()
new _df = df.loc[(df[‘marks’] <30 ) | (df[‘marks’] >60 ) ]