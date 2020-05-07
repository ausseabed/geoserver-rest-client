#!/bin/bash
for file in `cat modules.txt | grep workspaces`
do
	rootname=`echo $file | sed "s/\..*//"` 
	echo $rootname
	mkdir "$rootname"
	 (cd $rootname; curl -X POST \
  https://generator3.swagger.io/api/generate \
  -H 'content-type: application/json' \
  -d '{
  "specURL" : "https://docs.geoserver.org/latest/en/api/1.0.0/'"$file"'",
  "lang" : "python",
  "options": 
  {
    "additionalProperties" :
    {
  "apiPackage": "api",
    "modelPackage": "model",
    "packageName":"gs_rest_api_'"$rootname"'",
    "projectName":"gs-rest-api-'"$rootname"'"
    }
  },
  "type" : "CLIENT",
  "codegenVersion" : "V3"
}' -o "$rootname".zip; unzip "$rootname".zip)
done
