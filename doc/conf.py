"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.rsp.check.data


_g = globals()
_g.update(build_package_configs(
    project_name='rsp_check_data',
    version=lsst.rsp.check.data.version.__version__))
