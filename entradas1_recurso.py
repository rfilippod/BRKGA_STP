# todo: pegar tudo que o event possui, nome, eventgroupreference, absolutamente tudo
# todo: e colocar em um dict

"""
-----------------------------------------------------
Todos são metodos para se conseguem pegar algum valor necessário da entrada, seja esse valor
algum id, referencia ou nome
print(f'{idResourceType}\n') -> ['Teacher', 'Class']
print(f'{idResourceGroup}\n') -> ['gr_Teachers', 'gr_Classes']
print(f'{idResource}\n') -> ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'S1', 'S2', 'S3']
print(f'{referenceResourceType}\n') -> ['Teacher', 'Teacher', 'Teacher', 'Teacher', 'Teacher', 'Teacher', 'Teacher',
 'Teacher', 'Class', 'Class', 'Class']
print(f'{referenceResourceGroup}\n') -> ['gr_Teachers', 'gr_Teachers', 'gr_Teachers', 'gr_Teachers', 'gr_Teachers',
 'gr_Teachers', 'gr_Teachers', 'gr_Teachers', 'gr_Classes', 'gr_Classes', 'gr_Classes']

-----------------------------------------------------
"""

import xhstt as xhstt


idResourceType = []
idResourceGroup = []
idResource = []
referenceResourceType = []
referenceResourceGroup = []
time = {}
x = 0



for xml in xhstt.root.findall('./Instances/Instance/Resources/ResourceTypes/ResourceType'):
    idResourceType.append(xml.attrib.get('Id'))

for xml in xhstt.root.findall('./Instances/Instance/Resources/ResourceGroups/ResourceGroup'):
    idResourceGroup.append(xml.attrib.get('Id'))

for xml in xhstt.root.findall('./Instances/Instance/Resources/Resource'):
    idResource.append(xml.attrib.get('Id'))

for xml in xhstt.root.findall('./Instances/Instance/Resources/Resource/ResourceType'):
    referenceResourceType.append(xml.attrib.get('Reference'))

for xml in xhstt.root.findall('./Instances/Instance/Resources/Resource/ResourceGroups/ResourceGroup'):
    referenceResourceGroup.append(xml.attrib.get('Reference'))

# for i in range (len(idResource)):
#     for j in range (len(idResourceType)):
#         if referenceResourceType[i] == idResourceType[j]:
#             print(f'o {idResource[i]} é um {idResourceType[j]}')
#         if referenceResourceGroup[i] == idResourceGroup[j]:
#             print(f'o {idResource[i]} pertence ao grupo {idResourceGroup[j]}')

# print(idResourceType)
# print(idResourceGroup)
# print(idResource)
# print(referenceResourceType)
# print(referenceResourceGroup)

dict_resource_key = dict.fromkeys(idResource)

# print(dict_resource_key)
temp_resource = []
for i in range(len(idResource)):
    temp_resource.append(referenceResourceType[i])
    temp_resource.append(referenceResourceGroup[i])
    dict_resource_key[idResource[i]] = temp_resource
    temp_resource = []

#  print(f'dict_resource_key {dict_resource_key}')
