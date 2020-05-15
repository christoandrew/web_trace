from django.contrib import admin

# Register your models here.
import json
import logging
import os
import gzip
from fenix.app.tools import get_notification_data
from firebase_admin import messaging
from fenixdb import app
from django.conf import settings
from fenix.app.modules.common import serializers
from fenix.common.models import Country
from fenix.common.models import ZoneOne, ZoneTwo, ZoneThree, ZoneFour, ZoneFive
logger = logging.getLogger(__name__)
def dump_uganda():
    file_dump_dir = settings.APP_DATA_DUMP_DIR
    country = Country.objects.get(name='Uganda')
    print(file_dump_dir)
    print(country)
    zone_one_file_path = os.path.join(file_dump_dir, '{}_zone_ones.json'.format(country.id))
    zone_two_file_path = os.path.join(file_dump_dir, '{}_zone_twos.json'.format(country.id))
    zone_three_file_path = os.path.join(file_dump_dir, '{}_zone_threes.json'.format(country.id))
    zone_four_file_path = os.path.join(file_dump_dir, '{}_zone_fours.json'.format(country.id))
    zone_five_file_path = os.path.join(file_dump_dir, '{}_zone_fives.json'.format(country.id))
    zone_one_query_set = ZoneOne.objects.filter(parent=country)
    zone_two_query_set = ZoneTwo.objects.filter(parent__parent=country)
    zone_three_query_set = ZoneThree.objects.filter(parent__parent__parent=country)
    zone_four_query_set = ZoneFour.objects.filter(parent__parent__parent__parent=country)
    zone_five_query_set = ZoneFive.objects.filter(parent__parent__parent__parent__parent=country)
    zone_one_serializer = serializers.ZoneSerializer(zone_one_query_set, many=True)
    zone_two_serializer = serializers.ZoneSerializer(zone_two_query_set, many=True)
    zone_three_serializer = serializers.ZoneSerializer(zone_three_query_set, many=True)
    zone_four_serializer = serializers.ZoneSerializer(zone_four_query_set, many=True)
    zone_five_serializer = serializers.ZoneSerializer(zone_five_query_set, many=True)
    if not os.path.isdir(file_dump_dir):
        os.mkdir(file_dump_dir)
    file_paths = [zone_one_file_path, zone_two_file_path, zone_three_file_path, zone_four_file_path,
                    zone_five_file_path]
    for path in file_paths:
        if os.path.isfile(path):
            os.remove(path)
            gzip_path = "{}.gz".format(path)
            if os.path.isfile(path):
                os.remove(gzip_path)
    zone_one_data = zone_one_serializer.data
    with open(zone_one_file_path, 'w') as outfile:
        json.dump(zone_one_data, outfile)
    print("Zone 1s")
    zone_two_data = zone_two_serializer.data
    with open(zone_two_file_path, 'w') as outfile:
        json.dump(zone_two_data, outfile)
    print("Zone 2s")
    zone_three_data = zone_three_serializer.data
    with open(zone_three_file_path, 'w') as outfile:
        json.dump(zone_three_data, outfile)
    print("Zone 3s")
    zone_four_data = zone_four_serializer.data
    with open(zone_four_file_path, 'w') as outfile:
        json.dump(zone_four_data, outfile)
    print("Zone 4s")
    zone_five_data = zone_five_serializer.data
    with open(zone_five_file_path, 'w') as outfile:
        json.dump(zone_five_data, outfile)
    print("Zone 5s")
    try:
        for path in file_paths:
            fp = open(path, "rb")
            data = fp.read()
            with gzip.open("{}.gz".format(path), "wb") as f:
                f.write(data)
                print("Zipping {}".format(path))
            if os.path.isfile(path):
                os.remove(path)  # Remove raw json file
    except Exception as ex:
        print(ex)

dump_uganda()