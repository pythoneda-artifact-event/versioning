"""
pythonedaartifacteventversioning/version_requested.py

This file declares the VersionRequested event.

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

class VersionRequested(Event):
    """
    Represents the request for versionging a repository.

    Class name: VersionRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """
    def __init__(self, repositoryUrl: str, branch: str, previousEventId:str=None, id:str=None, previousEventIds:List[str]=None):
        """
        Creates a new VersionRequested instance.
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param branch: The branch to version.
        :type branch: str
        :param previousEventId: The id of the previous event, if any.
        :type previousEventId: str
        :param id: The id of the event, if it's generated externally.
        :type id: str
        :param previousEventIds: The id of the previous events, if an external event is being recostructed.
        :type previousEventIds: List[str]
        """
        super().__init__(previousEventId, id, previousEventIds)
        self._repository_url = repositoryUrl
        self._branch = branch

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository to version.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url

    @property
    @primary_key_attribute
    def branch(self) -> str:
        """
        Retrieves the branch of the repository to request a new version for.
        :return: Such name.
        :rtype: str
        """
        return self._branch
