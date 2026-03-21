# Community data sourced from Talisay_community_data.xlsx and comm_shel_distance_matrix.xlsx
# Population = total population; affected pop = ROUNDUP(0.12 * Population, 0)
# MaxDistance from Talisay_community_data.xlsx (in km)
# Distances from comm_shel_distance_matrix.xlsx (shelter -> community, in km)
# distanceswork from shel_work_distance_matrix.xlsx (shelter -> workplace, in km)
# portiontransfer and portionwork retained from original sample data (not in xlsx)

Community = [
    {"name": "Aya", "population": 746, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 26.105172,
        "Santa Clara Brgy. Hall": 48.452020,
        "Darasa Brgy. Hall": 16.207573,
        "San Antonio Brgy. Hall": 45.690049,
        "Tagaytay Unida Church": 7.663998,
        "Maugat Gymnasium": 53.297125,
        "Brgy. San Jose BB Court": 53.608224,
        "Suplang Covered Court": 9.202329,
        "City EC of Sto. Tomas": 13.128176,
        "Brgy. Asis-3 EC": 21.672758},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.02
     }
    },

    {"name": "Banga & San Guillermo", "population": 614, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 24.012869,
        "Santa Clara Brgy. Hall": 33.060373,
        "Darasa Brgy. Hall": 20.743523,
        "San Antonio Brgy. Hall": 30.298402,
        "Tagaytay Unida Church": 30.690432,
        "Maugat Gymnasium": 76.323559,
        "Brgy. San Jose BB Court": 38.541764,
        "Suplang Covered Court": 30.405826,
        "City EC of Sto. Tomas": 24.631970,
        "Brgy. Asis-3 EC": 44.699192},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.66
     }
    },

    {"name": "Caloocan & Leynes", "population": 391, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 33.404072,
        "Santa Clara Brgy. Hall": 53.793221,
        "Darasa Brgy. Hall": 23.506473,
        "San Antonio Brgy. Hall": 38.935148,
        "Tagaytay Unida Church": 0.787813,
        "Maugat Gymnasium": 47.095382,
        "Brgy. San Jose BB Court": 60.907124,
        "Suplang Covered Court": 16.501229,
        "City EC of Sto. Tomas": 20.427076,
        "Brgy. Asis-3 EC": 17.254099},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.34
     }
    },

    {"name": "Poblacion Barangay 1", "population": 231, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 27.730740,
        "Santa Clara Brgy. Hall": 50.077588,
        "Darasa Brgy. Hall": 17.833141,
        "San Antonio Brgy. Hall": 44.557608,
        "Tagaytay Unida Church": 5.556225,
        "Maugat Gymnasium": 51.189352,
        "Brgy. San Jose BB Court": 55.233792,
        "Suplang Covered Court": 10.827897,
        "City EC of Sto. Tomas": 14.753744,
        "Brgy. Asis-3 EC": 19.564985},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.34
     }
    },

    {"name": "Poblacion Barangay 5", "population": 32, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 12.202733,
        "Santa Clara Brgy. Hall": 42.342352,
        "Darasa Brgy. Hall": 1.900820,
        "San Antonio Brgy. Hall": 40.581799,
        "Tagaytay Unida Church": 21.124498,
        "Maugat Gymnasium": 66.757625,
        "Brgy. San Jose BB Court": 44.574221,
        "Suplang Covered Court": 12.973696,
        "City EC of Sto. Tomas": 3.625315,
        "Brgy. Asis-3 EC": 35.133258},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0
     }
    },

    {"name": "Poblacion Barangay 2,3,4,6,7,8", "population": 969, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 27.730740,
        "Santa Clara Brgy. Hall": 50.077588,
        "Darasa Brgy. Hall": 17.833141,
        "San Antonio Brgy. Hall": 44.557608,
        "Tagaytay Unida Church": 5.556225,
        "Maugat Gymnasium": 51.189352,
        "Brgy. San Jose BB Court": 55.233792,
        "Suplang Covered Court": 10.827897,
        "City EC of Sto. Tomas": 14.753744,
        "Brgy. Asis-3 EC": 19.564985},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.64
     }
    },

    {"name": "Quiling, Miranda, & Tumaway", "population": 1086, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 27.361166,
        "Santa Clara Brgy. Hall": 49.708014,
        "Darasa Brgy. Hall": 17.463567,
        "San Antonio Brgy. Hall": 45.519288,
        "Tagaytay Unida Church": 6.517905,
        "Maugat Gymnasium": 52.151032,
        "Brgy. San Jose BB Court": 54.864218,
        "Suplang Covered Court": 10.458323,
        "City EC of Sto. Tomas": 14.384170,
        "Brgy. Asis-3 EC": 20.526665},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.84
     }
    },

    {"name": "Sampaloc", "population": 544, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 33.768139,
        "Santa Clara Brgy. Hall": 53.014234,
        "Darasa Brgy. Hall": 23.870540,
        "San Antonio Brgy. Hall": 38.156161,
        "Tagaytay Unida Church": 1.151880,
        "Maugat Gymnasium": 46.316395,
        "Brgy. San Jose BB Court": 61.271191,
        "Suplang Covered Court": 16.865296,
        "City EC of Sto. Tomas": 20.791143,
        "Brgy. Asis-3 EC": 16.475112},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.25
     }
    },

    {"name": "Santa Maria, Balas, & Buco", "population": 471, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 30.901650,
        "Santa Clara Brgy. Hall": 53.248498,
        "Darasa Brgy. Hall": 21.004051,
        "San Antonio Brgy. Hall": 41.366676,
        "Tagaytay Unida Church": 2.365293,
        "Maugat Gymnasium": 49.526910,
        "Brgy. San Jose BB Court": 58.404702,
        "Suplang Covered Court": 13.998807,
        "City EC of Sto. Tomas": 17.924654,
        "Brgy. Asis-3 EC": 19.685627},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.07
     }
    },

    {"name": "Tranca", "population": 354, "maxdistance": 77,
     "distances": {
        "San Fernando Brgy. Hall": 24.038189,
        "Santa Clara Brgy. Hall": 50.226273,
        "Darasa Brgy. Hall": 14.140590,
        "San Antonio Brgy. Hall": 47.464302,
        "Tagaytay Unida Church": 10.938092,
        "Maugat Gymnasium": 56.571219,
        "Brgy. San Jose BB Court": 55.382477,
        "Suplang Covered Court": 5.081982,
        "City EC of Sto. Tomas": 11.061193,
        "Brgy. Asis-3 EC": 24.946852},
     "portiontransfer": 0.5,
     "portionwork": {
         "Sto Tomas Batangas": 0.42
     }
    }
]


# Shelter data sourced from Talisay_shelter_data.xlsx and shel_shel_distance_matrix.xlsx
# area1, cost1 (=7700*area1), area2 (=2*area1), cost2 (=60000*area2) from Talisay_shelter_data.xlsx
# distances (shelter-to-shelter) from shel_shel_distance_matrix.xlsx (in km)
# distanceswork (shelter-to-workplace) from shel_work_distance_matrix.xlsx (in km)

Shelters = [
    {"name": "San Fernando Brgy. Hall",
     "area1": 152.37, "cost1": 1173249.0, "area2": 304.74, "cost2": 9142200.0,
     "distances": {
         "San Fernando Brgy. Hall": 0.0,
         "Santa Clara Brgy. Hall": 39.398438,
         "Darasa Brgy. Hall": 10.582127,
         "San Antonio Brgy. Hall": 37.637885,
         "Tagaytay Unida Church": 32.922917,
         "Maugat Gymnasium": 78.556044,
         "Brgy. San Jose BB Court": 41.192638,
         "Suplang Covered Court": 24.118193,
         "City EC of Sto. Tomas": 13.007935,
         "Brgy. Asis-3 EC": 46.931677
     },
     "distanceswork": {
         "Sto Tomas Batangas": 15.517703
     }},

    {"name": "Santa Clara Brgy. Hall",
     "area1": 52.35, "cost1": 403095.0, "area2": 104.7, "cost2": 3141000.0,
     "distances": {
         "San Fernando Brgy. Hall": 39.398438,
         "Santa Clara Brgy. Hall": 0.0,
         "Darasa Brgy. Hall": 40.607955,
         "San Antonio Brgy. Hall": 17.843377,
         "Tagaytay Unida Church": 54.166114,
         "Maugat Gymnasium": 67.358562,
         "Brgy. San Jose BB Court": 15.536631,
         "Suplang Covered Court": 54.985159,
         "City EC of Sto. Tomas": 45.818102,
         "Brgy. Asis-3 EC": 57.389824
     },
     "distanceswork": {
         "Sto Tomas Batangas": 48.832434
     }},

    {"name": "Darasa Brgy. Hall",
     "area1": 247.08, "cost1": 1902516.0, "area2": 494.16, "cost2": 14824800.0,
     "distances": {
         "San Fernando Brgy. Hall": 10.582127,
         "Santa Clara Brgy. Hall": 40.607955,
         "Darasa Brgy. Hall": 0.0,
         "San Antonio Brgy. Hall": 38.847402,
         "Tagaytay Unida Church": 23.025318,
         "Maugat Gymnasium": 68.658445,
         "Brgy. San Jose BB Court": 42.839824,
         "Suplang Covered Court": 14.874516,
         "City EC of Sto. Tomas": 5.210147,
         "Brgy. Asis-3 EC": 37.034078
     },
     "distanceswork": {
         "Sto Tomas Batangas": 8.224479
     }},

    {"name": "San Antonio Brgy. Hall",
     "area1": 98.79, "cost1": 760683.0, "area2": 197.58, "cost2": 5927400.0,
     "distances": {
         "San Fernando Brgy. Hall": 37.637885,
         "Santa Clara Brgy. Hall": 17.843377,
         "Darasa Brgy. Hall": 38.847402,
         "San Antonio Brgy. Hall": 0.0,
         "Tagaytay Unida Church": 39.308041,
         "Maugat Gymnasium": 52.500489,
         "Brgy. San Jose BB Court": 30.474806,
         "Suplang Covered Court": 52.223188,
         "City EC of Sto. Tomas": 44.057549,
         "Brgy. Asis-3 EC": 42.531751
     },
     "distanceswork": {
         "Sto Tomas Batangas": 47.071881
     }},

    {"name": "Tagaytay Unida Church",
     "area1": 152.24, "cost1": 1172248.0, "area2": 304.48, "cost2": 9134400.0,
     "distances": {
         "San Fernando Brgy. Hall": 32.922917,
         "Santa Clara Brgy. Hall": 54.166114,
         "Darasa Brgy. Hall": 23.025318,
         "San Antonio Brgy. Hall": 39.308041,
         "Tagaytay Unida Church": 0.0,
         "Maugat Gymnasium": 47.468275,
         "Brgy. San Jose BB Court": 60.425969,
         "Suplang Covered Court": 16.020074,
         "City EC of Sto. Tomas": 19.945921,
         "Brgy. Asis-3 EC": 17.626992
     },
     "distanceswork": {
         "Sto Tomas Batangas": 21.507159
     }},

    {"name": "Maugat Gymnasium",
     "area1": 774.17, "cost1": 5961109.0, "area2": 1548.34, "cost2": 46450200.0,
     "distances": {
         "San Fernando Brgy. Hall": 78.556044,
         "Santa Clara Brgy. Hall": 67.358562,
         "Darasa Brgy. Hall": 68.658445,
         "San Antonio Brgy. Hall": 52.500489,
         "Tagaytay Unida Church": 47.468275,
         "Maugat Gymnasium": 0.0,
         "Brgy. San Jose BB Court": 79.989991,
         "Suplang Covered Court": 55.295807,
         "City EC of Sto. Tomas": 65.550027,
         "Brgy. Asis-3 EC": 36.925129
     },
     "distanceswork": {
         "Sto Tomas Batangas": 64.889195
     }},

    {"name": "Brgy. San Jose BB Court",
     "area1": 575.54, "cost1": 4431658.0, "area2": 1151.08, "cost2": 34532400.0,
     "distances": {
         "San Fernando Brgy. Hall": 41.192638,
         "Santa Clara Brgy. Hall": 15.536631,
         "Darasa Brgy. Hall": 42.839824,
         "San Antonio Brgy. Hall": 30.474806,
         "Tagaytay Unida Church": 60.425969,
         "Maugat Gymnasium": 79.989991,
         "Brgy. San Jose BB Court": 0.0,
         "Suplang Covered Court": 57.506986,
         "City EC of Sto. Tomas": 48.049971,
         "Brgy. Asis-3 EC": 70.021253
     },
     "distanceswork": {
         "Sto Tomas Batangas": 51.064303
     }},

    {"name": "Suplang Covered Court",
     "area1": 144.55, "cost1": 1113035.0, "area2": 289.1, "cost2": 8673000.0,
     "distances": {
         "San Fernando Brgy. Hall": 24.118193,
         "Santa Clara Brgy. Hall": 54.985159,
         "Darasa Brgy. Hall": 14.874516,
         "San Antonio Brgy. Hall": 52.223188,
         "Tagaytay Unida Church": 16.020074,
         "Maugat Gymnasium": 55.295807,
         "Brgy. San Jose BB Court": 57.506986,
         "Suplang Covered Court": 0.0,
         "City EC of Sto. Tomas": 11.110258,
         "Brgy. Asis-3 EC": 23.671440
     },
     "distanceswork": {
         "Sto Tomas Batangas": 10.449426
     }},

    {"name": "City EC of Sto. Tomas",
     "area1": 616.63, "cost1": 4748051.0, "area2": 1233.26, "cost2": 36997800.0,
     "distances": {
         "San Fernando Brgy. Hall": 13.007935,
         "Santa Clara Brgy. Hall": 45.818102,
         "Darasa Brgy. Hall": 5.210147,
         "San Antonio Brgy. Hall": 44.057549,
         "Tagaytay Unida Church": 19.945921,
         "Maugat Gymnasium": 65.550027,
         "Brgy. San Jose BB Court": 48.049971,
         "Suplang Covered Court": 11.110258,
         "City EC of Sto. Tomas": 0.0,
         "Brgy. Asis-3 EC": 33.925660
     },
     "distanceswork": {
         "Sto Tomas Batangas": 3.669908
     }},

    {"name": "Brgy. Asis-3 EC",
     "area1": 63.38, "cost1": 488026.0, "area2": 126.76, "cost2": 3802800.0,
     "distances": {
         "San Fernando Brgy. Hall": 46.931677,
         "Santa Clara Brgy. Hall": 57.389824,
         "Darasa Brgy. Hall": 37.034078,
         "San Antonio Brgy. Hall": 42.531751,
         "Tagaytay Unida Church": 17.626992,
         "Maugat Gymnasium": 36.925129,
         "Brgy. San Jose BB Court": 70.021253,
         "Suplang Covered Court": 23.671440,
         "City EC of Sto. Tomas": 33.925660,
         "Brgy. Asis-3 EC": 0.0
     },
     "distanceswork": {
         "Sto Tomas Batangas": 33.264828
     }},
]