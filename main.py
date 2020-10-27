import format
import parcel_info
import ups
import yaml
import sys

with open(r'config.yml') as file:
  # The FullLoader parameter handles the conversion from YAML
  # scalar values to Python the dictionary format
  CONFIG = yaml.load(file, Loader=yaml.FullLoader)

if len(sys.argv)>1:
  tracking_file = sys.argv[1]
else:
  tracking_file = CONFIG['TRACKING_FILE']

with open(tracking_file, "r+") as f:
  trackingNumbers = f.read().splitlines()

ups_conn = ups.UPSTrackerConnection(CONFIG['UPS_ACCESS_KEY'],
                                    CONFIG['UPS_USER_ID'],
                                    CONFIG['UPS_PASSWORD'])
parcel_object = parcel_info.ParcelInfo(ups_conn)
format.print_tracking(parcel_object, trackingNumbers)