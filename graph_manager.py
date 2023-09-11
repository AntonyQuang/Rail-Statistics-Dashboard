explanations = {"Key statistics": """**Number of full-time equivalent (FTE) employees** is calculated by comparing an 
employee’s average number of hours worked to the average hours of a full-time worker. 

**Number of stations managed** only includes stations called at by a mainline train service as of 31 March. Stations 
which have been permanently closed or where mainline services have ceased indefinitely are not included. 

**Route kilometres operated** includes the total extent of route available to operate on as of 31 March. It does not take 
into account multiple track routes (i.e. double tracks are only counted as one route kilometre but would be two track 
kilometres).""",
                "Passenger rail usage": """**Passenger journeys** are estimated based on travel from an origin 
                station to a destination station. Where travel includes one or more changes of train, each train used 
                is counted as one journey.

**Passenger kilometres** are calculated by multiplying the number of passenger journeys on a particular flow by the number of corresponding track kilometres between 
stations.

**Passenger train kilometres** refers to the number of train kilometres travelled by 
revenue earning passenger trains.""",

                "Passenger rail performance": """**On Time** is the percentage of recorded station stops that were early or 
                                               less than one minute after the scheduled arrival time.

**The Cancellations score** is the percentage of trains planned that were 
                                               cancelled, whereby full cancellations are counted as one and part 
                                               cancellations as half.

**The number of trains planned** is based on the daily schedule as agreed 
                                               between the train operator and Network Rail at 22:00 on the previous 
                                               evening.""",
                "Passenger rail delays": """**Delay minutes** are defined as the time lost between consecutive timing points"
                                          on the rail network. Delay incidents producing three or more minutes of 
                                          delay on Britain’s railways are attributed to either Network Rail or a 
                                          train operator.


There are three types of responsibility category:

**NR-on-TOC** are delays attributed to Network Rail affecting train operating 
                                          companies (e.g. Track, Network management, etc.).

**TOC-on-Self** are delays attributed to train operating companies affecting 
                                          their own train operating company (e.g. their own fleet, train crew, 
                                          etc.).

**TOC-on-TOC** are delays attributed to train operating companies affecting 
                                          other train operating companies (e.g. another operator’s fleet, train crew, 
                                          etc.).""",
                "Passenger experience":
                    """**Complaints** are defined as ‘any expression of dissatisfaction by a customer or 
                    potential customer about service delivery or about company or industry 
                    policy’.

**Passenger assists** data shows the number of assists that have been requested 
                    through the National Passenger Assistance Booking System (unbooked assistance 
                    such as ‘Turn Up and Go’ assists is not included).

**Delay compensation claims closed** refers to volume of claims closed when the 
                    train operator issues payment for a successful claim or when the passenger 
                    was informed that their claim was rejected. """
                }


all_tocs_mean_graphs = ["Cancellations score (percentage)", "On Time (percentage)"]

graph_types = {
    "Full-time equivalent (FTE) employees": "line",
    "Number of stations managed": "bar",
    "Passenger journeys (millions)": "line",
    "Passenger kilometres (millions)": "line",
    "Passenger train kilometres (millions)": "bar",
    "Route kilometres operated": "bar",
    "Complaints closed": "bar",
    "Passenger assists": "bar",
    "Cancellations score (percentage)": "line",
    "Trains planned": "bar",
    "On Time (percentage)": "line",
    "Network Rail on TOC delays (minutes)": "bar",
    "TOC on self delays (minutes)": "bar",
    "TOC on TOC delays (minutes)": "bar",
    "Delay compensation claims closed": "line"
}

graph_colours = {
    "Full-time equivalent (FTE) employees": "DodgerBlue",
    "Number of stations managed": "gnbu",
    "Passenger journeys (millions)": "SeaGreen",
    "Passenger kilometres (millions)": "RosyBrown",
    "Passenger train kilometres (millions)": "aggrnyl",
    "Route kilometres operated": "gnbu",
    "Complaints closed": "dense",
    "Passenger assists": "dense",
    "Cancellations score (percentage)": "coral",
    "Trains planned": "agsunset",
    "On Time (percentage)": "DarkSalmon",
    "Network Rail on TOC delays (minutes)": "fall",
    "TOC on self delays (minutes)": "fall",
    "TOC on TOC delays (minutes)": "fall",
    "Delay compensation claims closed": "RebeccaPurple"
}
