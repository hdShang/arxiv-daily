---
layout: default
title: AskNearby: An LLM-Based Application for Neighborhood Information Retrieval and Personalized Cognitive-Map Recommendations
---

# AskNearby: An LLM-Based Application for Neighborhood Information Retrieval and Personalized Cognitive-Map Recommendations

**arXiv**: [2512.02502v1](https://arxiv.org/abs/2512.02502) | [PDF](https://arxiv.org/pdf/2512.02502.pdf)

**作者**: Luyao Niu, Zhicheng Deng, Boyang Li, Nuoxian Huang, Ruiqi Liu, Wenjia Zhang

---

## 💡 一句话要点

**提出AskNearby应用，通过RAG与认知地图模型解决15分钟生活圈信息可及性问题。**

**关键词**: `15分钟城市` `检索增强生成` `认知地图` `本地信息检索` `个性化推荐` `社区应用`

## 📋 核心要点

1. 核心问题：现有基于位置系统忽视局部决策的空间、时间和认知因素，导致本地生活信息可及性不足。
2. 方法要点：结合三层RAG管道（图、语义向量、地理检索）与用户认知地图模型，实现检索与推荐统一。
3. 实验或效果：在真实社区数据集上，AskNearby在检索准确性和推荐质量上显著优于基线，部署验证有效。

## 📄 摘要（原文）

> The "15-minute city" envisions neighborhoods where residents can meet daily needs via a short walk or bike ride. Realizing this vision requires not only physical proximity but also efficient and reliable access to information about nearby places, services, and events. Existing location-based systems, however, focus mainly on city-level tasks and neglect the spatial, temporal, and cognitive factors that shape localized decision-making. We conceptualize this gap as the Local Life Information Accessibility (LLIA) problem and introduce AskNearby, an AI-driven community application that unifies retrieval and recommendation within the 15-minute life circle. AskNearby integrates (i) a three-layer Retrieval-Augmented Generation (RAG) pipeline that synergizes graph-based, semantic-vector, and geographic retrieval with (ii) a cognitive-map model that encodes each user's neighborhood familiarity and preferences. Experiments on real-world community datasets demonstrate that AskNearby significantly outperforms LLM-based and map-based baselines in retrieval accuracy and recommendation quality, achieving robust performance in spatiotemporal grounding and cognitive-aware ranking. Real-world deployments further validate its effectiveness. By addressing the LLIA challenge, AskNearby empowers residents to more effectively discover local resources, plan daily activities, and engage in community life.

