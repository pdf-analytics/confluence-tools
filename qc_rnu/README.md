# Confluence Tools Playground

## Instructions


1. In the Confluence Site (https://demo-site.atlassian.net), create a page, and add the 
   ‘QC - Read and Understood’ Macro for that page.

2. Clone the https://github.com/pdf-analytics/confluence-tools project locally

3. Create a **credentials.ini** file within the confluence-tools/qc_rnu directory

```
[CONFLUENCE]
url=https://demo-site.atlassian.net
username=email@address.com
password=token
```

4. Open a python console and execute the following :

```
import ConfluencePlayground 

playground = ConfluencePlayground()
rnu_dictionary = playground.get_rnu_in_page(page_id=775585805, rnu_id=775585805)
print(rnu_dictionary)

```

The outcome of the "get_rnu_in_page" method should return a list with content of the macro :

```
[[<User's full name>, <Last reviewed version>, <timestamp>, <status>, <status-style>, <timestamp-based-on-settings-timezone>, None]]

e.g. :
[['Evangelos Mantadakis', '6', 1571128222755, 'Accepted old version', 'moved', '10-15-2019 11:30', None]]

```
