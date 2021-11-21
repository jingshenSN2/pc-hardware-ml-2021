library(dplyr)
library(ggplot2)
library(ggthemes)
library(psych)
library(caTools)
library(e1071)
library(tidyverse)
library(caret)
library(cvms)

train <- read.csv("drive_train_labeled.csv")
test <- read.csv("drive_test.csv")
head(train) %>% knitr::kable(digits = 3)

y.train <- train$CHIA_IMPACT
table(y.train)
# y.test <- test$CHIA_IMPACT

X.train <- train %>% select(-c(CHIA_IMPACT, asin, product))
X.test <- test %>% select(-c(CHIA_IMPACT, asin, product))


nb.model <- naiveBayes(X.train, y.train)
y.pred.nb <- predict(nb.model, X.train)
plot_confusion_matrix(confusion_matrix(y.train, y.pred.nb),
                      add_row_percentages = FALSE,
                      add_col_percentages = FALSE,
                      rm_zero_percentages = FALSE,
                      rm_zero_text = FALSE,
                      add_zero_shading = TRUE,
                      counts_on_top = TRUE) +
  labs(title = "Training Set Confusion Matrix of Naive Bayes")
ggsave("nb_train.png", height = 6, width = 6)


ggsave("nb_test.png", height = 6, width = 6)

test$CHIA_IMPACT = predict(nb.model, X.test)
table(test$CHIA_IMPACT)
# CHIA_IMPACT
# 0   1 
# 81 175 

ggplot(test) +
  geom_jitter(aes(x=drive_subtype, y=drive_type, color = CHIA_IMPACT),
              width = 0.25, height = 0.25, alpha = 0.6) +
  theme_economist_white() +
  theme(axis.text.y = element_text(angle=90)) + 
  labs(title = "Chia Impact in different drive type",
       subtitle = "Predicted by Naive Bayes",
       x = "Drive SubType",
       y = "Drive Type")
ggsave("nb_drive_type.png", height = 6, width = 8)

ggplot(test) +
  geom_jitter(aes(x=brand, y=drive_type, color = CHIA_IMPACT),
              width = 0.25, height = 0.25, alpha = 0.6) +
  theme_economist_white() +
  theme(axis.text.y = element_text(angle=90),
        axis.text.x = element_text(angle=90)) + 
  labs(title = "Chia Impact in different drive type and brand",
       subtitle = "Predicted by Naive Bayes",
       x = "Drive Brand",
       y = "Drive Type")
ggsave("nb_drive_brand.png", height = 6, width = 8)

write.csv(test, "drive_test_nb.csv", row.names = F)

ggplot(test) +
  geom_density(aes(x=base_price/100, fill=CHIA_IMPACT), alpha = 0.6) +
  theme_economist_white() +
  theme(axis.text.y = element_text(angle=90)) + 
  labs(title = "Price Density Plot over CHIA_IMPACT",
       subtitle = "Predicted by Naive Bayes",
       x = "Drive Price($) at Jan 2021")
ggsave("nb_drive_price.png", height = 6, width = 8)

capacity <- test$capacity
capacity_c <- case_when(
  capacity %in% c("500gb") ~ "512gb",
  capacity %in% c("2tb", "3tb") ~ "2tb",
  capacity %in% c("4tb", "5tb", "6tb") ~ "4tb",
  capacity %in% c("10tb", "12tb", "14tb", "16tb", "18tb") ~ "10tb+",
  TRUE ~ capacity
)
capacity_c <- factor(capacity_c, levels = c("128gb", "256gb", "512gb",
                                            "1tb", "2tb", "4tb",
                                            "8tb", "10tb+"))

ggplot(test) +
  geom_bar(aes(x=capacity_c, fill=CHIA_IMPACT)) +
  theme_economist_white() +
  labs(title = "Capacity Count Plot over CHIA_IMPACT",
       subtitle = "Predicted by Naive Bayes",
       x = "Drive Capacity")
ggsave("nb_drive_cap.png", height = 6, width = 8)

with(test, table(CHIA_IMPACT, drive_type))
with(test, chisq.test(CHIA_IMPACT, drive_type))
# drive_type
# CHIA_IMPACT hdd ssd
# 0  19  62
# 1  71 104
# 
# Pearson's Chi-squared test with Yates' continuity correction
# 
# data:  CHIA_IMPACT and drive_type
# X-squared = 6.3836, df = 1, p-value = 0.01152

with(test, table(CHIA_IMPACT, drive_subtype))
with(test, chisq.test(CHIA_IMPACT, drive_subtype))
# drive_subtype
# CHIA_IMPACT 25 35 m2 nvme sata
# 0  3 16  3   35   24
# 1  7 64 16   24   64
# 
# Pearson's Chi-squared test
# 
# data:  CHIA_IMPACT and drive_subtype
# X-squared = 28.91, df = 4, p-value = 8.155e-06

X.train$brand <- factor(X.train$brand)
X.train$drive_type <- factor(X.train$drive_type)
X.train$drive_subtype <- factor(X.train$drive_subtype)
X.train$capacity <- factor(X.train$capacity)

Grid <- data.frame(usekernel=TRUE,laplace = 1,adjust=1)
mdl <- train(X.train, factor(y.train), method="naive_bayes",
             trControl=trainControl(method="none"),
             tuneGrid=Grid)

varImp(mdl)
