library(ggplot2)
library(ggthemes)
library(ggthemr)
library(gganimate)
library(dplyr)
library(lubridate)
library(tm)
library(tidytext)
library(qdap)
setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data")
comments = read.csv("comments_labeled.csv")

# select gpu related comments and group by year-month
gpu_related = comments[comments$LABEL == 1,]
gpu_related$published_at = as.Date(gpu_related$published_at)
gpu_related = gpu_related[year(gpu_related$published_at) > 2018,]

comments_by_month = gpu_related %>%
  mutate(ym = format.Date(published_at, '%Y-%m')) %>%
  group_by(ym) %>%
  summarise(comments_by_ym = paste(text, collapse = " "))

# convert to corpus and clean
source = VectorSource(comments_by_month$comments_by_ym)
corpus = VCorpus(source)
corpus

corpus = tm_map(corpus, tolower)
corpus = tm_map(corpus, stemDocument)
corpus = tm_map(corpus, removePunctuation)
for (j in seq(corpus)) {
  corpus[[j]] <- gsub("gpus", "gpu", corpus[[j]])
  corpus[[j]] <- gsub("cpus", "cpu", corpus[[j]])
  corpus[[j]] <- gsub("bought", "buy", corpus[[j]])
  # add space between number and alphabet
  corpus[[j]] <- gsub("([0-9]+)([a-z]+)", "\\1 \\2", corpus[[j]])
  corpus[[j]] <- gsub("([a-z]+)([0-9]+)", "\\1 \\2", corpus[[j]])
}
corpus = tm_map(corpus, removeWords, stopwords("english"))
corpus = tm_map(corpus, removeWords, c("actual", "becaus", "can", "cant", 
                                       "dont", "will",  "even", "just", "one"))
corpus = tm_map(corpus, stripWhitespace)

# declare top words data frame
top_by_ym = data.frame(ym = character(),
                       keyword = character(),
                       freq = numeric(), 
                       rank = integer(),
                       stringsAsFactors=FALSE)

# calculate freq of top 20 words each month
for (i in 1:nrow(comments_by_month)) {
  top20 = freq_terms(corpus[i], top = 20, extend = FALSE,
                     at.least = 3, digit.remove = FALSE)
  colnames(top20) = c('keyword', 'freq')
  top20$freq = top20$freq / top20$freq[1]
  top20$ym = comments_by_month$ym[i]
  top20$rank = 1:length(top20$ym)
  top_by_ym = rbind(top_by_ym, top20)
}

# plot by gganimate
staticplot <- ggplot(top_by_ym, aes(rank,
                             fill = as.factor(keyword),
                             color = as.factor(keyword))) +
  geom_tile(aes(y = freq/2,
                height = freq,
                width = 0.9), alpha = 0.5, color = NA) +
  geom_text(aes(y = 0, label = paste(keyword, " ")), vjust = 0.2, hjust = 1, size = 10) +
  geom_text(aes(y=freq, label = sprintf("%1.3f",freq), hjust=0),size = 5) +
  coord_flip(clip = "off", expand = TRUE) + 
  scale_y_continuous(labels = scales::comma) + 
  scale_x_reverse() +
  theme_minimal() +
  theme(axis.line=element_blank(),
        axis.text.x=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks=element_blank(),
        axis.title.x=element_blank(),
        axis.title.y=element_blank(),
        legend.position="none",
        panel.background=element_blank(),
        panel.border=element_blank(),
        panel.grid.major=element_blank(),
        panel.grid.minor=element_blank(),
        panel.grid.major.x = element_line( size=.1, color="grey" ),
        panel.grid.minor.x = element_line( size=.1, color="grey" ),
        plot.title=element_text(size=25, hjust=0.5, face="bold", colour="grey", vjust=-1),
        plot.background=element_blank(),
        plot.margin = margin(2, 2, 2, 6, "cm"))

anim <- staticplot + transition_states(ym, transition_length = 1, state_length = 1) +
  view_step(pause_length = 3, step_length = 1, fixed_x = TRUE) +
  labs(title = "Top 20 words of GPU-related comments in {closest_state}")

animate(anim, nrow(comments_by_month) * 20, fps = 20, 
        width = 1200, height = 1000,
        renderer = gifski_renderer("../eda/news/barplot.gif"))
