import xhstt as xhstt

tagConstraints = []
idEventGroup = []
idConstraints = []

# for xml in root.findall('./Instances/Instance/Constraints'):
#     idCourse.append(xml.attrib.get('Id'))



for xml in xhstt.root.findall('./Instances/Instance/Constraints/'):
    tagConstraints.append(xml.tag)


dict_constraint = dict.fromkeys(tagConstraints)
# for key in dict_constraint:
#     print(key)

for xml in xhstt.root.findall('./Instances/Instance/Events/EventGroups/EventGroup'):
    idEventGroup.append(xml.attrib.get('Id'))

# for xml in root.findall('./Instances/Instance/Constraints/AssignTimeConstraint'):
#     idConstraints.append(xml.attrib.get('Id'))
x = 0
y = 0
resto_dict = {}
dictConstraint = {}
appliesto = []
timegroup = []
time = []
dict_teste = {}
dict_teste2 = {}
tagConstraint = []
z = 0
for xml in xhstt.root.findall('./Instances/Instance/Constraints/'):
    x = 0
    idConstraints.append(xml.attrib.get('Id'))
    tagConstraint.append(xml.tag)

    # print(len(xml))
    # print(xml.attrib)
    # print(teste)
    dict_teste = {}
    dict_teste['Id'] = idConstraints[y]
    dict_teste['Tag'] = tagConstraint[y]
    # print(idConstraints[y])
    resto_dict = {}
    while x < len(xml):
        # print(xml[4][0][0].attrib.get('Reference'))

        dict_teste[xml[x].tag] = xml[x].text
        resto_dict['Tag'] = tagConstraints[y]
        resto_dict[xml[x].tag] = xml[x].text
        if xml[x].tag == 'AppliesTo':
            for z in range(len(xml[4][0])):
                # print(len(xml[4][0]))
                # print(xml[4][0][z].attrib.get('Reference'))
                appliesto.append(xml[4][0][z].attrib.get('Reference'))

                # z += 1
            resto_dict[xml[x].tag] = appliesto
            dict_teste[xml[x].tag] = appliesto
        if xml[x].tag == 'TimeGroups':
            for z in range(len(xml[x])):
                # print(len(xml[4][0]))
                # print(xml[x].tag)
                # print(xml[x][0][z].attrib.get('Reference'))
                timegroup.append(xml[x][z].attrib.get('Reference'))

                # z += 1
            resto_dict[xml[x].tag] = timegroup
            dict_teste[xml[x].tag] = timegroup
        if xml[x].tag == 'Times':
            for z in range(len(xml[x])):
                # print(len(xml[4][0]))
                # print(xml[x].tag)
                # print(xml[x][0][z].attrib.get('Reference'))
                time.append(xml[x][z].attrib.get('Reference'))

                # z += 1
            resto_dict[xml[x].tag] = time
            dict_teste[xml[x].tag] = time


        dictConstraint[idConstraints[y]] = resto_dict
        dict_teste2[y] = dict_teste

        appliesto = []
        timegroup = []
        time = []
        x += 1
    # print(dict_teste2[y])
    y += 1
# print(dict_constraint)
# # print(x)
# print(f'\ndicionario de teste {dict_teste["Id"]}\n')
# print(len(dict_teste))
# print(f'\n{dict_teste2}\n')
#
# print(f'restrição {tagConstraints}\n')
# print(f'dentro das tags {teste}\n')
# print(f'idConstraints {idConstraints}\n')
# print(appliesto)
# # print(timegroup)
# print(f'dentro das tags das restrições {resto_dict}\n')
# print(f'dicionario com as restricoes {dictConstraint}\n')

# print(dictConstraint)
