# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

from pymongo import MongoClient
from cvprac.cvp_client import CvpClient
import urllib3
from st2common.runners.base_action import Action

class AristaBaseAction(Action):
    def __init__(self,config):
        super(AristaBaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self):
        ipaddress = self.config['cvp']
        username = self.config['cvp_user']
        password = self.config['cvp_word']

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        client = CvpClient()
        # Connect to the CVP server
        client.connect([cvp], cvp_user, cvp_word)

        return client

class MongoBaseAction(Action):
    def __init__(self,config):
        super(MongoBaseAction, self).__init__(config=config)
        self.dbclient = self._get_db_client()

    def _get_db_client(self):
        dbuser = self.config['dbuser']
        dbpass = self.config['dbpass']

        dbclient = MongoClient('mongodb://%s:%s@localhost:27017/' % (dbuser,dbpass))

        return dbclient
