import pandas as pd
import os

file_path = '../../../../omegaTop10000.csv'

'''
# Read the CSV data
data = pd.read_csv(file_path)

# only keep the ecosystem and name
data = data[['Ecosystem', 'Package Name']]

#set(data.iloc[:,0])
#{'pypi', 'bower', 'maven', 'cocoapods', 'other', 'rubygems', 'Maven', 'Packagist', 'platform', 'cran', 'npm', 'github', 'conda', 'homebrew', 'packagist', 'nuget', 'cargo', 'go', 'clojars', 'pub', 'debian'}
# So 'pypi' and 'npm' should be working correctly

# filter to only pypi and npm *Just for now*
data = data[(data.iloc[:,0] == 'pypi') | (data.iloc[:,0] == 'npm')]
# data.reset_index() [no need for this]

for row in data.itertuples():
    name_ecosystem = row[1]
    name_package = row[2]
    s = "docker run -v ./%s/%s:/opt/export/%s/%s --env-file .env openssf/omega-toolshed:latest pkg:%s/%s@latest" % (name_ecosystem, name_package, name_ecosystem, name_package, name_ecosystem, name_package)
    os.system(s)
    break # testing for just one for now

# Print the data
#print(data.head())

'''

#What do we need as input?
name = input("Enter name:")
url = input("Enter url:")    #"https://github.com/" + name + "/" + name
ver = "0" # default to 0
pkg = "pkg:github/" + name + "@" + ver + "?local=true"

# download the repo
print("cd /opt/local_source")
print("git clone " + url)

# tar the repo
print("\ntar -czf " + name + ".tar.gz " + name)

# run the runtools
print("cd /opt/toolshed")
print("./runtools.sh " + pkg)
