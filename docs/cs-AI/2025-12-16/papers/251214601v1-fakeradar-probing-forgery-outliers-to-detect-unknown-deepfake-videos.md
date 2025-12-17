---
layout: default
title: FakeRadar: Probing Forgery Outliers to Detect Unknown Deepfake Videos
---

# FakeRadar: Probing Forgery Outliers to Detect Unknown Deepfake Videos

**arXiv**: [2512.14601v1](https://arxiv.org/abs/2512.14601) | [PDF](https://arxiv.org/pdf/2512.14601.pdf)

**作者**: Zhaolun Li, Jichang Li, Yinqi Cai, Junye Chen, Xiaonan Luo, Guanbin Li, Rushi Lan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出FakeRadar框架以解决深度伪造视频检测中的跨域泛化挑战，通过主动探测伪造异常来识别未知伪造类型。**

**关键词**: `深度伪造检测` `跨域泛化` `伪造异常探测` `预训练模型` `对比学习` `视频分析` `异常生成` `机器学习安全`

## 📋 核心要点

1. 现有深度伪造检测方法依赖已知伪造线索，对新兴技术泛化能力差，难以适应未知伪造模式。
2. FakeRadar利用预训练模型主动探测特征空间，通过伪造异常探测和异常引导训练模拟未知伪造，提升泛化性能。
3. 实验显示FakeRadar在跨域评估中优于现有方法，有效处理多种新兴操纵技术，验证了其泛化优势。

## 📝 摘要（中文）

本文提出FakeRadar，一种新颖的深度伪造视频检测框架，旨在解决现实场景中跨域泛化的挑战。现有检测方法通常依赖于特定操纵线索，在已知伪造类型上表现良好，但对新兴操纵技术表现出严重局限性。这种泛化能力差源于它们无法有效适应未见过的伪造模式。为克服此问题，我们利用大规模预训练模型（如CLIP）主动探测特征空间，明确突出真实视频、已知伪造和未知操纵之间的分布差距。具体而言，FakeRadar引入伪造异常探测，采用动态子聚类建模和聚类条件异常生成来合成估计子聚类边界附近的异常样本，模拟超出已知操纵类型的新伪造伪影。此外，我们设计异常引导的三重训练，通过提出的异常驱动对比学习和异常条件交叉熵损失优化检测器，以区分真实、伪造和异常样本。实验表明，FakeRadar在深度伪造视频检测的各种基准数据集上优于现有方法，特别是在跨域评估中，通过处理多种新兴操纵技术。

## 🔬 方法详解

FakeRadar的整体框架基于大规模预训练模型（如CLIP）构建，核心包括伪造异常探测和异常引导的三重训练。关键技术创新点在于：伪造异常探测通过动态子聚类建模和聚类条件异常生成，主动合成异常样本以模拟未知伪造伪影；异常引导的三重训练结合异常驱动对比学习和异常条件交叉熵损失，优化检测器区分真实、伪造和异常样本。与现有方法的主要区别在于，FakeRadar不依赖特定操纵线索，而是通过主动探测特征分布异常来增强对未知伪造的适应能力，从而提升跨域泛化性能。

## 📊 实验亮点

FakeRadar在多个深度伪造视频检测基准数据集上表现优异，特别是在跨域评估中显著优于现有方法，通过处理新兴操纵技术验证了其泛化优势，提升了未知伪造检测的准确性和鲁棒性。

## 🎯 应用场景

该研究可应用于网络安全、社交媒体内容审核、司法取证和数字媒体验证等领域，帮助自动检测深度伪造视频，特别是在面对新兴伪造技术时提供更可靠的泛化检测能力，具有实际价值。

## 📄 摘要（原文）

> In this paper, we propose FakeRadar, a novel deepfake video detection framework designed to address the challenges of cross-domain generalization in real-world scenarios. Existing detection methods typically rely on manipulation-specific cues, performing well on known forgery types but exhibiting severe limitations against emerging manipulation techniques. This poor generalization stems from their inability to adapt effectively to unseen forgery patterns. To overcome this, we leverage large-scale pretrained models (e.g. CLIP) to proactively probe the feature space, explicitly highlighting distributional gaps between real videos, known forgeries, and unseen manipulations. Specifically, FakeRadar introduces Forgery Outlier Probing, which employs dynamic subcluster modeling and cluster-conditional outlier generation to synthesize outlier samples near boundaries of estimated subclusters, simulating novel forgery artifacts beyond known manipulation types. Additionally, we design Outlier-Guided Tri-Training, which optimizes the detector to distinguish real, fake, and outlier samples using proposed outlier-driven contrastive learning and outlier-conditioned cross-entropy losses. Experiments show that FakeRadar outperforms existing methods across various benchmark datasets for deepfake video detection, particularly in cross-domain evaluations, by handling the variety of emerging manipulation techniques.

