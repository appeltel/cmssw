//<<<<<< INCLUDES                                                       >>>>>>

//#include "Geometry/EcalPreshowerData/interface/DDTestAlgorithm.h"
#include "Geometry/EcalTestBeam/interface/DDTBH4Algo.h"
#include "DetectorDescription/Algorithm/interface/DDAlgorithmFactory.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"

DEFINE_SEAL_MODULE ();
//DEFINE_SEAL_PLUGIN (DDAlgorithmFactory, DDTestAlgorithm, "DDTestAlgorithm");

DEFINE_SEAL_PLUGIN (DDAlgorithmFactory, DDTBH4Algo, "DDTBH4Algo");

#include "Geometry/EcalTestBeam/interface/EcalTBHodoscopeGeometryEP.h"

DEFINE_ANOTHER_FWK_EVENTSETUP_MODULE(EcalTBHodoscopeGeometryEP);

#include "Geometry/EcalTestBeam/interface/EcalTBGeometryBuilder.h"

DEFINE_ANOTHER_FWK_EVENTSETUP_MODULE(EcalTBGeometryBuilder);
