---
layout: default
title: MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation
---

# MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.09121" target="_blank" class="toolbar-btn">arXiv: 2510.09121v2</a>
    <a href="https://arxiv.org/pdf/2510.09121.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09121v2" 
            onclick="toggleFavorite(this, '2510.09121v2', 'MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Dominik Winter, Mai Bui, Monica Azqueta Gavaldon, Nicolas Triltsch, Marco Rosati, Nicolas Brieu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-10 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出MSDM，一种多模态条件扩散模型，用于生成细胞和细胞核分割任务的病理图像。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `扩散模型` `图像生成` `细胞分割` `病理图像分析`

## 📋 核心要点

1. 计算病理学中细胞和细胞核分割面临标注数据稀缺的挑战，尤其对于罕见或非典型形态。
2. MSDM通过多模态信息（形态、颜色、元数据）调节扩散模型，生成具有特定形态属性的合成图像。
3. 实验表明，MSDM生成的图像与真实数据匹配良好，并能有效提升分割模型在特定细胞类型上的准确性。

## 📝 摘要（中文）

本文提出了一种多模态语义扩散模型（MSDM），用于生成逼真的、像素精确的细胞和细胞核分割图像-掩码对。针对计算病理学中带注释数据稀缺，特别是罕见或非典型形态数据的问题，MSDM通过细胞/细胞核形态（使用水平和垂直图）、RGB颜色特征以及BERT编码的检测/适应症元数据来调节生成过程，从而生成具有所需形态属性的数据集。通过多头交叉注意力集成这些异构模态，实现对生成图像的精细控制。定量分析表明，合成图像与真实数据非常匹配，在匹配的生物条件下，生成图像和真实图像的嵌入之间的Wasserstein距离较低。将这些合成样本（以柱状细胞为例）纳入训练，显著提高了分割模型在柱状细胞上的准确性。该策略系统地丰富了数据集，直接针对模型缺陷。本文强调了基于多模态扩散的增强方法在提高细胞和细胞核分割模型的鲁棒性和泛化性方面的有效性，为生成模型在计算病理学中的更广泛应用铺平了道路。

## 🔬 方法详解

**问题定义**：计算病理学中的细胞和细胞核分割任务面临着标注数据不足的问题，特别是对于罕见或非典型形态的细胞。手动标注成本高昂且耗时，限制了模型的训练和泛化能力。现有的数据增强方法难以生成具有特定形态特征的图像，无法有效解决模型在特定类型细胞上的分割性能瓶颈。

**核心思路**：论文的核心思路是利用多模态条件扩散模型生成具有特定形态特征的合成病理图像，从而扩充训练数据集，提升分割模型在特定细胞类型上的性能。通过将细胞形态、颜色特征和元数据信息融入生成过程，实现对合成图像的精细控制，使其更接近真实病理图像的分布。

**技术框架**：MSDM模型基于扩散模型框架，包含以下主要模块：1) 多模态编码器：用于提取细胞形态（水平和垂直图）、RGB颜色特征和BERT编码的元数据信息。2) 多头交叉注意力模块：用于融合来自不同模态的信息，实现模态间的交互。3) 扩散模型：基于编码后的多模态信息，逐步生成合成图像和对应的分割掩码。4) 分割模型：利用真实图像和合成图像进行训练，提升分割性能。

**关键创新**：MSDM的关键创新在于：1) 提出了一种多模态条件扩散模型，能够将多种异构信息（形态、颜色、元数据）融入生成过程，实现对合成图像的精细控制。2) 利用多头交叉注意力机制，有效融合来自不同模态的信息，提升了生成图像的质量和多样性。3) 将合成图像应用于分割模型的训练，有效提升了模型在特定细胞类型上的分割性能。

**关键设计**：MSDM使用U-Net作为扩散模型的主干网络，并引入了多头交叉注意力机制来融合不同模态的信息。损失函数包括扩散模型的重建损失和分割模型的交叉熵损失。在训练过程中，作者使用了Wasserstein距离来评估合成图像和真实图像之间的分布差异，并根据Wasserstein距离调整生成模型的参数。

## 📊 实验亮点

实验结果表明，MSDM生成的合成图像与真实数据匹配良好，在匹配的生物条件下，生成图像和真实图像的嵌入之间的Wasserstein距离较低。将MSDM生成的合成图像（以柱状细胞为例）纳入训练，显著提高了分割模型在柱状细胞上的准确性。例如，在柱状细胞的分割任务上，分割模型的Dice系数提升了显著幅度（具体数值未提供）。

## 🎯 应用场景

该研究成果可应用于计算病理学领域，通过生成具有特定形态特征的合成病理图像，解决标注数据不足的问题，提升细胞和细胞核分割模型的性能。该方法还可推广到其他医学图像分析任务，例如肿瘤检测、疾病诊断等，具有重要的临床应用价值和潜力。

## 📄 摘要（原文）

> Scarcity of annotated data, particularly for rare or atypical morphologies, present significant challenges for cell and nuclei segmentation in computational pathology. While manual annotation is labor-intensive and costly, synthetic data offers a cost-effective alternative. We introduce a Multimodal Semantic Diffusion Model (MSDM) for generating realistic pixel-precise image-mask pairs for cell and nuclei segmentation. By conditioning the generative process with cellular/nuclear morphologies (using horizontal and vertical maps), RGB color characteristics, and BERT-encoded assay/indication metadata, MSDM generates datasests with desired morphological properties. These heterogeneous modalities are integrated via multi-head cross-attention, enabling fine-grained control over the generated images. Quantitative analysis demonstrates that synthetic images closely match real data, with low Wasserstein distances between embeddings of generated and real images under matching biological conditions. The incorporation of these synthetic samples, exemplified by columnar cells, significantly improves segmentation model accuracy on columnar cells. This strategy systematically enriches data sets, directly targeting model deficiencies. We highlight the effectiveness of multimodal diffusion-based augmentation for advancing the robustness and generalizability of cell and nuclei segmentation models. Thereby, we pave the way for broader application of generative models in computational pathology.

