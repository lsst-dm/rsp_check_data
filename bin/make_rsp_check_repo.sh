#!/bin/bash
mkdir rsp_data_export
butler create RSP_CHECK_REPO
butler register-instrument RSP_CHECK_REPO lsst.obs.subaru.HyperSuprimeCam
python ${RSP_CHECK_DATA_DIR}/bin.src/minimal_hsc_export.py
butler import RSP_CHECK_REPO rsp_data_export --skip-dimensions instrument,detector,physical_filter --transfer copy
python ${RSP_CHECK_DATA_DIR}/bin.src/fix_collections.py
rm -r rsp_data_export