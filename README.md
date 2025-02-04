# strava-segment-elevation

A Python script to retrieve elevation and distance data for a specific Strava segment using the Strava API and export the resulting elevation profile as a CSV file.

## Overview

This project fetches **altitude** and **distance** streams for a specified Strava segment and saves them in a CSV file. It is useful for analyzing or visualizing the elevation profile of a segment.

## Features

- Accepts **Strava segment ID as a command-line argument**.
- Fetches **altitude** and **distance** streams for the segment.
- Exports the elevation profile as a **CSV file** (`elevation_profile.csv`).
- Uses **environment variables** (or a `.env` file) for secure API token management.

## Prerequisites

- Python 3.x
- A Strava account with an API application registered to obtain your **Client ID**, **Client Secret**, and **Access Token**.
- The following Python packages:
  - `requests`
  - `python-dotenv`

## Installation

1. **Clone the Repository**  
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
   ```bash
   pip install -r requirements.txt
   ```

   If you don’t have a `requirements.txt` file yet, you can install manually:
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
   Follow the [Strava API documentation](https://developers.strava.com/) to register an application and obtain your access token.

## Usage

### Fetch Elevation Data for a Strava Segment

```bash
python strava_elevation.py <segment_id>
```

Example:
```bash
python strava_elevation.py 30408380
```

### Specify an Output CSV File

By default, the script saves the CSV as `elevation_profile.csv`. To specify a different filename, use the `-o` option:

```bash
python strava_elevation.py 30408380 -o my_segment_data.csv
```

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
