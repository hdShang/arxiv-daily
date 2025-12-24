---
layout: default
title: "JEPA-T: Joint-Embedding Predictive Architecture with Text Fusion for Image Generation"
---

# JEPA-T: Joint-Embedding Predictive Architecture with Text Fusion for Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00974" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00974v1</a>
  <a href="https://arxiv.org/pdf/2510.00974.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00974v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00974v1', 'JEPA-T: Joint-Embedding Predictive Architecture with Text Fusion for Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siheng Wan, Zhengtao Yao, Zhengdao Li, Junhao Dong, Yanshu Li, Yikai Li, Linshan Li, Haoyan Xu, Yijiang Li, Zhikang Dong, Huacan Wang, Jifeng Shen

**分类**: cs.CV

**发布日期**: 2025-10-01

**🔗 代码/项目**: [GITHUB](https://github.com/justin-herry/JEPA-T.git)

---

## 💡 一句话要点

**提出JEPA-T，通过文本融合的联合嵌入预测架构提升图像生成效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `联合嵌入` `Transformer` `交叉注意力` `条件去噪` `多模态融合` `自监督学习`

## 📋 核心要点

1. 现有文本到图像生成方法难以有效融合文本和视觉token，限制了生成效果。
2. JEPA-T提出联合嵌入预测Transformer，结合交叉注意力和目标级别对齐，增强文本和图像的融合。
3. 实验表明，JEPA-T在数据效率和开放词汇泛化方面表现出色，优于现有基线方法。

## 📝 摘要（中文）

现代文本到图像（T2I）生成越来越依赖于使用自监督训练的以token为中心的架构，然而，有效地融合文本和视觉token仍然是一个挑战。我们提出了JEPA-T，一个统一的多模态框架，它将图像和标题编码为离散的视觉和文本token，并由联合嵌入预测Transformer处理。为了增强融合，我们在特征预测器之后加入了交叉注意力，用于条件去噪，同时保持任务无关的骨干网络。此外，在流匹配损失之前注入原始文本嵌入，以提高训练期间的对齐。在推理过程中，同一网络通过迭代地对以文本为条件的视觉token进行去噪，来执行类条件和自由文本图像生成。在ImageNet-1K上的评估表明，JEPA-T实现了强大的数据效率、开放词汇泛化，并且始终优于非融合和晚期融合基线。我们的方法表明，晚期架构融合与目标级别的对齐相结合，在基于token的T2I中，在条件强度和骨干通用性之间提供了一个有效的平衡。

## 🔬 方法详解

**问题定义**：现有文本到图像生成模型，特别是基于token的架构，在如何有效地将文本信息融入到视觉token的处理流程中面临挑战。简单的拼接或晚期融合策略可能无法充分利用文本信息，导致生成图像与文本描述不一致或细节缺失。现有方法在条件强度和骨干通用性之间难以取得平衡。

**核心思路**：JEPA-T的核心思路是采用联合嵌入预测架构，将图像和文本编码为离散的token，并在Transformer中进行联合处理。通过在特征预测器后引入交叉注意力机制，实现文本信息对视觉token的条件去噪，从而增强文本和图像的融合。此外，在训练过程中，通过在流匹配损失之前注入原始文本嵌入，进一步提高文本和图像的对齐。

**技术框架**：JEPA-T的整体架构包含以下几个主要模块：1) 图像和文本编码器：将图像和文本分别编码为离散的视觉和文本token。2) 联合嵌入预测Transformer：处理视觉和文本token，进行特征预测和融合。3) 交叉注意力模块：在特征预测器之后，利用文本信息对视觉token进行条件去噪。4) 流匹配损失：用于训练模型，并在损失计算前注入原始文本嵌入以提高对齐。在推理阶段，通过迭代去噪视觉token生成图像。

**关键创新**：JEPA-T的关键创新在于其融合策略，即晚期架构融合与目标级别对齐相结合。这种策略在保持骨干网络通用性的同时，增强了文本信息的条件作用。具体来说，交叉注意力模块的引入和原始文本嵌入的注入，使得文本信息能够更有效地指导图像生成过程。

**关键设计**：JEPA-T的关键设计包括：1) 使用离散的视觉和文本token表示图像和文本信息。2) 在特征预测器后添加交叉注意力模块，实现条件去噪。3) 在流匹配损失之前注入原始文本嵌入，以提高训练期间的对齐。4) 使用Transformer作为核心处理模块，进行特征预测和融合。具体的参数设置和网络结构细节未在摘要中详细说明，需要参考论文全文。

## 📊 实验亮点

JEPA-T在ImageNet-1K数据集上进行了评估，实验结果表明，JEPA-T实现了强大的数据效率和开放词汇泛化能力，并且始终优于非融合和晚期融合基线方法。具体的性能数据和提升幅度需要在论文全文中查找。

## 🎯 应用场景

JEPA-T在文本到图像生成领域具有广泛的应用前景，例如艺术创作、图像编辑、虚拟现实、游戏开发等。该研究可以用于生成高质量、与文本描述高度一致的图像，提升用户体验和创作效率。未来，该技术可以进一步扩展到视频生成、3D模型生成等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Modern Text-to-Image (T2I) generation increasingly relies on token-centric architectures that are trained with self-supervision, yet effectively fusing text with visual tokens remains a challenge. We propose \textbf{JEPA-T}, a unified multimodal framework that encodes images and captions into discrete visual and textual tokens, processed by a joint-embedding predictive Transformer. To enhance fusion, we incorporate cross-attention after the feature predictor for conditional denoising while maintaining a task-agnostic backbone. Additionally, raw texts embeddings are injected prior to the flow matching loss to improve alignment during training. During inference, the same network performs both class-conditional and free-text image generation by iteratively denoising visual tokens conditioned on text. Evaluations on ImageNet-1K demonstrate that JEPA-T achieves strong data efficiency, open-vocabulary generalization, and consistently outperforms non-fusion and late-fusion baselines. Our approach shows that late architectural fusion combined with objective-level alignment offers an effective balance between conditioning strength and backbone generality in token-based T2I.The code is now available: https://github.com/justin-herry/JEPA-T.git

