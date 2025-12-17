---
layout: default
title: CKDA: Cross-modality Knowledge Disentanglement and Alignment for Visible-Infrared Lifelong Person Re-identification
---

# CKDA: Cross-modality Knowledge Disentanglement and Alignment for Visible-Infrared Lifelong Person Re-identification

**arXiv**: [2511.15016v1](https://arxiv.org/abs/2511.15016) | [PDF](https://arxiv.org/pdf/2511.15016.pdf)

**作者**: Zhenyu Cui, Jiahuan Zhou, Yuxin Peng

---

## 💡 一句话要点

**提出CKDA方法以解决可见光-红外终身行人重识别中的知识干扰问题**

**关键词**: `终身学习` `行人重识别` `跨模态学习` `知识解耦` `知识对齐`

## 📋 核心要点

1. 核心问题：模态特定知识与模态通用知识在持续学习中相互干扰，导致协作遗忘
2. 方法要点：使用MCP和MSP模块解耦知识，CKA模块对齐新旧知识
3. 实验或效果：在四个基准数据集上验证优于现有方法，代码已开源

## 📄 摘要（原文）

> Lifelong person Re-IDentification (LReID) aims to match the same person employing continuously collected individual data from different scenarios. To achieve continuous all-day person matching across day and night, Visible-Infrared Lifelong person Re-IDentification (VI-LReID) focuses on sequential training on data from visible and infrared modalities and pursues average performance over all data. To this end, existing methods typically exploit cross-modal knowledge distillation to alleviate the catastrophic forgetting of old knowledge. However, these methods ignore the mutual interference of modality-specific knowledge acquisition and modality-common knowledge anti-forgetting, where conflicting knowledge leads to collaborative forgetting. To address the above problems, this paper proposes a Cross-modality Knowledge Disentanglement and Alignment method, called CKDA, which explicitly separates and preserves modality-specific knowledge and modality-common knowledge in a balanced way. Specifically, a Modality-Common Prompting (MCP) module and a Modality-Specific Prompting (MSP) module are proposed to explicitly disentangle and purify discriminative information that coexists and is specific to different modalities, avoiding the mutual interference between both knowledge. In addition, a Cross-modal Knowledge Alignment (CKA) module is designed to further align the disentangled new knowledge with the old one in two mutually independent inter- and intra-modality feature spaces based on dual-modality prototypes in a balanced manner. Extensive experiments on four benchmark datasets verify the effectiveness and superiority of our CKDA against state-of-the-art methods. The source code of this paper is available at https://github.com/PKU-ICST-MIPL/CKDA-AAAI2026.

