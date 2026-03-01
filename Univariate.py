class Univariate():
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for ColumnName in dataset.columns:
            print(ColumnName)
            if (dataset[ColumnName].dtype==bool):
                qual.append(ColumnName)
            elif (dataset[ColumnName].nunique()== 2):
                qual.append(ColumnName)
            elif (dataset[ColumnName].nunique()==len(dataset)):
                qual.append(ColumnName)
            else:
                quan.append(ColumnName)
    
        return quan,qual
        