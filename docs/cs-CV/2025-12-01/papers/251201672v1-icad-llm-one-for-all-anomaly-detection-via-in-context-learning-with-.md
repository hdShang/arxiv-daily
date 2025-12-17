---
layout: default
title: ICAD-LLM: One-for-All Anomaly Detection via In-Context Learning with Large Language Models
---

# ICAD-LLM: One-for-All Anomaly Detection via In-Context Learning with Large Language Models

**arXiv**: [2512.01672v1](https://arxiv.org/abs/2512.01672) | [PDF](https://arxiv.org/pdf/2512.01672.pdf)

**作者**: Zhongyuan Wu, Jingyuan Wang, Zexuan Cheng, Yilong Zhou, Weizhi Wang, Juhua Pu, Chao Li, Changqing Ma

---

## 💡 一句话要点

**提出ICAD-LLM框架，利用大语言模型上下文学习实现多模态异常检测统一处理**

**关键词**: `异常检测` `上下文学习` `大语言模型` `多模态处理` `跨域泛化`

## 📋 核心要点

1. 核心问题：现有异常检测方法难以处理异构数据模态且缺乏跨域泛化能力
2. 方法要点：基于上下文异常检测范式，通过大语言模型统一处理时间序列、日志等数据
3. 实验或效果：在多种任务上表现竞争性，泛化能力强，降低部署成本

## 📄 摘要（原文）

> Anomaly detection (AD) is a fundamental task of critical importance across numerous domains. Current systems increasingly operate in rapidly evolving environments that generate diverse yet interconnected data modalities -- such as time series, system logs, and tabular records -- as exemplified by modern IT systems. Effective AD methods in such environments must therefore possess two critical capabilities: (1) the ability to handle heterogeneous data formats within a unified framework, allowing the model to process and detect multiple modalities in a consistent manner during anomalous events; (2) a strong generalization ability to quickly adapt to new scenarios without extensive retraining. However, most existing methods fall short of these requirements, as they typically focus on single modalities and lack the flexibility to generalize across domains. To address this gap, we introduce a novel paradigm: In-Context Anomaly Detection (ICAD), where anomalies are defined by their dissimilarity to a relevant reference set of normal samples. Under this paradigm, we propose ICAD-LLM, a unified AD framework leveraging Large Language Models' in-context learning abilities to process heterogeneous data within a single model. Extensive experiments demonstrate that ICAD-LLM achieves competitive performance with task-specific AD methods and exhibits strong generalization to previously unseen tasks, which substantially reduces deployment costs and enables rapid adaptation to new environments. To the best of our knowledge, ICAD-LLM is the first model capable of handling anomaly detection tasks across diverse domains and modalities.

