import time
import sys

def main():

          def testing(str):
              for letter in str:
                  sys.stdout.write(letter)
                  sys.stdout.flush()
                  time.sleep(0.009)

          testing("""
===============================================================
Target: Murphy
===============================================================
IP info:

{
    "ip": "34.111.62.90",
    "country_code": "US",
    "country_name": "United States of America",
    "region_name": "Missouri",
    "district": "Jackson County",
    "city_name": "Kansas City",
    "latitude": 39.09973,
    "longitude": -94.57857,
    "zip_code": "64121",
    "time_zone": "-05:00",
    "asn": "396982",
    "as": x”aGoogle LLC",
    "isp": "Google LLC",
    "domain": "google.com",
    "net_speed": "T1",
    "idd_code": "1",
    "area_code": "816",
    "weather_station_code": "USMO0460",
    "weather_station_name": "Kansas City",
    "mcc": "-",
    "mnc": "-",
    "mobile_brand": "-",
    "elevation": 274,
    "usage_type": "DCH",
    "address_type": "Anycast",
    "ads_category": "IAB19-11",
    "ads_category_name": "Data Centers",
    "continent": {
        "name": "North America",
        "code": "NA",
        "hemisphere": [
            "north",
            "west"
        ],
        "translation": {
            "lang": "en",
            "value": "North America"
        }
    },
    "country": {
        "name": "United States of America",
        "alpha3_code": "USA",
        "numeric_code": 840,
        "demonym": "Americans",
        "flag": "https://cdn.ip2location.io/assets/img/flags/us.png",
        "capital": "Washington, D.C.",
        "total_area": 9826675,
        "population": 339665118,
        "currency": {
            "code": "USD",
            "name": "United States Dollar",
            "symbol": "$"
        },
        "language": {
            "code": "EN",
            "name": "English"
        },
        "tld": "us",
        "translation": {
            "lang": "en",
            "value": "United States of America"
        }
    },
    "region": {
        "name": "Missouri",
        "code": "US-MO",
        "translation": {
            "lang": "en",
            "value": "Missouri"
        }
    },
    "city": {
        "name": "Kansas City",
        "translation": {
            "lang": "en",
            "value": "Kansas City"
        }
    },
    "time_zone_info": {
        "olson": "America/Chicago",
        "current_time": "2025-04-28T20:52:53-05:00",
        "gmt_offset": -18000,
        "is_dst": true,
        "sunrise": "06:20",
        "sunset": "20:10"
    },
    "geotargeting": {
        "metro": "616"
    },
    "is_proxy": false,
    "fraud_score": 0,
    "proxy": {
        "last_seen": 28,
        "proxy_type": "DCH",
        "threat": "-",
        "provider": "-",
        "is_vpn": false,
        "is_tor": false,
        "is_data_center": true,
        "is_public_proxy": false,
        "is_web_proxy": false,
        "is_web_crawler": false,
        "is_residential_proxy": false,
        "is_consumer_privacy_network": false,
        "is_enterprise_private_network": false,
        "is_spammer": false,
        "is_scanner": false,
        "is_botnet": false
{
    "query": "34.111.62.90",
    "status": "success",
    "continent": "North America",
    "continentCode": "NA",
    "country": "United States",
    "countryCode": "US",
    "region": "MO",
    "regionName": "Missouri",
    "city": "Kansas City",
    "district": "",
    "zip": "",
    "lat": 39.0997,
    "lon": -94.5785,
    "timezone": "America/Chicago",
    "offset": -18000,
    "currency": "USD",
    "isp": "Google LLC",
    "org": "Google Cloud",
    "as": "AS396982 Google LLC",
    "asname": "GOOGLE-CLOUD-PLATFORM",
    "mobile": false,
    "proxy": false,
    "hosting": true
{

    "carrier": null,
    "city": "Kansas",
    "continent": "North America",
    "continentCode": "NA",
    "country": "US",
    "countryName": "United States",
    "currency": "USD",
    "dialFromCountryCode": "US",
    "dialFromCountryNumber": "1 (913) 703-5368",
    "ext": null,
    "formatE164": "+19137035368",
    "formatInternational": "+1 913-703-5368",
    "formatNational": "(913) 703-5368",
    "isDisposible": false,
    "languageLikely": [
        "en-US",
        "es-US",
        "haw",
        "fr"
    ],
    "lat": 39.1,
    "lon": -94.579,
    "numberAreaCode": 913,
    "numberCountryCode": 1,
    "numberType": "FIXED LINE OR MOBILE",
    "numberValid": true,
    "numberValidForRegion": true,
    "offset": -18000,
    "query": "19137035368",
    "region": "MO",
    "regionName": "Missouri",
    "status": "success",
    "timezone": "America/Chicago",
    "zip": "64999"
}
  "city": {
    "names": {
      "en": "Kansas City"
    },
    "name": "Kansas City"
  },
  "continent": {
    "code": "NA",
    "geoname_id": 6255149,
    "names": {
      "de": "Nordamerika",
      "en": "North America",
      "es": "Norteamérica",
      "fa": " امریکای شمالی",
      "fr": "Amérique Du Nord",
      "ja": "北アメリカ大陸",
      "ko": "북아메리카",
      "pt-BR": "América Do Norte",
      "ru": "Северная Америка",
      "zh-CN": "北美洲"
    },
    "name": "North America"
  },
  "country": {
    "geoname_id": 6252001,
    "iso_code": "US",
    "names": {
      "de": "Vereinigte Staaten von Amerika",
      "en": "United States",
      "es": "Estados Unidos de América (los)",
      "fa": "ایالات متحدهٔ امریکا",
      "fr": "États-Unis",
      "ja": "アメリカ合衆国",
      "ko": "미국",
      "pt-BR": "Estados Unidos",
      "ru": "США",
      "zh-CN": "美国"
    },
    "name": "United States",
    "name_native": "United States",
    "phone_code": "1",
    "capital": "Washington D.C.",
    "currency": "USD,USN,USS",
    "flag": "🇺🇸",
    "languages": [
      {
        "iso_code": "en",
        "name": "English",
        "name_native": "English"
      }
    ]
  },
  "location": {
    "latitude": 39.0997,
    "longitude": -94.5786
  },
  "subdivisions": [
    {
      "names": {
        "en": "Missouri"
      }
    }
  ],
  "state": {
    "name": "Missouri"
  },
  "datasource": [
    {
      "name": "IP to City Lite",
      "attribution": "<a href='https://db-ip.com'>IP Geolocation by DB-IP</a>",
      "license": "Creative Commons Attribution License"
    }
  ],
  "ip": "34.111.62.90"
}

{
  "results": [
    {
      "datasource": {
        "sourcename": "openstreetmap",
        "attribution": "© OpenStreetMap contributors",
        "license": "Open Database License",
        "url": "https://www.openstreetmap.org/copyright"
      },
Nearby Places:
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "name": "StorageMart",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66212",
        "street": "West 91st Street",
        "housenumber": "6801",
        "iso3166_2": "US-KS",
        "lon": -94.66422810785555,
        "lat": 38.962724949999995,
        "state_code": "KS",
        "formatted": "StorageMart, 6801 West 91st Street, Overland Park, KS 66212, United States of America",
        "address_line1": "StorageMart",
        "address_line2": "6801 West 91st Street, Overland Park, KS 66212, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "rental",
          "rental.storage"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "StorageMart",
            "shop": "storage_rental",
            "brand": "StorageMart",
            "phone": "+1-913-600-5139",
            "osm_id": -16297345,
            "website": "https://www.storage-mart.com/kansas-city/overland-park/66212-west-91st-street",
            "building": "yes",
            "osm_type": "r",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "West 91st Street",
            "addr:postcode": 66212,
            "brand:wikidata": "Q16226585",
            "addr:housenumber": 6801
          }
        },
        "website": "https://www.storage-mart.com/kansas-city/overland-park/66212-west-91st-street",
        "brand": "StorageMart",
        "brand_details": {
          "wikidata": "Q16226585"
        },
        "contact": {
          "phone": "+1-913-600-5139"
        },
        "commercial": {
          "type": "storage_rental"
        },
        "distance": 2097,
        "place_id": "51b5149cb682aa57c059c7e737923a7b4340f00101f90181adf8000000000092030b53746f726167654d617274"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.66422810785555,
          38.962724950120496
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "McCarthy-Morse Chevrolet",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66212",
        "street": "Metcalf Avenue",
        "housenumber": "9201",
        "iso3166_2": "US-KS",
        "lon": -94.66651768079811,
        "lat": 38.96186795,
        "state_code": "KS",
        "formatted": "McCarthy-Morse Chevrolet, 9201 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "address_line1": "McCarthy-Morse Chevrolet",
        "address_line2": "9201 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.vehicle"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "McCarthy-Morse Chevrolet",
            "shop": "car",
            "brand": "Chevrolet",
            "phone": "+1-913-649-6000",
            "osm_id": 1205327800,
            "website": "https://www.mccarthymorsechevrolet.com/",
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "Metcalf Avenue",
            "second_hand": "yes",
            "addr:postcode": 66212,
            "brand:wikidata": "Q29570",
            "addr:housenumber": 9201
          }
        },
        "website": "https://www.mccarthymorsechevrolet.com/",
        "brand": "Chevrolet",
        "brand_details": {
          "wikidata": "Q29570"
        },
        "contact": {
          "phone": "+1-913-649-6000"
        },
        "commercial": {
          "type": "car"
        },
        "distance": 2247,
        "place_id": "51f44ec639a8aa57c059366b2e7d1e7b4340f00102f901b8d7d747000000009203184d634361727468792d4d6f7273652043686576726f6c6574"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.66651768079811,
          38.96186795012038
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Bob Allen Ford",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66212",
        "street": "Metcalf Avenue",
        "housenumber": "9239",
        "iso3166_2": "US-KS",
        "lon": -94.66653161541203,
        "lat": 38.9610008,
        "state_code": "KS",
        "formatted": "Bob Allen Ford, 9239 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "address_line1": "Bob Allen Ford",
        "address_line2": "9239 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.vehicle"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Bob Allen Ford",
            "shop": "car",
            "brand": "Ford",
            "phone": "+1-913-381-3000",
            "osm_id": 624025493,
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "Metcalf Avenue",
            "second_hand": "yes",
            "addr:postcode": 66212,
            "brand:wikidata": "Q44294",
            "addr:housenumber": 9239,
            "service:vehicle:repairs": "yes",
            "service:vehicle:car_repair": "yes",
            "service:vehicle:oil_change": "yes",
            "service:vehicle:diagnostics": "yes",
            "service:vehicle:new_car_sales": "yes",
            "service:vehicle:used_car_sales": "yes"
          }
        },
        "brand": "Ford",
        "brand_details": {
          "wikidata": "Q44294"
        },
        "contact": {
          "phone": "+1-913-381-3000"
        },
        "commercial": {
          "type": "car"
        },
        "distance": 2197,
        "place_id": "51767c3874a8aa57c05920f9ff12027b4340f00102f90195df31250000000092030e426f6220416c6c656e20466f7264"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.66653161541203,
          38.961000800120246
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Price Chopper",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Leawood",
        "postcode": "66219",
        "street": "West 95th Street",
        "iso3166_2": "US-KS",
        "lon": -94.6285651700882,
        "lat": 38.95810045,
        "state_code": "KS",
        "formatted": "Price Chopper, West 95th Street, Leawood, KS 66219, United States of America",
        "address_line1": "Price Chopper",
        "address_line2": "West 95th Street, Leawood, KS 66219, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.supermarket"
        ],
        "details": [
          "details"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Price Chopper",
            "shop": "supermarket",
            "brand": "Price Chopper",
            "osm_id": 505345689,
            "building": "yes",
            "osm_type": "w",
            "brand:wikidata": "Q7242572"
          }
        },
        "brand": "Price Chopper",
        "brand_details": {
          "wikidata": "Q7242572"
        },
        "commercial": {
          "type": "supermarket"
        },
        "distance": 1229,
        "place_id": "51be3b68693aa857c05917c61909a37a4340f00102f90199f61e1e0000000092030d50726963652043686f70706572"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.6285651700882,
          38.95810045011984
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Hallmark",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Leawood",
        "postcode": "66207",
        "street": "Mission Road",
        "iso3166_2": "US-KS",
        "lon": -94.6297971,
        "lat": 38.9576351,
        "state_code": "KS",
        "formatted": "Hallmark, Mission Road, Leawood, KS 66207, United States of America",
        "address_line1": "Hallmark",
        "address_line2": "Mission Road, Leawood, KS 66207, United States of America",
        "categories": [
          "commercial",
          "commercial.gift_and_souvenir"
        ],
        "details": [
          "details"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Hallmark",
            "shop": "gift",
            "brand": "Hallmark",
            "osm_id": 1028300070,
            "osm_type": "n",
            "brand:wikidata": "Q1521910"
          }
        },
        "brand": "Hallmark",
        "brand_details": {
          "wikidata": "Q1521910"
        },
        "commercial": {
          "type": "gift"
        },
        "distance": 1166,
        "place_id": "5166e77e984ea857c059104276c9937a4340f00103f901269d4a3d0000000092030848616c6c6d61726b"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.62979709999999,
          38.957635100119774
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Walgreens",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Prairie Village",
        "postcode": "66207",
        "street": "West 95th Street",
        "housenumber": "4016",
        "iso3166_2": "US-KS",
        "lon": -94.63181092766774,
        "lat": 38.957248,
        "state_code": "KS",
        "formatted": "Walgreens, 4016 West 95th Street, Prairie Village, KS 66207, United States of America",
        "address_line1": "Walgreens",
        "address_line2": "4016 West 95th Street, Prairie Village, KS 66207, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.chemist"
        ],
        "details": [
          "details"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Walgreens",
            "shop": "chemist",
            "brand": "Walgreens",
            "osm_id": 506284200,
            "website": "https://www.walgreens.com/locator/walgreens-4016+w+95th+st-prairie+village-ks-66207/id=13032",
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Prairie Village",
            "addr:state": "KS",
            "addr:street": "West 95th Street",
            "addr:postcode": 66207,
            "brand:wikidata": "Q1591889",
            "addr:housenumber": 4016
          }
        },
        "website": "https://www.walgreens.com/locator/walgreens-4016+w+95th+st-prairie+village-ks-66207/id=13032",
        "brand": "Walgreens",
        "brand_details": {
          "wikidata": "Q1591889"
        },
        "commercial": {
          "type": "chemist"
        },
        "distance": 963,
        "place_id": "51a7e519976fa857c05979563b1a877a4340f00102f901a8482d1e0000000092030957616c677265656e73"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.63181092766773,
          38.95724800011971
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Pride Cleaners",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66207",
        "street": "West 95th Street",
        "housenumber": "5700",
        "iso3166_2": "US-KS",
        "lon": -94.6516865,
        "lat": 38.957147750000004,
        "state_code": "KS",
        "formatted": "Pride Cleaners, 5700 West 95th Street, Overland Park, KS 66207, United States of America",
        "address_line1": "Pride Cleaners",
        "address_line2": "5700 West 95th Street, Overland Park, KS 66207, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "service",
          "service.cleaning",
          "service.cleaning.dry_cleaning"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Pride Cleaners",
            "shop": "dry_cleaning",
            "osm_id": 376260736,
            "building": "commercial",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "West 95th Street",
            "addr:postcode": 66207,
            "addr:housenumber": 5700
          }
        },
        "building": {
          "type": "commercial"
        },
        "commercial": {
          "type": "dry_cleaning"
        },
        "distance": 882,
        "place_id": "51a82f4b3bb5a957c059201a46d1837a4340f00102f90180486d160000000092030e507269646520436c65616e657273"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.65168649999998,
          38.9571477501197
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Prairie Village",
        "postcode": "66206",
        "street": "Mission Road",
        "housenumber": "9440",
        "iso3166_2": "US-KS",
        "lon": -94.6307949,
        "lat": 38.9571262,
        "state_code": "KS",
        "formatted": "9440 Mission Road, Prairie Village, KS 66206, United States of America",
        "address_line1": "9440 Mission Road",
        "address_line2": "Prairie Village, KS 66206, United States of America",
        "categories": [
          "commercial",
          "commercial.convenience"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "shop": "convenience",
            "osm_id": 1028304817,
            "osm_type": "n"
          }
        },
        "commercial": {
          "type": "convenience"
        },
        "distance": 1065,
        "place_id": "51f37e92f15ea857c05954d47f1c837a4340f00103f901b1af4a3d00000000"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.6307949,
          38.95712620011969
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Drs Hawks, Besler and Rogers, Optometrists",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66207",
        "street": "West 95th Street",
        "housenumber": "5703",
        "iso3166_2": "US-KS",
        "lon": -94.6525478,
        "lat": 38.9564597,
        "state_code": "KS",
        "formatted": "Drs Hawks, Besler and Rogers, Optometrists, 5703 West 95th Street, Overland Park, KS 66207, United States of America",
        "address_line1": "Drs Hawks, Besler and Rogers, Optometrists",
        "address_line2": "5703 West 95th Street, Overland Park, KS 66207, United States of America",
        "categories": [
          "commercial",
          "commercial.health_and_beauty",
          "commercial.health_and_beauty.optician"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Drs Hawks, Besler and Rogers, Optometrists",
            "shop": "optician",
            "osm_id": 3797082846,
            "osm_type": "n",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "West 95th Street",
            "addr:postcode": 66207,
            "addr:housenumber": 5703
          }
        },
        "commercial": {
          "type": "optician"
        },
        "distance": 936,
        "place_id": "51e904d957c3a957c05953fa7d456d7a4340f00103f901dee252e20000000092032a447273204861776b732c204265736c657220616e6420526f676572732c204f70746f6d65747269737473"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.6525478,
          38.9564597001196
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Ranch Mart Ace Hardware",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66207",
        "street": "West 95th Street",
        "iso3166_2": "US-KS",
        "lon": -94.629155,
        "lat": 38.9561572,
        "state_code": "KS",
        "formatted": "Ranch Mart Ace Hardware, West 95th Street, Overland Park, KS 66207, United States of America",
        "address_line1": "Ranch Mart Ace Hardware",
        "address_line2": "West 95th Street, Overland Park, KS 66207, United States of America",
        "categories": [
          "commercial",
          "commercial.houseware_and_hardware",
          "commercial.houseware_and_hardware.doityourself"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Ranch Mart Ace Hardware",
            "shop": "doityourself",
            "osm_id": 4972948026,
            "osm_type": "n"
          }
        },
        "commercial": {
          "type": "doityourself"
        },
        "distance": 1171,
        "place_id": "515a47551344a857c059982cf05b637a4340f00103f9013a2a69280100000092031752616e6368204d61727420416365204861726477617265"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.629155,
          38.95615720011955
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "CVS Pharmacy",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66206",
        "street": "Nall Avenue",
        "iso3166_2": "US-KS",
        "lon": -94.64849717621813,
        "lat": 38.95604325,
        "state_code": "KS",
        "formatted": "CVS Pharmacy, Nall Avenue, Overland Park, KS 66206, United States of America",
        "address_line1": "CVS Pharmacy",
        "address_line2": "Nall Avenue, Overland Park, KS 66206, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.chemist"
        ],
        "details": [
          "details"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "CVS Pharmacy",
            "shop": "chemist",
            "brand": "CVS Pharmacy",
            "osm_id": 463619223,
            "website": "https://www.cvs.com/store-locator/overland-park-ks-pharmacies/9501-nall-ave-overland-park-ks-66207/storeid=5271",
            "building": "yes",
            "osm_type": "w",
            "short_name": "CVS",
            "brand:website": "https://www.cvs.com/",
            "brand:wikidata": "Q2078880",
            "brand:wikipedia": "en:CVS Pharmacy"
          }
        },
        "website": "https://www.cvs.com/store-locator/overland-park-ks-pharmacies/9501-nall-ave-overland-park-ks-66207/storeid=5271",
        "brand": "CVS Pharmacy",
        "brand_details": {
          "wikidata": "Q2078880",
          "wikipedia": "en:CVS Pharmacy",
          "website": "https://www.cvs.com/"
        },
        "name_other": {
          "short_name": "CVS"
        },
        "commercial": {
          "type": "chemist"
        },
        "distance": 566,
        "place_id": "51eed94cfa80a957c05998690ea05f7a4340f00102f9019744a21b0000000092030c43565320506861726d616379"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.64849717621811,
          38.956043250119535
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Savers",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66207",
        "street": "West 95th Terrace",
        "iso3166_2": "US-KS",
        "lon": -94.64773519851093,
        "lat": 38.955995200000004,
        "state_code": "KS",
        "formatted": "Savers, West 95th Terrace, Overland Park, KS 66207, United States of America",
        "address_line1": "Savers",
        "address_line2": "West 95th Terrace, Overland Park, KS 66207, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Savers",
            "shop": "charity",
            "osm_id": 463619230,
            "building": "yes",
            "osm_type": "w"
          }
        },
        "commercial": {
          "type": "charity"
        },
        "distance": 492,
        "place_id": "51a484557e74a957c059bcd2fb0c5e7a4340f00102f9019e44a21b00000000920306536176657273"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.64773519851093,
          38.95599520011953
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Lowe's",
        "ref": 3379,
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66212",
        "street": "West 95th Street",
        "housenumber": "7001",
        "iso3166_2": "US-KS",
        "lon": -94.66506680398436,
        "lat": 38.9557717,
        "state_code": "KS",
        "formatted": "Lowe's, 7001 West 95th Street, Overland Park, KS 66212, United States of America",
        "address_line1": "Lowe's",
        "address_line2": "7001 West 95th Street, Overland Park, KS 66212, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.houseware_and_hardware",
          "commercial.houseware_and_hardware.doityourself"
        ],
        "details": [
          "details",
          "details.building",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "ref": 3379,
            "name": "Lowe's",
            "shop": "doityourself",
            "brand": "Lowe's",
            "phone": "+1 913-218-2500",
            "osm_id": 696696696,
            "website": "https://www.lowes.com/store/KS-Overland-Park/3379",
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "start_date": "2018-08-16",
            "addr:street": "West 95th Street",
            "addr:postcode": 66212,
            "opening_hours": "Mo-Sa 06:00-22:00; Su 08:00-20:00",
            "brand:wikidata": "Q1373493",
            "addr:housenumber": 7001
          }
        },
        "website": "https://www.lowes.com/store/KS-Overland-Park/3379",
        "opening_hours": "Mo-Sa 06:00-22:00; Su 08:00-20:00",
        "brand": "Lowe's",
        "brand_details": {
          "wikidata": "Q1373493"
        },
        "contact": {
          "phone": "+1 913-218-2500"
        },
        "building": {
          "start_date": "2018-08-16"
        },
        "commercial": {
          "type": "doityourself"
        },
        "distance": 1917,
        "place_id": "5128315b7490aa57c059503a21ba567a4340f00102f90178bf8629000000009203064c6f77652773"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.66506680398436,
          38.9557717001195
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Sprouts Farmers Market",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66207",
        "street": "Nall Avenue",
        "housenumber": "9628",
        "iso3166_2": "US-KS",
        "lon": -94.6495106,
        "lat": 38.9548373,
        "state_code": "KS",
        "formatted": "Sprouts Farmers Market, 9628 Nall Avenue, Overland Park, KS 66207, United States of America",
        "address_line1": "Sprouts Farmers Market",
        "address_line2": "9628 Nall Avenue, Overland Park, KS 66207, United States of America",
        "categories": [
          "commercial",
          "commercial.supermarket"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Sprouts Farmers Market",
            "shop": "supermarket",
            "brand": "Sprouts Farmers Market",
            "phone": "+1 913-643-9170",
            "osm_id": 4949316863,
            "website": "https://www.sprouts.com/store/ks/overland-park/overland-park-nall-ave/",
            "osm_type": "n",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "short_name": "Sprouts",
            "addr:street": "Nall Avenue",
            "addr:postcode": 66207,
            "opening_hours": "Mo-Su 07:00-22:00",
            "brand:wikidata": "Q7581369",
            "addr:housenumber": 9628
          }
        },
        "website": "https://www.sprouts.com/store/ks/overland-park/overland-park-nall-ave/",
        "opening_hours": "Mo-Su 07:00-22:00",
        "brand": "Sprouts Farmers Market",
        "brand_details": {
          "wikidata": "Q7581369"
        },
        "name_other": {
          "short_name": "Sprouts"
        },
        "contact": {
          "phone": "+1 913-643-9170"
        },
        "commercial": {
          "type": "supermarket"
        },
        "distance": 635,
        "place_id": "51f159e89491a957c059bf81d01b387a4340f00103f901ff940027010000009203165370726f757473204661726d657273204d61726b6574"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.6495106,
          38.95483730011937
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Salon Spice",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66207",
        "street": "Nall Avenue",
        "housenumber": "9561",
        "iso3166_2": "US-KS",
        "lon": -94.6484368,
        "lat": 38.9542848,
        "state_code": "KS",
        "formatted": "Salon Spice, 9561 Nall Avenue, Overland Park, KS 66207, United States of America",
        "address_line1": "Salon Spice",
        "address_line2": "9561 Nall Avenue, Overland Park, KS 66207, United States of America",
        "categories": [
          "commercial",
          "commercial.health_and_beauty",
          "service",
          "service.beauty",
          "service.beauty.spa"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Salon Spice",
            "shop": "beauty",
            "phone": "+1-913-766-0001",
            "osm_id": 4588628317,
            "website": "http://www.salonspice.com",
            "osm_type": "n",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "Nall Avenue",
            "addr:postcode": 66207,
            "addr:housenumber": 9561
          }
        },
        "website": "http://www.salonspice.com",
        "contact": {
          "phone": "+1-913-766-0001"
        },
        "commercial": {
          "type": "beauty"
        },
        "distance": 534,
        "place_id": "51766110fd7fa957c05986ca1b01267a4340f00103f9015de980110100000092030b53616c6f6e205370696365"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.64843679999998,
          38.95428480011928
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66206",
        "street": "West 97th Street",
        "iso3166_2": "US-KS",
        "lon": -94.66911892964887,
        "lat": 38.9536684,
        "state_code": "KS",
        "formatted": "West 97th Street, Overland Park, KS 66206, United States of America",
        "address_line1": "West 97th Street",
        "address_line2": "Overland Park, KS 66206, United States of America",
        "categories": [
          "commercial",
          "commercial.garden"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "shop": "garden_centre",
            "osm_id": 1343025481,
            "osm_type": "w"
          }
        },
        "commercial": {
          "type": "garden_centre"
        },
        "distance": 2309,
        "place_id": "517efe33d8d2aa57c059cade5ece117a4340f00102f90149f10c5000000000"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.66911892964887,
          38.953668400119184
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "The Home Depot",
        "ref": 2203,
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66212",
        "street": "Metcalf Avenue",
        "housenumber": "9600",
        "iso3166_2": "US-KS",
        "lon": -94.67010493314885,
        "lat": 38.9536676,
        "state_code": "KS",
        "formatted": "The Home Depot, 9600 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "address_line1": "The Home Depot",
        "address_line2": "9600 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.houseware_and_hardware",
          "commercial.houseware_and_hardware.doityourself"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "ref": 2203,
            "name": "The Home Depot",
            "shop": "doityourself",
            "brand": "The Home Depot",
            "phone": "+1 913-648-7811",
            "branch": "North Overland Park",
            "osm_id": 388937067,
            "website": "https://www.homedepot.com/l/n-overland-park/ks/overland-park/66212/2203",
            "alt_name": "Home Depot",
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "addr:street": "Metcalf Avenue",
            "addr:postcode": 66212,
            "opening_hours": "Mo-Sa 06:00-22:00; Su 08:00-20:00",
            "brand:wikidata": "Q864407",
            "addr:housenumber": 9600
          }
        },
        "website": "https://www.homedepot.com/l/n-overland-park/ks/overland-park/66212/2203",
        "opening_hours": "Mo-Sa 06:00-22:00; Su 08:00-20:00",
        "brand": "The Home Depot",
        "brand_details": {
          "wikidata": "Q864407"
        },
        "branch": "North Overland Park",
        "name_other": {
          "alt_name": "Home Depot"
        },
        "contact": {
          "phone": "+1 913-648-7811"
        },
        "commercial": {
          "type": "doityourself"
        },
        "distance": 2339,
        "place_id": "51ce30cdffe2aa57c05924e2a8c7117a4340f00102f9016bb52e170000000092030e54686520486f6d65204465706f74"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.67010493314885,
          38.95366760011919
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "QuikTrip",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66212",
        "street": "Metcalf Avenue",
        "housenumber": "9731",
        "iso3166_2": "US-KS",
        "lon": -94.66705360645199,
        "lat": 38.952520750000005,
        "state_code": "KS",
        "formatted": "QuikTrip, 9731 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "address_line1": "QuikTrip",
        "address_line2": "9731 Metcalf Avenue, Overland Park, KS 66212, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.convenience"
        ],
        "details": [
          "details",
          "details.contact"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "QuikTrip",
            "shop": "convenience",
            "brand": "QuikTrip",
            "phone": "+1-913-401-2986",
            "osm_id": 1265090364,
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "short_name": "QT",
            "addr:street": "Metcalf Avenue",
            "addr:postcode": 66212,
            "brand:wikidata": "Q7271953",
            "addr:housenumber": 9731
          }
        },
        "brand": "QuikTrip",
        "brand_details": {
          "wikidata": "Q7271953"
        },
        "name_other": {
          "short_name": "QT"
        },
        "contact": {
          "phone": "+1-913-401-2986"
        },
        "commercial": {
          "type": "convenience"
        },
        "distance": 2140,
        "place_id": "51f8189c01b1aa57c059e4422f33ec794340f00102f9013cbf674b000000009203085175696b54726970"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.66705360645199,
          38.95252075011902
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "Suburban Lawn & Garden",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66211",
        "street": "Indian Creek Trail",
        "iso3166_2": "US-KS",
        "lon": -94.63894761402656,
        "lat": 38.9373858,
        "state_code": "KS",
        "formatted": "Suburban Lawn & Garden, Indian Creek Trail, Overland Park, KS 66211, United States of America",
        "address_line1": "Suburban Lawn & Garden",
        "address_line2": "Indian Creek Trail, Overland Park, KS 66211, United States of America",
        "categories": [
          "commercial",
          "commercial.garden"
        ],
        "details": [],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "Suburban Lawn & Garden",
            "shop": "garden_centre",
            "osm_id": 198381931,
            "osm_type": "w"
          }
        },
        "commercial": {
          "type": "garden_centre"
        },
        "distance": 1765,
        "place_id": "517c868884e4a857c059489e0542fc774340f00102f9016b11d30b00000000920316537562757262616e204c61776e20262047617264656e"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.63894761402656,
          38.93738580011683
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "QuikTrip",
        "country": "United States",
        "country_code": "us",
        "state": "Kansas",
        "county": "Johnson County",
        "city": "Overland Park",
        "postcode": "66211",
        "street": "Roe Avenue",
        "housenumber": "10700",
        "iso3166_2": "US-KS",
        "lon": -94.64065542470264,
        "lat": 38.934233750000004,
        "state_code": "KS",
        "formatted": "QuikTrip, 10700 Roe Avenue, Overland Park, KS 66211, United States of America",
        "address_line1": "QuikTrip",
        "address_line2": "10700 Roe Avenue, Overland Park, KS 66211, United States of America",
        "categories": [
          "building",
          "building.commercial",
          "commercial",
          "commercial.convenience",
          "wheelchair",
          "wheelchair.yes"
        ],
        "details": [
          "details",
          "details.facilities"
        ],
        "datasource": {
          "sourcename": "openstreetmap",
          "attribution": "© OpenStreetMap contributors",
          "license": "Open Database License",
          "url": "https://www.openstreetmap.org/copyright",
          "raw": {
            "name": "QuikTrip",
            "shop": "convenience",
            "brand": "QuikTrip",
            "osm_id": 198500672,
            "building": "yes",
            "osm_type": "w",
            "addr:city": "Overland Park",
            "addr:state": "KS",
            "short_name": "QT",
            "wheelchair": "yes",
            "addr:street": "Roe Avenue",
            "addr:postcode": 66211,
            "opening_hours": "24/7",
            "brand:wikidata": "Q7271953",
            "addr:housenumber": 10700
          }
        },
        "opening_hours": "24/7",
        "brand": "QuikTrip",
        "brand_details": {
          "wikidata": "Q7271953"
        },
        "name_other": {
          "short_name": "QT"
        },
        "facilities": {
          "wheelchair": true
        },
        "commercial": {
          "type": "convenience"
        },
        "distance": 2155,
        "place_id": "5194469c7f00a957c059dec8b5f894774340f00102f90140e1d40b000000009203085175696b54726970"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -94.64065542470263,
          38.93423375011638
        ]
      }
      "name": "Metro KC Fitness",
      "country": "United States",
      "country_code": "us",
      "state": "Missouri",
      "county": "Jackson County",
      "city": "Kansas City",
      "postcode": "64106",
      "district": "Central Business District KC",
      "suburb": "Downtown Kansas City",
      "street": "East 12th Street",
      "housenumber": "320",
      "iso3166_2": "US-MO",
      "lon": -94.5787842,
      "lat": 39.0999591,
      "state_code": "MO",
      "county_code": "JC",
      "distance": 32.904532712086876,
      "result_type": "amenity",
      "formatted": "Metro KC Fitness, 320 East 12th Street, Kansas City, MO 64106, United States of America",
      "address_line1": "Metro KC Fitness",
      "address_line2": "320 East 12th Street, Kansas City, MO 64106, United States of America",
      "category": "sport.fitness.fitness_centre",
      "timezone": {
        "name": "America/Chicago",
        "offset_STD": "-06:00",
        "offset_STD_seconds": -21600,
        "offset_DST": "-05:00",
        "offset_DST_seconds": -18000,
        "abbreviation_STD": "CST",
        "abbreviation_DST": "CDT"
      },
      "plus_code": "86F73CXC+XF",
      "plus_code_short": "+XF, 64106 Kansas City, United States",
      "rank": {
        "importance": 0.00000999999999995449,
        "popularity": 6.193599761681923
      },
      "place_id": "51429ce2cc0aa557c05903b8b475cb8c4340f00103f9011f5c0ae302000000c002019203104d6574726f204b43204669746e657373e203246f70656e7374726565746d61703a76656e75653a6e6f64652f3132333939303431353637",
      "bbox": {
        "lon1": -94.5788342,
        "lat1": 39.0999091,
        "lon2": -94.5787342,
        "lat2": 39.1000091
      }
    }
  ],
  "query": {
    "lat": 39.0997,
    "lon": -94.5786,
    "plus_code": "86F73CXC+VH"
  }
}

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "postcode": "64106",
        "distance": 0,
        "lon": -94.5700876,
        "lat": 39.1052737,
        "datasource": {
          "sourcename": "census",
          "attribution": "Census",
          "license": "Open Government Licence (OGL)",
          "url": "https://www.ons.gov.uk/census/2001censusandearlier/dataandproducts/copyrightandlicensing"
        },
        "country": "United States",
        "country_code": "us",
        "state": "Missouri",
        "county": "Jackson County",
        "city": "Kansas City",
        "state_code": "MO",
        "formatted": "Kansas City, MO 64106, United States of America",
        "address_line1": "Kansas City, MO 64106",
        "address_line2": "United States of America",
        "timezone": {
          "name": "America/Chicago",
          "offset_STD": "-06:00",
          "offset_STD_seconds": -21600,
          "offset_DST": "-05:00",
          "offset_DST_seconds": -18000,
          "abbreviation_STD": "CST",
          "abbreviation_DST": "CDT"
        },
        "plus_code": "86F74C4H+4X",
        "plus_code_short": "4H+4X, 64106 Kansas City, United States",
        "iso3166_2": "US-MO",
        "place_id": "51ba76b3507ca457c0598050cd9b798d4340c0020792031136343130362b75732b696d706f72746564"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -94.583663,
              39.110824
            ],
            [
              -94.582473,
              39.111071
            ],
            [
              -94.580974,
              39.111381
            ],
            [
              -94.580938,
              39.111506
            ],
            [
              -94.580707,
              39.112342
            ],
            [
              -94.580671,
              39.112608
            ],
            [
              -94.58065,
              39.112681
            ],
            [
              -94.580523,
              39.112989
            ],
            [
              -94.57945,
              39.113082
            ],
            [
              -94.578244,
              39.113188
            ],
            [
              -94.578181,
              39.113193
            ],
            [
              -94.5782,
              39.11329
            ],
            [
              -94.578024,
              39.113304
            ],
            [
              -94.577971,
              39.113308
            ],
            [
              -94.577944,
              39.113214
            ],
            [
              -94.57714,
              39.113284
            ],
            [
              -94.574493,
              39.113407
            ],
            [
              -94.574056,
              39.113428
            ],
            [
              -94.573129,
              39.113492
            ],
            [
              -94.572187,
              39.11358
            ],
            [
              -94.571989,
              39.113598
            ],
            [
              -94.570061,
              39.113785
            ],
            [
              -94.568681,
              39.113953
            ],
            [
              -94.568635,
              39.113962
            ],
            [
              -94.56859,
              39.113966
            ],
            [
              -94.567462,
              39.114142
            ],
            [
              -94.566436,
              39.114335
            ],
            [
              -94.565418,
              39.114555
            ],
            [
              -94.564707,
              39.114728
            ],
            [
              -94.564557,
              39.114766
            ],
            [
              -94.563243,
              39.115128
            ],
            [
              -94.559644,
              39.11588
            ],
            [
              -94.55869,
              39.11608
            ],
            [
              -94.556775,
              39.11648
            ],
            [
              -94.553802,
              39.117115
            ],
            [
              -94.553391,
              39.117203
            ],
            [
              -94.552374,
              39.11742
            ],
            [
              -94.551463,
              39.117614
            ],
            [
              -94.551222,
              39.117659
            ],
            [
              -94.55025,
              39.117842
            ],
            [
              -94.549867,
              39.117913
            ],
            [
              -94.549143,
              39.118028
            ],
            [
              -94.548223,
              39.118174
            ],
            [
              -94.548182,
              39.118183
            ],
            [
              -94.548079,
              39.117695
            ],
            [
              -94.548026,
              39.117348
            ],
            [
              -94.548059,
              39.116113
            ],
            [
              -94.548148,
              39.114251
            ],
            [
              -94.548152,
              39.113575
            ],
            [
              -94.549409,
              39.113576
            ],
            [
              -94.549401,
              39.113621
            ],
            [
              -94.549347,
              39.1138
            ],
            [
              -94.549238,
              39.114029
            ],
            [
              -94.548918,
              39.114591
            ],
            [
              -94.548833,
              39.114707
            ],
            [
              -94.548796,
              39.114798
            ],
            [
              -94.548779,
              39.114892
            ],
            [
              -94.548784,
              39.114988
            ],
            [
              -94.54881,
              39.115081
            ],
            [
              -94.548907,
              39.115235
            ],
            [
              -94.549227,
              39.115485
            ],
            [
              -94.549595,
              39.115772
            ],
            [
              -94.549637,
              39.115864
            ],
            [
              -94.549629,
              39.115934
            ],
            [
              -94.549592,
              39.115997
            ],
            [
              -94.549077,
              39.116459
            ],
            [
              -94.548997,
              39.116556
            ],
            [
              -94.548941,
              39.116662
            ],
            [
              -94.548905,
              39.116798
            ],
            [
              -94.548884,
              39.117054
            ],
            [
              -94.548917,
              39.117115
            ],
            [
              -94.548974,
              39.117163
            ],
            [
              -94.549029,
              39.117188
            ],
            [
              -94.549111,
              39.117203
            ],
            [
              -94.549177,
              39.117197
            ],
            [
              -94.549819,
              39.117022
            ],
            [
              -94.550121,
              39.116988
            ],
            [
              -94.550603,
              39.116914
            ],
            [
              -94.551269,
              39.116802
            ],
            [
              -94.552014,
              39.116606
            ],
            [
              -94.552651,
              39.11645
            ],
            [
              -94.553296,
              39.11631
            ],
            [
              -94.553946,
              39.116145
            ],
            [
              -94.554509,
              39.115997
            ],
            [
              -94.555035,
              39.115829
            ],
            [
              -94.555532,
              39.115665
            ],
            [
              -94.556348,
              39.115465
            ],
            [
              -94.55647,
              39.115396
            ],
            [
              -94.55661,
              39.115282
            ],
            [
              -94.556734,
              39.115157
            ],
            [
              -94.556855,
              39.115003
            ],
            [
              -94.557057,
              39.114822
            ],
            [
              -94.557273,
              39.114666
            ],
            [
              -94.557509,
              39.114528
            ],
            [
              -94.557719,
              39.114428
            ],
            [
              -94.557939,
              39.114343
            ],
            [
              -94.558588,
              39.114154
            ],
            [
              -94.559099,
              39.114004
            ],
            [
              -94.559361,
              39.113893
            ],
            [
              -94.55955,
              39.113799
            ],
            [
              -94.559697,
              39.113727
            ],
            [
              -94.560017,
              39.113545
            ],
            [
              -94.560321,
              39.113345
            ],
            [
              -94.560373,
              39.113305
            ],
            [
              -94.560673,
              39.113072
            ],
            [
              -94.560678,
              39.112975
            ],
            [
              -94.560628,
              39.112819
            ],
            [
              -94.560547,
              39.112672
            ],
            [
              -94.560451,
              39.11255
            ],
            [
              -94.559486,
              39.111702
            ],
            [
              -94.558948,
              39.111157
            ],
            [
              -94.558779,
              39.110732
            ],
            [
              -94.558732,
              39.110612
            ],
            [
              -94.558613,
              39.110146
            ],
            [
              -94.558567,
              39.109671
            ],
            [
              -94.558595,
              39.109196
            ],
            [
              -94.558441,
              39.10919
            ],
            [
              -94.55847,
              39.108775
            ],
            [
              -94.558506,
              39.108246
            ],
            [
              -94.559963,
              39.10831
            ],
            [
              -94.560076,
              39.106643
            ],
            [
              -94.560244,
              39.10665
            ],
            [
              -94.560346,
              39.105195
            ],
            [
              -94.560361,
              39.104814
            ],
            [
              -94.558132,
              39.104752
            ],
            [
              -94.558203,
              39.103768
            ],
            [
              -94.55825,
              39.102702
            ],
            [
              -94.559552,
              39.102776
            ],
            [
              -94.559665,
              39.102807
            ],
            [
              -94.55989,
              39.102838
            ],
            [
              -94.560451,
              39.102894
            ],
            [
              -94.560457,
              39.102775
            ],
            [
              -94.560522,
              39.101539
            ],
            [
              -94.560585,
              39.100359
            ],
            [
              -94.559439,
              39.100323
            ],
            [
              -94.559599,
              39.099141
            ],
            [
              -94.560651,
              39.099107
            ],
            [
              -94.560708,
              39.097823
            ],
            [
              -94.560769,
              39.096448
            ],
            [
              -94.560783,
              39.096151
            ],
            [
              -94.560785,
              39.096115
            ],
            [
              -94.560794,
              39.095928
            ],
            [
              -94.560796,
              39.095882
            ],
            [
              -94.560834,
              39.09511
            ],
            [
              -94.561789,
              39.09514
            ],
            [
              -94.562838,
              39.095173
            ],
            [
              -94.564006,
              39.095209
            ],
            [
              -94.564553,
              39.095226
            ],
            [
              -94.565836,
              39.095268
            ],
            [
              -94.568781,
              39.09537
            ],
            [
              -94.570097,
              39.095415
            ],
            [
              -94.571387,
              39.095461
            ],
            [
              -94.571579,
              39.095467
            ],
            [
              -94.571517,
              39.095707
            ],
            [
              -94.571459,
              39.096025
            ],
            [
              -94.571438,
              39.096187
            ],
            [
              -94.571692,
              39.096197
            ],
            [
              -94.572795,
              39.096244
            ],
            [
              -94.572892,
              39.096663
            ],
            [
              -94.572934,
              39.096648
            ],
            [
              -94.573172,
              39.096587
            ],
            [
              -94.573378,
              39.096555
            ],
            [
              -94.573507,
              39.096541
            ],
            [
              -94.574011,
              39.096454
            ],
            [
              -94.574117,
              39.096436
            ],
            [
              -94.575227,
              39.096245
            ],
            [
              -94.576216,
              39.096075
            ],
            [
              -94.576735,
              39.096001
            ],
            [
              -94.577501,
              39.095884
            ],
            [
              -94.577587,
              39.095871
            ],
            [
              -94.577608,
              39.095868
            ],
            [
              -94.57769,
              39.095856
            ],
            [
              -94.577781,
              39.095842
            ],
            [
              -94.577828,
              39.095835
            ],
            [
              -94.57796,
              39.095815
            ],
            [
              -94.578245,
              39.095796
            ],
            [
              -94.578479,
              39.09579
            ],
            [
              -94.578741,
              39.095794
            ],
            [
              -94.579928,
              39.095858
            ],
            [
              -94.581112,
              39.095923
            ],
            [
              -94.582275,
              39.095983
            ],
            [
              -94.583396,
              39.096038
            ],
            [
              -94.583388,
              39.096196
            ],
            [
              -94.583378,
              39.096385
            ],
            [
              -94.583334,
              39.097222
            ],
            [
              -94.583261,
              39.098597
            ],
            [
              -94.583196,
              39.099916
            ],
            [
              -94.583166,
              39.100808
            ],
            [
              -94.583157,
              39.101095
            ],
            [
              -94.583117,
              39.102288
            ],
            [
              -94.582903,
              39.102299
            ],
            [
              -94.581964,
              39.102283
            ],
            [
              -94.581894,
              39.103524
            ],
            [
              -94.581841,
              39.104455
            ],
            [
              -94.583043,
              39.104489
            ],
            [
              -94.583023,
              39.105246
            ],
            [
              -94.583017,
              39.105521
            ],
            [
              -94.582756,
              39.106041
            ],
            [
              -94.582614,
              39.106342
            ],
            [
              -94.581514,
              39.106271
            ],
            [
              -94.581438,
              39.106644
            ],
            [
              -94.58143,
              39.106683
            ],
            [
              -94.581406,
              39.106815
            ],
            [
              -94.581397,
              39.106859
            ],
            [
              -94.581316,
              39.107332
            ],
            [
              -94.581321,
              39.107579
            ],
            [
              -94.582135,
              39.107469
            ],
            [
              -94.582244,
              39.107838
            ],
            [
              -94.582692,
              39.107746
            ],
            [
              -94.582871,
              39.108311
            ],
            [
              -94.582463,
              39.108389
            ],
            [
              -94.582559,
              39.108702
            ],
            [
              -94.582567,
              39.108838
            ],
            [
              -94.582842,
              39.109568
            ],
            [
              -94.583,
              39.109638
            ],
            [
              -94.583274,
              39.109585
            ],
            [
              -94.583363,
              39.109867
            ],
            [
              -94.583587,
              39.110582
            ],
            [
              -94.583663,
              39.110824
            ]
          ]
        ]
      },
      "bbox": [
        -94.583663,
        39.09511,
        -94.548026,
        39.118183
      ]
    }
  ]
}

{
  "ip": "34.111.62.90",
  "type": "IPv4",
  "hostname": "90.62.111.34.bc.googleusercontent.com",
  "carrier": {
    "name": null,
    "mcc": null,
    "mnc": null
  },
  "company": {
    "domain": "google.com",
    "name": "Google LLC",
    "type": "hosting"
  },
  "connection": {
    "asn": 396982,
    "domain": "google.com",
    "organization": "Google LLC",
    "route": "34.108.0.0/14",
    "type": "hosting"
  },
  "currency": {
    "code": "USD",
    "name": "US Dollar",
    "name_native": "US Dollar",
    "plural": "US dollars",
    "plural_native": "US dollars",
    "symbol": "$",
    "symbol_native": "$",
    "format": {
      "decimal_separator": ".",
      "group_separator": ",",
      "negative": {
        "prefix": "-$",
        "suffix": ""
      },
      "positive": {
        "prefix": "$",
        "suffix": ""
      }
    }
  },
  "location": {
    "continent": {
      "code": "NA",
      "name": "North America"
    },
    "country": {
      "area": 9629091,
      "borders": [
        "CA",
        "MX"
      ],
      "calling_code": "1",
      "capital": "Washington D.C.",
      "code": "US",
      "name": "United States",
      "population": 334914895,
      "population_density": 34.78,
      "flag": {
        "emoji": "🇺🇸",
        "emoji_unicode": "U+1F1FA U+1F1F8",
        "emojitwo": "https://cdn.ipregistry.co/flags/emojitwo/us.svg",
        "noto": "https://cdn.ipregistry.co/flags/noto/us.png",
        "twemoji": "https://cdn.ipregistry.co/flags/twemoji/us.svg",
        "wikimedia": "https://cdn.ipregistry.co/flags/wikimedia/us.svg"
      },
      "languages": [
        {
          "code": "en",
          "name": "English",
          "native": "English"
        },
        {
          "code": "es",
          "name": "Spanish",
          "native": "espaÃ±ol"
        },
        {
          "code": "fr",
          "name": "French",
          "native": "franÃ§ais"
        }
      ],
      "tld": ".us"
    },
    "region": {
      "code": "US-MO",
      "name": "Missouri"
    },
    "city": "Kansas City",
    "postal": "64999",
    "latitude": 39.1001,
    "longitude": -94.57814,
    "language": {
      "code": "en",
      "name": "English",
      "native": "English"
    },
    "in_eu": false
  },
  "security": {
    "is_abuser": false,
    "is_attacker": false,
    "is_bogon": false,
    "is_cloud_provider": true,
    "is_proxy": false,
    "is_relay": false,
    "is_tor": false,
    "is_tor_exit": false,
    "is_vpn": false,
    "is_anonymous": false,
    "is_threat": false
  },
  "time_zone": {
    "id": "America/Chicago",
    "abbreviation": "CST",
    "current_time": "2025-04-28T20:44:56-05:00",
    "name": "Central Standard Time",
    "offset": -18000,
    "in_daylight_saving": true
  }
}

{
 "ip": "34.111.62.90",
 "localityLanguageRequested": "en",
 "isReachableGlobally": true,
 "country": {
  "isoAlpha2": "US",
  "isoAlpha3": "USA",
  "m49Code": 840,
  "name": "United States of America (the)",
  "isoName": "United States of America (the)",
  "isoNameFull": "the United States of America",
  "isoAdminLanguages": [
   {
    "isoAlpha3": "eng",
    "isoAlpha2": "en",
    "isoName": "English",
    "nativeName": "English"
   }
  ],
  "unRegion": "Europe and Northern America/Northern America",
  "currency": {
   "numericCode": 840,
   "code": "USD",
   "name": "US Dollar",
   "minorUnits": 2
  },
  "wbRegion": {
   "id": "NAC",
   "iso2Code": "XU",
   "value": "North America"
  },
  "wbIncomeLevel": {
   "id": "HIC",
   "iso2Code": "XD",
   "value": "High income"
  },
  "callingCode": "1",
  "countryFlagEmoji": "🇺🇸",
  "wikidataId": "Q30",
  "geonameId": 6252001,
  "isIndependent": true
 },
 "location": {
  "principalSubdivision": "Missouri",
  "isoPrincipalSubdivision": "Missouri",
  "isoPrincipalSubdivisionCode": "US-MO",
  "continent": "North America",
  "continentCode": "NA",
  "city": "Kansas City",
  "localityName": "Kansas City",
  "postcode": "64106",
  "latitude": 39.1,
  "longitude": -94.58,
  "plusCode": "86F73CX9+XX",
  "fips": {
   "state": "29",
   "county": "095",
   "countySubdivision": "38054",
   "place": "38000"
  },
  "timeZone": {
   "ianaTimeId": "America/Chicago",
   "displayName": "(UTC-06:00) Central Time (Chicago)",
   "effectiveTimeZoneFull": "Central Daylight Time",
   "effectiveTimeZoneShort": "CDT",
   "utcOffsetSeconds": -18000,
   "utcOffset": "-05",
   "isDaylightSavingTime": true,
   "localTime": "2025-04-28T20:46:00.2412627"
  },
  "localityInfo": {
   "administrative": [
    {
     "name": "United States of America (the)",
     "description": "country in North America",
     "isoName": "United States of America (the)",
     "order": 2,
     "adminLevel": 2,
     "isoCode": "US",
     "wikidataId": "Q30",
     "geonameId": 6252001
    },
    {
     "name": "Missouri",
     "description": "state of the United States of America",
     "isoName": "Missouri",
     "order": 6,
     "adminLevel": 4,
     "isoCode": "US-MO",
     "wikidataId": "Q1581",
     "geonameId": 4398678
    },
    {
     "name": "Jackson County",
     "description": "county in Missouri, United States",
     "order": 7,
     "adminLevel": 6,
     "wikidataId": "Q127238",
     "geonameId": 4392183
    },
    {
     "name": "Kansas City",
     "description": "city in Missouri, United States",
     "order": 8,
     "adminLevel": 8,
     "wikidataId": "Q41819",
     "geonameId": 4393217
    }
   ],
   "informative": [
    {
     "name": "North America",
     "description": "continent",
     "isoName": "North America",
     "order": 1,
     "isoCode": "NA",
     "wikidataId": "Q49",
     "geonameId": 6255149
    },
    {
     "name": "contiguous United States",
     "description": "the 48 states of the United States (all but Alaska and Hawaii) and the District of Columbia",
     "order": 3,
     "wikidataId": "Q578170"
    },
    {
     "name": "America/Chicago",
     "description": "time zone",
     "order": 4
    },
    {
     "name": "Central Lowlands",
     "order": 5
    },
    {
     "name": "29-38000",
     "description": "FIPS code",
     "order": 9
    },
    {
     "name": "29-095-38054",
     "description": "FIPS code",
     "order": 10
    },
    {
     "name": "64106",
     "description": "postal code",
     "order": 11
    },
    {
     "name": "Downtown Kansas City",
     "order": 12
    }
   ]
  }
 },
 "lastUpdated": "2025-04-28T16:33:24.2575728Z",
 "network": {
  "registry": "ARIN",
  "registryStatus": "assigned",
  "registeredCountry": "US",
  "registeredCountryName": "United States of America (the)",
  "organisation": "Google LLC",
  "isReachableGlobally": true,
  "isBogon": false,
  "bgpPrefix": "34.111.0.0/16",
  "bgpPrefixNetworkAddress": "34.111.0.0",
  "bgpPrefixLastAddress": "34.111.255.255",
  "totalAddresses": 65536,
  "carriers": [
   {
    "asn": "AS396982",
    "asnNumeric": 396982,
    "organisation": "Google LLC",
    "name": "GOOGLE-CLOUD-PLATFORM",
    "registry": "Arin",
    "registeredCountry": "US",
    "registeredCountryName": "United States of America (the)",
    "registrationDate": "2018-08-15",
    "registrationLastChange": "2021-11-16",
    "totalIpv4Addresses": 14862435,
    "totalIpv4Prefixes": 3014,
    "totalIpv4BogonPrefixes": 0,
    "totalIpv6Prefixes": 206,
    "totalIpv6BogonPrefixes": 0,
    "rank": 28,
    "rankText": "#28 out of 78,231"
   }
  ],
  "viaCarriers": [
   {
    "asn": "AS15169",
    "asnNumeric": 15169,
    "organisation": "Google LLC",
    "name": "GOOGLE",
    "registry": "Arin",
    "registeredCountry": "US",
    "registeredCountryName": "United States of America (the)",
    "totalIpv4Addresses": 2746851,
    "rank": 159,
    "rankText": "#159 out of 78,231"
   }
  ]
 },
 "confidence": "low",
 "securityThreat": "unknown",
 "hazardReport": {
  "isKnownAsTorServer": false,
  "isKnownAsVpn": false,
  "isKnownAsProxy": false,
  "isSpamhausDrop": false,
  "isSpamhausEdrop": false,
  "isSpamhausAsnDrop": false,
  "isBlacklistedUceprotect": false,
  "isBlacklistedBlocklistDe": false,
  "isKnownAsMailServer": false,
  "isKnownAsPublicRouter": false,
  "isBogon": false,
  "isUnreachable": false,
  "hostingLikelihood": 0,
  "isHostingAsn": false,
  "isCellular": false,
  "iCloudPrivateRelay": false
 }
}

===============================================================
Family:
*
*
===============================================================
Other information:
*
*
===============================================================
          """)
          time.sleep(0.5)


main()