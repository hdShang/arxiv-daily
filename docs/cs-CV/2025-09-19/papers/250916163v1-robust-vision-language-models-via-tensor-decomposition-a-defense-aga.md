---
layout: default
title: "Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks"
---

# Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16163" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16163v1</a>
  <a href="https://arxiv.org/pdf/2509.16163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16163v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16163v1', 'Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Het Patel, Muzammil Allie, Qian Zhang, Jia Chen, Evangelos E. Papalexakis

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-19

**备注**: To be presented as a poster at the Workshop on Safe and Trustworthy Multimodal AI Systems (SafeMM-AI), 2025

---

## 💡 一句话要点

**提出轻量级张量分解方法以增强视觉语言模型的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `对抗性攻击` `张量分解` `鲁棒性增强` `多模态理解` `深度学习` `模型防御`

## 📋 核心要点

1. 现有的视觉语言模型在面对对抗性攻击时表现脆弱，防御措施往往需要复杂的重新训练或架构调整。
2. 本文提出了一种基于张量分解的轻量级防御方法，能够在不重新训练的情况下增强模型的鲁棒性。
3. 实验结果显示，该方法在Flickr30K和COCO数据集上显著提高了模型的性能，尤其在对抗攻击下的恢复能力。

## 📝 摘要（中文）

视觉语言模型（VLMs）在多模态理解方面表现出色，但易受到对抗性攻击的影响。现有防御方法通常需要昂贵的重新训练或显著的架构更改。本文提出了一种轻量级的防御机制，利用张量分解技术，适用于任何预训练的VLM，无需重新训练。通过对视觉编码器表示进行分解和重构，该方法能够过滤对抗噪声，同时保持语义完整性。实验结果表明，在COCO和Flickr30K数据集上，使用CLIP模型的鲁棒性得到了显著提升。Flickr30K上恢复了12.3%的性能，Recall@1准确率从7.5%提升至19.8%；而在COCO上恢复了8.1%的性能，准确率从3.8%提升至11.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在对抗性攻击下的脆弱性。现有的防御方法通常需要昂贵的重新训练或复杂的架构调整，限制了其实际应用。

**核心思路**：提出了一种基于张量分解的防御机制，通过对视觉编码器的表示进行分解和重构，过滤对抗噪声，同时保持语义信息的完整性。

**技术框架**：该方法的整体架构包括张量分解模块和重构模块。首先对视觉编码器的输出进行张量分解，然后通过重构过程恢复干净的表示。

**关键创新**：最重要的创新在于引入了张量分解技术，特别是张量列车分解，能够在低秩和低残差强度下有效过滤对抗噪声，与传统方法相比，显著降低了计算开销。

**关键设计**：在参数设置上，低秩范围为8-32，低残差强度设置为α=0.1-0.2，经过实验验证，这些设置能够达到最佳的防御效果。

## 📊 实验亮点

实验结果显示，在Flickr30K数据集上，该方法恢复了12.3%的性能，Recall@1准确率从7.5%提升至19.8%；在COCO数据集上，恢复了8.1%的性能，准确率从3.8%提升至11.9%。这些结果表明，张量分解技术在对抗性攻击下的有效性和实用性。

## 🎯 应用场景

该研究的防御方法具有广泛的应用潜力，尤其在需要高鲁棒性的多模态系统中，如自动驾驶、智能监控和人机交互等领域。通过增强视觉语言模型的鲁棒性，可以提高这些系统在复杂环境下的安全性和可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Vision language models (VLMs) excel in multimodal understanding but are prone to adversarial attacks. Existing defenses often demand costly retraining or significant architecture changes. We introduce a lightweight defense using tensor decomposition suitable for any pre-trained VLM, requiring no retraining. By decomposing and reconstructing vision encoder representations, it filters adversarial noise while preserving meaning. Experiments with CLIP on COCO and Flickr30K show improved robustness. On Flickr30K, it restores 12.3\% performance lost to attacks, raising Recall@1 accuracy from 7.5\% to 19.8\%. On COCO, it recovers 8.1\% performance, improving accuracy from 3.8\% to 11.9\%. Analysis shows Tensor Train decomposition with low rank (8-32) and low residual strength ($α=0.1-0.2$) is optimal. This method is a practical, plug-and-play solution with minimal overhead for existing VLMs.

