---
layout: default
title: "ACM-UNet: Adaptive Integration of CNNs and Mamba for Efficient Medical Image Segmentation"
---

# ACM-UNet: Adaptive Integration of CNNs and Mamba for Efficient Medical Image Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24481" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24481v1</a>
  <a href="https://arxiv.org/pdf/2505.24481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24481v1', 'ACM-UNet: Adaptive Integration of CNNs and Mamba for Efficient Medical Image Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Huang, Yongkang Zhao, Yuhan Li, Zhitao Dai, Cheng Chen, Qiying Lai

**分类**: cs.CV

**发布日期**: 2025-05-30

**备注**: 10 pages, 3 figures, 5 tables

**🔗 代码/项目**: [GITHUB](https://github.com/zyklcode/ACM-UNet)

---

## 💡 一句话要点

**提出ACM-UNet以解决医疗图像分割中的结构不匹配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `医疗图像分割` `卷积神经网络` `Mamba模型` `特征融合` `深度学习`

## 📋 核心要点

1. 现有的医疗图像分割方法在利用预训练模型时常因结构不匹配而无法充分发挥其优势。
2. ACM-UNet通过轻量级适配器机制有效整合CNN和Mamba模型，解决了架构不兼容问题。
3. 在Synapse数据集上，ACM-UNet达到了85.12%的Dice Score和13.89mm的HD95，展示了其优越的性能和计算效率。

## 📝 摘要（中文）

U型编码器-解码器架构因其简单有效而成为医疗图像分割的主流范式。尽管许多研究致力于通过设计更强大的编码器和解码器来改进这一框架，但现有方法在充分利用预训练视觉骨干网络（如ResNet、ViT、VMamba）时常面临结构不匹配的问题。为此，本文提出了ACM-UNet，一个通用的分割框架，保留了简单的UNet设计，同时通过轻量级适配器机制有效整合预训练的CNN和Mamba模型，解决了架构不兼容问题，充分发挥了CNN和SSM的互补优势。此外，本文在解码器中提出了分层多尺度小波变换模块，以增强特征融合和重建精度。大量实验表明，ACM-UNet在Synapse和ACDC基准测试上实现了最先进的性能，同时保持了计算效率。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗图像分割中预训练模型与现有架构之间的结构不匹配问题，导致无法充分利用其特征提取能力。

**核心思路**：ACM-UNet通过引入轻量级适配器机制，保留UNet的简单设计，同时有效整合CNN和Mamba模型，充分发挥它们在局部细节提取和长程依赖建模方面的互补优势。

**技术框架**：ACM-UNet的整体架构包括一个U型编码器-解码器结构，结合了轻量级适配器和分层多尺度小波变换模块，以增强特征融合和重建精度。

**关键创新**：最重要的创新在于轻量级适配器的设计，使得预训练的CNN和Mamba模型能够无缝集成，克服了以往方法的结构不兼容问题。

**关键设计**：在网络结构中，适配器的参数设置经过精心设计，以确保模型在保持计算效率的同时，能够实现高质量的特征提取和融合。

## 📊 实验亮点

在Synapse数据集上，ACM-UNet达到了85.12%的Dice Score和13.89mm的HD95，计算复杂度为17.93G FLOPs，展现了其在性能和效率上的显著优势，超越了现有的基线方法。

## 🎯 应用场景

ACM-UNet在医疗图像分割领域具有广泛的应用潜力，能够有效提高医学影像的处理精度，辅助医生进行诊断和治疗决策。未来，该方法还可扩展到其他图像处理任务，如自动驾驶、遥感图像分析等，具有重要的实际价值和影响。

## 📄 摘要（原文）

> The U-shaped encoder-decoder architecture with skip connections has become a prevailing paradigm in medical image segmentation due to its simplicity and effectiveness. While many recent works aim to improve this framework by designing more powerful encoders and decoders, employing advanced convolutional neural networks (CNNs) for local feature extraction, Transformers or state space models (SSMs) such as Mamba for global context modeling, or hybrid combinations of both, these methods often struggle to fully utilize pretrained vision backbones (e.g., ResNet, ViT, VMamba) due to structural mismatches. To bridge this gap, we introduce ACM-UNet, a general-purpose segmentation framework that retains a simple UNet-like design while effectively incorporating pretrained CNNs and Mamba models through a lightweight adapter mechanism. This adapter resolves architectural incompatibilities and enables the model to harness the complementary strengths of CNNs and SSMs-namely, fine-grained local detail extraction and long-range dependency modeling. Additionally, we propose a hierarchical multi-scale wavelet transform module in the decoder to enhance feature fusion and reconstruction fidelity. Extensive experiments on the Synapse and ACDC benchmarks demonstrate that ACM-UNet achieves state-of-the-art performance while remaining computationally efficient. Notably, it reaches 85.12% Dice Score and 13.89mm HD95 on the Synapse dataset with 17.93G FLOPs, showcasing its effectiveness and scalability. Code is available at: https://github.com/zyklcode/ACM-UNet.

