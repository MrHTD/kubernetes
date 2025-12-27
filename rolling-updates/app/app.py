from flask import Flask, render_template, jsonify
from kubernetes import client, config
import os

app = Flask(__name__)

# 1. Load Kubernetes Configuration
try:
    # This works when running INSIDE the cluster
    config.load_incluster_config()
except:
    # This works when running LOCALLY (for testing)
    config.load_kube_config()

v1 = client.CoreV1Api()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pods')
def get_pods():
    # 2. Get all pods with the label "app=rolling-app"
    label_selector = "app=rolling-app"
    pods = v1.list_namespaced_pod(namespace="default", label_selector=label_selector)
    
    pod_data = []
    for pod in pods.items:
        # 3. Extract Real Data
        name = pod.metadata.name
        status = pod.status.phase
        # We assume your image name ends in :v1 or :v2 to detect version
        image = pod.spec.containers[0].image 
        version = "v2" if "v2" in image else "v1"
        
        pod_data.append({
            "name": name,
            "status": status,
            "version": version,
            "image": image
        })
        
    return jsonify(pod_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)