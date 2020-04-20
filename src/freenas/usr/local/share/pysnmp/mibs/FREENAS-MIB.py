# PySNMP SMI module. Autogenerated from smidump -f python FREENAS-MIB
# by libsmi2pysnmp-0.1.3 at Sun May 12 20:39:39 2019,
# Python version sys.version_info(major=2, minor=7, micro=15, releaselevel='candidate', serial=1)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")

# Types

class AlertLevelType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,2,3,5,7,4,6,)
    namedValues = NamedValues(("info", 1), ("notice", 2), ("warning", 3), ("error", 4), ("critical", 5), ("alert", 6), ("emergency", 7), )
    
class ZPoolHealthType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,5,4,1,0,3,)
    namedValues = NamedValues(("online", 0), ("degraded", 1), ("faulted", 2), ("offline", 3), ("unavail", 4), ("removed", 5), )
    

# Objects

freeNas = ModuleIdentity((1, 3, 6, 1, 4, 1, 50536)).setRevisions(("2019-05-12 00:00",))
if mibBuilder.loadTexts: freeNas.setOrganization("www.ixsystems.com")
if mibBuilder.loadTexts: freeNas.setContactInfo("postal:   2490 Kruse Dr\nSan Jose, CA 95131\n\nemail:    support@iXsystems.com")
if mibBuilder.loadTexts: freeNas.setDescription("")
zfs = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1))
zpool = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 1))
zpoolTable = MibTable((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1))
if mibBuilder.loadTexts: zpoolTable.setDescription("")
zpoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1)).setIndexNames((0, "FREENAS-MIB", "zpoolIndex"))
if mibBuilder.loadTexts: zpoolEntry.setDescription("")
zpoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: zpoolIndex.setDescription("")
zpoolDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolDescr.setDescription("")
zpoolAllocationUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolAllocationUnits.setDescription("")
zpoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zpoolSize.setDescription("")
zpoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolUsed.setDescription("")
zpoolAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolAvailable.setDescription("")
zpoolHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 7), ZPoolHealthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolHealth.setDescription("The current health of the containing pool, as reported\nby zpool status.")
zpoolReadOps = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadOps.setDescription("The number of read I/O operations sent to the pool or device,\nincluding metadata requests (averaged since system booted).")
zpoolWriteOps = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteOps.setDescription("The number of write I/O operations sent to the pool or device\n(averaged since system booted).")
zpoolReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadBytes.setDescription("The bandwidth of all read operations (including metadata),\nexpressed as units per second (averaged since system booted)")
zpoolWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteBytes.setDescription("The bandwidth of all write operations, expressed as units per\nsecond (averaged since system booted).")
zpoolReadOps1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadOps1sec.setDescription("The number of read I/O operations sent to the pool or device,\nincluding metadata requests (over 1 second interval).")
zpoolWriteOps1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteOps1sec.setDescription("The number of write I/O operations sent to the pool or device\n(over 1 second interval).")
zpoolReadBytes1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadBytes1sec.setDescription("The bandwidth of all read operations (including metadata),\nexpressed as units per second (over 1 second interval)")
zpoolWriteBytes1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteBytes1sec.setDescription("The bandwidth of all write operations, expressed as units per\nsecond (over 1 second interval).")
dataset = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 2))
datasetTable = MibTable((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1))
if mibBuilder.loadTexts: datasetTable.setDescription("")
datasetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1)).setIndexNames((0, "FREENAS-MIB", "datasetIndex"))
if mibBuilder.loadTexts: datasetEntry.setDescription("")
datasetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: datasetIndex.setDescription("")
datasetDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetDescr.setDescription("")
datasetAllocationUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetAllocationUnits.setDescription("")
datasetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: datasetSize.setDescription("")
datasetUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetUsed.setDescription("")
datasetAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetAvailable.setDescription("")
zvol = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 3))
zvolTable = MibTable((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1))
if mibBuilder.loadTexts: zvolTable.setDescription("")
zvolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1)).setIndexNames((0, "FREENAS-MIB", "zvolIndex"))
if mibBuilder.loadTexts: zvolEntry.setDescription("")
zvolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: zvolIndex.setDescription("")
zvolDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolDescr.setDescription("")
zvolAllocationUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolAllocationUnits.setDescription("")
zvolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zvolSize.setDescription("")
zvolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolUsed.setDescription("")
zvolAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolAvailable.setDescription("")
zvolReferenced = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolReferenced.setDescription("")
arc = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 4))
zfsArcSize = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcSize.setDescription("")
zfsArcMeta = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcMeta.setDescription("")
zfsArcData = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcData.setDescription("")
zfsArcHits = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcHits.setDescription("")
zfsArcMisses = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcMisses.setDescription("")
zfsArcC = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcC.setDescription("")
zfsArcP = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcP.setDescription("")
zfsArcMissPercent = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcMissPercent.setDescription("Arc Miss Percentage.\n(Note: Floating precision sent across SNMP as a String")
zfsArcCacheHitRatio = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcCacheHitRatio.setDescription("Arc Cache Hit Ration Percentage.\n(Note: Floating precision sent across SNMP as a String")
zfsArcCacheMissRatio = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcCacheMissRatio.setDescription("Arc Cache Miss Ration Percentage.\n(Note: Floating precision sent across SNMP as a String")
l2arc = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 5))
zfsL2ArcHits = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcHits.setDescription("")
zfsL2ArcMisses = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcMisses.setDescription("")
zfsL2ArcRead = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcRead.setDescription("")
zfsL2ArcWrite = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcWrite.setDescription("")
zfsL2ArcSize = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcSize.setDescription("")
zil = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 6))
zfsZilstatOps1sec = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 6, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsZilstatOps1sec.setDescription("The ops column parsed from the command zilstat 1 1")
zfsZilstatOps5sec = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 6, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsZilstatOps5sec.setDescription("The ops column parsed from the command zilstat 5 1")
zfsZilstatOps10sec = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 6, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsZilstatOps10sec.setDescription("The ops column parsed from the command zilstat 10 1")
notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 2))
notificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 2, 1))
notificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 2, 2))
alertId = MibScalar((1, 3, 6, 1, 4, 1, 50536, 2, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertId.setDescription("")
alertLevel = MibScalar((1, 3, 6, 1, 4, 1, 50536, 2, 2, 2), AlertLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertLevel.setDescription("")
alertMessage = MibScalar((1, 3, 6, 1, 4, 1, 50536, 2, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertMessage.setDescription("")

# Augmentions

# Notifications

alert = NotificationType((1, 3, 6, 1, 4, 1, 50536, 2, 1, 1)).setObjects(*(("FREENAS-MIB", "alertMessage"), ("FREENAS-MIB", "alertLevel"), ("FREENAS-MIB", "alertId"), ) )
if mibBuilder.loadTexts: alert.setDescription("An alert raised")
alertCancellation = NotificationType((1, 3, 6, 1, 4, 1, 50536, 2, 1, 2)).setObjects(*(("FREENAS-MIB", "alertId"), ) )
if mibBuilder.loadTexts: alertCancellation.setDescription("An alert cancelled")

# Exports

# Module identity
mibBuilder.exportSymbols("FREENAS-MIB", PYSNMP_MODULE_ID=freeNas)

# Types
mibBuilder.exportSymbols("FREENAS-MIB", AlertLevelType=AlertLevelType, ZPoolHealthType=ZPoolHealthType)

# Objects
mibBuilder.exportSymbols("FREENAS-MIB", freeNas=freeNas, zfs=zfs, zpool=zpool, zpoolTable=zpoolTable, zpoolEntry=zpoolEntry, zpoolIndex=zpoolIndex, zpoolDescr=zpoolDescr, zpoolAllocationUnits=zpoolAllocationUnits, zpoolSize=zpoolSize, zpoolUsed=zpoolUsed, zpoolAvailable=zpoolAvailable, zpoolHealth=zpoolHealth, zpoolReadOps=zpoolReadOps, zpoolWriteOps=zpoolWriteOps, zpoolReadBytes=zpoolReadBytes, zpoolWriteBytes=zpoolWriteBytes, zpoolReadOps1sec=zpoolReadOps1sec, zpoolWriteOps1sec=zpoolWriteOps1sec, zpoolReadBytes1sec=zpoolReadBytes1sec, zpoolWriteBytes1sec=zpoolWriteBytes1sec, dataset=dataset, datasetTable=datasetTable, datasetEntry=datasetEntry, datasetIndex=datasetIndex, datasetDescr=datasetDescr, datasetAllocationUnits=datasetAllocationUnits, datasetSize=datasetSize, datasetUsed=datasetUsed, datasetAvailable=datasetAvailable, zvol=zvol, zvolTable=zvolTable, zvolEntry=zvolEntry, zvolIndex=zvolIndex, zvolDescr=zvolDescr, zvolAllocationUnits=zvolAllocationUnits, zvolSize=zvolSize, zvolUsed=zvolUsed, zvolAvailable=zvolAvailable, zvolReferenced=zvolReferenced, arc=arc, zfsArcSize=zfsArcSize, zfsArcMeta=zfsArcMeta, zfsArcData=zfsArcData, zfsArcHits=zfsArcHits, zfsArcMisses=zfsArcMisses, zfsArcC=zfsArcC, zfsArcP=zfsArcP, zfsArcMissPercent=zfsArcMissPercent, zfsArcCacheHitRatio=zfsArcCacheHitRatio, zfsArcCacheMissRatio=zfsArcCacheMissRatio, l2arc=l2arc, zfsL2ArcHits=zfsL2ArcHits, zfsL2ArcMisses=zfsL2ArcMisses, zfsL2ArcRead=zfsL2ArcRead, zfsL2ArcWrite=zfsL2ArcWrite, zfsL2ArcSize=zfsL2ArcSize, zil=zil, zfsZilstatOps1sec=zfsZilstatOps1sec, zfsZilstatOps5sec=zfsZilstatOps5sec, zfsZilstatOps10sec=zfsZilstatOps10sec, notifications=notifications, notificationPrefix=notificationPrefix, notificationObjects=notificationObjects, alertId=alertId, alertLevel=alertLevel, alertMessage=alertMessage)

# Notifications
mibBuilder.exportSymbols("FREENAS-MIB", alert=alert, alertCancellation=alertCancellation)

