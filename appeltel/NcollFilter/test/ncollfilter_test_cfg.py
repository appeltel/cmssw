import FWCore.ParameterSet.Config as cms

process = cms.Process('ANA')
process.load('Configuration.StandardSequences.Services_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

#process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( 
'/store/user/appelte1/HYDJET_MinBias_5020GeV_HIRun2015Development_7_2_0_pre6_v2/HYDJET_MinBias_5020GeV_HIRun2015Development_7_2_0_pre6_v2_HLTDEBUG/1cd0ca6c61f855318bc29f97df0adbcb/RAW_3_1_Bju.root'
  )
)

process.load('appeltel.NcollFilter.NcollFilter_cfi')
process.ncFilter = process.ncollFilter.clone(
    ncollmax = 1000
)

process.p = cms.Path( process.ncFilter)
