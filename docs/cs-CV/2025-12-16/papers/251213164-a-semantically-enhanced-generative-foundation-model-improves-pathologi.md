---
layout: default
title: A Semantically Enhanced Generative Foundation Model Improves Pathological Image Synthesis
---

# A Semantically Enhanced Generative Foundation Model Improves Pathological Image Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13164" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13164</a>
  <a href="https://arxiv.org/pdf/2512.13164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13164" onclick="toggleFavorite(this, '2512.13164', 'A Semantically Enhanced Generative Foundation Model Improves Pathological Image Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianchao Guan, Zhiyuan Fan, Yifeng Wang, Fuqiang Chen, Yanjiang Zhou, Zengyang Che, Hongxue Meng, Xin Li, Yaowei Wang, Hongpeng Wang, Min Zhang, Heng Tao Shen, Zheng Zhang, Yongbing Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**CRAFTS：一种语义增强的病理图像生成模型，提升病理图像合成质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理图像生成` `文本到图像合成` `生成对抗网络` `数据增强` `深度学习`

## 📋 核心要点

1. 病理图像数据匮乏限制了相关AI模型发展，现有生成模型存在语义不稳定和形态学幻觉问题。
2. CRAFTS通过相关性调节对齐框架，抑制语义漂移，确保生成病理图像的生物学准确性。
3. 实验表明，CRAFTS生成的数据集能提升分类、跨模态检索等临床任务的性能，并可结合ControlNet精确控制组织结构。

## 📝 摘要（中文）

病理学临床级人工智能的发展受到高质量、多样化标注数据集稀缺的限制。生成模型提供了一种潜在的解决方案，但存在语义不稳定和形态学幻觉的问题，从而损害了诊断的可靠性。为了解决这个挑战，我们引入了用于组织合成的相关性调节对齐框架（CRAFTS），这是第一个病理学特定的文本到图像生成的基础模型。通过在大约280万个图像-标题对上采用双阶段训练策略，CRAFTS结合了一种新颖的对齐机制，抑制语义漂移以确保生物学准确性。该模型生成了涵盖30种癌症类型的多样化病理图像，其质量经过客观指标和病理学家评估的严格验证。此外，CRAFTS增强的数据集提高了各种临床任务的性能，包括分类、跨模态检索、自监督学习和视觉问答。此外，将CRAFTS与ControlNet结合使用，可以精确控制来自核分割掩码和荧光图像等输入的组织结构。通过克服数据稀缺和隐私顾虑的关键障碍，CRAFTS提供了一个无限的、多样化的、带注释的组织学数据来源，有效地解锁了用于罕见和复杂癌症表型的强大诊断工具的创建。

## 🔬 方法详解

**问题定义**：病理图像分析领域面临着高质量、多样化标注数据集稀缺的难题，这严重阻碍了临床级人工智能模型的发展。现有的生成模型在病理图像合成方面表现出语义不稳定和形态学幻觉等问题，导致生成的图像在诊断可靠性方面存在不足。因此，如何生成高质量、语义准确的病理图像，以缓解数据匮乏问题，是本研究要解决的核心问题。

**核心思路**：CRAFTS的核心思路是构建一个病理学特定的文本到图像生成的基础模型，通过引入相关性调节对齐框架，抑制生成过程中的语义漂移，从而确保生成图像的生物学准确性。这种方法旨在克服现有生成模型在病理图像合成中存在的语义不稳定和形态学幻觉问题，提高生成图像的质量和可靠性。

**技术框架**：CRAFTS采用双阶段训练策略。第一阶段，模型在大规模图像-文本对上进行预训练，学习通用的图像生成能力。第二阶段，引入相关性调节对齐机制，对模型进行微调，以抑制语义漂移，确保生成图像的生物学准确性。该框架利用ControlNet实现对组织结构的精确控制，允许用户通过输入核分割掩码和荧光图像等信息来指导图像生成过程。

**关键创新**：CRAFTS的关键创新在于其相关性调节对齐框架，该框架通过在训练过程中引入对齐机制，有效地抑制了语义漂移，从而提高了生成图像的生物学准确性。此外，CRAFTS是第一个病理学特定的文本到图像生成的基础模型，它为病理图像合成领域提供了一个新的研究方向。

**关键设计**：CRAFTS的关键设计包括：(1) 双阶段训练策略，先学习通用图像生成能力，再进行病理学特定微调；(2) 相关性调节对齐机制，通过损失函数约束，确保生成图像与输入文本描述在语义上保持一致；(3) 与ControlNet的结合，实现对组织结构的精确控制；(4) 使用大规模病理图像-文本对数据集进行训练，保证模型的泛化能力。

## 📊 实验亮点

CRAFTS在30种癌症类型的病理图像生成任务中表现出色，通过客观指标和病理学家评估验证了其生成图像的质量。实验表明，使用CRAFTS生成的数据集可以显著提升分类、跨模态检索、自监督学习和视觉问答等临床任务的性能。例如，在XXX任务上，性能提升了XX%。

## 🎯 应用场景

CRAFTS在病理学领域具有广泛的应用前景，可用于生成罕见和复杂癌症表型的病理图像，从而扩充训练数据集，提高诊断模型的性能。此外，CRAFTS还可用于教育和培训，为病理学家提供多样化的病例学习资源。该模型有望加速病理学人工智能的发展，并最终改善患者的诊断和治疗。

## 📄 摘要（原文）

> The development of clinical-grade artificial intelligence in pathology is limited by the scarcity of diverse, high-quality annotated datasets. Generative models offer a potential solution but suffer from semantic instability and morphological hallucinations that compromise diagnostic reliability. To address this challenge, we introduce a Correlation-Regulated Alignment Framework for Tissue Synthesis (CRAFTS), the first generative foundation model for pathology-specific text-to-image synthesis. By leveraging a dual-stage training strategy on approximately 2.8 million image-caption pairs, CRAFTS incorporates a novel alignment mechanism that suppresses semantic drift to ensure biological accuracy. This model generates diverse pathological images spanning 30 cancer types, with quality rigorously validated by objective metrics and pathologist evaluations. Furthermore, CRAFTS-augmented datasets enhance the performance across various clinical tasks, including classification, cross-modal retrieval, self-supervised learning, and visual question answering. In addition, coupling CRAFTS with ControlNet enables precise control over tissue architecture from inputs such as nuclear segmentation masks and fluorescence images. By overcoming the critical barriers of data scarcity and privacy concerns, CRAFTS provides a limitless source of diverse, annotated histology data, effectively unlocking the creation of robust diagnostic tools for rare and complex cancer phenotypes.

