---
layout: default
title: Colon-X: Advancing Intelligent Colonoscopy from Multimodal Understanding to Clinical Reasoning
---

# Colon-X: Advancing Intelligent Colonoscopy from Multimodal Understanding to Clinical Reasoning

**arXiv**: [2512.03667v1](https://arxiv.org/abs/2512.03667) | [PDF](https://arxiv.org/pdf/2512.03667.pdf)

**作者**: Ge-Peng Ji, Jingyi Liu, Deng-Ping Fan, Nick Barnes

---

## 💡 一句话要点

**提出Colon-X以推进结肠镜从多模态理解到临床推理的智能分析**

**关键词**: `结肠镜多模态理解` `临床推理数据集` `视觉问答` `任务自适应奖励` `梯度稳定优化` `多模态大语言模型评估`

## 📋 核心要点

1. 构建ColonVQA数据集，包含110万+视觉问答条目，覆盖76种临床发现和18个多模态任务
2. 评估22个多模态大语言模型，发现其临床输出在扰动下可靠性不足，需提升稳健性
3. 开发ColonR1模型，通过任务自适应奖励和梯度稳定优化，在数据稀缺条件下准确率达56.61%，优于监督微调25.22%

## 📄 摘要（原文）

> In this study, we present Colon-X, an open initiative aimed at advancing multimodal intelligence in colonoscopy. We begin by constructing ColonVQA, the most comprehensive multimodal dataset ever built for colonoscopy, featuring over 1.1M+ visual question answering entries across 76 clinical findings and 18 multimodal tasks. Beyond serving as a community-wide data foundation, we further investigate a critical yet underexplored transition in colonoscopy - evolving from multimodal understanding to clinical reasoning: (a) To capture the current landscape of multimodal understanding behaviors, we systematically assess the generalizability of 22 multimodal large language models and examine their reliability under human-induced perturbations. The results reveal that clinical outputs from leading MLLMs remain far from robust and trustworthy. (b) To narrow this gap, we further explore reasoning-centric intelligence tailored for colonoscopy. Specifically, we curate ColonReason, a clinically grounded reasoning dataset annotated through a multi-expert debating pipeline, and develop ColonR1, the first R1-styled model incorporating task-adaptive rewarding and gradient-stable optimization techniques. Under data-scarce conditions, our ColonR1 achieves 56.61% overall accuracy, outperforming supervised fine-tuning by 25.22%, and sets a new reasoning-enabled baseline for multimodal colonoscopy analysis. All data and model resources are publicly available at https://github.com/ai4colonoscopy/Colon-X.

