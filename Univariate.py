class Univariate():
   def QuanQual(dataset, option):
    quan = []
    qual = []

    for ColumnName in dataset.columns:
        
        if dataset[ColumnName].dtype == bool:
            qual.append(ColumnName)

        elif dataset[ColumnName].nunique() == 2:
            qual.append(ColumnName)

        elif dataset[ColumnName].nunique() == len(dataset):
            qual.append(ColumnName)

        else:
            quan.append(ColumnName)

    if option == "quan":
        return quan
    elif option == "qual":
        return qual
    else:
        return "Please choose either 'quan' or 'qual'"