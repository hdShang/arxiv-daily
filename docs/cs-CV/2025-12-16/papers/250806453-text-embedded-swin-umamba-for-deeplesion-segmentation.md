---
layout: default
title: Text Embedded Swin-UMamba for DeepLesion Segmentation
---

# Text Embedded Swin-UMamba for DeepLesion Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06453" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06453</a>
  <a href="https://arxiv.org/pdf/2508.06453.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06453" onclick="toggleFavorite(this, '2508.06453', 'Text Embedded Swin-UMamba for DeepLesion Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruida Cheng, Tejas Sudharshan Mathai, Pritam Mukherjee, Benjamin Hou, Qingqing Zhu, Zhiyong Lu, Matthew McAuliffe, Ronald M. Summers

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Text Embedded Swin-UMamba模型，用于融合文本信息的DeepLesion病灶分割。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病灶分割` `深度学习` `Swin Transformer` `Mamba` `文本嵌入` `医学影像` `多模态融合`

## 📋 核心要点

1. 现有病灶分割方法缺乏对放射报告文本信息的有效利用，限制了分割精度和临床应用价值。
2. 提出Text-Swin-U/Mamba模型，通过嵌入文本特征，增强模型对病灶特征的理解和分割能力。
3. 实验结果表明，该模型在DeepLesion数据集上显著优于现有方法，Dice score提升显著。

## 📝 摘要（中文）

本研究探讨了将大型语言模型（LLM）集成到Swin-UMamba架构中，用于病灶分割的可行性，旨在结合影像特征与放射报告中的病灶描述。该方法应用于公开的ULS23 DeepLesion数据集，并结合报告中的简短描述。实验结果表明，该方法在测试数据集上实现了82.64的高Dice score和6.34像素的低Hausdorff距离。所提出的Text-Swin-U/Mamba模型优于现有方法，相比于LLM驱动的LanGuideMedSeg模型提升了37.79%（p < 0.001），并且超越了纯图像的XLSTM-UNet和nnUNet模型，分别提升了2.58%和1.01%。数据集和代码可在指定URL获取。

## 🔬 方法详解

**问题定义**：论文旨在解决CT图像中病灶的精确分割问题。现有方法，如纯图像分割模型，忽略了放射报告中包含的丰富文本信息，这些信息可以提供关于病灶特征的重要线索。因此，如何有效地融合图像和文本信息，提高病灶分割的准确性，是本研究要解决的关键问题。

**核心思路**：论文的核心思路是将放射报告的文本描述嵌入到Swin-UMamba架构中，利用文本信息增强模型对病灶特征的理解。Swin Transformer和Mamba架构分别擅长处理图像和序列数据，通过有效融合二者，可以充分利用图像和文本信息，提高分割精度。

**技术框架**：该模型基于Swin-UMamba架构，并引入文本嵌入模块。整体流程包括：1）图像输入经过Swin Transformer编码器提取图像特征；2）文本输入经过文本编码器（可能是预训练的语言模型）提取文本特征；3）图像特征和文本特征通过融合模块进行融合；4）融合后的特征输入到UMamba解码器进行分割；5）输出分割结果。

**关键创新**：该研究的关键创新在于将文本信息有效地融入到Swin-UMamba架构中，实现了图像和文本信息的联合建模。与传统的纯图像分割方法相比，该方法能够利用放射报告中的文本描述，提高对病灶特征的理解和分割精度。与直接使用LLM的方法相比，该方法更加轻量级，且针对病灶分割任务进行了优化。

**关键设计**：具体的文本嵌入方式、图像和文本特征的融合策略、以及UMamba解码器的具体结构是关键的设计细节。论文可能采用了某种注意力机制或跨模态融合模块来实现图像和文本特征的有效融合。损失函数可能包括Dice loss、交叉熵损失等，用于优化分割结果。

## 📊 实验亮点

实验结果表明，Text-Swin-U/Mamba模型在DeepLesion数据集上取得了显著的性能提升。Dice score达到了82.64，Hausdorff距离为6.34像素。相比于LLM驱动的LanGuideMedSeg模型，性能提升了37.79%（p < 0.001）。同时，该模型也超越了纯图像的XLSTM-UNet和nnUNet模型，分别提升了2.58%和1.01%。

## 🎯 应用场景

该研究成果可应用于医学影像辅助诊断，例如淋巴瘤等慢性疾病的病灶自动测量和评估。通过结合影像特征和文本描述，可以提高诊断效率和准确性，辅助医生进行临床决策。未来，该方法可以推广到其他医学影像分割任务，并与其他临床信息系统集成，实现更智能化的医疗服务。

## 📄 摘要（原文）

> Segmentation of lesions on CT enables automatic measurement for clinical assessment of chronic diseases (e.g., lymphoma). Integrating large language models (LLMs) into the lesion segmentation workflow has the potential to combine imaging features with descriptions of lesion characteristics from the radiology reports. In this study, we investigate the feasibility of integrating text into the Swin-UMamba architecture for the task of lesion segmentation. The publicly available ULS23 DeepLesion dataset was used along with short-form descriptions of the findings from the reports. On the test dataset, our method achieved a high Dice score of 82.64, and a low Hausdorff distance of 6.34 pixels was obtained for lesion segmentation. The proposed Text-Swin-U/Mamba model outperformed prior approaches: 37.79% improvement over the LLM-driven LanGuideMedSeg model (p < 0.001), and surpassed the purely image-based XLSTM-UNet and nnUNet models by 2.58% and 1.01%, respectively. The dataset and code can be accessed atthis https URL

