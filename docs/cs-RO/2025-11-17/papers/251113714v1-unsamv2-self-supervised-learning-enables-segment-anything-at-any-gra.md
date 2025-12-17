---
layout: default
title: UnSAMv2: Self-Supervised Learning Enables Segment Anything at Any Granularity
---

# UnSAMv2: Self-Supervised Learning Enables Segment Anything at Any Granularity

**arXiv**: [2511.13714v1](https://arxiv.org/abs/2511.13714) | [PDF](https://arxiv.org/pdf/2511.13714.pdf)

**作者**: Junwei Yu, Trevor Darrell, XuDong Wang

---

## 💡 一句话要点

**提出UnSAMv2以无监督方式实现任意粒度图像分割**

**关键词**: `自监督学习` `图像分割` `粒度控制` `无标注数据` `视觉基础模型`

## 📋 核心要点

1. SAM模型难以控制分割粒度，需人工干预，标注成本高
2. 引入自监督学习，发现掩码-粒度对，使用粒度控制嵌入
3. 少量未标注数据显著提升SAM-2，在11个基准上改进指标

## 📄 摘要（原文）

> The Segment Anything Model (SAM) family has become a widely adopted vision foundation model, but its ability to control segmentation granularity remains limited. Users often need to refine results manually - by adding more prompts or selecting from pre-generated masks - to achieve the desired level of detail. This process can be ambiguous, as the same prompt may correspond to several plausible masks, and collecting dense annotations across all granularities is prohibitively expensive, making supervised solutions infeasible. To address this limitation, we introduce UnSAMv2, which enables segment anything at any granularity without human annotations. UnSAMv2 extends the divide-and-conquer strategy of UnSAM by discovering abundant mask-granularity pairs and introducing a novel granularity control embedding that enables precise, continuous control over segmentation scale. Remarkably, with only $6$K unlabeled images and $0.02\%$ additional parameters, UnSAMv2 substantially enhances SAM-2, achieving segment anything at any granularity across interactive, whole-image, and video segmentation tasks. Evaluated on over $11$ benchmarks, UnSAMv2 improves $\text{NoC}_{90}$ (5.69 $\rightarrow$ 4.75), 1-IoU (58.0 $\rightarrow$ 73.1), and $\text{AR}_{1000}$ (49.6 $\rightarrow$ 68.3), showing that small amounts of unlabeled data with a granularity-aware self-supervised learning method can unlock the potential of vision foundation models.

