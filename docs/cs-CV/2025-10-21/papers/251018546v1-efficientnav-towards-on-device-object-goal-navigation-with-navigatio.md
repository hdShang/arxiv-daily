---
layout: default
title: EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval
---

# EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval

**arXiv**: [2510.18546v1](https://arxiv.org/abs/2510.18546) | [PDF](https://arxiv.org/pdf/2510.18546.pdf)

**作者**: Zebin Yang, Sunjian Zheng, Tong Xie, Tianshi Xu, Bo Yu, Fan Wang, Jie Tang, Shaoshan Liu, Meng Li

---

## 💡 一句话要点

**提出EfficientNav以解决设备端对象目标导航中的高延迟和低成功率问题**

**关键词**: `对象目标导航` `设备端推理` `记忆检索` `KV缓存优化` `语义感知` `导航地图`

## 📋 核心要点

1. 核心问题：设备端小语言模型在对象目标导航中因地图理解能力不足导致成功率下降和延迟高
2. 方法要点：采用语义感知记忆检索和离散记忆缓存优化导航地图处理与KV缓存重用
3. 实验或效果：在HM3D基准上成功率提升11.1%，延迟降低6.7倍实时和4.7倍端到端

## 📄 摘要（原文）

> Object-goal navigation (ObjNav) tasks an agent with navigating to the
> location of a specific object in an unseen environment. Embodied agents
> equipped with large language models (LLMs) and online constructed navigation
> maps can perform ObjNav in a zero-shot manner. However, existing agents heavily
> rely on giant LLMs on the cloud, e.g., GPT-4, while directly switching to small
> LLMs, e.g., LLaMA3.2-11b, suffer from significant success rate drops due to
> limited model capacity for understanding complex navigation maps, which
> prevents deploying ObjNav on local devices. At the same time, the long prompt
> introduced by the navigation map description will cause high planning latency
> on local devices. In this paper, we propose EfficientNav to enable on-device
> efficient LLM-based zero-shot ObjNav. To help the smaller LLMs better
> understand the environment, we propose semantics-aware memory retrieval to
> prune redundant information in navigation maps. To reduce planning latency, we
> propose discrete memory caching and attention-based memory clustering to
> efficiently save and re-use the KV cache. Extensive experimental results
> demonstrate that EfficientNav achieves 11.1% improvement in success rate on
> HM3D benchmark over GPT-4-based baselines, and demonstrates 6.7x real-time
> latency reduction and 4.7x end-to-end latency reduction over GPT-4 planner. Our
> code will be released soon.

