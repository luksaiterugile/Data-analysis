library("RWeka")

initial_data <- read.arff("D:/IV_Semestras/Duomenų tyrimas/2 užduotis/kidney_disease_nominal.arff")
frequencies <- table(initial_data[,7])

train_data <-  read.arff("D:/IV_Semestras/Duomenų tyrimas/2 užduotis/kidney_disease_train_set.arff")
frequencies_2 <- table(train_data[,7])

test_data <- read.arff("D:/IV_Semestras/Duomenų tyrimas/2 užduotis/kidney_disease_test_set.arff")
frequencies_3 <- table(test_data[,7])

proportion <- as.vector(frequencies)
proportion_2 <- as.vector(frequencies_2)
proportion_3 <- as.vector(frequencies_3)

sickproportion <- proportion[1]/proportion[2]
sickproportion_2 <- proportion_2[1]/proportion_2[2]
sickproportion_3 <- proportion_3[1]/proportion_3[2]
