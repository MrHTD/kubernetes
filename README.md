# Helm Chart

Helm is a package manager for Kubernetes that simplifies the deployment and management of applications. It uses "charts," which are pre-configured Kubernetes resources, to define, install, and upgrade applications.

## Why Use Helm?

- **Simplifies Deployment**: Helm charts bundle Kubernetes manifests, making it easier to deploy complex applications.
- **Version Control**: Helm allows you to manage application versions and rollbacks.
- **Reusable Configurations**: Charts can be customized with values files, enabling reuse across environments.

## Key Concepts

- **Chart**: A collection of files that describe a set of Kubernetes resources.
- **Release**: An instance of a chart running in a Kubernetes cluster.
- **Repository**: A collection of Helm charts.

## Getting Started with Helm

1. **Install Helm**: Follow the [Helm installation guide](https://helm.sh/docs/intro/install/).
2. **Add a Repository**: Add a chart repository, such as the official Helm stable repository:
    ```bash
    helm repo add stable https://charts.helm.sh/stable
    ```
3. **Search for Charts**: Find charts in the repository:
    ```bash
    helm search repo stable
    ```
4. **Install a Chart**: Deploy an application using a chart:
    ```bash
    helm install my-release stable/<chart-name>
    ```
5. **Upgrade or Rollback**: Manage application versions with:
    ```bash
    helm upgrade my-release stable/<chart-name>
    helm rollback my-release <revision>
    ```

## Resources

- [Helm Documentation](https://helm.sh/docs/)
- [Artifact Hub](https://artifacthub.io/) - A central repository for Helm charts.
- [Helm Charts Repository](https://github.com/helm/charts) Kubernetes Learning Repository

This repository contains resources and examples for learning Kubernetes.