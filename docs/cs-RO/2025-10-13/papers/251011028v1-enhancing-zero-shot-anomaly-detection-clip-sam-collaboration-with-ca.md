---
layout: default
title: Enhancing Zero-Shot Anomaly Detection: CLIP-SAM Collaboration with Cascaded Prompts
---

# Enhancing Zero-Shot Anomaly Detection: CLIP-SAM Collaboration with Cascaded Prompts

**arXiv**: [2510.11028v1](https://arxiv.org/abs/2510.11028) | [PDF](https://arxiv.org/pdf/2510.11028.pdf)

**作者**: Yanning Hou, Ke Xu, Junfa Li, Yanran Ruan, Jianfeng Qiu

---

## 💡 一句话要点

**提出CLIP-SAM协作框架以解决工业零样本异常分割问题**

**关键词**: `零样本异常检测` `异常分割` `CLIP模型` `SAM模型` `提示工程` `工业视觉`

## 📋 核心要点

1. 核心问题：基础模型在零样本异常分割中难以正确引导，导致对象分割倾向和边界粗糙。
2. 方法要点：设计两阶段框架，包括PPG模块生成点提示和CPS模块优化分割结果。
3. 实验或效果：在多个数据集上实现SOTA，Visa数据集F1-max和AP指标分别提升10.3%和7.7%。

## 📄 摘要（原文）

> Recently, the powerful generalization ability exhibited by foundation models
> has brought forth new solutions for zero-shot anomaly segmentation tasks.
> However, guiding these foundation models correctly to address downstream tasks
> remains a challenge. This paper proposes a novel two-stage framework, for
> zero-shot anomaly segmentation tasks in industrial anomaly detection. This
> framework excellently leverages the powerful anomaly localization capability of
> CLIP and the boundary perception ability of SAM.(1) To mitigate SAM's
> inclination towards object segmentation, we propose the Co-Feature Point Prompt
> Generation (PPG) module. This module collaboratively utilizes CLIP and SAM to
> generate positive and negative point prompts, guiding SAM to focus on
> segmenting anomalous regions rather than the entire object. (2) To further
> optimize SAM's segmentation results and mitigate rough boundaries and isolated
> noise, we introduce the Cascaded Prompts for SAM (CPS) module. This module
> employs hybrid prompts cascaded with a lightweight decoder of SAM, achieving
> precise segmentation of anomalous regions. Across multiple datasets, consistent
> experimental validation demonstrates that our approach achieves
> state-of-the-art zero-shot anomaly segmentation results. Particularly
> noteworthy is our performance on the Visa dataset, where we outperform the
> state-of-the-art methods by 10.3\% and 7.7\% in terms of {$F_1$-max} and AP
> metrics, respectively.

