# Accelerator Log

## Options
```json
{
  "gitRepository" : "https://github.com/afewell/my-qabot-1",
  "projectName" : "simple-accelerator",
  "vectorStoreIndexStorageContext" : "https://scrapyfarm.blob.core.windows.net/scrapyfarm/tanzubot_storage-0_2.tar.gz"
}
```
## Log
```
┏ engine (Chain)
┃  Info Running Chain(GeneratorValidationTransform, UniquePath)
┃ ┏ ┏ engine.transformations[0].validated (Combo)
┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ engine.transformations[0].validated.delegate (Chain)
┃ ┃ ┃  Info Running Chain(Merge, UniquePath)
┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0] (Merge)
┃ ┃ ┃ ┃  Info Running Merge(Combo)
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0] (Combo)
┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate (Chain)
┃ ┃ ┃ ┃ ┃  Info Running Chain(Include, ReplaceText, ReplaceText, ReplaceText, ReplaceText)
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate.transformations[0] (Include)
┃ ┃ ┃ ┃ ┃ ┃  Info Will include [**/*]
┃ ┃ ┃ ┃ ┃ ┃ Debug .github/workflows/semantic_release.yml matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug .releaserc.json matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug .tanzuignore matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug CHANGELOG.md matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug Procfile matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug README.md matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug ingest.py matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug init.py matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug k8s/qabot1-deployment.yaml matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug k8s/qabot1-ingress-contour.yaml matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug k8s/qabot1-ingress-nginx.yaml matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug requirements.txt matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┗ Debug web.py matched [**/*] -> included
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate.transformations[1] (ReplaceText)
┃ ┃ ┃ ┃ ┃ ┗  Info Will replace [my-qabot-1->simple-accelerator]
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate.transformations[2] (ReplaceText)
┃ ┃ ┃ ┃ ┃ ┗  Info Will replace [https://git.example.com/my-repo->https://github.com/a...(truncated)]
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate.transformations[3] (ReplaceText)
┃ ┃ ┃ ┃ ┃ ┗  Info Will replace [https://github.com/afewell/qabot-1-accelerator->https://github.com/a...(truncated)]
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate.transformations[4] (ReplaceText)
┃ ┃ ┃ ┗ ┗ ┗  Info Will replace [My_Vector_Store_Index_Storage_Context->https://scrapyfarm.b...(truncated)]
┃ ┗ ┗ ╺ engine.transformations[0].validated.delegate.transformations[1] (UniquePath)
┗ ╺ engine.transformations[1] (UniquePath)
```
