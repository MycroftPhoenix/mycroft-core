# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest.mock import Mock
from mycroft.audio.services import AudioBackend


class WorkingBackend(AudioBackend):
    def __init__(self, config, bus, name='Working'):
        super(WorkingBackend, self).__init__(config, bus)

        # Override instance methods with mocks
        self.name = name
        self.add_list = Mock()
        self.clear_list = Mock()
        self.play = Mock()
        self.pause = Mock()
        self.resume = Mock()
        self.stop = Mock()
        self.next = Mock()
        self.previous = Mock()
        self.lower_volume = Mock()
        self.restore_volume = Mock()
        self.seek_forward = Mock()
        self.seek_backward = Mock()
        self.track_info = Mock()
        self.shutdown = Mock()

    def supported_uris(self):
        return ['file', 'http']

    def play(self):
        pass

    def stop(self):
        pass

    def add_list(self, playlist):
        pass

    def clear_list(self):
        pass


def load_service(base_config, bus):
    instances = [WorkingBackend(base_config, bus)]
    return instances
