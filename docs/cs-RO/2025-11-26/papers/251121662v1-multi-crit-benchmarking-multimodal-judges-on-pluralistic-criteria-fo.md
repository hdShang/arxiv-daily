---
layout: default
title: Multi-Crit: Benchmarking Multimodal Judges on Pluralistic Criteria-Following
---

# Multi-Crit: Benchmarking Multimodal Judges on Pluralistic Criteria-Following

**arXiv**: [2511.21662v1](https://arxiv.org/abs/2511.21662) | [PDF](https://arxiv.org/pdf/2511.21662.pdf)

**作者**: Tianyi Xiong, Yi Ge, Ming Li, Zuolong Zhang, Pranav Kulkarni, Kaishen Wang, Qi He, Zeying Zhu, Chenxi Liu, Ruibo Chen, Tong Zheng, Yanshuo Chen, Xiyao Wang, Renrui Zhang, Wenhu Chen, Heng Huang

---

## 💡 一句话要点

**提出Multi-Crit基准以评估多模态模型在多元标准遵循上的能力**

**关键词**: `多模态评估` `基准构建` `标准遵循` `模型分析` `视觉推理`

## 📋 核心要点

1. 核心问题：多模态模型在遵循多元细粒度评估标准方面能力不足
2. 方法要点：构建涵盖开放生成与可验证推理任务的基准，引入新指标
3. 实验或效果：分析25个模型，显示专有和开源模型在标准遵循上存在差距

## 📄 摘要（原文）

> Large multimodal models (LMMs) are increasingly adopted as judges in multimodal evaluation systems due to their strong instruction following and consistency with human preferences. However, their ability to follow diverse, fine-grained evaluation criteria remains underexplored. We develop Multi-Crit, a benchmark for evaluating multimodal judges on their capacity to follow pluralistic criteria and produce reliable criterion-level judgments. Covering both open-ended generation and verifiable reasoning tasks, Multi-Crit is built through a rigorous data curation pipeline that gathers challenging response pairs with multi-criterion human annotations. It further introduces three novel metrics for systematically assessing pluralistic adherence, criterion-switching flexibility, and the ability to recognize criterion-level preference conflicts. Comprehensive analysis of 25 LMMs reveals that 1) proprietary models still struggle to maintain consistent adherence to pluralistic criteria--especially in open-ended evaluation; 2) open-source models lag further behind in flexibly following diverse criteria; and 3) critic fine-tuning with holistic judgment signals enhances visual grounding but fails to generalize to pluralistic criterion-level judgment. Additional analyses on reasoning fine-tuning, test-time scaling, and boundary consistency between open-source and proprietary models further probe the limits of current multimodal judges. As a pioneering study, Multi-Crit lays the foundation for building reliable and steerable multimodal AI evaluation.

