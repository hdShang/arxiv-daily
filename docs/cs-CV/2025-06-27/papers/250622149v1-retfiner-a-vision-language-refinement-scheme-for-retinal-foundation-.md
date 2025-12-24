---
layout: default
title: "RetFiner: A Vision-Language Refinement Scheme for Retinal Foundation Models"
---

# RetFiner: A Vision-Language Refinement Scheme for Retinal Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22149" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22149v1</a>
  <a href="https://arxiv.org/pdf/2506.22149.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22149v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22149v1', 'RetFiner: A Vision-Language Refinement Scheme for Retinal Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ronald Fecso, José Morano, Ursula Schmidt-Erfurth, Hrvoje Bogunović

**分类**: cs.CV

**发布日期**: 2025-06-27

**备注**: Accepted for presentation at MICCAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ronnief1/RetFiner)

---

## 💡 一句话要点

**提出RetFiner以解决视网膜基础模型的语义理解不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜疾病` `自监督学习` `视觉-语言模型` `光学相干断层扫描` `深度学习` `医学影像分析` `模型精炼`

## 📋 核心要点

1. 现有的视网膜基础模型在复杂任务中表现不佳，缺乏全面的语义理解，导致需要进行监督微调。
2. RetFiner是一种自监督学习的视觉-语言精炼方案，利用文本数据中的丰富监督信号来改善模型表示。
3. 在七个OCT分类任务中，RetFiner显著提升了模型性能，平均提高了5.8、3.9和2.1个百分点。

## 📝 摘要（中文）

随着光学相干断层扫描（OCT）等成像技术的发展以及深度学习的进步，临床医生和研究人员能够更高效地进行视网膜疾病分期。然而，现有的视网膜基础模型（FMs）仅基于图像数据训练，缺乏全面的语义理解，导致在复杂任务中的表现不佳。因此，本文提出了RetFiner，一种自监督学习（SSL）视觉-语言精炼方案，旨在改善现有FMs的表示能力，并使其能够高效适应特定人群，从而提升下游任务的表现。实验结果表明，RetFiner在七个多样化的OCT分类任务中，分别在RETFound、UrFound和VisionFM上实现了显著的性能提升，平均提高了5.8、3.9和2.1个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视网膜基础模型在复杂任务中缺乏语义理解的问题。这些模型仅基于图像数据训练，导致在特定应用和人群中的适应性不足。

**核心思路**：RetFiner通过自监督学习（SSL）结合视觉和语言信息，利用文本数据中的丰富监督信号来改善模型的表示能力，从而提高下游任务的性能。

**技术框架**：RetFiner的整体架构包括多个训练目标，利用文本与图像的关联性来增强模型的学习效果。主要模块包括图像特征提取、文本特征提取和多任务学习模块。

**关键创新**：RetFiner的创新在于将视觉和语言信息结合，通过自监督学习的方式提升模型的语义理解能力，与传统仅依赖图像数据的训练方法形成鲜明对比。

**关键设计**：在模型设计中，采用了多样化的损失函数以平衡视觉和语言特征的学习，同时在网络结构上进行了优化，以适应不同的下游任务需求。具体的参数设置和训练策略在实验中进行了详细验证。

## 📊 实验亮点

RetFiner在七个OCT分类任务中表现出色，分别在RETFound、UrFound和VisionFM上实现了平均5.8、3.9和2.1个百分点的性能提升，显著优于基线模型，证明了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、视网膜疾病的自动诊断和分期等。通过提升模型的语义理解能力，RetFiner能够帮助临床医生更准确地分析OCT图像，进而改善患者的治疗效果。未来，该方法也可能扩展到其他医学成像领域，具有广泛的实际价值。

## 📄 摘要（原文）

> The rise of imaging techniques such as optical coherence tomography (OCT) and advances in deep learning (DL) have enabled clinicians and researchers to streamline retinal disease staging. A popular DL approach is self-supervised learning (SSL), where models learn from vast amounts of unlabeled data, avoiding costly annotation. SSL has allowed the development of foundation models (FMs), large models that can be used for a variety of downstream tasks. However, existing FMs for OCT, trained solely on image data, lack a comprehensive and robust semantic understanding of images, as evidenced by their downstream performance (especially for complex tasks), and thus require supervised fine-tuning (which may be unfeasible) to better adapt to specific applications and populations. To address this, we propose RetFiner, an SSL vision-language refinement scheme that improves the representations of existing FMs and enables their efficient and direct adaptation to specific populations for improved downstream performance. Our method uses a diverse set of training objectives which take advantage of the rich supervisory signal found in textual data. We tested RetFiner on the retinal FMs RETFound, UrFound, and VisionFM, showing significant improvements in linear probing performance on seven highly diverse OCT classification tasks, with an average increase of 5.8, 3.9, and 2.1 percentage points over their baselines, respectively. Our code and model weights are publicly available at https://github.com/ronnief1/RetFiner.

