---
layout: default
title: Towards Cross-View Point Correspondence in Vision-Language Models
---

# Towards Cross-View Point Correspondence in Vision-Language Models

**arXiv**: [2512.04686v1](https://arxiv.org/abs/2512.04686) | [PDF](https://arxiv.org/pdf/2512.04686.pdf)

**作者**: Yipu Wang, Yuheng Ji, Yuyang Liu, Enshen Zhou, Ziqiang Yang, Yuxuan Tian, Ziheng Qin, Yue Liu, Huajie Tan, Cheng Chi, Zhiyuan Ma, Daniel Dajun Zeng, Xiaolong Zheng

---

## 💡 一句话要点

**提出跨视图点对应任务与基准，以提升视觉语言模型在空间理解中的精确对应能力。**

**关键词**: `跨视图对应` `视觉语言模型` `点级对应` `空间理解` `基准评估` `数据集构建`

## 📋 核心要点

1. 核心问题：视觉语言模型在跨视图点对应任务上表现不佳，影响精确交互。
2. 方法要点：构建分层基准CrossPoint-Bench和数据集CrossPoint-378K，并训练模型CroPond。
3. 实验或效果：CroPond在基准上超越Gemini-2.5-Pro 39.7%，缩小与人类差距。

## 📄 摘要（原文）

> Cross-view correspondence is a fundamental capability for spatial understanding and embodied AI. However, it is still far from being realized in Vision-Language Models (VLMs), especially in achieving precise point-level correspondence, which is crucial for precise affordance interaction. So we propose the Cross-View Point Correspondence (CVPC) task and CrossPoint-Bench, a comprehensive benchmark with hierarchical design, inspired by the human cognitive process of "perceive", "reason", and "correspond". Our evaluation shows the state-of-the-art models (e.g., Gemini-2.5-Pro) still fall far behind humans, with a gap of over 54.65% in overall accuracy, exposing a challenge in transitioning from coarse-grained judgement to fine-grained coordinate prediction. To address this problem, we construct CrossPoint-378K, a dataset with 378K question-answering pairs across 900 scenes, focused on actionable affordance regions that better reflect real-world manipulation and interaction scenarios. Furthermore, we propose CroPond that trained on the CrossPoint-378K dataset. Our CroPond achieves state-of-the-art performance on CrossPoint-Bench, surpassing Gemini-2.5-Pro by 39.7% accuracy, which offers a foundation for advancing future work on cross-view correspondence. The benchmark, dataset, and model are publicly available at https://github.com/WangYipu2002/CrossPoint.

