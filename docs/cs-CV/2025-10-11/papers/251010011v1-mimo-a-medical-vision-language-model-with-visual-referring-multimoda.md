---
layout: default
title: MIMO: A medical vision language model with visual referring multimodal input and pixel grounding multimodal output
---

# MIMO: A medical vision language model with visual referring multimodal input and pixel grounding multimodal output

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10011" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10011v1</a>
  <a href="https://arxiv.org/pdf/2510.10011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10011v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10011v1', 'MIMO: A medical vision language model with visual referring multimodal input and pixel grounding multimodal output')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanyuan Chen, Dexuan Xu, Yu Huang, Songkun Zhan, Hanpin Wang, Dongxue Chen, Xueping Wang, Meikang Qiu, Hang Li

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: CVPR 2025

---

## 💡 一句话要点

**MIMO：一种具有视觉指代多模态输入和像素级定位多模态输出的医学视觉语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学视觉语言模型` `多模态学习` `视觉指代` `像素级定位` `医学影像` `视觉问答` `Transformer` `MIMOSeg数据集`

## 📋 核心要点

1. 现有医学视觉语言模型仅依赖文本指令，忽略了图像中的视觉线索，限制了模型对复杂医学图像的理解。
2. MIMO模型通过引入视觉指代多模态输入和像素级定位多模态输出，增强了模型对医学图像的理解和解释能力。
3. MIMOSeg数据集的构建，为医学多模态任务提供了大量数据支持，实验结果验证了MIMO在视觉指代和像素级定位方面的优势。

## 📝 摘要（中文）

目前，医学视觉语言模型被广泛应用于医学视觉问答任务。然而，现有模型面临两个问题：对于输入，模型仅依赖于文本指令，缺乏对图像中视觉线索的直接理解；对于输出，模型仅给出文本答案，缺乏与图像中关键区域的联系。为了解决这些问题，我们提出了一种统一的医学视觉语言模型MIMO，它具有视觉指代多模态输入和像素级定位多模态输出。MIMO不仅可以结合视觉线索和文本指令来理解复杂的医学图像和语义，还可以将文本输出中的医学术语定位到图像中。为了克服医学领域相关数据的稀缺性，我们提出了MIMOSeg，一个包含895K样本的综合医学多模态数据集。MIMOSeg从四个不同的角度构建，涵盖了具有多模态输入和多模态输出的基本指令跟随和复杂问题回答。我们在几个下游医学多模态任务上进行了实验。大量的实验结果验证了MIMO可以独特地结合视觉指代和像素级定位能力，这是以前的模型所不具备的。

## 🔬 方法详解

**问题定义**：现有医学视觉语言模型在处理医学视觉问答任务时，主要依赖文本指令作为输入，忽略了医学图像本身包含的丰富视觉信息。此外，模型输出通常仅为文本答案，无法将答案与图像中的具体区域关联起来，缺乏可解释性。这些问题限制了模型在实际医疗场景中的应用。

**核心思路**：MIMO的核心思路是同时利用视觉和文本信息作为输入，并生成既包含文本答案又包含像素级定位信息的输出。通过视觉指代多模态输入，模型可以更好地理解图像中的视觉线索。通过像素级定位多模态输出，模型可以将文本答案中的医学术语与图像中的对应区域关联起来，提高模型的可解释性。

**技术框架**：MIMO模型采用统一的架构，包含视觉编码器、文本编码器和多模态融合模块。视觉编码器负责提取医学图像的视觉特征，文本编码器负责提取文本指令的语义特征。多模态融合模块将视觉特征和语义特征融合，生成多模态表示。解码器根据多模态表示生成文本答案和像素级定位信息。整个流程实现了从多模态输入到多模态输出的端到端学习。

**关键创新**：MIMO的关键创新在于同时引入了视觉指代多模态输入和像素级定位多模态输出。视觉指代多模态输入使模型能够直接利用图像中的视觉信息，而像素级定位多模态输出使模型能够将文本答案与图像中的具体区域关联起来。这种双重创新使得MIMO在医学视觉语言任务中具有更强的理解和解释能力。

**关键设计**：MIMO模型使用了Transformer架构作为其核心组件。视觉编码器和文本编码器均采用Transformer编码器，多模态融合模块采用Transformer解码器。损失函数包括文本答案的交叉熵损失和像素级定位的Dice损失。MIMOSeg数据集的构建考虑了不同类型的医学图像和问答场景，包括基本指令跟随和复杂问题回答。

## 📊 实验亮点

该论文提出了MIMO模型，并在自建的MIMOSeg数据集上进行了实验。实验结果表明，MIMO模型在医学视觉问答任务中取得了显著的性能提升。与现有模型相比，MIMO模型能够更准确地理解医学图像和文本指令，并生成更具解释性的答案。具体性能数据和提升幅度在论文中详细给出。

## 🎯 应用场景

MIMO模型在医学影像诊断、辅助决策和医学教育等领域具有广泛的应用前景。它可以帮助医生更准确地理解医学图像，提供更全面的诊断信息，并为患者提供更清晰的解释。此外，MIMO还可以用于医学教育，帮助学生更好地理解医学图像和相关知识。

## 📄 摘要（原文）

> Currently, medical vision language models are widely used in medical vision question answering tasks. However, existing models are confronted with two issues: for input, the model only relies on text instructions and lacks direct understanding of visual clues in the image; for output, the model only gives text answers and lacks connection with key areas in the image. To address these issues, we propose a unified medical vision language model MIMO, with visual referring Multimodal Input and pixel grounding Multimodal Output. MIMO can not only combine visual clues and textual instructions to understand complex medical images and semantics, but can also ground medical terminologies in textual output within the image. To overcome the scarcity of relevant data in the medical field, we propose MIMOSeg, a comprehensive medical multimodal dataset including 895K samples. MIMOSeg is constructed from four different perspectives, covering basic instruction following and complex question answering with multimodal input and multimodal output. We conduct experiments on several downstream medical multimodal tasks. Extensive experimental results verify that MIMO can uniquely combine visual referring and pixel grounding capabilities, which are not available in previous models.

