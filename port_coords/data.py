from datapackage import Package

package = Package("https://datahub.io/core/un-locode/datapackage.json")

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
# for resource in package.resources:
#     if resource.descriptor["datahub"]["type"] == "derived/csv":
#         print(resource.read())

code_list = "code-list_csv"
country_codes = "country-codes_csv"
function_classifiers = "function-classifiers_csv"
status_indicator = "status-indicators_csv"
subdivision_codes = "subdivision-codes_csv"

