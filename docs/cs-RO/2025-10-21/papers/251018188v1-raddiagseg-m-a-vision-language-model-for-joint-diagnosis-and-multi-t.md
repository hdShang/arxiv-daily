---
layout: default
title: RadDiagSeg-M: A Vision Language Model for Joint Diagnosis and Multi-Target Segmentation in Radiology
---

# RadDiagSeg-M: A Vision Language Model for Joint Diagnosis and Multi-Target Segmentation in Radiology

**arXiv**: [2510.18188v1](https://arxiv.org/abs/2510.18188) | [PDF](https://arxiv.org/pdf/2510.18188.pdf)

**作者**: Chengrun Li, Corentin Royer, Haozhe Luo, Bastian Wittmann, Xia Li, Ibrahim Hamamci, Sezgin Er, Anjany Sekuboyina, Bjoern Menze

---

## 💡 一句话要点

**提出RadDiagSeg-M视觉语言模型，以联合生成诊断文本和分割掩码解决放射学辅助诊断问题**

**关键词**: `视觉语言模型` `医学图像分割` `放射学诊断` `多目标分割` `异常检测`

## 📋 核心要点

1. 当前医学视觉语言模型难以同时生成诊断文本和像素级分割掩码，限制临床应用
2. 引入RadDiagSeg-D数据集，并开发RadDiagSeg-M模型，支持联合异常检测、诊断和灵活分割
3. 基准测试显示模型在多目标文本和掩码生成任务中表现强劲，建立竞争基线

## 📄 摘要（原文）

> Most current medical vision language models struggle to jointly generate
> diagnostic text and pixel-level segmentation masks in response to complex
> visual questions. This represents a major limitation towards clinical
> application, as assistive systems that fail to provide both modalities
> simultaneously offer limited value to medical practitioners. To alleviate this
> limitation, we first introduce RadDiagSeg-D, a dataset combining abnormality
> detection, diagnosis, and multi-target segmentation into a unified and
> hierarchical task. RadDiagSeg-D covers multiple imaging modalities and is
> precisely designed to support the development of models that produce
> descriptive text and corresponding segmentation masks in tandem. Subsequently,
> we leverage the dataset to propose a novel vision-language model, RadDiagSeg-M,
> capable of joint abnormality detection, diagnosis, and flexible segmentation.
> RadDiagSeg-M provides highly informative and clinically useful outputs,
> effectively addressing the need to enrich contextual information for assistive
> diagnosis. Finally, we benchmark RadDiagSeg-M and showcase its strong
> performance across all components involved in the task of multi-target
> text-and-mask generation, establishing a robust and competitive baseline.

