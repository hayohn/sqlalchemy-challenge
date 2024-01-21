from flask import Flask, jsonify
import datetime as dt
app = Flask(__name__)
def home():
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify({"example": "precipitation_data"})

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    return jsonify({"example": "station_data"})

# Define the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify({"example": "temperature_data"})

# Define the start date route
@app.route("/api/v1.0/start_date")
def start_date():
    return jsonify({"example": "data_from_start_date"})

@app.route("/api/v1.0/start_date/end_date")
def start_end_date():
    return jsonify({"example": "data_from_start_to_end_date"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
#@app.route("/api/v1.0/precipitation")
def precipitation():
    one_year_ago = dt.datetime.strptime(latest_date[0], '%Y-%m-%d') - dt.timedelta(days=365)

    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()

    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

    return jsonify(precipitation_dict)
@app.route("/api/v1.0/stations")
def stations():
    all_stations = session.query(Measurement.station).distinct().all()

    station_list = [station[0] for station in all_stations]

    return jsonify(station_list)
# Define the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
# Define the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations for the most active station in the last 12 months
    temperature_data_most_active = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station, Measurement.date >= one_year_ago).all()

    # Create a list of dictionaries with date and tobs
    tobs_list = [{'date': date, 'temperature': tobs} for date, tobs in temperature_data_most_active]

    # Return the JSON list of dates and temperature observations
    return jsonify(tobs_list)
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Query TMIN, TAVG, and TMAX for dates greater than or equal to the start date
    temperature_stats_start = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    # Create a dictionary with TMIN, TAVG, and TMAX
    temperature_stats_dict_start = {
        'TMIN': temperature_stats_start[0][0],
        'TAVG': temperature_stats_start[0][1],
        'TMAX': temperature_stats_start[0][2]
    }

    # Return the JSON representation of the dictionary
    return jsonify(temperature_stats_dict_start)

# Define the start_date/end_date route
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Query TMIN, TAVG, and TMAX for dates from start date to end date (inclusive)
    temperature_stats_start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start, Measurement.date <= end).all()

    # Create a dictionary with TMIN, TAVG, and TMAX
    temperature_stats_dict_start_end = {
        'TMIN': temperature_stats_start_end[0][0],
        'TAVG': temperature_stats_start_end[0][1],
        'TMAX': temperature_stats_start_end[0][2]
    }

    # Return the JSON representation of the dictionary
    return jsonify(temperature_stats_dict_start_end)