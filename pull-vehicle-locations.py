from gtfs_rt import parse_vehicle_location, parse_service_alerts, parse_trip_updates
import time
import sqlalchemy
from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd

def main():
    print("Successfully Initialized")
    SERVER = 'DESKTOP-2GHI09J'
    DATABASE = 'ac_transit'
    DRIVER = 'SQL Server Native Client 11.0'
    DATABASE_CONNECTION = f'mssql://@{SERVER}/{DATABASE}?driver={DRIVER}?trusted_conection=yes'
    engine = create_engine(DATABASE_CONNECTION)

    print("Connected to Local Database")
    service_url = "http://api.actransit.org/transit/gtfsrt/alerts/?token=135FD452FD06F53DF88B522DFC4D0512"
    vehicle_url = "http://api.actransit.org/transit/gtfsrt/vehicles/?token=135FD452FD06F53DF88B522DFC4D0512"
    trip_url = "http://api.actransit.org/transit/gtfsrt/tripupdates/?token=135FD452FD06F53DF88B522DFC4D0512"
    while(True):
        try:
            vehicle_locations = parse_vehicle_location(vehicle_url)
            vehicle_locations.to_sql(name = "vehiclepositions2" ,if_exists="append", con = engine, index = False)
            service_alerts = parse_service_alerts(service_url)
            service_alerts.to_sql(name = "servicealerts" ,if_exists = "append", con = engine, index = False)
            #trip_updates = parse_trip_updates(trip_url)
            #trip_updates.to_sql(name = "tripupdates",if_exists = "append", con = engine, index = False)
            print("Successfully Inserted at " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            time.sleep(15)
        except:
            pass




main()
