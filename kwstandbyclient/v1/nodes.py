# Copyright (c) 2014 Bull.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from kwstandbyclient import base
from kwstandbyclient.openstack.common.gettextutils import _  # noqa


class NodeClientManager(base.BaseClientManager):
    """Manager for the Node connected requests."""

    def get(self, node_id):
        """Get node status."""
        return self._get('/status/%s/' % node_id, 'nodes_status')

    def list(self, sort_by=None):
        """List node status."""
        nodes = self._get('/status/', 'nodes_status')
        if sort_by:
            nodes = sorted(nodes, key=lambda l: l[sort_by])
        return nodes

    def update(self, node_id, status):
        """Update node status."""
        if not status:
            return _('No status to update passed.')
        return self._update('/status/%s/' % node_id, {'status': status},
                            response_key='nodes_status')
