---
layout: default
title: SS4D: Native 4D Generative Model via Structured Spacetime Latents
---

# SS4D: Native 4D Generative Model via Structured Spacetime Latents

**arXiv**: [2512.14284v1](https://arxiv.org/abs/2512.14284) | [PDF](https://arxiv.org/pdf/2512.14284.pdf)

**作者**: Zhibing Li, Mengchen Zhang, Tong Wu, Jing Tan, Jiaqi Wang, Dahua Lin

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: ToG(Siggraph Asia 2025)

**期刊**: ACM Transactions on Graphics, 44(6): Article 244, 12 pages, December 2025

**DOI**: [10.1145/3763302](https://doi.org/10.1145/3763302)

---

## 💡 一句话要点

**提出SS4D原生4D生成模型，通过结构化时空潜在表示从单目视频直接合成动态3D对象。**

**关键词**: `4D生成模型` `动态3D合成` `时空潜在表示` `单目视频处理` `时间一致性` `结构一致性` `长视频压缩` `遮挡鲁棒性`

## 📋 核心要点

1. 现有方法依赖3D或视频生成模型优化构建4D表示，导致保真度、时间一致性和结构一致性不足。
2. SS4D通过结构化时空潜在表示，结合预训练单图像到3D模型、时序层和压缩机制，直接训练4D生成器。
3. 实验表明，SS4D在动态3D对象合成中实现了高保真度、时间一致性和高效性，优于现有方法。

## 📝 摘要（中文）

我们提出了SS4D，一种原生4D生成模型，能够直接从单目视频合成动态3D对象。与先前通过优化3D或视频生成模型来构建4D表示的方法不同，我们直接在4D数据上训练生成器，实现了高保真度、时间一致性和结构一致性。我们方法的核心是一组压缩的结构化时空潜在表示。具体来说：(1) 为了解决4D训练数据稀缺的问题，我们基于预训练的单图像到3D模型构建，保持了强大的空间一致性。(2) 通过引入专门的时序层来跨帧推理，强制实现时间一致性。(3) 为了支持长视频序列的高效训练和推理，我们使用分解的4D卷积和时序下采样块沿时间轴压缩潜在序列。此外，我们采用精心设计的训练策略来增强对遮挡的鲁棒性。

## 🔬 方法详解

SS4D的整体框架是一个原生4D生成模型，直接从单目视频输入生成动态3D对象。关键技术创新点包括：使用结构化时空潜在表示来编码4D数据；基于预训练单图像到3D模型确保空间一致性；引入时序层强制时间一致性；采用分解4D卷积和时序下采样块压缩潜在序列以支持长视频处理。与现有方法的主要区别在于，SS4D直接在4D数据上训练生成器，而非通过优化3D或视频模型间接构建4D表示，从而提升了生成质量和效率。

## 📊 实验亮点

SS4D在动态3D对象合成任务中表现出高保真度和时间一致性，通过结构化时空潜在表示和压缩机制，实现了对长视频的高效处理，实验结果显示其在生成质量上优于现有4D生成方法。

## 🎯 应用场景

该研究在虚拟现实、增强现实、游戏开发和电影特效等领域有潜在应用，可用于自动生成动态3D内容，减少人工建模成本，提升内容创作的效率和真实感。

## 📄 摘要（原文）

> We present SS4D, a native 4D generative model that synthesizes dynamic 3D objects directly from monocular video. Unlike prior approaches that construct 4D representations by optimizing over 3D or video generative models, we train a generator directly on 4D data, achieving high fidelity, temporal coherence, and structural consistency. At the core of our method is a compressed set of structured spacetime latents. Specifically, (1) To address the scarcity of 4D training data, we build on a pre-trained single-image-to-3D model, preserving strong spatial consistency. (2) Temporal consistency is enforced by introducing dedicated temporal layers that reason across frames. (3) To support efficient training and inference over long video sequences, we compress the latent sequence along the temporal axis using factorized 4D convolutions and temporal downsampling blocks. In addition, we employ a carefully designed training strategy to enhance robustness against occlusion

