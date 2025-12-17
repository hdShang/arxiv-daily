---
layout: default
title: NAUTILUS: A Large Multimodal Model for Underwater Scene Understanding
---

# NAUTILUS: A Large Multimodal Model for Underwater Scene Understanding

**arXiv**: [2510.27481v1](https://arxiv.org/abs/2510.27481) | [PDF](https://arxiv.org/pdf/2510.27481.pdf)

**作者**: Wei Xu, Cheng Wang, Dingkang Liang, Zongchuang Zhao, Xingyu Jiang, Peng Zhang, Xiang Bai

---

## 💡 一句话要点

**提出NAUTILUS大模型以解决水下场景理解问题**

**关键词**: `水下场景理解` `多模态大模型` `视觉特征增强` `多任务学习` `图像退化处理`

## 📋 核心要点

1. 核心问题：缺乏大规模水下多任务指令调优数据集和图像退化干扰。
2. 方法要点：构建NautData数据集并引入视觉特征增强模块提升鲁棒性。
3. 实验或效果：在NautData和公共数据集上验证模块有效性，提升基线模型性能。

## 📄 摘要（原文）

> Underwater exploration offers critical insights into our planet and attracts
> increasing attention for its broader applications in resource exploration,
> national security, etc. We study the underwater scene understanding methods,
> which aim to achieve automated underwater exploration. The underwater scene
> understanding task demands multi-task perceptions from multiple granularities.
> However, the absence of large-scale underwater multi-task instruction-tuning
> datasets hinders the progress of this research. To bridge this gap, we
> construct NautData, a dataset containing 1.45 M image-text pairs supporting
> eight underwater scene understanding tasks. It enables the development and
> thorough evaluation of the underwater scene understanding models. Underwater
> image degradation is a widely recognized challenge that interferes with
> underwater tasks. To improve the robustness of underwater scene understanding,
> we introduce physical priors derived from underwater imaging models and propose
> a plug-and-play vision feature enhancement (VFE) module, which explicitly
> restores clear underwater information. We integrate this module into renowned
> baselines LLaVA-1.5 and Qwen2.5-VL and build our underwater LMM, NAUTILUS.
> Experiments conducted on the NautData and public underwater datasets
> demonstrate the effectiveness of the VFE module, consistently improving the
> performance of both baselines on the majority of supported tasks, thus ensuring
> the superiority of NAUTILUS in the underwater scene understanding area. Data
> and models are available at https://github.com/H-EmbodVis/NAUTILUS.

