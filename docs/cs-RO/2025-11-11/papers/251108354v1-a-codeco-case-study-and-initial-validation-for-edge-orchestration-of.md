---
layout: default
title: A CODECO Case Study and Initial Validation for Edge Orchestration of Autonomous Mobile Robots
---

# A CODECO Case Study and Initial Validation for Edge Orchestration of Autonomous Mobile Robots

**arXiv**: [2511.08354v1](https://arxiv.org/abs/2511.08354) | [PDF](https://arxiv.org/pdf/2511.08354.pdf)

**作者**: H. Zhu, T. Samizadeh, R. C. Sofia

---

## 💡 一句话要点

**提出CODECO编排以优化边缘自主移动机器人资源使用与通信稳定性**

**关键词**: `边缘编排` `自主移动机器人` `容器编排` `资源优化` `通信稳定性`

## 📋 核心要点

1. Kubernetes在移动机器人环境中假设稳定网络和充足资源不成立
2. 通过案例研究比较CODECO与Kubernetes在KinD环境中的性能
3. CODECO降低CPU消耗、稳定通信，但增加内存开销和延迟

## 📄 摘要（原文）

> Autonomous Mobile Robots (AMRs) increasingly adopt containerized micro-services across the Edge-Cloud continuum. While Kubernetes is the de-facto orchestrator for such systems, its assumptions of stable networks, homogeneous resources, and ample compute capacity do not fully hold in mobile, resource-constrained robotic environments.
>   This paper describes a case study on smart-manufacturing AMRs and performs an initial comparison between CODECO orchestration and standard Kubernetes using a controlled KinD environment. Metrics include pod deployment and deletion times, CPU and memory usage, and inter-pod data rates. The observed results indicate that CODECO offers reduced CPU consumption and more stable communication patterns, at the cost of modest memory overhead (10-15%) and slightly increased pod lifecycle latency due to secure overlay initialization.

