---
layout: default
title: Leveraging Large-Scale Pretrained Spatial-Spectral Priors for General Zero-Shot Pansharpening
---

# Leveraging Large-Scale Pretrained Spatial-Spectral Priors for General Zero-Shot Pansharpening

**arXiv**: [2512.02643v1](https://arxiv.org/abs/2512.02643) | [PDF](https://arxiv.org/pdf/2512.02643.pdf)

**作者**: Yongchuan Cui, Peng Liu, Yi Zeng

---

## 💡 一句话要点

**提出基于大规模模拟数据预训练的策略，以提升遥感图像融合的跨域泛化能力**

**关键词**: `遥感图像融合` `零样本泛化` `预训练策略` `空间-光谱先验` `跨域适应`

## 📋 核心要点

1. 现有深度学习方法因真实数据有限和传感器差异，在未见数据集上泛化能力差
2. 通过模拟退化与增强操作构建数据集，预训练学习鲁棒的空间-光谱先验
3. 在多个卫星数据集上验证，预训练模型在零样本和少样本场景中表现优异

## 📄 摘要（原文）

> Existing deep learning methods for remote sensing image fusion often suffer from poor generalization when applied to unseen datasets due to the limited availability of real training data and the domain gap between different satellite sensors. To address this challenge, we explore the potential of foundation models by proposing a novel pretraining strategy that leverages large-scale simulated datasets to learn robust spatial-spectral priors. Specifically, our approach first constructs diverse simulated datasets by applying various degradation operations (blur, noise, downsampling) and augmentations (bands generation, channel shuffling, high-pass filtering, color jittering, etc.) to natural images from ImageNet and remote sensing images from SkyScript. We then pretrain fusion models on these simulated data to learn generalizable spatial-spectral representations. The pretrained models are subsequently evaluated on six datasets (WorldView-2/3/4, IKONOS, QuickBird, GaoFen-2) using zero-shot and one-shot paradigms, with both full- and freeze-tuning approaches for fine-tuning. Extensive experiments on different network architectures including convolutional neural networks, Transformer, and Mamba demonstrate that our pretraining strategy significantly improves generalization performance across different satellite sensors and imaging conditions for various fusion models. The pretrained models achieve superior results in zero-shot scenarios and show remarkable adaptation capability with minimal real data in one-shot settings. Our work provides a practical solution for cross-domain pansharpening, establishes a new benchmark for generalization in remote sensing image fusion tasks, and paves the way for leveraging foundation models through advanced training strategies.

