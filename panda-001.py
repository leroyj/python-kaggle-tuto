import pandas as pd
from sklearn.tree  import DecisionTreeRegressor
from sklearn.ensemble  import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

print("** Hello ! **")
dataset_file =  "Melbourne_housing_FULL.csv"
dataset = pd.read_csv(dataset_file)
dataset = dataset.dropna(axis=0)
print("=> Describing dataset")
print (dataset.describe())
print (dataset.columns)

y = dataset['Price']
print("=> Describing target")
print (y.describe())

feature_names = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = dataset[feature_names]
print("=> Describing features")
print (X.describe())

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# my_model = DecisionTreeRegressor(random_state=1)
# my_model.fit(train_X,train_y)
# val_prediction = my_model.predict(val_X)
# print(mean_absolute_error(val_y, val_prediction))

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
    

#my_testset_values=[100,2010,2,4]
#my_testset=pd.DataFrame(my_testset_values,columns=feature_names)
#print("=> My test set")
#print(my_testset)
#my_model.predict(my_testset)
print("***************")
print("** H E L L O **")
print("***************")

my_random_forest_model = RandomForestRegressor(random_state=0)
my_random_forest_model.fit(train_X,train_y)
preds_val = my_random_forest_model.predict(val_X)
mae = mean_absolute_error(val_y, preds_val)
print(mae)


