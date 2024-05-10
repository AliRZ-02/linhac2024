library(gt)
library(readr)
library(dplyr)
library(tibble)
library(stringr)
average_stats <- read_csv("summary_stat_by_cluster.csv", col_select = -1, show_col_types = F)

as.data.frame(t(average_stats[,-1])) %>% 
  rownames_to_column("metric") %>% 
  mutate(metric = str_remove(metric, "mean_")
         # metric = case_match(
         #   "time" ~ "Offensive Zone Time",
         #   "time" ~ "Offensive Zone",
         #   "cmltv_xG" ~ "Cumulative xG",
         #   .default = metric,
         #   
         # )
         
  ) %>% 
  relocate(V4, .before = V5) %>% 
  gt() %>% 
  fmt_number(decimals = 3) %>% 
  data_color(
    columns = -metric,
    direction = "row",
    colors = scales::col_numeric(
      #palette = c("white", "orange", "red"), 
      colorspace::diverge_hcl(n = 9, palette = "Blue-Red 3"),
      domain = NULL)
  ) %>% 
  cols_label_with(fn = ~str_replace(.x, "V", "Cluster ")) %>% 
  cols_label(metric = "Metric (mean)", V4 = "Cluster 5", V5 = "Cluster 4") %>% 
  cols_move(V4, after = V5) %>% 
  tab_header("Mean Metric Values for Each Cluster") 
