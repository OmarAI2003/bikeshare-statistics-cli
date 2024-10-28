# Bikeshare Statistics CLI App(August 2022)

I did this in 2022 when I started to learn about python.

Welcome to the Bikeshare Statistics CLI App! This application allows users to explore and analyze bikeshare data from three major US cities: Chicago, New York City, and Washington.

## Table of Contents

- [Bikeshare Statistics CLI App(August 2022)](#bikeshare-statistics-cli-appaugust-2022)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Clone the repository](#clone-the-repository)
    - [Install required libraries](#install-required-libraries)
  - [Usage](#usage)
  - [Statistics Computed](#statistics-computed)
  - [Data Files](#data-files)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Interactive command-line interface for easy data exploration
- Provides various descriptive statistics related to bikeshare usage
- Filters data by city, month, and day of the week
- Displays raw data upon user request

## Getting Started

To get started with this project, you will need Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the repository

You can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/OmarAI2003/bikeshare-statistics-cli.git
```

### Install required libraries

This project uses built-in Python libraries, so no additional installations are necessary. However, ensure you have Pandas and Numpy installed for data manipulation. You can install it via pip:

```bash
pip install pandas
pip install numpy
```

## Usage

To run the application, navigate to the project directory and execute the following command in your terminal:

```bash
python bikeshare.py
```

Follow the prompts to select the city, month, and day of the week you want to analyze. Here's an example of running the application:

```plaintext
Hello! Let's explore some US bikeshare data!
Enter the city name you would like to see data for (ch, ny, or w):

w

To filter data by a chosen month type a month or 'all' for no filtering by a month:

january
february
march
april
may
june
all

April
Type a weekday you want to filter the data by or the string 'All' for no filtering by days:

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
All

Monday
----------------------------------------

Calculating The Most Frequent Times of Travel...

the most common month in the dataset is:  4
The most common day that people travel in this dataset is: Monday
The most common hour that people start to travel in this dataset is: 7

This took 0.019 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

the most start station people usually use is: Columbus Circle / Union Station
the most end station people usually use is: Jefferson Dr & 14th St SW
most travel that usually occurs is between: Jefferson Dr & 14th St SW----Jefferson Dr & 14th St SW

This took 0.012 seconds.
----------------------------------------

Calculating Trip Duration...

The total travel time for this dataset is about: 8613095.0
The average travel time for this dataset is about: 8613095.0

This took 0.0005 seconds.
----------------------------------------

Raw data is available to check it.

If you want to see the available raw data in scraps of 5 rows type: Yes
No

Fleeing...

Would you like to restart? Enter yes or no.
```

## Statistics Computed

The application computes the following statistics:

1. **Popular times of travel**
   - Most common month
   - Most common day of the week
   - Most common hour of day
2. **Popular stations and trip**
   - Most common start station
   - Most common end station
   - Most common trip from start to end
3. **Trip duration**
   - Total travel time
   - Average travel time
4. **User info**
   - Counts of each user type
   - Counts of each gender (only available for NYC and Chicago)
   - Earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Data Files

To answer the above questions using Python for the three cities, the following CSV files are required:

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

These files should be placed in the same directory as the `bikeshare.py` file.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to customize any sections as needed or add any additional information specific to your project!