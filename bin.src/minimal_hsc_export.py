#!/usr/bin/env python

from lsst.pipe.base import QuantumGraph
from lsst.daf.butler import DimensionUniverse, Butler
butler = Butler('/repo/main')
du = DimensionUniverse()
qgraph = QuantumGraph.loadUri('/home/krughoff/public_html/data/two_ccd_processccd.qgraph', du)
exports = set()


def runner(nodes, exports, visited=None):
    if not visited:
        visited = set()
    for node in nodes:
        if node in visited:
            continue
        exports.update([ref for thing in node.quantum.inputs.values() for ref in thing])
        exports.update([ref for thing in node.quantum.outputs.values() for ref in thing])
        exports.update([ref for ref in node.quantum.initInputs.values()])
        before = qgraph.determineAncestorsOfQuantumNode(node)
        visited.add(node)
        if before:
            runner(before, exports, visited)


runner([node for node in qgraph.getNodesForTask(qgraph.findTaskDefByLabel('calibrate'))], exports)
resolved_refs = [butler.registry.findDataset(datasetType=ex.datasetType, dataId=ex.dataId,
                 collections=butler.registry.queryCollections()) for ex in exports]

with butler.export(filename='export.yaml', directory='rsp_data_export', transfer='copy') as export:
    export.saveDatasets(resolved_refs)
    export.saveCollection("HSC/calib")
    export.saveCollection("HSC/calib/DM-28636")
    export.saveCollection("HSC/calib/gen2/20180117")
    export.saveCollection("HSC/calib/gen2/20180117/unbounded")
    export.saveCollection("HSC/calib/DM-28636/unbounded")
    export.saveCollection("HSC/calib/gen2/20180117")
    export.saveCollection("HSC/calib/gen2/20200115")
    export.saveCollection("refcats/DM-28636")
