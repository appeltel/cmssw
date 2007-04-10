// Here are the necessary incantations to declare your module to the
// framework, so it can be referenced in a cmsRun file.
//
#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "HLTrigger/HLTanalyzers/interface/L1TrigReport.h"
#include "HLTrigger/HLTanalyzers/interface/HLTrigReport.h"

#include "HLTrigger/HLTanalyzers/interface/HLTAnalyzer.h"

DEFINE_SEAL_MODULE();

DEFINE_ANOTHER_FWK_MODULE(L1TrigReport);
DEFINE_ANOTHER_FWK_MODULE(HLTrigReport);

DEFINE_ANOTHER_FWK_MODULE(HLTAnalyzer);
