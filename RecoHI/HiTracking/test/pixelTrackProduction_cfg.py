import FWCore.ParameterSet.Config as cms
import sys


process = cms.Process("PIXELTRACKRECO")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration/StandardSequences/Reconstruction_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.ReconstructionHeavyIons_cff")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(200) )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.MessageLogger.cerr.FwkReport.reportEvery = 10

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_53_LV6::All', '')

# trigger selection 
process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
process.hltMinBiasHFOrBSC = process.hltHighLevel.clone()
process.hltMinBiasHFOrBSC.HLTPaths = ["HLT_HIMinBiasHfOrBSC_*","HLT_HIUCC*_*"]
process.hltMinBiasHFOrBSC.andOr = cms.bool(True) # this is the default meaning either of the paths above
process.hltMinBiasHFOrBSC.throw = cms.bool(False)



# Common offline event selection
process.load("HeavyIonsAnalysis.Configuration.collisionEventSelection_cff")

# Coincidence of HF towers (threshold 3)
#process.load("HeavyIonsAnalysis.Configuration.hfCoincFilter_cff")
#process.filter_step = cms.Path(process.hfCoincFilter3)

# selection of non-fake vertex (i.e. at least one pixel track)
#process.primaryVertexFilter = cms.EDFilter("VertexSelector",
#                                           src = cms.InputTag("hiSelectedVertex"),
#                                           cut = cms.string("!isFake && abs(z) <= 10 && position.Rho <= 2"),
#                                           filter = cms.bool(True),   # otherwise it won't filter the events, instead making an empty vertex collection
 #                                          )

# Cluster-shape filter re-run offline
#process.load("HLTrigger.special.hltPixelClusterShapeFilter_cfi")
#process.hltPixelClusterShapeFilter.inputTag = "siPixelRecHits"
#process.filter_step = cms.Path(process.hfCoincFilter3*process.siPixelRecHits*process.hltPixelClusterShapeFilter)


# Reject BSC beam halo L1 technical bits
#process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff")
#process.load("HLTrigger.HLTfilters.hltLevel1GTSeed_cfi")
#process.noBSChalo = process.hltLevel1GTSeed.clone(
#        L1TechTriggerSeeding = cms.bool(True),
#        L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)')
#        )
#
process.filter_step = cms.Path(process.hltMinBiasHFOrBSC *
                               process.collisionEventSelection *
                               process.hiConformalPixelTracks *
                               process.hiPixelOnlyStepSelector *
                               process.hiHighPtStepSelector *
                               process.hiGeneralAndPixelTracks 
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/hidata/HIRun2011/HIMinBiasUPC/RECO/14Mar2014-v2/00014/8444772D-F3AF-E311-A462-FA163E99DECA.root'
#'/store/hidata/HIRun2011/HIMinBiasUPC/RECO/14Mar2014-v2/00014/807448C0-F4AF-E311-8EA3-FA163E2E5B23.root',
#'/store/hidata/HIRun2011/HIMinBiasUPC/RECO/14Mar2014-v2/00014/867550C5-F4AF-E311-8980-FA163E11930F.root'
)
                            )


process.output = cms.OutputModule("PoolOutputModule",
                                  outputCommands = process.RECOEventContent.outputCommands,
                                  fileName = cms.untracked.string('pixeltrackreco.root'),
                                  SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filter_step')),
                                  dataset = cms.untracked.PSet(
    dataTier = cms.untracked.string('RECO'))
                                  )

#Drop everything
process.output.outputCommands = ['drop *_*_*_*']

#Keeping tracks and pixel tracks
process.output.outputCommands += ['keep TrackingRecHitsOwned_hiConformalPixelTracks_*_*']
process.output.outputCommands += ['keep TrackingRecHitsOwned_hiGeneralAndPixelTracks_*_*']
process.output.outputCommands += ['keep recoTracks_hiConformalPixelTracks_*_*']
process.output.outputCommands += ['keep recoTracks_hiGeneralAndPixelTracks_*_*']
process.output.outputCommands += ['keep recoTrackExtras_hiConformalPixelTracks_*_*']
process.output.outputCommands += ['keep recoTrackExtras_hiGeneralAndPixelTracks_*_*']

process.output_step = cms.EndPath(process.output)



process.schedule = cms.Schedule(process.filter_step,
                            process.output_step
)
