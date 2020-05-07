#!/bin/bash
cd modules
# Tested using swagger-codegen-cli-3.0.19
for file in `cat ../modules.txt | grep workspaces`
do
	rootname=`echo $file | sed "s/\..*//"` 
	echo $rootname
	mkdir "$rootname"
	 (cd $rootname; \
   swagger-codegen generate -l python -i ../../geoserver_yaml_cache/$file \
   --model-package "model" \
   --additional-properties="packageName=gs_rest_api_$rootname,projectName=gs-rest-api-$rootname" 
    )
done
