import pandas as pd

df = pd.DataFrame({"Name":["John" , "James" , "Alex" , "Andrew" , "Sara", "Albert"] ,
                   "Age" :["20" , "30" , "23" , "13" , '42' , "12"] ,
                   "Country": ["USA" , "Canada" , "Brazil" , "Argentina" , "Australia" , "England"]})

df.to_excel(excel_writer="names_data.xlsx",
            columns=['Name' , 'Age' , 'Country'],
            header=True,
            index=True,
            index_label='Index',
            startrow=0,
            startcol=0,
            )