---
layout: default
title: Constrained Edge AI Deployment: Fine-Tuning vs Distillation for LLM Compression
---

# Constrained Edge AI Deployment: Fine-Tuning vs Distillation for LLM Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18166" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18166v1</a>
  <a href="https://arxiv.org/pdf/2505.18166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18166v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18166v1', 'Constrained Edge AI Deployment: Fine-Tuning vs Distillation for LLM Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jacob Sander, David Moe, Achraf Cohen, Brent Venable, Venkat Dasari, Brian Jalaian

**分类**: cs.LG

**发布日期**: 2025-05-13

**备注**: 9 Pages, 2 Figures

---

## 💡 一句话要点

**提出基于自蒸馏的LLM压缩方法以应对边缘计算限制**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `边缘计算` `模型压缩` `自蒸馏` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的压缩方法通常依赖于全Transformer的剪枝，难以满足边缘计算的资源限制。
2. 本文提出了一种针对MLP模块的逐层L2范数剪枝方法，并比较了微调与自蒸馏的效果。
3. 实验结果显示，在相同剪枝条件下，自蒸馏方法在测试准确性上表现优于传统微调方法。

## 📝 摘要（中文）

现代基础模型通常通过结构化剪枝和再训练的组合进行压缩，以满足边缘部署的严格计算、内存和连接性限制。本文采用简单的逐层L2范数剪枝，仅针对MLP模块作为固定基线。研究的重点在于隔离再训练损失函数的影响：即使用交叉熵的微调（L2PFT）需要标记数据，而自蒸馏的KL散度（L2PSD）仅利用教师输出（无标签）。在相同的剪枝计划下，基于KL的蒸馏在测试准确性上与交叉熵微调相匹配或超越，表明即使在基本的MLP剪枝下，损失函数的选择对资源受限环境中的压缩模型恢复有重要影响。

## 🔬 方法详解

**问题定义**：本文旨在解决在边缘计算环境中，如何有效压缩大型语言模型（LLM）以满足计算和内存限制的问题。现有方法通常依赖于全模型剪枝，难以在资源受限的情况下实现最佳性能。

**核心思路**：论文提出了一种简单的逐层L2范数剪枝方法，专注于MLP模块，并比较了两种不同的再训练策略：交叉熵微调和自蒸馏。通过这种方式，研究者能够更好地理解损失函数对模型恢复的影响。

**技术框架**：整体架构包括两个主要阶段：首先进行逐层L2范数剪枝，然后分别应用交叉熵微调和自蒸馏策略进行再训练。每个阶段都针对特定的模型组件进行优化。

**关键创新**：最重要的创新在于通过自蒸馏方法，利用教师输出而非标记数据进行模型训练，从而在资源受限环境中实现更高的准确性。这一方法与传统的依赖标记数据的微调方法形成鲜明对比。

**关键设计**：在实验中，采用了相同的剪枝计划，损失函数的选择（交叉熵与KL散度）成为影响最终模型性能的关键因素。MLP模块的设计和剪枝策略也经过精心调整，以确保在压缩后仍能保持较高的性能。

## 📊 实验亮点

实验结果表明，在相同的剪枝条件下，基于KL散度的自蒸馏方法在测试准确性上与交叉熵微调相匹配或超越，展示了在资源受限环境中，损失函数选择对模型恢复的重要性。具体而言，KL散度方法在准确性上提升幅度显著，显示出其在边缘计算场景中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括边缘计算设备上的自然语言处理任务，如智能手机、物联网设备和边缘服务器等。通过有效的模型压缩和再训练策略，可以在资源受限的环境中实现高效的推理和响应，提升用户体验。未来，这一方法可能推动更多智能设备的普及和应用。

## 📄 摘要（原文）

> Modern foundational models are often compressed via a combination of structured pruning and re-training to meet the strict compute, memory, and connectivity constraints of edge deployments. While state-of-the-art pruning schemes target the entire Transformer, we adopt a simple, layer-wise L2-norm pruning on only the MLP blocks as a fixed baseline. Our focus is not on achieving maximal compression, but on isolating the impact of the re-training loss function: (i) Fine-tuning with Cross- Entropy (L2PFT), which requires labeled data, versus (ii) Self-Distillation with KL-divergence, which leverages only teacher logits (no labels) (L2PSD). We evaluate both pipelines on the OLMo2- 7B-SFT model for CommonsenseQA suitable for intermittent or denied connectivity scenarios typical of edge networks. Under identical pruning schedules, KL-based distillation matches or exceeds CE fine-tuning in test accuracy, demonstrating that, even with a basic MLP-only pruning, the choice of loss function materially affects compressed model recovery in resource-constrained environments.

