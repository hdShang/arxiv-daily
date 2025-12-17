---
layout: default
title: Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs
---

# Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17771" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17771v1</a>
  <a href="https://arxiv.org/pdf/2510.17771.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17771v1" onclick="toggleFavorite(this, '2510.17771v1', 'Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhining Liu, Ziyi Chen, Hui Liu, Chen Luo, Xianfeng Tang, Suhang Wang, Joy Zeng, Zhenwei Dai, Zhan Shi, Tianxin Wei, Benoit Dumoulin, Hanghang Tong

**分类**: cs.AI, cs.CV

**发布日期**: 2025-10-20

**备注**: 21 pages, 10 figures, 6 tables

---

## 💡 一句话要点

**揭示视觉语言模型“视而不信”现象，提出无需训练的注意力干预方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `视觉问答` `注意力机制` `推理时干预` `视而不信`

## 📋 核心要点

1. 现有视觉语言模型在视觉问答任务中，即使存在正确视觉证据，仍会给出错误答案，原因尚不明确。
2. 该研究发现深层注意力机制能够定位到关键视觉证据，但模型未能有效利用这些信息进行推理。
3. 提出一种无需训练的推理时干预方法，通过突出深层注意力区域，显著提升了多种VLMs的准确性。

## 📝 摘要（中文）

视觉语言模型(VLMs)在视觉问答等多模态任务中表现出色，但即使存在正确的视觉证据，仍然可能失败。本文系统地研究了这些失败是源于未能感知到证据，还是未能有效地利用证据。通过检查逐层注意力动态，发现浅层主要关注文本，而深层稀疏但可靠地关注局部证据区域。令人惊讶的是，VLMs在输出错误答案时通常感知到视觉证据，这种现象被称为“视而不信”，广泛存在于主要的VLM家族中。在此基础上，本文提出了一种推理时干预方法，通过基于选择性注意力的掩码突出显示深层证据区域。该方法无需训练，并能持续提高多个VLM家族（包括LLaVA、Qwen、Gemma和InternVL）的准确性。这些结果表明，VLMs在内部编码了可靠的证据，但未能充分利用它，使这些信号显式化可以弥合感知和推理之间的差距，从而提高VLMs的诊断理解能力和可靠性。

## 🔬 方法详解

**问题定义**：视觉语言模型在视觉问答任务中，即使能够“看到”正确的视觉证据，仍然会给出错误的答案。现有的方法缺乏对这种“视而不信”现象的深入理解，无法有效利用模型内部已经存在的视觉信息，导致性能瓶颈。

**核心思路**：论文的核心思路是，虽然VLMs的深层网络能够定位到关键的视觉证据，但这些证据并没有被充分利用。通过在推理时对深层网络的注意力进行干预，突出显示这些关键区域，可以迫使模型更加关注这些证据，从而提高答案的正确性。

**技术框架**：该方法主要分为两个阶段：首先，分析VLMs的逐层注意力动态，确定深层网络中能够有效定位视觉证据的层。然后，在推理时，基于这些深层网络的注意力权重，对输入图像进行选择性掩码，突出显示注意力集中的区域。修改后的图像和原始问题一起输入到VLM中，得到最终的答案。

**关键创新**：该方法的关键创新在于发现了VLMs的“视而不信”现象，并提出了一种无需训练的推理时干预方法来解决这个问题。与需要重新训练模型或修改模型结构的传统方法不同，该方法可以在现有模型的基础上直接应用，具有很强的通用性和实用性。

**关键设计**：该方法的关键设计包括：1) 选择合适的深层网络层进行注意力分析和干预；2) 设计有效的选择性掩码策略，以突出显示注意力集中的区域，同时避免过度干扰原始图像的信息；3) 确定合适的干预强度，以平衡视觉证据的突出和原始信息的保留。

## 📊 实验亮点

实验结果表明，该方法在多个VLM家族（包括LLaVA、Qwen、Gemma和InternVL）上均取得了显著的性能提升。例如，在视觉问答任务中，该方法能够在不进行任何训练的情况下，提高模型的准确率。这一结果验证了VLMs内部编码了可靠的视觉证据，但未能充分利用这些证据。

## 🎯 应用场景

该研究成果可应用于提升现有视觉语言模型的可靠性和准确性，尤其是在需要精确视觉推理的场景，如医疗影像诊断、自动驾驶、智能客服等领域。通过提高模型对视觉证据的利用率，可以减少错误答案的产生，增强用户对模型的信任度，并为未来的VLM研究提供新的方向。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) achieve strong results on multimodal tasks such as visual question answering, yet they can still fail even when the correct visual evidence is present. In this work, we systematically investigate whether these failures arise from not perceiving the evidence or from not leveraging it effectively. By examining layer-wise attention dynamics, we find that shallow layers focus primarily on text, while deeper layers sparsely but reliably attend to localized evidence regions. Surprisingly, VLMs often perceive the visual evidence when outputting incorrect answers, a phenomenon we term ``seeing but not believing'' that widely exists in major VLM families. Building on this, we introduce an inference-time intervention that highlights deep-layer evidence regions through selective attention-based masking. It requires no training and consistently improves accuracy across multiple families, including LLaVA, Qwen, Gemma, and InternVL. These results show that VLMs encode reliable evidence internally but under-utilize it, making such signals explicit can bridge the gap between perception and reasoning, advancing the diagnostic understanding and reliability of VLMs.

