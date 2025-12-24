---
layout: default
title: "LGCC: Enhancing Flow Matching Based Text-Guided Image Editing with Local Gaussian Coupling and Context Consistency"
---

# LGCC: Enhancing Flow Matching Based Text-Guided Image Editing with Local Gaussian Coupling and Context Consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01894" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01894v1</a>
  <a href="https://arxiv.org/pdf/2511.01894.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01894v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.01894v1', 'LGCC: Enhancing Flow Matching Based Text-Guided Image Editing with Local Gaussian Coupling and Context Consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangbing Liu, Pengfei Duan, Wen Li, Yi He

**分类**: cs.GR, cs.AI, cs.LG

**发布日期**: 2025-10-29

---

## 💡 一句话要点

**LGCC：通过局部高斯耦合和上下文一致性增强Flow Matching文本引导图像编辑**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本引导图像编辑` `Flow Matching` `局部高斯耦合` `内容一致性` `多模态学习`

## 📋 核心要点

1. 现有基于Flow Matching的文本引导图像编辑方法，如BAGEL，存在细节退化和内容不一致等问题。
2. LGCC通过局部高斯噪声耦合(LGNC)保留细节，并通过内容一致性损失(CCL)确保编辑指令与图像修改的语义对齐。
3. 实验表明，LGCC显著减少推理步骤，提升了图像编辑的细节保留和整体质量，并实现了推理速度的提升。

## 📝 摘要（中文）

本文提出了一种名为LGCC的新框架，旨在提升基于Flow Matching的多模态大语言模型(MLLM)在图像编辑方面的性能。现有方法如BAGEL存在细节退化、内容不一致和效率低下的问题，主要原因是它们依赖于随机噪声初始化。LGCC包含两个关键组件：局部高斯噪声耦合(LGNC)和内容一致性损失(CCL)。LGNC通过将目标图像嵌入及其局部扰动对应项建模为耦合对来保留空间细节，而CCL确保编辑指令和图像修改之间的语义对齐，防止意外的内容移除。通过课程学习将LGCC与BAGEL预训练模型集成，显著减少了推理步骤，在I2EBench上局部细节得分提高了1.60%，总体得分提高了0.53%。LGCC实现了轻量级编辑3倍-5倍的加速，通用编辑2倍的加速，仅需BAGEL或Flux 40%-50%的推理时间。这些结果表明LGCC能够保留细节、保持上下文完整性并提高推理速度，提供了一种经济高效的解决方案，且不影响编辑质量。

## 🔬 方法详解

**问题定义**：论文旨在解决基于Flow Matching的文本引导图像编辑中，现有方法（如BAGEL）存在的细节退化、内容不一致以及推理效率低下的问题。这些方法通常依赖随机噪声初始化，导致编辑后的图像细节模糊，并且可能出现与编辑指令不符的内容变化。

**核心思路**：论文的核心思路是通过引入局部高斯噪声耦合(LGNC)来更好地保留图像细节，并使用内容一致性损失(CCL)来确保编辑后的图像与文本指令在语义上保持一致。LGNC旨在捕捉图像局部区域的细微变化，而CCL则约束编辑过程，避免不必要的内容移除或语义偏差。

**技术框架**：LGCC框架主要包含两个核心模块：LGNC和CCL。首先，LGNC将目标图像嵌入及其局部扰动版本建模为耦合对，通过学习这些耦合对之间的关系来保留空间细节。然后，CCL计算编辑前后图像的内容一致性损失，以确保编辑过程不会引入与文本指令不符的语义变化。最后，通过课程学习的方式将LGCC集成到预训练的BAGEL模型中，以逐步提升编辑性能。

**关键创新**：LGCC的关键创新在于同时考虑了局部细节的保留和全局语义的一致性。LGNC通过局部高斯耦合的方式，能够更有效地捕捉图像的局部特征，从而避免细节信息的丢失。CCL则通过显式地约束编辑过程，确保编辑后的图像在语义上与文本指令对齐，从而避免内容不一致的问题。与现有方法相比，LGCC在细节保留和语义一致性方面都取得了显著的提升。

**关键设计**：LGNC的关键设计在于如何生成局部扰动。论文采用高斯噪声对图像嵌入进行局部扰动，并控制噪声的强度和范围，以确保扰动不会过度改变图像的整体结构。CCL的关键设计在于如何定义内容一致性损失。论文采用预训练的CLIP模型来提取编辑前后图像的特征，并计算这些特征之间的相似度，以此作为内容一致性的度量。此外，论文还采用了课程学习策略，逐步增加LGCC的训练强度，以避免训练初期出现不稳定的情况。

## 📊 实验亮点

实验结果表明，LGCC在I2EBench数据集上取得了显著的性能提升。局部细节得分提高了1.60%，总体得分提高了0.53%。此外，LGCC在轻量级编辑任务中实现了3倍-5倍的加速，在通用编辑任务中实现了2倍的加速，并且仅需BAGEL或Flux 40%-50%的推理时间。这些数据充分证明了LGCC在细节保留、上下文完整性和推理速度方面的优势。

## 🎯 应用场景

LGCC技术可广泛应用于图像编辑领域，例如电商产品图的美化、社交媒体图片的个性化修改、以及艺术创作等。该研究的实际价值在于提升了图像编辑的质量和效率，降低了计算成本，使得高质量的图像编辑更加普及。未来，LGCC有望应用于更复杂的图像编辑任务，例如视频编辑、3D模型编辑等。

## 📄 摘要（原文）

> Recent advancements have demonstrated the great potential of flow matching-based Multimodal Large Language Models (MLLMs) in image editing. However, state-of-the-art works like BAGEL face limitations, including detail degradation, content inconsistency, and inefficiency due to their reliance on random noise initialization. To address these issues, we propose LGCC, a novel framework with two key components: Local Gaussian Noise Coupling (LGNC) and Content Consistency Loss (CCL). LGNC preserves spatial details by modeling target image embeddings and their locally perturbed counterparts as coupled pairs, while CCL ensures semantic alignment between edit instructions and image modifications, preventing unintended content removal. By integrating LGCC with the BAGEL pre-trained model via curriculum learning, we significantly reduce inference steps, improving local detail scores on I2EBench by 1.60% and overall scores by 0.53%. LGCC achieves 3x -- 5x speedup for lightweight editing and 2x for universal editing, requiring only 40% -- 50% of the inference time of BAGEL or Flux. These results demonstrate LGCC's ability to preserve detail, maintain contextual integrity, and enhance inference speed, offering a cost-efficient solution without compromising editing quality.

