---
layout: default
title: LocalSearchBench: Benchmarking Agentic Search in Real-World Local Life Services
---

# LocalSearchBench: Benchmarking Agentic Search in Real-World Local Life Services

**arXiv**: [2512.07436v1](https://arxiv.org/abs/2512.07436) | [PDF](https://arxiv.org/pdf/2512.07436.pdf)

**作者**: Hang He, Chuhuai Yue, Chengqi Dong, Mingxue Tian, Zhenfeng Liu, Jiajun Chai, Xiaohan Wang, Yufei Zhang, Qun Liao, Guojun Yin, Wei Lin, Chengcheng Wan, Haiying Sun, Ting Su

---

## 💡 一句话要点

**提出LocalSearchBench基准以评估本地生活服务中的智能搜索代理性能**

**关键词**: `智能搜索代理` `本地生活服务` `多跳推理` `基准测试` `大推理模型` `垂直领域`

## 📋 核心要点

1. 核心问题：现有智能搜索研究多关注通用信息检索，缺乏针对本地生活服务等垂直领域的基准，该领域查询模糊且需多跳推理。
2. 方法要点：构建包含15万条高质量条目的基准，基于真实用户查询设计300个多跳问答任务，并开发统一交互环境LocalPlayground。
3. 实验或效果：实验显示，即使最先进的大推理模型（如DeepSeek-V3.1）在基准上正确率仅34.34%，凸显领域特定训练的必要性。

## 📄 摘要（原文）

> Recent advances in large reasoning models (LRMs) have enabled agentic search systems to perform complex multi-step reasoning across multiple sources. However, most studies focus on general information retrieval and rarely explores vertical domains with unique challenges. In this work, we focus on local life services and introduce LocalSearchBench, which encompass diverse and complex business scenarios. Real-world queries in this domain are often ambiguous and require multi-hop reasoning across merchants and products, remaining challenging and not fully addressed. As the first comprehensive benchmark for agentic search in local life services, LocalSearchBench includes over 150,000 high-quality entries from various cities and business types. We construct 300 multi-hop QA tasks based on real user queries, challenging agents to understand questions and retrieve information in multiple steps. We also developed LocalPlayground, a unified environment integrating multiple tools for agent interaction. Experiments show that even state-of-the-art LRMs struggle on LocalSearchBench: the best model (DeepSeek-V3.1) achieves only 34.34% correctness, and most models have issues with completeness (average 77.33%) and faithfulness (average 61.99%). This highlights the need for specialized benchmarks and domain-specific agent training in local life services. Code, Benchmark, and Leaderboard are available at localsearchbench.github.io.

