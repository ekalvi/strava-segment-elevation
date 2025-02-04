
# strava-segment-elevation

A Python script to retrieve elevation and distance data for a specific Strava segment using the Strava API and export the resulting elevation profile as a CSV file.

## Overview

This project uses the Strava API to fetch stream data (distance and altitude) for a given segment and writes the data to a CSV file. It is useful for anyone looking to analyze or visualize the elevation profile of a Strava segment.

## Features

- Fetches **altitude** and **distance** streams for a Strava segment.
- Exports the elevation profile as a CSV file (`elevation_profile.csv`).
- Uses environment variables (or a `.env` file) for secure configuration of your Strava access token.

## Prerequisites

- Python 3.x
- A Strava account with an API application registered to obtain your **Client ID**, **Client Secret**, and **Access Token**.
- The following Python packages:
  - `requests`
  - `python-dotenv`

## Installation

1. **Clone the Repository**  
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/strava-segment-elevation.git
   cd strava-segment-elevation
   ```

2. **Set Up a Virtual Environment (Optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   If you have a `requirements.txt` file, run:

   ```bash
   pip install -r requirements.txt
   ```

   Otherwise, install manually:

   ```bash
   pip install requests python-dotenv
   ```

## Configuration

1. **Create a `.env` File**  
   In the project root directory, create a file named `.env` and add your Strava access token:

   ```ini
   STRAVA_ACCESS_TOKEN=your_actual_access_token_here
   ```

2. **Obtain Your Access Token**  
   Follow the [Strava API documentation](https://developers.strava.com/) to register an application and obtain your access token through the OAuth process.

## Usage

1. **Edit the Segment ID (Optional)**  
   The default segment ID is set to `30408380` in the script. Edit the `SEGMENT_ID` variable in the script if you wish to fetch data for another segment.

2. **Run the Script**

   ```bash
   python strava_elevation.py
   ```

   If everything is configured correctly, the script will fetch the elevation data and write it to a CSV file named `elevation_profile.csv`.

## Troubleshooting

- **Environment Variable Not Found**  
  Ensure that the `.env` file is in the same directory as your script and that you have installed `python-dotenv` to load the environment variables.
  
- **API Errors**  
  Check your Strava access token and ensure your OAuth application has the necessary permissions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Strava API Documentation](https://developers.strava.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Requests Library](https://pypi.org/project/requests/)
```
