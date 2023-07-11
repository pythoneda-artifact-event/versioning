"""
pythonedaartifacteventversioning/version_created.py

This file declares the VersionCreated event.

Copyright (C) 2023-today rydnr's pythoneda-artifact-event/versioning

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythoneda.value_object import primary_key_attribute
from typing import List

class VersionCreated(Event):
    """
    Represents the moment a new version has been created.

    Class name: VersiongCreated

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self, version: str, repositoryUrl: str, versionRequestedId:str=None, id:str=None, previousEventIds:List[str]=None):
        """
        Creates a new VersionCreated instance.
        :param version: The version.
        :type version: str
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param versionRequestedId: The id of the VersionRequested event.
        :type versionRequestedId: str
        :param id: The id of the event, if it's generated externally.
        :type id: str
        :param previousEventIds: The id of the previous events, if an external event is being recostructed.
        :type previousEventIds: List[str]
        """
        super().__init__(versionRequestedId, id, previousEventIds)
        self._version = version
        self._repository_url = repositoryUrl

    @property
    @primary_key_attribute
    def version(self) -> str:
        """
        Retrieves the version.
        :return: Such value.
        :rtype: str
        """
        return self._version

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository the version applies to.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url
