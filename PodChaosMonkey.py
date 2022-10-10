from kubernetes import client, config
from kubernetes.config import load_config
import pandas as pd
import numpy as np

config.load_incluster_config()
v1 = client.CoreV1Api()

def fetchPods(namespc):
    pods = v1.list_namespaced_pod(namespace=namespc)
    selectedpods = []
    if not pods.items:
        return None
    else:
        for p in pods.items:
            selectedpods.append(p.metadata.name)
            print(p.metadata.name)
        return selectedpods
    
def fetchTarget(pods):
    selectedpods = []
    if pods is not None:
        selectedpods += list(np.random.choice(pods,1))
    return selectedpods

namespc='workloads'
targets = fetchTarget(fetchPods(namespc))
if targets is not None:
    print(f"targets are {targets}")
    for victim in targets:
        v1.delete_namespaced_pod(victim,namespc)
        print(f"{victim} pod is deleted")
