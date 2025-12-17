---
layout: default
title: Learning from Single Timestamps: Complexity Estimation in Laparoscopic Cholecystectomy
---

# Learning from Single Timestamps: Complexity Estimation in Laparoscopic Cholecystectomy

**arXiv**: [2511.04525v1](https://arxiv.org/abs/2511.04525) | [PDF](https://arxiv.org/pdf/2511.04525.pdf)

**作者**: Dimitrios Anastasiou, Santiago Barbarisi, Lucy Culshaw, Jayna Patel, Evangelos B. Mazomenos, Imanol Luengo, Danail Stoyanov

---

## 💡 一句话要点

**提出STC-Net框架，基于单时间戳从完整腹腔镜胆囊切除术视频中自动评估手术复杂度。**

**关键词**: `手术视频分析` `弱监督学习` `时间定位` `复杂度评估` `腹腔镜胆囊切除术`

## 📋 核心要点

1. 核心问题：腹腔镜胆囊切除术中炎症严重度评估依赖完整视频，自动化方法需处理弱时间监督。
2. 方法要点：STC-Net联合执行时间定位和分级，引入硬软定位损失和背景感知监督。
3. 实验或效果：在1859个视频数据集上，准确率达62.11%，F1分数61.42%，优于基线10%以上。

## 📄 摘要（原文）

> Purpose: Accurate assessment of surgical complexity is essential in
> Laparoscopic Cholecystectomy (LC), where severe inflammation is associated with
> longer operative times and increased risk of postoperative complications. The
> Parkland Grading Scale (PGS) provides a clinically validated framework for
> stratifying inflammation severity; however, its automation in surgical videos
> remains largely unexplored, particularly in realistic scenarios where complete
> videos must be analyzed without prior manual curation. Methods: In this work,
> we introduce STC-Net, a novel framework for SingleTimestamp-based Complexity
> estimation in LC via the PGS, designed to operate under weak temporal
> supervision. Unlike prior methods limited to static images or manually trimmed
> clips, STC-Net operates directly on full videos. It jointly performs temporal
> localization and grading through a localization, window proposal, and grading
> module. We introduce a novel loss formulation combining hard and soft
> localization objectives and background-aware grading supervision. Results:
> Evaluated on a private dataset of 1,859 LC videos, STC-Net achieves an accuracy
> of 62.11% and an F1-score of 61.42%, outperforming non-localized baselines by
> over 10% in both metrics and highlighting the effectiveness of weak supervision
> for surgical complexity assessment. Conclusion: STC-Net demonstrates a scalable
> and effective approach for automated PGS-based surgical complexity estimation
> from full LC videos, making it promising for post-operative analysis and
> surgical training.

