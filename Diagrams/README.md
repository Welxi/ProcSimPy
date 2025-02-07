to view the C4 model you will need docker installed

read further at [Structurizr Lite Docs](https://docs.structurizr.com/lite/quickstart)

docker pull structurizr/lite
docker run -it --rm -p 8080:8080 -v PATH:/usr/local/structurizr structurizr/lite
docker run -it --rm -p 8080:8080 -v C:\spellbook\HePYaestus\Diagrams:/usr/local/structurizr structurizr/lite