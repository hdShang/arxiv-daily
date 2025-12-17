---
layout: default
title: Learning to Recognize Correctly Completed Procedure Steps in Egocentric Assembly Videos through Spatio-Temporal Modeling
---

# Learning to Recognize Correctly Completed Procedure Steps in Egocentric Assembly Videos through Spatio-Temporal Modeling

**arXiv**: [2510.12385v1](https://arxiv.org/abs/2510.12385) | [PDF](https://arxiv.org/pdf/2510.12385.pdf)

**作者**: Tim J. Schoonbeek, Shao-Hsuan Hung, Dan Lehman, Hans Onvlee, Jacek Kustra, Peter H. N. de With, Fons van der Sommen

---

## 💡 一句话要点

**提出STORM-PSR双流框架，通过时空建模提升第一人称装配视频中步骤识别的鲁棒性。**

**关键词**: `步骤识别` `时空建模` `第一人称视频` `遮挡鲁棒性` `Transformer编码器` `弱监督学习`

## 📋 核心要点

1. 核心问题：现有方法仅依赖单帧物体状态检测，忽略时序特征，导致在部分遮挡时识别精度受限。
2. 方法要点：结合空间流和时空流，空间编码器预训练捕获空间特征，时序编码器基于Transformer建模时间关系。
3. 实验或效果：在MECCANO和IndustReal数据集上，平均延迟分别降低11.2%和26.1%，优于先前方法。

## 📄 摘要（原文）

> Procedure step recognition (PSR) aims to identify all correctly completed
> steps and their sequential order in videos of procedural tasks. The existing
> state-of-the-art models rely solely on detecting assembly object states in
> individual video frames. By neglecting temporal features, model robustness and
> accuracy are limited, especially when objects are partially occluded. To
> overcome these limitations, we propose Spatio-Temporal Occlusion-Resilient
> Modeling for Procedure Step Recognition (STORM-PSR), a dual-stream framework
> for PSR that leverages both spatial and temporal features. The assembly state
> detection stream operates effectively with unobstructed views of the object,
> while the spatio-temporal stream captures both spatial and temporal features to
> recognize step completions even under partial occlusion. This stream includes a
> spatial encoder, pre-trained using a novel weakly supervised approach to
> capture meaningful spatial representations, and a transformer-based temporal
> encoder that learns how these spatial features relate over time. STORM-PSR is
> evaluated on the MECCANO and IndustReal datasets, reducing the average delay
> between actual and predicted assembly step completions by 11.2% and 26.1%,
> respectively, compared to prior methods. We demonstrate that this reduction in
> delay is driven by the spatio-temporal stream, which does not rely on
> unobstructed views of the object to infer completed steps. The code for
> STORM-PSR, along with the newly annotated MECCANO labels, is made publicly
> available at https://timschoonbeek.github.io/stormpsr .

