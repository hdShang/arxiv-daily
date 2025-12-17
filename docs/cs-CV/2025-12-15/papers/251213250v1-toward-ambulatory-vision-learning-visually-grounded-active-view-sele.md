---
layout: default
title: Toward Ambulatory Vision: Learning Visually-Grounded Active View Selection
---

# Toward Ambulatory Vision: Learning Visually-Grounded Active View Selection

**arXiv**: [2512.13250v1](https://arxiv.org/abs/2512.13250) | [PDF](https://arxiv.org/pdf/2512.13250.pdf)

**作者**: Juil Koo, Daehyeon Choi, Sangwoo Youn, Phillip Y. Lee, Minhyuk Sung

---

## 💡 一句话要点

**提出视觉基础主动视角选择框架，以增强视觉语言模型在移动场景中的视觉信息获取能力。**

**关键词**: `主动视角选择` `视觉语言模型` `强化学习` `移动视觉` `视觉问答` `场景探索`

## 📋 核心要点

1. 核心问题：视觉语言模型局限于静态图像，无法主动选择视角以获取更丰富视觉信息。
2. 方法要点：通过监督微调和强化学习优化预训练模型，实现仅基于当前图像的视角选择。
3. 实验或效果：在合成和真实场景中泛化良好，并提升现有场景探索问答系统的准确性。

## 📄 摘要（原文）

> Vision Language Models (VLMs) excel at visual question answering (VQA) but remain limited to snapshot vision, reasoning from static images. In contrast, embodied agents require ambulatory vision, actively moving to obtain more informative views. We introduce Visually Grounded Active View Selection (VG-AVS), a task that selects the most informative next viewpoint using only the visual information in the current image, without relying on scene memory or external knowledge. To support this task, we construct a synthetic dataset with automatically generated paired query-target views and question-answer prompts. We also propose a framework that fine-tunes pretrained VLMs through supervised fine-tuning (SFT) followed by RL-based policy optimization. Our approach achieves strong question answering performance based on viewpoint selection and generalizes robustly to unseen synthetic and real scenes. Furthermore, incorporating our learned VG-AVS framework into existing scene-exploration-based EQA systems improves downstream question-answering accuracy.

