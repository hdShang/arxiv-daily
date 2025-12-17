---
layout: default
title: PROMISE: Prompt-Attentive Hierarchical Contrastive Learning for Robust Cross-Modal Representation with Missing Modalities
---

# PROMISE: Prompt-Attentive Hierarchical Contrastive Learning for Robust Cross-Modal Representation with Missing Modalities

**arXiv**: [2511.10997v1](https://arxiv.org/abs/2511.10997) | [PDF](https://arxiv.org/pdf/2511.10997.pdf)

**作者**: Jiajun Chen, Sai Cheng, Yutao Yuan, Yirui Zhang, Haitao Yuan, Peng Peng, Yi Zhong

---

## 💡 一句话要点

**提出PROMISE框架以解决缺失模态下跨模态表示鲁棒性问题**

**关键词**: `多模态学习` `缺失模态` `提示学习` `对比学习` `跨模态表示`

## 📋 核心要点

1. 核心问题：真实场景中模态缺失导致多模态模型性能显著下降
2. 方法要点：结合多模态提示学习和层次对比学习，动态生成鲁棒表示
3. 实验或效果：在基准数据集上优于现有方法，并通过消融研究验证有效性

## 📄 摘要（原文）

> Multimodal models integrating natural language and visual information have substantially improved generalization of representation models. However, their effectiveness significantly declines in real-world situations where certain modalities are missing or unavailable. This degradation primarily stems from inconsistent representation learning between complete multimodal data and incomplete modality scenarios. Existing approaches typically address missing modalities through relatively simplistic generation methods, yet these approaches fail to adequately preserve cross-modal consistency, leading to suboptimal performance. To overcome this limitation, we propose a novel multimodal framework named PROMISE, a PROMpting-Attentive HIerarchical ContraStive LEarning approach designed explicitly for robust cross-modal representation under conditions of missing modalities. Specifically, PROMISE innovatively incorporates multimodal prompt learning into a hierarchical contrastive learning framework, equipped with a specially designed prompt-attention mechanism. This mechanism dynamically generates robust and consistent representations for scenarios where particular modalities are absent, thereby effectively bridging the representational gap between complete and incomplete data. Extensive experiments conducted on benchmark datasets, along with comprehensive ablation studies, clearly demonstrate the superior performance of PROMISE compared to current state-of-the-art multimodal methods.

