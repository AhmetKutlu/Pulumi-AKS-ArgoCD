1. In order to create the infrastructure, run "pulumi up" at infra directory.
2. Get AKS credentials to connect to the cluster.
3. Create argocd, prod, staging and dev namespaces in Kubernetes cluster using kubectl.
4. Install ArgoCD to argocd namespace in Kubernetes cluster using Helm.
5. Install ArgoCD image updater to argocd namespace in Kubernetes cluster using Helm.
6. Create ArgoCD applications in argocd namespace for each environment using manifest files in argo-cd-apps directory.