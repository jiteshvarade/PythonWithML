from sklearn import tree

#Rough = 1
#Smooth = 0

#Tennis = 1
#Crickte = 2

if __name__ == "__main__":
    print("Ball classification case study")

    # Feature Enconding
    Features = [[35,1],
                [45,1],
                [90,0],
                [48,1],
                [90,0],
                [35,1],
                [92,0],
                [35,1],
                [96,0],
                [35,1]
    ]

    #Label Encoding
    Labels = [1,1,2,1,2,1, 2,1, 2,1]

    # Decide the algorithm
    obj = tree.DecisionTreeClassifier()

    #Train the model
    obj = obj.fit(Features, Labels) # used to train the model

    #Test the model
    print(obj.predict([[10,1]]))

#Dataset size : 15
#Training size : 10
# Testing size :