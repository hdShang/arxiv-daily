---
layout: default
title: An integrated language-vision foundation model for conversational diagnostics and triaging in primary eye care
---

# An integrated language-vision foundation model for conversational diagnostics and triaging in primary eye care

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08414" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08414v1</a>
  <a href="https://arxiv.org/pdf/2505.08414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08414v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08414v1', 'An integrated language-vision foundation model for conversational diagnostics and triaging in primary eye care')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhi Da Soh, Yang Bai, Kai Yu, Yang Zhou, Xiaofeng Lei, Sahil Thakur, Zann Lee, Lee Ching Linette Phang, Qingsheng Peng, Can Can Xue, Rachel Shujuan Chong, Quan V. Hoang, Lavanya Raghavan, Yih Chung Tham, Charumathi Sabanayagam, Wei-Chi Wu, Ming-Chih Ho, Jiangnan He, Preeti Gupta, Ecosse Lamoureux, Seang Mei Saw, Vinay Nangia, Songhomitra Panda-Jonas, Jie Xu, Ya Xing Wang, Xinxing Xu, Jost B. Jonas, Tien Yin Wong, Rick Siow Mong Goh, Yong Liu, Ching-Yu Cheng

**分类**: eess.IV, cs.CV

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出Meta-EyeFM以解决初级眼科诊断中的多任务整合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `眼科疾病诊断` `多功能模型` `视觉基础模型` `大型语言模型` `路由机制` `低秩适应` `决策支持工具`

## 📋 核心要点

1. 现有的深度学习模型大多专注于单一任务，缺乏整合多种功能的能力，导致在眼科诊断中效率低下。
2. Meta-EyeFM通过结合大型语言模型与视觉模型，利用路由机制实现多任务处理，提升了眼科疾病评估的准确性和用户体验。
3. 实验结果显示，Meta-EyeFM在眼病检测和严重程度区分上表现优异，准确率显著高于现有模型，且与专业眼科医生的诊断水平相当。

## 📝 摘要（中文）

当前的深度学习模型大多是针对特定任务的，缺乏用户友好的操作界面。我们提出了Meta-EyeFM，这是一种多功能基础模型，将大型语言模型（LLM）与视觉基础模型（VFM）结合用于眼科疾病评估。Meta-EyeFM利用路由机制，根据文本查询实现准确的任务特定分析。通过低秩适应，我们对VFM进行了微调，以检测眼部和系统性疾病、区分眼病严重程度以及识别常见眼部症状。该模型在将眼底图像路由到适当的VFM时达到了100%的准确率，在疾病检测、严重程度区分和症状识别方面分别达到了≥82.2%、≥89%和≥76%的准确率。Meta-EyeFM在检测各种眼病时比Gemini-1.5-flash和ChatGPT-4o LMMs的准确率高出11%至43%，并且与眼科医生的表现相当。该系统提升了可用性和诊断性能，是初级眼科的重要决策支持工具或在线LLM用于眼底评估。

## 🔬 方法详解

**问题定义**：本论文旨在解决当前眼科疾病诊断中深度学习模型的单一任务限制及用户操作不便的问题。现有方法往往缺乏整合多种功能的能力，导致效率低下和准确性不足。

**核心思路**：Meta-EyeFM的核心思路是将大型语言模型与视觉基础模型相结合，通过路由机制实现任务特定分析，从而提升眼科疾病评估的准确性和用户友好性。

**技术框架**：该模型的整体架构包括一个大型语言模型和多个视觉基础模型，利用路由机制根据用户的文本查询将输入的眼底图像准确路由到相应的视觉模型进行分析。

**关键创新**：Meta-EyeFM的主要创新在于其多功能整合能力和高效的路由机制，使其在处理复杂的眼科诊断任务时表现出色，显著优于传统的单一任务模型。

**关键设计**：在技术细节上，模型采用低秩适应方法对视觉基础模型进行微调，设置了特定的损失函数以优化疾病检测、严重程度区分和症状识别的性能。

## 📊 实验亮点

实验结果显示，Meta-EyeFM在将眼底图像路由到适当的视觉模型时达到了100%的准确率，并在疾病检测、严重程度区分和症状识别方面分别取得了≥82.2%、≥89%和≥76%的准确率。与Gemini-1.5-flash和ChatGPT-4o LMMs相比，Meta-EyeFM的准确率提高了11%至43%，表现出色。

## 🎯 应用场景

Meta-EyeFM在初级眼科诊断中具有广泛的应用潜力，能够作为决策支持工具帮助医生进行更准确的疾病评估。此外，该系统也可以作为在线平台，为患者提供便捷的眼底图像分析服务，提升医疗服务的可及性和效率。

## 📄 摘要（原文）

> Current deep learning models are mostly task specific and lack a user-friendly interface to operate. We present Meta-EyeFM, a multi-function foundation model that integrates a large language model (LLM) with vision foundation models (VFMs) for ocular disease assessment. Meta-EyeFM leverages a routing mechanism to enable accurate task-specific analysis based on text queries. Using Low Rank Adaptation, we fine-tuned our VFMs to detect ocular and systemic diseases, differentiate ocular disease severity, and identify common ocular signs. The model achieved 100% accuracy in routing fundus images to appropriate VFMs, which achieved $\ge$ 82.2% accuracy in disease detection, $\ge$ 89% in severity differentiation, $\ge$ 76% in sign identification. Meta-EyeFM was 11% to 43% more accurate than Gemini-1.5-flash and ChatGPT-4o LMMs in detecting various eye diseases and comparable to an ophthalmologist. This system offers enhanced usability and diagnostic performance, making it a valuable decision support tool for primary eye care or an online LLM for fundus evaluation.

