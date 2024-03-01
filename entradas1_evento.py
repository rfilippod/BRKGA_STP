# todo: pegar tudo que o event possui, nome, eventgroupreference, absolutamente tudo
import xhstt as xhstt
"""
-----------------------------------------------------
Todos são metodos para se conseguem pegar algum valor necessário da entrada, seja esse valor
algum id, referencia ou nome

print(idCourse) -> ['gr_T1-S1', 'gr_T1-S2', 'gr_T1-S3', 'gr_T2-S1', 'gr_T2-S2', 'gr_T3-S1', 'gr_T3-S2', 'gr_T3-S3', 'gr_T4-S1', 'gr_T4-S2', 'gr_T4-S3', 'gr_T5-S2', 'gr_T5-S3', 'gr_T6-S1', 'gr_T6-S2', 'gr_T6-S3', 'gr_T7-S1', 'gr_T7-S3', 'gr_T8-S1', 'gr_T8-S2', 'gr_T8-S3']
print(idEventGroup) -> ['gr_AllEvents']
print(resourceReference) -> ['S3']
print(eventInternal) -> {'duration': ['2'], 'course': ['gr_T8-S3'], 'resourceReference': ['S3', 'T8']}
print(idDuration) -> {'T1-S1': {'duration': ['3'], 'course': ['gr_T1-S1'], 'resourceReference': ['S1', 'T1']}, 'T1-S2': {'duration': ['3'], 'course': ['gr_T1-S2'], 'resourceReference': ['S2', 'T1']}, 'T1-S3': {'duration': ['3'], 'course': ['gr_T1-S3'], 'resourceReference': ['S3', 'T1']}, 'T2-S1': {'duration': ['5'], 'course': ['gr_T2-S1'], 'resourceReference': ['S1', 'T2']}, 'T2-S2': {'duration': ['5'], 'course': ['gr_T2-S2'], 'resourceReference': ['S2', 'T2']}, 'T3-S1': {'duration': ['3'], 'course': ['gr_T3-S1'], 'resourceReference': ['S1', 'T3']}, 'T3-S2': {'duration': ['3'], 'course': ['gr_T3-S2'], 'resourceReference': ['S2', 'T3']}, 'T3-S3': {'duration': ['3'], 'course': ['gr_T3-S3'], 'resourceReference': ['S3', 'T3']}, 'T4-S1': {'duration': ['3'], 'course': ['gr_T4-S1'], 'resourceReference': ['S1', 'T4']}, 'T4-S2': {'duration': ['3'], 'course': ['gr_T4-S2'], 'resourceReference': ['S2', 'T4']}, 'T4-S3': {'duration': ['3'], 'course': ['gr_T4-S3'], 'resourceReference': ['S3', 'T4']}, 'T5-S2': {'duration': ['5'], 'course': ['gr_T5-S2'], 'resourceReference': ['S2', 'T5']}, 'T5-S3': {'duration': ['5'], 'course': ['gr_T5-S3'], 'resourceReference': ['S3', 'T5']}, 'T6-S1': {'duration': ['4'], 'course': ['gr_T6-S1'], 'resourceReference': ['S1', 'T6']}, 'T6-S2': {'duration': ['4'], 'course': ['gr_T6-S2'], 'resourceReference': ['S2', 'T6']}, 'T6-S3': {'duration': ['4'], 'course': ['gr_T6-S3'], 'resourceReference': ['S3', 'T6']}, 'T7-S1': {'duration': ['5'], 'course': ['gr_T7-S1'], 'resourceReference': ['S1', 'T7']}, 'T7-S3': {'duration': ['5'], 'course': ['gr_T7-S3'], 'resourceReference': ['S3', 'T7']}, 'T8-S1': {'duration': ['2'], 'course': ['gr_T8-S1'], 'resourceReference': ['S1', 'T8']}, 'T8-S2': {'duration': ['2'], 'course': ['gr_T8-S2'], 'resourceReference': ['S2', 'T8']}, 'T8-S3': {'duration': ['2'], 'course': ['gr_T8-S3'], 'resourceReference': ['S3', 'T8']}}
print(idEvent) -> ['T1-S1', 'T1-S2', 'T1-S3', 'T2-S1', 'T2-S2', 'T3-S1', 'T3-S2', 'T3-S3', 'T4-S1', 'T4-S2', 'T4-S3', 'T5-S2', 'T5-S3', 'T6-S1', 'T6-S2', 'T6-S3', 'T7-S1', 'T7-S3', 'T8-S1', 'T8-S2', 'T8-S3']

-----------------------------------------------------
"""
idCourse = []
idEventGroup = []
idEvent = []

for xml in xhstt.root.findall('./Instances/Instance/Events/EventGroups/Course'):
    idCourse.append(xml.attrib.get('Id'))

for xml in xhstt.root.findall('./Instances/Instance/Events/EventGroups/EventGroup'):
    idEventGroup.append(xml.attrib.get('Id'))

duration = []
course = []
idDuration = {}
eventInternal = {}
x = 0
resourceReference = []
for xml in xhstt.root.findall('./Instances/Instance/Events/Event'):
    eventInternal = {}
    course = []
    duration = []
    resourceReference = []
    idEvent.append(xml.attrib.get('Id'))
    keyIdEvent = xml.attrib.get('Id')
    duration.append(xml.find('Duration').text)
    course.append(xml.find('Course').attrib.get('Reference'))
    resourceReference.append(xml.find('Resources/Resource').attrib.get('Reference'))
    # k = []
    k = [x.attrib.get('Reference') for x in xml.findall('Resources/Resource')]
    y = [x.attrib.get('Reference') for x in xml.findall('Resources/Resource/ResourceType')]
    role = [x.text for x in xml.findall('Resources/Resource/Role')]
    eventGroups = [x.attrib.get('Reference') for x in xml.findall('EventGroups/EventGroup')]
    eventInternal['duration'] = duration
    eventInternal['course'] = course
    eventInternal['resourceReference'] = k
    if y:
        eventInternal['resourceTypeReference'] = y
    elif role:
        eventInternal['resourceTypeReference'] = role
    eventInternal['eventGroups'] = eventGroups
    idDuration[keyIdEvent] = eventInternal
    # print(eventGroups)

# print(f' idEventGroup: {idEventGroup}')
# print(f' id duration {idDuration}')
