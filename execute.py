import src as Script

actual_path = 'data/raw/ChocolateSales.csv'
new_path = 'data/processed/ClonedFile.csv'

df = Script.load_csv(actual_path)

df= Script.clean_data(df,['Sales Person','Date','Amount','Product'])

Script.save_csv(df,new_path)

Script.create_graph(df,'Country','Boxes Shipped')