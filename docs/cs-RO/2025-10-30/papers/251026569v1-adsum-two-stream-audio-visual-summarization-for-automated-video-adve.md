---
layout: default
title: AdSum: Two-stream Audio-visual Summarization for Automated Video Advertisement Clipping
---

# AdSum: Two-stream Audio-visual Summarization for Automated Video Advertisement Clipping

**arXiv**: [2510.26569v1](https://arxiv.org/abs/2510.26569) | [PDF](https://arxiv.org/pdf/2510.26569.pdf)

**作者**: Wen Xie, Yanjun Zhu, Gijs Overgoor, Yakov Bart, Agata Lapedriza Garcia, Sarah Ostadabbas

---

## 💡 一句话要点

**提出双流音视频融合模型以自动化视频广告剪辑**

**关键词**: `视频广告剪辑` `双流融合模型` `音视频摘要` `帧重要性预测` `AdSum204数据集`

## 📋 核心要点

1. 核心问题：传统广告剪辑依赖人工，耗时费力，需自动生成多时长版本。
2. 方法要点：采用双流音视频融合模型预测帧重要性，强调音频在广告中的作用。
3. 实验或效果：在AdSum204数据集上，模型在多项指标上优于现有方法。

## 📄 摘要（原文）

> Advertisers commonly need multiple versions of the same advertisement (ad) at
> varying durations for a single campaign. The traditional approach involves
> manually selecting and re-editing shots from longer video ads to create shorter
> versions, which is labor-intensive and time-consuming. In this paper, we
> introduce a framework for automated video ad clipping using video summarization
> techniques. We are the first to frame video clipping as a shot selection
> problem, tailored specifically for advertising. Unlike existing general video
> summarization methods that primarily focus on visual content, our approach
> emphasizes the critical role of audio in advertising. To achieve this, we
> develop a two-stream audio-visual fusion model that predicts the importance of
> video frames, where importance is defined as the likelihood of a frame being
> selected in the firm-produced short ad. To address the lack of ad-specific
> datasets, we present AdSum204, a novel dataset comprising 102 pairs of
> 30-second and 15-second ads from real advertising campaigns. Extensive
> experiments demonstrate that our model outperforms state-of-the-art methods
> across various metrics, including Average Precision, Area Under Curve,
> Spearman, and Kendall.

