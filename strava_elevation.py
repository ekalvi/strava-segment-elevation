import os
import csv
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file if present.
load_dotenv()


def get_segment_elevation(segment_id, access_token):
    """
    Retrieve the altitude and distance streams for the given segment.

    Parameters:
        segment_id (str): The ID of the Strava segment.
        access_token (str): Your Strava API OAuth access token.

    Returns:
        tuple: (distance_data, altitude_data) as lists, or (None, None) if the request fails.
    """
    url = f"https://www.strava.com/api/v3/segments/{segment_id}/streams"
    params = {
        "keys": "altitude,distance",
        "resolution": "medium"  # Options: 'low', 'medium', or 'high'
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}\n{response.text}")
        return None, None

    streams = response.json()
    altitude_data = None
    distance_data = None

    for stream in streams:
        if stream.get("type") == "altitude":
            altitude_data = stream.get("data")
        elif stream.get("type") == "distance":
            distance_data = stream.get("data")

    if altitude_data is None:
        print("Altitude data not found in the response.")
    if distance_data is None:
        print("Distance data not found in the response.")

    return distance_data, altitude_data


def write_elevation_csv(distance, altitude, output_filename):
    """
    Write the elevation profile to a CSV file.

    Parameters:
        distance (list): List of distance values.
        altitude (list): List of altitude values.
        output_filename (str): Name of the CSV file to write.
    """
    # Ensure the lists are of the same length.
    if len(distance) != len(altitude):
        print("Warning: The distance and altitude data have different lengths.")

    with open(output_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Write header row
        writer.writerow(["distance_m", "altitude_m"])

        # Write each row as a pairing of distance and altitude
        for d, a in zip(distance, altitude):
            writer.writerow([d, a])

    print(f"Elevation profile saved to {output_filename}")


if __name__ == "__main__":
    # The segment ID for which you want to retrieve elevation data.
    SEGMENT_ID = "30408380"

    # Retrieve your Strava access token from an environment variable.
    ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")
    if not ACCESS_TOKEN:
        print("Please set the STRAVA_ACCESS_TOKEN environment variable.")
        exit(1)

    distance, altitude = get_segment_elevation(SEGMENT_ID, ACCESS_TOKEN)

    if distance and altitude:
        output_csv = "elevation_profile.csv"
        write_elevation_csv(distance, altitude, output_csv)
    else:
        print("Failed to retrieve elevation data.")
