---
layout: default
title: Graph Neural Network Based Adaptive Threat Detection for Cloud Identity and Access Management Logs
---

# Graph Neural Network Based Adaptive Threat Detection for Cloud Identity and Access Management Logs

**arXiv**: [2512.10280v1](https://arxiv.org/abs/2512.10280) | [PDF](https://arxiv.org/pdf/2512.10280.pdf)

**作者**: Venkata Tanuja Madireddy

---

## 💡 一句话要点

**提出基于图神经网络的云身份与访问管理日志自适应威胁检测框架，以应对传统方法对新威胁的不足。**

**关键词**: `图神经网络` `云安全` `身份与访问管理` `威胁检测` `自适应学习` `零信任分析`

## 📋 核心要点

1. 核心问题：云基础设施扩展导致身份与访问管理日志复杂化，传统规则或签名方法难以检测统计良性但上下文恶意的异常行为。
2. 方法要点：将IAM日志建模为异构动态图，利用图神经网络捕获实体间的时间、关系和上下文依赖，通过注意力聚合和图嵌入更新实现自适应学习。
3. 实验或效果：在合成和真实IAM数据集上评估，相比基线LSTM和GCN分类器，该方法实现了更高的检测精确率和召回率，并保持多租户云环境下的可扩展性。

## 📄 摘要（原文）

> The rapid expansion of cloud infrastructures and distributed identity systems has significantly increased the complexity and attack surface of modern enterprises. Traditional rule based or signature driven detection systems are often inadequate in identifying novel or evolving threats within Identity and Access Management logs, where anomalous behavior may appear statistically benign but contextually malicious. This paper presents a Graph Neural Network Based Adaptive Threat Detection framework designed to learn latent user resource interaction patterns from IAM audit trails in real time. By modeling IAM logs as heterogeneous dynamic graphs, the proposed system captures temporal, relational, and contextual dependencies across entities such as users, roles, sessions, and access actions. The model incorporates attention based aggregation and graph embedding updates to enable continual adaptation to changing cloud environments. Experimental evaluation on synthesized and real world IAM datasets demonstrates that the proposed method achieves higher detection precision and recall than baseline LSTM and GCN classifiers, while maintaining scalability across multi tenant cloud environments. The frameworks adaptability enables proactive mitigation of insider threats, privilege escalation, and lateral movement attacks, contributing to the foundation of AI driven zero trust access analytics. This work bridges the gap between graph based machine learning and operational cloud security intelligence.

