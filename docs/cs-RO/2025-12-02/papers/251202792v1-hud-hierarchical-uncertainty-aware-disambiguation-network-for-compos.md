---
layout: default
title: HUD: Hierarchical Uncertainty-Aware Disambiguation Network for Composed Video Retrieval
---

# HUD: Hierarchical Uncertainty-Aware Disambiguation Network for Composed Video Retrieval

**arXiv**: [2512.02792v1](https://arxiv.org/abs/2512.02792) | [PDF](https://arxiv.org/pdf/2512.02792.pdf)

**作者**: Zhiwei Chen, Yupeng Hu, Zixu Li, Zhiheng Fu, Haokun Wen, Weili Guan

---

## 💡 一句话要点

**提出HUD网络以解决组合视频检索中的模态信息密度差异问题**

**关键词**: `组合视频检索` `多模态查询` `不确定性建模` `语义对齐` `跨模态交互`

## 📋 核心要点

1. 核心问题：视频与文本模态信息密度差异导致修改主题指代模糊和语义细节关注不足
2. 方法要点：通过整体代词消歧、原子不确定性建模和整体到原子对齐增强多模态查询理解
3. 实验或效果：在CVR和CIR任务中实现SOTA性能，代码已开源

## 📄 摘要（原文）

> Composed Video Retrieval (CVR) is a challenging video retrieval task that utilizes multi-modal queries, consisting of a reference video and modification text, to retrieve the desired target video. The core of this task lies in understanding the multi-modal composed query and achieving accurate composed feature learning. Within multi-modal queries, the video modality typically carries richer semantic content compared to the textual modality. However, previous works have largely overlooked the disparity in information density between these two modalities. This limitation can lead to two critical issues: 1) modification subject referring ambiguity and 2) limited detailed semantic focus, both of which degrade the performance of CVR models. To address the aforementioned issues, we propose a novel CVR framework, namely the Hierarchical Uncertainty-aware Disambiguation network (HUD). HUD is the first framework that leverages the disparity in information density between video and text to enhance multi-modal query understanding. It comprises three key components: (a) Holistic Pronoun Disambiguation, (b) Atomistic Uncertainty Modeling, and (c) Holistic-to-Atomistic Alignment. By exploiting overlapping semantics through holistic cross-modal interaction and fine-grained semantic alignment via atomistic-level cross-modal interaction, HUD enables effective object disambiguation and enhances the focus on detailed semantics, thereby achieving precise composed feature learning. Moreover, our proposed HUD is also applicable to the Composed Image Retrieval (CIR) task and achieves state-of-the-art performance across three benchmark datasets for both CVR and CIR tasks. The codes are available on https://zivchen-ty.github.io/HUD.github.io/.

