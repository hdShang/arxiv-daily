---
layout: default
title: "LaTo: Landmark-tokenized Diffusion Transformer for Fine-grained Human Face Editing"
---

# LaTo: Landmark-tokenized Diffusion Transformer for Fine-grained Human Face Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25731" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25731v1</a>
  <a href="https://arxiv.org/pdf/2509.25731.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25731v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25731v1', 'LaTo: Landmark-tokenized Diffusion Transformer for Fine-grained Human Face Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenghao Zhang, Ziying Zhang, Junchao Liao, Xiangyu Meng, Qiang Hu, Siyu Zhu, Xiaoyun Zhang, Long Qin, Weizhi Wang

**分类**: cs.CV

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**LaTo：用于精细人脸编辑的地标Token化扩散Transformer**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人脸编辑` `扩散模型` `Transformer` `地标Token化` `身份保持` `视觉语言模型` `精细控制`

## 📋 核心要点

1. 现有基于指令的人脸编辑方法难以在精确控制属性和保持身份信息之间取得平衡。
2. LaTo通过地标Token化、位置映射编码和地标预测器实现精细化、身份保持的人脸编辑。
3. 实验表明，LaTo在身份保持和语义一致性方面显著优于现有方法，并构建了大规模数据集HFL-150K。

## 📝 摘要（中文）

最近基于指令的多模态人脸编辑模型虽然能够进行语义操作，但在精确属性控制和身份保持方面仍然存在困难。诸如地标的结构化面部表示对于中间监督是有效的，但现有方法大多将其视为刚性几何约束，当条件地标与源图像差异较大时（例如，大的表情或姿势变化，不准确的地标估计），会降低身份保持能力。为了解决这些限制，我们提出了LaTo，一种用于精细、身份保持的人脸编辑的地标Token化扩散Transformer。我们的关键创新包括：（1）一个地标Token化器，它直接将原始地标坐标量化为离散的面部Token，从而消除了对密集像素级对应关系的需求；（2）一个位置映射位置编码，它集成了面部和图像Token以进行统一处理，从而以高效率和强大的身份保持能力实现灵活但解耦的几何-外观交互；（3）一个地标预测器，它利用视觉-语言模型从指令和源图像推断目标地标，其结构化的思维链提高了估计精度和交互控制。为了缓解数据稀缺问题，我们整理了HFL-150K，据我们所知，这是该任务最大的基准，包含超过15万个带有精细指令的真实面部对。大量实验表明，LaTo在身份保持方面比最先进的方法高出7.8%，在语义一致性方面高出4.6%。代码和数据集将在接受后公开发布。

## 🔬 方法详解

**问题定义**：现有基于指令的人脸编辑方法，虽然可以进行语义操作，但在精确控制面部属性（如眼睛大小、嘴唇厚度）和保持身份信息方面存在困难。现有方法通常将人脸地标作为刚性几何约束，当目标地标与源图像差异较大时，容易导致身份信息丢失，并且依赖于像素级别的对应关系，计算成本高昂。

**核心思路**：LaTo的核心思路是将人脸地标信息转化为离散的Token，并结合扩散Transformer模型，实现对人脸属性的精细控制和身份信息的有效保持。通过地标Token化，避免了对像素级别对应关系的依赖，提高了效率。通过位置映射编码，实现了几何信息和外观信息的灵活交互。

**技术框架**：LaTo的整体框架包含三个主要模块：地标Token化器、位置映射位置编码和地标预测器。首先，地标预测器根据指令和源图像预测目标地标。然后，地标Token化器将原始地标坐标量化为离散的Token。接着，位置映射位置编码将面部Token和图像Token进行整合，输入到扩散Transformer中进行处理。最后，扩散Transformer生成编辑后的人脸图像。

**关键创新**：LaTo的关键创新在于：（1）地标Token化器，它将连续的地标坐标转化为离散的Token，避免了对像素级别对应关系的依赖；（2）位置映射位置编码，它实现了面部几何信息和图像外观信息的灵活且解耦的交互，从而在保持身份信息的同时，实现对人脸属性的精细控制；（3）地标预测器，利用视觉-语言模型，通过结构化的思维链，提高了地标预测的准确性和交互控制能力。

**关键设计**：地标Token化器使用可学习的码本将地标坐标量化为离散Token。位置映射位置编码通过学习到的映射函数，将地标Token的位置信息嵌入到图像Token中。地标预测器使用预训练的视觉-语言模型，并引入思维链提示，逐步推理出目标地标。扩散Transformer采用U-Net结构，并引入注意力机制，实现对全局信息的建模。

## 📊 实验亮点

LaTo在身份保持方面比现有最先进方法提升了7.8%，在语义一致性方面提升了4.6%。作者还构建了一个包含超过15万个真实人脸对的大规模数据集HFL-150K，为该领域的研究提供了重要的数据支持。这些实验结果表明，LaTo在精细人脸编辑方面具有显著优势。

## 🎯 应用场景

LaTo技术可应用于人脸美化、虚拟形象定制、人脸动画生成、以及数字内容创作等领域。该技术能够实现对人脸属性的精细控制，同时保持身份信息，具有广泛的应用前景和商业价值。未来，该技术有望在元宇宙、游戏、社交媒体等领域发挥重要作用。

## 📄 摘要（原文）

> Recent multimodal models for instruction-based face editing enable semantic manipulation but still struggle with precise attribute control and identity preservation. Structural facial representations such as landmarks are effective for intermediate supervision, yet most existing methods treat them as rigid geometric constraints, which can degrade identity when conditional landmarks deviate significantly from the source (e.g., large expression or pose changes, inaccurate landmark estimates). To address these limitations, we propose LaTo, a landmark-tokenized diffusion transformer for fine-grained, identity-preserving face editing. Our key innovations include: (1) a landmark tokenizer that directly quantizes raw landmark coordinates into discrete facial tokens, obviating the need for dense pixel-wise correspondence; (2) a location-mapping positional encoding that integrates facial and image tokens for unified processing, enabling flexible yet decoupled geometry-appearance interactions with high efficiency and strong identity preservation; and (3) a landmark predictor that leverages vision-language models to infer target landmarks from instructions and source images, whose structured chain-of-thought improves estimation accuracy and interactive control. To mitigate data scarcity, we curate HFL-150K, to our knowledge the largest benchmark for this task, containing over 150K real face pairs with fine-grained instructions. Extensive experiments show that LaTo outperforms state-of-the-art methods by 7.8% in identity preservation and 4.6% in semantic consistency. Code and dataset will be made publicly available upon acceptance.

