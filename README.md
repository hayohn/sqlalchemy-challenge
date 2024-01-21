# Climate App README

This is a Flask API for climate analysis and data exploration. It provides several routes to retrieve climate data and statistics.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python (version 3.x recommended)
- Flask
- SQLAlchemy
- Pandas
- Matplotlib

### Installation

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/yourusername/climate-app.git
   cd climate-app

### Routes

/api/v1.0/precipitation: Retrieve precipitation data for the last 12 months.
/api/v1.0/stations: Retrieve a JSON list of stations.
/api/v1.0/tobs: Retrieve dates and temperature observations for the most active station in the last 12 months.
/api/v1.0/<start>: Retrieve TMIN, TAVG, and TMAX for dates greater than or equal to the specified start date.
/api/v1.0/<start>/<end>: Retrieve TMIN, TAVG, and TMAX for the dates from the start date to the end date (inclusive).
Replace <start> and <end> with actual dates in the format 'YYYY-MM-DD'.

### Testing

To test the routes, use your web browser, or curl commands. Ensure the Flask app is running during testing.

### Author 
Haya Abu Sharar
