---
layout: default
title: Human-centered Interactive Learning via MLLMs for Text-to-Image Person Re-identification
---

# Human-centered Interactive Learning via MLLMs for Text-to-Image Person Re-identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11036" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11036v1</a>
  <a href="https://arxiv.org/pdf/2506.11036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11036v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11036v1', 'Human-centered Interactive Learning via MLLMs for Text-to-Image Person Re-identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Qin, Chao Chen, Zhihang Fu, Dezhong Peng, Xi Peng, Peng Hu

**分类**: cs.LG, cs.MM

**发布日期**: 2025-05-21

---

## 💡 一句话要点

**提出人本交互学习框架以提升文本到图像的行人重识别效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `行人重识别` `跨模态学习` `多模态大语言模型` `人本交互` `数据增强`

## 📋 核心要点

1. 现有的文本到图像行人重识别方法在处理复杂候选图像时存在显著的局限性，主要受限于网络架构和数据质量。
2. 本文提出了一种交互式跨模态学习框架（ICL），通过人本交互和多模态大语言模型（MLLM）提升文本查询的可区分性。
3. 在CUHK-PEDES、ICFG-PEDES、RSTPReid和UFine6926等四个基准测试上，实验结果显示该方法显著提高了行人重识别的性能。

## 📝 摘要（中文）

尽管跨模态嵌入模型在文本到图像的行人重识别（TIReID）方面取得了显著进展，但现有方法在区分具有挑战性的候选图像时仍面临网络架构和数据质量等内在限制。为了解决这些问题，本文提出了一种交互式跨模态学习框架（ICL），通过人本交互增强文本查询的可区分性。我们设计了一个即插即用的测试时人本交互模块（THI），该模块专注于人类特征的视觉问答，促进与多模态大语言模型（MLLM）的多轮交互，以对齐查询意图与潜在目标图像。THI根据MLLM的反馈优化用户查询，从而提高排名准确性。此外，针对低质量训练文本的限制，我们引入了一种新颖的数据重组增强（RDA）策略，通过丰富、分解和重组人物描述来增强查询的可区分性。大量实验表明，我们的方法在四个TIReID基准上取得了显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到图像行人重识别（TIReID）中，现有方法在区分复杂候选图像时的局限性，尤其是由于网络架构和数据质量导致的识别准确性不足。

**核心思路**：提出的交互式跨模态学习框架（ICL）通过人本交互来增强文本查询的可区分性，利用多模态大语言模型（MLLM）进行多轮交互，以更好地对齐查询意图与目标图像。

**技术框架**：整体架构包括人本交互模块（THI）和数据重组增强（RDA）策略。THI模块专注于视觉问答，RDA策略则通过丰富和重组描述来提升训练文本质量。

**关键创新**：最重要的创新在于引入了THI模块，通过与MLLM的交互优化用户查询，从而显著提高了图像匹配的准确性。这一方法与传统的静态查询处理方式有本质区别。

**关键设计**：在THI模块中，设计了多轮交互机制以优化查询，同时RDA策略通过信息丰富和多样性增强来提升训练文本的质量，确保了模型在低质量数据下的鲁棒性。

## 📊 实验亮点

在CUHK-PEDES、ICFG-PEDES、RSTPReid和UFine6926等四个基准测试中，本文的方法在行人重识别任务上取得了显著的性能提升，具体提升幅度达到XX%，相较于现有基线方法表现出更高的准确性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、安防系统和人流管理等场景，能够有效提升行人重识别的准确性和效率。未来，该方法还可扩展到其他跨模态任务，如图像检索和视频分析，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> Despite remarkable advancements in text-to-image person re-identification (TIReID) facilitated by the breakthrough of cross-modal embedding models, existing methods often struggle to distinguish challenging candidate images due to intrinsic limitations, such as network architecture and data quality. To address these issues, we propose an Interactive Cross-modal Learning framework (ICL), which leverages human-centered interaction to enhance the discriminability of text queries through external multimodal knowledge. To achieve this, we propose a plug-and-play Test-time Humane-centered Interaction (THI) module, which performs visual question answering focused on human characteristics, facilitating multi-round interactions with a multimodal large language model (MLLM) to align query intent with latent target images. Specifically, THI refines user queries based on the MLLM responses to reduce the gap to the best-matching images, thereby boosting ranking accuracy. Additionally, to address the limitation of low-quality training texts, we introduce a novel Reorganization Data Augmentation (RDA) strategy based on information enrichment and diversity enhancement to enhance query discriminability by enriching, decomposing, and reorganizing person descriptions. Extensive experiments on four TIReID benchmarks, i.e., CUHK-PEDES, ICFG-PEDES, RSTPReid, and UFine6926, demonstrate that our method achieves remarkable performance with substantial improvement.

