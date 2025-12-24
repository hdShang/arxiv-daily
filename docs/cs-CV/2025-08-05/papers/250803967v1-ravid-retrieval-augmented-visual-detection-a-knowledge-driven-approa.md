---
layout: default
title: "RAVID: Retrieval-Augmented Visual Detection: A Knowledge-Driven Approach for AI-Generated Image Identification"
---

# RAVID: Retrieval-Augmented Visual Detection: A Knowledge-Driven Approach for AI-Generated Image Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03967" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03967v1</a>
  <a href="https://arxiv.org/pdf/2508.03967.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03967v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03967v1', 'RAVID: Retrieval-Augmented Visual Detection: A Knowledge-Driven Approach for AI-Generated Image Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mamadou Keita, Wassim Hamidouche, Hessen Bougueffa Eutamene, Abdelmalik Taleb-Ahmed, Abdenour Hadid

**分类**: cs.CV, cs.CR, cs.IR

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出RAVID框架以解决AI生成图像检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成图像` `图像检测` `视觉检索` `多模态融合` `鲁棒性`

## 📋 核心要点

1. 现有的AI生成图像检测方法在泛化能力和鲁棒性方面存在不足，通常依赖低级特征，限制了适应性。
2. RAVID框架通过动态检索相关图像，结合微调的CLIP编码器和视觉语言模型，增强了检测的准确性和鲁棒性。
3. 在UniversalFakeDetect基准测试中，RAVID实现了93.85%的平均准确率，且在图像降质情况下表现优异，平均准确率达到80.27%。

## 📝 摘要（中文）

本文介绍了RAVID，这是第一个利用视觉检索增强生成（RAG）技术的AI生成图像检测框架。尽管RAG方法在减轻基础模型的事实不准确性方面表现出色，但主要集中在文本上，视觉知识的探索仍显不足。现有检测方法在泛化和鲁棒性方面存在挑战，通常依赖低级伪影和模型特定特征，限制了其适应性。RAVID通过动态检索相关图像来增强检测，采用微调的CLIP图像编码器RAVID CLIP，并结合类别相关提示以改善表示学习。实验结果显示，RAVID在UniversalFakeDetect基准测试中实现了93.85%的平均准确率，且在图像降质条件下仍保持高鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决AI生成图像的检测问题，现有方法在泛化和鲁棒性方面表现不佳，依赖于低级伪影和特定模型特征，限制了其适用性。

**核心思路**：RAVID通过动态检索与查询图像相关的图像，结合微调的CLIP图像编码器和视觉语言模型，增强输入信息，从而提高检测的准确性和鲁棒性。

**技术框架**：RAVID的整体架构包括三个主要模块：首先，使用RAVID CLIP生成查询图像的嵌入；其次，从数据库中检索最相关的图像；最后，将检索到的图像与查询图像结合，形成丰富的输入供视觉语言模型处理。

**关键创新**：RAVID的核心创新在于引入了视觉检索增强生成（RAG）技术，动态检索相关图像以增强检测能力，这与传统方法依赖固定特征的方式有本质区别。

**关键设计**：在设计上，RAVID CLIP经过微调以适应特定类别，并结合类别相关提示以改善表示学习，确保模型在多种生成模型下的鲁棒性。

## 📊 实验亮点

RAVID在UniversalFakeDetect基准测试中表现出色，平均准确率达到93.85%，在图像降质条件下的准确率为80.27%，显著高于传统方法C2P-CLIP的63.44%。该框架在高斯模糊和JPEG压缩等降质场景中均展现出优越的鲁棒性。

## 🎯 应用场景

RAVID框架在AI生成图像检测领域具有广泛的应用潜力，能够有效识别和分类生成图像，适用于社交媒体内容审核、虚假信息检测以及数字版权保护等场景。随着生成技术的不断发展，该研究将为相关领域提供重要的技术支持和理论基础。

## 📄 摘要（原文）

> In this paper, we introduce RAVID, the first framework for AI-generated image detection that leverages visual retrieval-augmented generation (RAG). While RAG methods have shown promise in mitigating factual inaccuracies in foundation models, they have primarily focused on text, leaving visual knowledge underexplored. Meanwhile, existing detection methods, which struggle with generalization and robustness, often rely on low-level artifacts and model-specific features, limiting their adaptability. To address this, RAVID dynamically retrieves relevant images to enhance detection. Our approach utilizes a fine-tuned CLIP image encoder, RAVID CLIP, enhanced with category-related prompts to improve representation learning. We further integrate a vision-language model (VLM) to fuse retrieved images with the query, enriching the input and improving accuracy. Given a query image, RAVID generates an embedding using RAVID CLIP, retrieves the most relevant images from a database, and combines these with the query image to form an enriched input for a VLM (e.g., Qwen-VL or Openflamingo). Experiments on the UniversalFakeDetect benchmark, which covers 19 generative models, show that RAVID achieves state-of-the-art performance with an average accuracy of 93.85%. RAVID also outperforms traditional methods in terms of robustness, maintaining high accuracy even under image degradations such as Gaussian blur and JPEG compression. Specifically, RAVID achieves an average accuracy of 80.27% under degradation conditions, compared to 63.44% for the state-of-the-art model C2P-CLIP, demonstrating consistent improvements in both Gaussian blur and JPEG compression scenarios. The code will be publicly available upon acceptance.

