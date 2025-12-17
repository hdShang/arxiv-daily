---
layout: default
title: MaskCaptioner : Learning to Jointly Segment and Caption Object Trajectories in Videos
---

# MaskCaptioner : Learning to Jointly Segment and Caption Object Trajectories in Videos

**arXiv**: [2510.14904v1](https://arxiv.org/abs/2510.14904) | [PDF](https://arxiv.org/pdf/2510.14904.pdf)

**作者**: Gabriel Fiastre, Antoine Yang, Cordelia Schmid

---

## 💡 一句话要点

**提出MaskCaptioner以联合分割和描述视频中物体轨迹，解决密集视频物体描述任务。**

**关键词**: `密集视频物体描述` `端到端模型` `合成数据生成` `物体轨迹分割` `视觉语言模型` `视频理解`

## 📋 核心要点

1. 核心问题：密集视频物体描述需联合检测、跟踪和描述物体轨迹，但手动标注成本高，现有方法训练不连贯。
2. 方法要点：利用先进视觉语言模型生成合成描述，扩展LVIS和LV-VIS数据集，训练端到端模型。
3. 实验或效果：在VidSTG、VLN和BenSMOT基准上实现最先进性能，提供数据集和代码。

## 📄 摘要（原文）

> Dense Video Object Captioning (DVOC) is the task of jointly detecting,
> tracking, and captioning object trajectories in a video, requiring the ability
> to understand spatio-temporal details and describe them in natural language.
> Due to the complexity of the task and the high cost associated with manual
> annotation, previous approaches resort to disjoint training strategies,
> potentially leading to suboptimal performance. To circumvent this issue, we
> propose to generate captions about spatio-temporally localized entities
> leveraging a state-of-the-art VLM. By extending the LVIS and LV-VIS datasets
> with our synthetic captions (LVISCap and LV-VISCap), we train MaskCaptioner, an
> end-to-end model capable of jointly detecting, segmenting, tracking and
> captioning object trajectories. Moreover, with pretraining on LVISCap and
> LV-VISCap, MaskCaptioner achieves state-of-the-art DVOC results on three
> existing benchmarks, VidSTG, VLN and BenSMOT. The datasets and code are
> available at https://www.gabriel.fiastre.fr/maskcaptioner/.

