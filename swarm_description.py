# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

SWARM_DESCRIPTION = {
  "includedFields": [
    {
      "fieldName": "EMP_NO",
      "fieldType": "int"
    },
    {
      "fieldName": "TIME_OF_SWIPE",
      "fieldType": "datetime",
    },
    {
      "fieldName": "IN_OUT_STATUS",
      "fieldType": "string",
    }
  ],
  "streamDef": {
    "info": "IN_OUT_STATUS",
    "version": 1,
    "streams": [
      {
        "info": "Rec Center",
        "source": "file://data1.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },

  "inferenceType": "TemporalMultiStep",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "IN_OUT_STATUS"
  },
  "iterationCount": 1,
  "swarmSize": "medium"
}
