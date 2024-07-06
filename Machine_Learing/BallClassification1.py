import sklearn

if __name__ == "__main__":
    print("Ball classification case study")

    Features = [[35,"Rough"],
                [45,"Rough"],
                [90,"Smooth"],
                [48,"Rough"],
                [90,"Smooth"],
                [35,"Rough"],
                [92,"Smooth"],
                [35,"Rough"],
                [96,"Smooth"],
                [35,"Rough"]
    ]

    Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis", "Cricket","Tennis", "Cricket","Tennis"]

#Dataset size : 15
#Training size : 10
# Testing size :