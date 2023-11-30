#!/usr/bin/env python

from lsst.daf.butler import Butler, CollectionType
butler = Butler('RSP_CHECK_REPO', writeable=True)
butler.registry.registerCollection('HSC/defaults', CollectionType.CHAINED,
                                   'A CHAINED collection to package up the collections to be queried')
colls = [el for el in butler.registry.queryCollections() if el != 'HSC/defaults']
butler.registry.setCollectionChain('HSC/defaults', colls)
