# 1. Terminology

- GCP: Google Cloud Platform
- GCPC: Google Cloud Platform Console
- Bucket:


# 2. General
| Description            | Command              |
| :---------------------------------------------------- |:-------------------------------------------------|
| login to glcoud account | `gcloud auth <account>` |
| help on topic | `gsutil help <topic>` |
| list all the buckets | `gsutil ls` |

# 3. Resource handling
| description            | command              |
| :---------------------------------------------------- |:-------------------------------------------------|
| create bucket | `gsutil mb gs://<bucket_name>` |
| delete bucket | `gsutil rb gs://<bucket_name>` |
| copy local file to bucket/object | `gsutil cp <file_name> gs://<bucket_name>/<object_name>` |
| copy local file to bucket | `gsutil cp <file_name> gs://<bucket_name>/` |
| move local file to bucket/object | `gsutil mv <file_name> gs://<bucket_name>/<object_name>/<target_file_name>` |
| remove an object on cloud | `gsutil rm gs://<bucket_name>/<object_name>` |
| get all public url to all objects in a bucket or an object | `gsutil ls gs://<bucket_name>/<object_name> | sed 's/gs:\//https:\/\/storage.googleapis.com/'` |

# 3. Authentication
| Description            | Command              |
| :---------------------------------------------------- |:-------------------------------------------------|
| login to gcloud account | `gcloud auth <account>` |
| grant read permission for all users to read all files in an object  | `gsutil acl ch -u AllUsers:r gs://<bucket_name>/<object_name>/*` |


