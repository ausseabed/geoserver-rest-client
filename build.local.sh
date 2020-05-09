#!/bin/bash
cd modules
# Tested using swagger-codegen-cli-3.0.19
for file in `cat ../list_of_modules.txt | grep "coverages.yaml"`
do
	rootname=`echo $file | sed "s/\..*//"` 
	echo $rootname
	mkdir "$rootname"
	 (cd $rootname; \
   swagger-codegen generate -l python -i ../../geoserver_yaml_cache/$file \
   --model-package "model" \
   --git-user-id "ausseabed" \
   --git-repo-id "geoserver-rest-client.git#subdirectory=modules/$rootname\&ignore=" \
   --additional-properties="packageName=gs_rest_api_$rootname,projectName=gs-rest-api-$rootname" 
    )
done
