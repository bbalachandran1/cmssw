import FWCore.ParameterSet.Config as cms

source = cms.Source("FedRawDataInputSource",
    getLSFromFilename = cms.untracked.bool(True),
    eventChunkSize = cms.untracked.uint32(32),
    eventChunkBlock = cms.untracked.uint32(32),
    numBuffers = cms.untracked.uint32(2),
    verifyAdler32 = cms.untracked.bool(True)
    )

