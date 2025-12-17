---
layout: default
title: Cortical-SSM: A Deep State Space Model for EEG and ECoG Motor Imagery Decoding
---

# Cortical-SSM: A Deep State Space Model for EEG and ECoG Motor Imagery Decoding

**arXiv**: [2510.15371v1](https://arxiv.org/abs/2510.15371) | [PDF](https://arxiv.org/pdf/2510.15371.pdf)

**作者**: Shuntaro Suzuki, Shunya Nagashima, Masayuki Hirata, Komei Sugiura

---

## 💡 一句话要点

**提出Cortical-SSM以解决EEG和ECoG信号中依赖关系捕获不足的问题**

**关键词**: `脑电信号解码` `状态空间模型` `运动想象分类` `多模态依赖` `神经生理解释`

## 📋 核心要点

1. 核心问题：EEG和ECoG信号易受生理伪影干扰，现有方法难以捕捉细粒度依赖关系
2. 方法要点：扩展深度状态空间模型，整合时间、空间和频域依赖关系
3. 实验或效果：在三个基准数据集上超越基线方法，模型可视化显示捕获神经生理相关区域

## 📄 摘要（原文）

> Classification of electroencephalogram (EEG) and electrocorticogram (ECoG)
> signals obtained during motor imagery (MI) has substantial application
> potential, including for communication assistance and rehabilitation support
> for patients with motor impairments. These signals remain inherently
> susceptible to physiological artifacts (e.g., eye blinking, swallowing), which
> pose persistent challenges. Although Transformer-based approaches for
> classifying EEG and ECoG signals have been widely adopted, they often struggle
> to capture fine-grained dependencies within them. To overcome these
> limitations, we propose Cortical-SSM, a novel architecture that extends deep
> state space models to capture integrated dependencies of EEG and ECoG signals
> across temporal, spatial, and frequency domains. We validated our method across
> three benchmarks: 1) two large-scale public MI EEG datasets containing more
> than 50 subjects, and 2) a clinical MI ECoG dataset recorded from a patient
> with amyotrophic lateral sclerosis. Our method outperformed baseline methods on
> the three benchmarks. Furthermore, visual explanations derived from our model
> indicate that it effectively captures neurophysiologically relevant regions of
> both EEG and ECoG signals.

