---
layout: default
title: Taming Modality Entanglement in Continual Audio-Visual Segmentation
---

# Taming Modality Entanglement in Continual Audio-Visual Segmentation

**arXiv**: [2510.17234v1](https://arxiv.org/abs/2510.17234) | [PDF](https://arxiv.org/pdf/2510.17234.pdf)

**作者**: Yuyang Hong, Qi Yang, Tao Zhang, Zili Wang, Zhaojin Fu, Kun Ding, Bin Fan, Shiming Xiang

---

## 💡 一句话要点

**提出碰撞式多模态排练框架以解决持续音频-视觉分割中的模态纠缠问题**

**关键词**: `持续学习` `多模态分割` `音频-视觉` `模态纠缠` `样本排练` `语义漂移`

## 📋 核心要点

1. 核心问题：模态纠缠导致多模态语义漂移和共现混淆，影响细粒度持续学习。
2. 方法要点：设计多模态样本选择和碰撞式样本排练机制，增强模态一致性和减少混淆。
3. 实验或效果：在三个音频-视觉增量场景中验证，显著优于单模态持续学习方法。

## 📄 摘要（原文）

> Recently, significant progress has been made in multi-modal continual
> learning, aiming to learn new tasks sequentially in multi-modal settings while
> preserving performance on previously learned ones. However, existing methods
> mainly focus on coarse-grained tasks, with limitations in addressing modality
> entanglement in fine-grained continual learning settings. To bridge this gap,
> we introduce a novel Continual Audio-Visual Segmentation (CAVS) task, aiming to
> continuously segment new classes guided by audio. Through comprehensive
> analysis, two critical challenges are identified: 1) multi-modal semantic
> drift, where a sounding objects is labeled as background in sequential tasks;
> 2) co-occurrence confusion, where frequent co-occurring classes tend to be
> confused. In this work, a Collision-based Multi-modal Rehearsal (CMR) framework
> is designed to address these challenges. Specifically, for multi-modal semantic
> drift, a Multi-modal Sample Selection (MSS) strategy is proposed to select
> samples with high modal consistency for rehearsal. Meanwhile, for co-occurence
> confusion, a Collision-based Sample Rehearsal (CSR) mechanism is designed,
> allowing for the increase of rehearsal sample frequency of those confusable
> classes during training process. Moreover, we construct three audio-visual
> incremental scenarios to verify effectiveness of our method. Comprehensive
> experiments demonstrate that our method significantly outperforms single-modal
> continual learning methods.

