import numpy as np
import pandas as pd

raw_key_stats_data = pd.read_excel("./data/2200_key_statistics_by_operator.ods", "2200_Key_statistics_by_operator",
                                   engine="odf")
raw_key_stats_data_2 = pd.read_excel("./data/table-2200_key_statistics_by_operator_2.ods",
                                     "2200_Key_statistics_by_operator",
                                     engine="odf")

raw_datasets = [raw_key_stats_data, raw_key_stats_data_2]
for dataset in raw_datasets:
    dataset.columns = dataset.iloc[4]
    dataset = dataset.drop(dataset.index[0:5])
    dataset = dataset.replace(to_replace=r"\[r]", value=None, regex=True)
    dataset = dataset.replace(to_replace=r"\[b]", value=None, regex=True)
    dataset = dataset.replace(to_replace=r"\[z]", value=None, regex=True)
    dataset = dataset.replace(to_replace=r"\[x]", value=None, regex=True)
raw_data = pd.concat(raw_datasets)
raw_data = raw_data.rename_axis(None, axis=1)

raw_data = raw_data[raw_data["Measure"] != "Measure"]
raw_data = raw_data.dropna(subset=['Measure'])

raw_data["Measure"] = raw_data["Measure"].replace({
    "Delays-NR-on-TOC": "Network Rail on TOC delays (minutes)",
    "Delays-TOC-on-Self": "TOC on self delays (minutes)",
    "Delays-TOC-on-TOC": "TOC on TOC delays (minutes)",
    "On Time": "On Time (percentage)",
},
    regex=True)

raw_data["Measure"] = raw_data["Measure"].replace({
    "On Time \(percentage\) \(percentage\)": "On Time (percentage)",
},
    regex=True)

raw_data["Measure"] = raw_data["Measure"].replace({
    r"On Time \[.*\]": "",
},
    regex=True)

raw_data = raw_data.replace({r" \[.*\]": "", r"\[.*]": np.nan, r"As at": "As of"}, regex=True)

raw_data = raw_data.rename(columns={"Lumo [note 1]": "Lumo", "TfL Rail": "Elizabeth line 1"})
raw_data["Elizabeth line"] = raw_data["Elizabeth line 1"].fillna(raw_data["Elizabeth line [note 2]"])
raw_data = raw_data.drop(columns=['Elizabeth line 1', 'Elizabeth line [note 2]'])
raw_data["Time period"] = raw_data["Time period"].str.strip()

data_tables = {}
for measure in raw_data["Measure"].value_counts().index:
    data_tables[measure] = raw_data[raw_data["Measure"] == measure]
    data_tables[measure] = data_tables[measure].drop_duplicates("Time period", keep="last").reset_index(drop=True)
    data_tables[measure] = data_tables[measure].drop('Measure', axis=1)
    data_tables[measure] = data_tables[measure].set_index("Time period")
    data_tables[measure] = data_tables[measure].reindex(sorted(data_tables[measure].columns, key=str.lower), axis=1)

table_headings = ["Full-time equivalent (FTE) employees", "Number of stations managed",
                  "Passenger journeys (millions)", "Passenger kilometres (millions)",
                  "Passenger train kilometres (millions)", "Route kilometres operated",
                  "Complaints closed", "Passenger assists",
                  "Cancellations score (percentage)", "Trains planned",
                  "On Time (percentage)", "Network Rail on TOC delays (minutes)",
                  "TOC on self delays (minutes)", "TOC on TOC delays (minutes)",
                  "Delay compensation claims closed"]

table_sub_headings = {"Key statistics": ["Full-time equivalent (FTE) employees",
                                         "Number of stations managed",
                                         "Route kilometres operated"
                                         ],
                      "Passenger rail usage": ["Passenger journeys (millions)",
                                               "Passenger kilometres (millions)",
                                               "Passenger train kilometres (millions)"
                                               ],
                      "Passenger rail performance": ["Cancellations score (percentage)",
                                                     "Trains planned",
                                                     "On Time (percentage)"
                                                     ],
                      "Passenger rail delays": ["TOC on self delays (minutes)",
                                                "TOC on TOC delays (minutes)",
                                                "TOC on self delays (minutes)"
                                                ],
                      "Passenger experience": ["Delay compensation claims closed",
                                               "Complaints closed",
                                               "Passenger assists",
                                               ]
                      }


toc_list = sorted(raw_data.columns.tolist()[2:], key=str.lower)
toc_list.insert(0, "All TOC's")
