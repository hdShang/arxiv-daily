---
layout: default
title: Shrinking the Teacher: An Adaptive Teaching Paradigm for Asymmetric EEG-Vision Alignment
---

# Shrinking the Teacher: An Adaptive Teaching Paradigm for Asymmetric EEG-Vision Alignment

**arXiv**: [2511.11422v1](https://arxiv.org/abs/2511.11422) | [PDF](https://arxiv.org/pdf/2511.11422.pdf)

**作者**: Lukun Wu, Jie Li, Ziqi Ren, Kaifan Zhang, Xinbo Gao

---

## 💡 一句话要点

**提出自适应教学范式以解决脑电-视觉不对称对齐问题**

**关键词**: `脑电-视觉对齐` `不对称模态` `自适应教学` `ShrinkAdapter` `零样本检索`

## 📋 核心要点

1. 核心问题：脑电与视觉模态存在保真度和语义不对称，导致对齐困难。
2. 方法要点：教师模态动态调整知识结构，通过ShrinkAdapter模块适配学生模态。
3. 实验或效果：零样本脑到图像检索准确率达60.2%，优于先前方法9.8%。

## 📄 摘要（原文）

> Decoding visual features from EEG signals is a central challenge in neuroscience, with cross-modal alignment as the dominant approach. We argue that the relationship between visual and brain modalities is fundamentally asymmetric, characterized by two critical gaps: a Fidelity Gap (stemming from EEG's inherent noise and signal degradation, vs. vision's high-fidelity features) and a Semantic Gap (arising from EEG's shallow conceptual representation, vs. vision's rich semantic depth). Previous methods often overlook this asymmetry, forcing alignment between the two modalities as if they were equal partners and thereby leading to poor generalization. To address this, we propose the adaptive teaching paradigm. This paradigm empowers the ``teacher" modality (vision) to dynamically shrink and adjust its knowledge structure under task guidance, tailoring its semantically dense features to match the ``student" modality (EEG)'s capacity. We implement this paradigm with the ShrinkAdapter, a simple yet effective module featuring a residual-free design and a bottleneck structure. Through extensive experiments, we validate the underlying rationale and effectiveness of our paradigm. Our method achieves a top-1 accuracy of 60.2\% on the zero-shot brain-to-image retrieval task, surpassing previous state-of-the-art methods by a margin of 9.8\%. Our work introduces a new perspective for asymmetric alignment: the teacher must shrink and adapt to bridge the vision-brain gap.

