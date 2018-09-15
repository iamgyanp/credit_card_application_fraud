library(dplyr)
library(lubridate)

#upload cleaned dataset
df <- read.csv("new_applications.csv")

#create unique identifier by combining first name, last name, and ssn

ID = paste0(df$firstname,"_", df$lastname)
df$ID = paste0(ID, "_", df$newssn)


#Create time intervals
df$appdate = mdy(df$appdate)

df$Day <- yday(df$appdate)


ceiling(3.2)

df$groupThree = ceiling(df$Day/3)
df$groupTwo = ceiling(df$Day/2)
df$groupFive = ceiling(df$Day/5)
df$groupOne = df$Day


#create expert variables by ssn and time interval

ssnOne = df %>% group_by(groupOne,newssn) %>% summarize(count=n()) %>% arrange(desc(count))

ssnTwo = df %>% group_by(groupTwo,newssn) %>% summarize(count=n()) %>% arrange(desc(count))

ssnThree = df %>% group_by(groupThree,newssn) %>% summarize(count=n()) %>% arrange(desc(count))

ssnFive = df %>% group_by(groupFive,newssn) %>% summarize(count=n()) %>% arrange(desc(count))



#Create expert variables by phone and time interval

phoneOne = df %>% group_by(groupOne,homephone) %>% summarize(count=n()) %>% arrange(desc(count))

phoneTwo = df %>% group_by(groupTwo,homephone) %>% summarize(count=n()) %>% arrange(desc(count))

phoneThree = df %>% group_by(groupThree,homephone) %>% summarize(count=n()) %>% arrange(desc(count))

phoneFive = df %>% group_by(groupFive,homephone) %>% summarize(count=n()) %>% arrange(desc(count))


#Create expert variables by zip and time interval

zipOne = df %>% group_by(groupOne,zip5) %>% summarize(count=n()) %>% arrange(desc(count))

zipTwo = df %>% group_by(groupTwo,zip5) %>% summarize(count=n()) %>% arrange(desc(count))

zipThree = df %>% group_by(groupThree,zip5) %>% summarize(count=n()) %>% arrange(desc(count))

zipFive = df %>% group_by(groupFive,zip5) %>% summarize(count=n()) %>% arrange(desc(count))


#Create expert variables by address and time interval

addressOne = df %>% group_by(groupOne,address) %>% summarize(count=n()) %>% arrange(desc(count))

addressTwo = df %>% group_by(groupTwo,address) %>% summarize(count=n()) %>% arrange(desc(count))

addressThree = df %>% group_by(groupThree,address) %>% summarize(count=n()) %>% arrange(desc(count))

addressFive = df %>% group_by(groupFive,address) %>% summarize(count=n()) %>% arrange(desc(count))


