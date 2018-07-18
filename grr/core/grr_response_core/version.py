#!/usr/bin/env python
"""GRR Rapid Response Framework."""

import ConfigParser
import os

from grr_response_core.lib import config_lib


def VersionPath():
  """Returns a path to version.ini."""

  # Try to get a version.ini. It should be in the resources if the code
  # was packed with "pip sdist". It will be 2 levels up from grr_response_core
  # if the code was installed via "pip install -e".
  try:
    version_ini = config_lib.Resource().Filter("version.ini")
  except config_lib.FilterError:
    version_ini = config_lib.Resource().Filter("../../version.ini")

  if not os.path.exists(version_ini):
    raise RuntimeError("Can't find version.ini at %s" % version_ini)

  return version_ini


def Version():
  """Return a dict with GRR version information."""

  version_ini = VersionPath()

  config = ConfigParser.SafeConfigParser()
  config.read(version_ini)
  return dict(
      packageversion=config.get("Version", "packageversion"),
      major=config.getint("Version", "major"),
      minor=config.getint("Version", "minor"),
      revision=config.getint("Version", "revision"),
      release=config.getint("Version", "release"))
