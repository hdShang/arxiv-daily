---
layout: default
title: Dynadiff: Single-stage Decoding of Images from Continuously Evolving fMRI
---

# Dynadiff: Single-stage Decoding of Images from Continuously Evolving fMRI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14556" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14556v1</a>
  <a href="https://arxiv.org/pdf/2505.14556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14556v1', 'Dynadiff: Single-stage Decoding of Images from Continuously Evolving fMRI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marlène Careil, Yohann Benchetrit, Jean-Rémi King

**分类**: cs.CV

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出Dynadiff以解决动态fMRI图像解码问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `动态fMRI` `脑到图像解码` `单阶段模型` `扩散模型` `神经活动重建` `时间分辨率` `生成性AI` `图像重建`

## 📋 核心要点

1. 现有脑到图像解码方法依赖复杂的多阶段流程，导致时间分辨率受限。
2. Dynadiff是一种新型单阶段扩散模型，旨在从动态fMRI记录中重建图像，简化训练过程。
3. 实验结果表明，Dynadiff在时间分辨率的fMRI信号上表现优异，尤其在高层次语义图像重建指标上超越了现有模型。

## 📝 摘要（中文）

脑到图像的解码近年来受到生成性AI模型和超高场功能性磁共振成像(fMRI)数据的推动。然而，现有方法依赖复杂的多阶段流程和预处理步骤，通常会压缩脑电信号的时间维度，从而限制了时间分辨率的脑解码器。本文提出Dynadiff（动态神经活动扩散模型），旨在从动态演变的fMRI记录中重建图像。我们的研究有三大贡献：首先，Dynadiff简化了训练过程；其次，在时间分辨率的fMRI信号上，该模型在高层次语义图像重建指标上超越了现有最先进模型，并在压缩时间的fMRI数据上保持竞争力；最后，该方法能够精确表征脑活动中图像表示的演变。总体而言，这项工作为时间分辨率的脑到图像解码奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决从动态演变的fMRI记录中重建图像的具体问题。现有方法通常依赖复杂的多阶段流程和预处理步骤，导致时间维度的压缩，从而限制了时间分辨率的脑解码能力。

**核心思路**：Dynadiff模型的核心思路是通过单阶段扩散模型直接从动态fMRI信号中重建图像，避免了多阶段处理的复杂性。这种设计使得模型能够更好地捕捉时间变化的信息。

**技术框架**：Dynadiff的整体架构包括输入动态fMRI信号、通过扩散模型进行图像重建、以及输出重建图像。模型的训练过程相对简单，能够有效利用时间序列数据。

**关键创新**：Dynadiff的主要创新在于其单阶段解码的能力，显著简化了训练过程，并在时间分辨率的信号上表现优越。这与现有依赖多阶段流程的解码方法形成了鲜明对比。

**关键设计**：模型采用了特定的损失函数以优化图像重建质量，并在网络结构上进行了调整，以适应动态fMRI信号的特性。具体的参数设置和网络层次设计在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，Dynadiff在时间分辨率的fMRI信号上超越了现有最先进模型，尤其在高层次语义图像重建指标上表现优异。具体而言，相较于基线模型，Dynadiff在图像重建质量上提升了XX%，展现了其在动态脑活动解码中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括神经科学研究、脑机接口、以及临床诊断等。通过提高脑到图像解码的时间分辨率，Dynadiff能够帮助研究人员更好地理解脑活动与视觉感知之间的关系，推动相关领域的发展。

## 📄 摘要（原文）

> Brain-to-image decoding has been recently propelled by the progress in generative AI models and the availability of large ultra-high field functional Magnetic Resonance Imaging (fMRI). However, current approaches depend on complicated multi-stage pipelines and preprocessing steps that typically collapse the temporal dimension of brain recordings, thereby limiting time-resolved brain decoders. Here, we introduce Dynadiff (Dynamic Neural Activity Diffusion for Image Reconstruction), a new single-stage diffusion model designed for reconstructing images from dynamically evolving fMRI recordings. Our approach offers three main contributions. First, Dynadiff simplifies training as compared to existing approaches. Second, our model outperforms state-of-the-art models on time-resolved fMRI signals, especially on high-level semantic image reconstruction metrics, while remaining competitive on preprocessed fMRI data that collapse time. Third, this approach allows a precise characterization of the evolution of image representations in brain activity. Overall, this work lays the foundation for time-resolved brain-to-image decoding.

