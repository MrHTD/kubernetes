# Kubernetes Deployment Strategies

This project demonstrates **real-world Kubernetes deployment strategies** using clean and modular YAML manifests.  
It focuses on **traffic flow, pod ownership, and safe application rollouts**.

---

## 🚀 Strategies Covered

### 1. Blue-Green Deployment
- Two environments: **Blue (current)** and **Green (new)**
- Traffic is switched instantly via Service selector
- Enables zero-downtime releases and fast rollback

### 2. Canary Deployment
- Gradual rollout of a new version
- Small percentage of traffic routed to Canary
- Traffic split handled using **Gateway API + HTTPRoute**

---

## 📁 Directory Structure

```text
deployment-strategies/
├── blue-green/
│   ├── deployment-blue.yaml
│   ├── deployment-green.yaml
│   └── service.yaml
│   ├── gateway.yaml
│   ├── httproute.yaml
│   └── loadbalancer.yaml
│
├── canary/
│   ├── deployment-stable.yaml
│   ├── deployment-canary.yaml
│   ├── service.yaml
│   ├── gateway.yaml
│   ├── httproute.yaml
│   └── loadbalancer.yaml
```
## Canary Deployment Traffic Flow

```text
User
 ↓
LoadBalancer (External)
 ↓
Gateway
 ↓
HTTPRoute (Traffic Splitting)
 ↓
Service
 ↓
Pods (Stable + Canary)
```
Example traffic split:

- 90% → Stable version
- 10% → Canary version