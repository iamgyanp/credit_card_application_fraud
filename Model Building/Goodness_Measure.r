library(dplyr)
library(readxl)
library(xlsx)

train = read_excel("Probabilities for all Models.xlsx", sheet = 'Training')
test = read_excel("Probabilities for all Models.xlsx", sheet = 'Testing')
oot = read_excel("Probabilities for all Models.xlsx", sheet = 'OOT')

train = train[, 1:6]
test = test[, 1:6]
oot = oot[, 1:6]

train = train[sample(nrow(train)),]
test = test[sample(nrow(test)),]
oot = oot[sample(nrow(oot)),]

train_nrows = nrow(train)
test_nrows = nrow(test)
oot_nrows = nrow(oot)
x=oot[0:floor(100*1/oot_nrows),]

for(i in seq(1,25)){
  x[i] = sum(oot[0:floor(0.01*i*oot_nrows),]$fraud)
}


