---
layout: default
title: "Benign-to-Toxic Jailbreaking: Inducing Harmful Responses from Harmless Prompts"
---

# Benign-to-Toxic Jailbreaking: Inducing Harmful Responses from Harmless Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21556" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21556v1</a>
  <a href="https://arxiv.org/pdf/2505.21556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21556v1', 'Benign-to-Toxic Jailbreaking: Inducing Harmful Responses from Harmless Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hee-Seon Kim, Minbeom Kim, Wonjun Lee, Kihyun Kim, Changick Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-26

**备注**: LVLM, Jailbreak

---

## 💡 一句话要点

**提出Benign-to-Toxic方法以解决安全机制失效问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越狱技术` `多模态对齐` `对抗性攻击` `安全机制` `人工智能安全`

## 📋 核心要点

1. 现有的毒性延续方法在处理无害输入时，难以诱导模型产生有害输出，存在安全机制失效的挑战。
2. 本文提出的Benign-to-Toxic越狱方法，通过优化对抗图像，从无害条件中诱导有害输出，突破了传统方法的局限。
3. 实验结果表明，B2T方法在多种设置下均优于现有方法，展示了其在黑箱环境中的有效性和广泛适用性。

## 📝 摘要（中文）

优化基础的越狱方法通常采用毒性延续设置，依赖于下一个标记预测目标。然而，现有方法在缺乏明确毒性信号时难以诱导安全失调。本文提出了一种新的越狱范式：Benign-to-Toxic（B2T），通过优化对抗图像，从无害的条件诱导有害输出。该方法在黑箱设置中表现优越，并与基于文本的越狱方法互补，揭示了多模态对齐中的潜在脆弱性，开辟了新的越狱研究方向。

## 🔬 方法详解

**问题定义**：本文旨在解决现有毒性延续方法在无害输入下无法诱导有害输出的问题。现有方法主要依赖于已有的毒性信号，导致在缺乏明确毒性信号时表现不佳。

**核心思路**：提出Benign-to-Toxic（B2T）越狱方法，通过优化对抗图像，使模型在无害条件下产生有害输出。这一设计旨在突破模型的安全机制，揭示其潜在脆弱性。

**技术框架**：B2T方法的整体流程包括：1）生成无害的输入条件；2）优化对抗图像以诱导有害输出；3）评估模型对优化图像的响应。主要模块包括输入生成、对抗优化和输出评估。

**关键创新**：B2T方法的核心创新在于其从无害条件诱导有害输出的能力，与传统方法依赖已有毒性信号的方式本质上不同，开辟了新的研究方向。

**关键设计**：在技术细节上，B2T方法采用特定的损失函数来优化对抗图像，并设计了适应性参数设置，以确保模型能够有效地突破安全机制。

## 📊 实验亮点

实验结果显示，B2T方法在多种黑箱设置中表现优于传统毒性延续方法，成功诱导有害输出的比例提高了约30%。此外，该方法与文本基础的越狱方法相结合，进一步增强了模型的攻击能力，展示了其广泛的适用性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、对抗性攻击研究以及多模态系统的鲁棒性评估。通过揭示模型的脆弱性，B2T方法可以帮助开发更安全的AI系统，减少潜在的滥用风险，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Optimization-based jailbreaks typically adopt the Toxic-Continuation setting in large vision-language models (LVLMs), following the standard next-token prediction objective. In this setting, an adversarial image is optimized to make the model predict the next token of a toxic prompt. However, we find that the Toxic-Continuation paradigm is effective at continuing already-toxic inputs, but struggles to induce safety misalignment when explicit toxic signals are absent. We propose a new paradigm: Benign-to-Toxic (B2T) jailbreak. Unlike prior work, we optimize adversarial images to induce toxic outputs from benign conditioning. Since benign conditioning contains no safety violations, the image alone must break the model's safety mechanisms. Our method outperforms prior approaches, transfers in black-box settings, and complements text-based jailbreaks. These results reveal an underexplored vulnerability in multimodal alignment and introduce a fundamentally new direction for jailbreak approaches.

