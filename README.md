# UWAGGS LINHAC 2024
[LINHAC](https://www.ida.liu.se/research/sportsanalytics/LINHAC/LINHAC24/home.html) is an event geared in bringing together the world of hockey analytics. Our team, formed from members of the University of Waterloo Analytics Group for Games and Sports (UWAGGS), analyzed offensive zone possessions to categorize SHL teams within the 2023-24 season based on their offensive-zone playstyle.

## Abstract
Advance scouting is essential to adequately prepare teams for
upcoming contests. Traditional process involve spending copious amounts of time reviewing video and visually identifying key items. To expedite this process and more efficiently guide film study, this work analyzes offensive zone actions to identify and categorize patterns in strategy.

## Keywords
hockey analytics · spatiotemporal data · sports statistics

## Directory Structure
```bash
├── csv_results/
│   ├── data_clustered.csv // Final Averaged & Merged Team Metrics & Associated Clusters
    ├── ozone_averages.csv // Initial O-zone Averaged Metrics
    ├── summary_stat_by_cluster.csv // Final Averaged & Merged Cluster Metrics
├── eda/
    ├── outputs/
        ├── plot.png // Initial EDA Heatmap for passes
        ├── plot2.png // Initial EDA Heatmap for pass vectors
    ├── eda.ipynb // Exploratory Data Analysis for O-Zone event sequences
    ├── hockey_rink.png // Image needed to create heatmap in EDA
    ├── Ice_hockey_layout.svg // Image needed to create heatmap in EDA
    ├── summarizedLINHAC2024Data.csv // Summarized O-Zone Data about in-depth shot quality
├── final_scripts/
    ├── linhac_clustering.Rmd // R Markdown script used to generate clusters
    ├── LinHac.Rmd // R Markdown script to generate aggregated o-zone metrics for time and passes between shots
    ├── ozone_dequence_mapping.py // Python script to generate aggregated o-zone metrics for shot quality, positive o-zone events, etc.
    ├── tables.R // R script to generate table graphics for final paper
├── .gitignore // Miscellaneous
├── LICENSE // Miscellaneous
├── README.md // Miscellaneous
├── requirements.txt // Miscellaneous
├── UWAGGS_LINHAC2024.pdf // Final Paper
```

## Adding to the repo
Feel free to put your own work in a branch like so `eda/<your-name>`
