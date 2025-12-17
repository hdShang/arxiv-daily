---
layout: default
title: ProPL: Universal Semi-Supervised Ultrasound Image Segmentation via Prompt-Guided Pseudo-Labeling
---

# ProPL: Universal Semi-Supervised Ultrasound Image Segmentation via Prompt-Guided Pseudo-Labeling

**arXiv**: [2511.15057v1](https://arxiv.org/abs/2511.15057) | [PDF](https://arxiv.org/pdf/2511.15057.pdf)

**作者**: Yaxiong Chen, Qicong Wang, Chunlei Li, Jingliang Hu, Yilei Shi, Shengwu Xiong, Xiao Xiang Zhu, Lichao Mou

---

## 💡 一句话要点

**提出ProPL框架以解决通用半监督超声图像分割问题**

**关键词**: `超声图像分割` `半监督学习` `提示学习` `伪标签校准` `通用分割` `医学影像分析`

## 📋 核心要点

1. 现有超声图像分割方法局限于特定器官或任务，实用性不足
2. 采用共享视觉编码器和提示引导双解码器，结合不确定性伪标签校准
3. 在5器官8任务数据集上实验，性能优于现有方法，建立新基准

## 📄 摘要（原文）

> Existing approaches for the problem of ultrasound image segmentation, whether supervised or semi-supervised, are typically specialized for specific anatomical structures or tasks, limiting their practical utility in clinical settings. In this paper, we pioneer the task of universal semi-supervised ultrasound image segmentation and propose ProPL, a framework that can handle multiple organs and segmentation tasks while leveraging both labeled and unlabeled data. At its core, ProPL employs a shared vision encoder coupled with prompt-guided dual decoders, enabling flexible task adaptation through a prompting-upon-decoding mechanism and reliable self-training via an uncertainty-driven pseudo-label calibration (UPLC) module. To facilitate research in this direction, we introduce a comprehensive ultrasound dataset spanning 5 organs and 8 segmentation tasks. Extensive experiments demonstrate that ProPL outperforms state-of-the-art methods across various metrics, establishing a new benchmark for universal ultrasound image segmentation.

