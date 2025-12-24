---
layout: default
title: "ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding"
---

# ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15235" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15235v5</a>
  <a href="https://arxiv.org/pdf/2509.15235.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15235v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15235v5', 'ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialiang Kang, Han Shu, Wenshuo Li, Yingjie Zhai, Xinghao Chen

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-17 (更新: 2025-10-23)

**备注**: NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/KangJialiang/ViSpec)

---

## 💡 一句话要点

**ViSpec：利用视觉感知推测解码加速视觉-语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `推测解码` `模型加速` `多模态学习` `视觉适配器`

## 📋 核心要点

1. 现有视觉-语言模型（VLM）的推测解码加速效果不佳，未能充分利用VLM在视觉信息处理上的优势。
2. ViSpec通过轻量级视觉适配器压缩图像token，并提取全局图像特征增强多模态一致性，从而提升推测解码效率。
3. ViSpec通过定制数据集和训练策略，避免草稿模型学习捷径，实验证明其能显著加速VLM的推测解码过程。

## 📝 摘要（中文）

推测解码是一种广泛应用于加速大型语言模型（LLMs）推理的技术，但其在视觉-语言模型（VLMs）中的应用仍未得到充分探索，现有方法仅实现了适度的加速（<1.5倍）。随着多模态能力成为大型模型的核心，这种差距日益显著。我们假设，大型VLM可以有效地逐层过滤冗余图像信息，而不会影响文本理解，而较小的草稿模型则难以做到这一点。为了解决这个问题，我们引入了视觉感知推测解码（ViSpec），这是一个专为VLM量身定制的新框架。ViSpec采用轻量级的视觉适配器模块将图像token压缩成紧凑的表示，该表示无缝集成到草稿模型的注意力机制中，同时保留原始图像的位置信息。此外，我们为每个输入图像提取全局特征向量，并使用该特征增强所有后续文本token，以增强多模态一致性。为了克服缺乏具有长助手响应的多模态数据集的问题，我们通过重新利用现有数据集并使用目标VLM和修改后的提示生成扩展输出来策划专门的训练数据集。我们的训练策略减轻了草稿模型利用直接访问目标模型隐藏状态的风险，否则可能导致仅在目标模型输出上训练时的捷径学习。大量的实验验证了ViSpec，据我们所知，它首次实现了VLM推测解码的显著加速。

## 🔬 方法详解

**问题定义**：现有VLM的推测解码加速效果不明显，主要原因是草稿模型无法有效处理和理解视觉信息，导致推测的准确性较低，需要更多的回滚操作，从而限制了加速效果。现有方法未能充分利用大型VLM在视觉信息过滤和理解方面的能力。

**核心思路**：ViSpec的核心思路是让草稿模型具备更强的视觉感知能力，使其能够更好地理解图像内容，从而更准确地预测后续的文本token。通过增强草稿模型的视觉理解能力，减少推测错误，提高推测解码的效率。

**技术框架**：ViSpec包含以下主要模块：1) 轻量级视觉适配器：用于压缩图像token，提取图像特征。2) 注意力机制集成：将压缩后的图像特征集成到草稿模型的注意力机制中，使草稿模型能够感知视觉信息。3) 全局特征增强：提取全局图像特征，并将其添加到后续的文本token中，以增强多模态一致性。4) 定制训练数据集：通过重新利用现有数据集和使用目标VLM生成扩展输出来创建。

**关键创新**：ViSpec的关键创新在于：1) 提出了视觉感知的推测解码框架，专门针对VLM设计。2) 设计了轻量级的视觉适配器，能够在不显著增加计算负担的情况下，增强草稿模型的视觉感知能力。3) 提出了全局特征增强方法，进一步提升了多模态一致性。4) 提出了定制训练数据集和训练策略，避免了草稿模型学习捷径。

**关键设计**：视觉适配器采用轻量级网络结构，例如几层卷积层或线性层，以减少计算量。全局特征向量通过对图像特征进行池化操作得到。训练数据集通过修改现有数据集的提示，并使用目标VLM生成更长的回复来扩充。训练过程中，采用损失函数来鼓励草稿模型学习目标模型的行为，同时避免其直接复制目标模型的隐藏状态。

## 📊 实验亮点

ViSpec在VLM推测解码上取得了显著的加速效果，是首个在该领域取得实质性突破的方法。实验结果表明，ViSpec能够显著提升VLM的推理速度，具体的性能数据和对比基线将在论文中详细展示。通过定制的训练数据集和训练策略，ViSpec有效地避免了草稿模型学习捷径的问题，保证了加速效果的可靠性。

## 🎯 应用场景

ViSpec可应用于各种需要快速推理的视觉-语言任务，例如图像描述生成、视觉问答、多模态对话等。该技术能够显著提升VLM的推理速度，降低计算成本，使其更易于部署在资源受限的设备上，并促进VLM在实际场景中的广泛应用。未来，ViSpec可以进一步扩展到其他多模态模型和任务中。

## 📄 摘要（原文）

> Speculative decoding is a widely adopted technique for accelerating inference in large language models (LLMs), yet its application to vision-language models (VLMs) remains underexplored, with existing methods achieving only modest speedups (<1.5x). This gap is increasingly significant as multimodal capabilities become central to large-scale models. We hypothesize that large VLMs can effectively filter redundant image information layer by layer without compromising textual comprehension, whereas smaller draft models struggle to do so. To address this, we introduce Vision-Aware Speculative Decoding (ViSpec), a novel framework tailored for VLMs. ViSpec employs a lightweight vision adaptor module to compress image tokens into a compact representation, which is seamlessly integrated into the draft model's attention mechanism while preserving original image positional information. Additionally, we extract a global feature vector for each input image and augment all subsequent text tokens with this feature to enhance multimodal coherence. To overcome the scarcity of multimodal datasets with long assistant responses, we curate a specialized training dataset by repurposing existing datasets and generating extended outputs using the target VLM with modified prompts. Our training strategy mitigates the risk of the draft model exploiting direct access to the target model's hidden states, which could otherwise lead to shortcut learning when training solely on target model outputs. Extensive experiments validate ViSpec, achieving, to our knowledge, the first substantial speedup in VLM speculative decoding. Code is available at https://github.com/KangJialiang/ViSpec.

