# The following functions will:
#  - Manipulate the data to find the 5%, 50% and 95% intervals of the given variable at
#  each time point
#  - Plot the data with a ribbon

import seaborn as sb

# defining function for data manipulation
def med_data(data, ID, Var):
    """
    Computes the 5th, 50th (median), and 95th quantile of the Var column of data per the ID column.
    
    data:  pandas DataFrame object containing
    ID  :  name of a column in the data to group by
    Var :  name of a column in the data to aggregate on
    """
    # summarise data
  data = data[["ID", "Var"]].groupby(ID).quantile(q = [0.05, 0.5, 0.95])
    
    # reset index and name columns
    data = data.reset_index().rename(columns={ID : "ID", "level_1" : "Quantile", Var : "Var"})
    
    # make quantile categorical
    data["quantile"] = data["quantile"].astype("category")
        
    return(data)
    
# defining function for plotting
def plot_med_data(med_data):
    """
    Takes data outputted from med_data and plots it
    
    med_data:  output from function med_data (i.e. data with columns ID, Quantile, Var)
    """
    sns.lineplot(x=ID, y=Var, data=med_data)

# running functions on data
flights = sns.load_dataset("flights")
data = med_data(data=flights, ID="year", Var="passengers")
plot_med_data(data)