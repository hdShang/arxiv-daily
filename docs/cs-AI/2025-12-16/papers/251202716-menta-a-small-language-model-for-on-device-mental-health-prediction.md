---
layout: default
title: Menta: A Small Language Model for On-Device Mental Health Prediction
---

# Menta: A Small Language Model for On-Device Mental Health Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.02716" class="toolbar-btn" target="_blank">📄 arXiv: 2512.02716</a>
  <a href="https://arxiv.org/pdf/2512.02716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.02716" onclick="toggleFavorite(this, '2512.02716', 'Menta: A Small Language Model for On-Device Mental Health Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Zhang, Xiangyuan Xue, Lingyan Ruan, Shiya Fu, Feng Xia, Simon D'Alfonso, Vassilis Kostakos, Ting Dang, Hong Jia

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Menta：用于设备端心理健康预测的小型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `心理健康预测` `社交媒体分析` `设备端部署` `LoRA微调`

## 📋 核心要点

1. 现有大型语言模型在心理健康预测中表现出色，但其高计算成本和体积限制了实际部署。
2. Menta通过LoRA微调小型语言模型，并采用跨数据集训练和平衡准确率损失，优化模型性能。
3. 实验表明，Menta在抑郁、压力和自杀倾向预测任务上优于现有SLM，且可在移动设备上实时运行。

## 📝 摘要（中文）

全球数亿人受到心理健康问题的影响，但早期检测仍然有限。大型语言模型（LLM）在心理健康应用中显示出潜力，但其规模和计算需求阻碍了实际部署。小型语言模型（SLM）提供了一种轻量级的替代方案，但其在基于社交媒体的心理健康预测中的应用仍未得到充分探索。本研究介绍了Menta，这是第一个专门为从社交媒体数据中进行多任务心理健康预测而优化的SLM。Menta使用基于LoRA的框架、跨数据集策略和面向平衡准确性的损失函数，在六个分类任务上进行联合训练。与九个最先进的SLM基线相比，Menta在涵盖抑郁、压力和自杀倾向的任务中，平均提高了15.2％，优于性能最佳的非微调SLM。与13B参数的LLM相比，它在抑郁和压力分类任务上也实现了更高的准确性，同时体积缩小了约3.25倍。此外，我们展示了Menta在iPhone 15 Pro Max上的实时设备端部署，仅需约3GB RAM。通过与现有SLM和LLM的全面基准测试，Menta突出了可扩展、保护隐私的心理健康监测的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决心理健康问题早期检测困难的问题，特别是利用社交媒体数据进行预测。现有的大型语言模型虽然有效，但计算资源需求高，难以在移动设备等资源受限的环境中部署。小型语言模型虽然体积小，但在社交媒体心理健康预测方面的潜力尚未充分挖掘。

**核心思路**：论文的核心思路是利用小型语言模型（SLM）的轻量化优势，通过针对性的优化和微调，使其在心理健康预测任务上达到与大型语言模型相媲美的性能，并能够在设备端实时部署。这种方法旨在实现可扩展、保护隐私的心理健康监测。

**技术框架**：Menta的整体框架包括数据收集与预处理、模型选择与微调、以及设备端部署三个主要阶段。首先，从社交媒体平台收集相关数据，并进行清洗和标注。然后，选择合适的小型语言模型作为基础模型，并使用LoRA（Low-Rank Adaptation）进行微调。LoRA通过引入低秩矩阵来减少需要训练的参数量，从而降低计算成本。最后，将微调后的模型部署到移动设备上，实现实时预测。

**关键创新**：Menta的关键创新在于其针对社交媒体心理健康预测任务的优化策略。这包括：1) 基于LoRA的微调框架，有效降低了训练成本；2) 跨数据集训练策略，利用多个数据集来提高模型的泛化能力；3) 平衡准确率导向的损失函数，解决数据不平衡问题，提高模型在少数类别上的预测准确率。

**关键设计**：Menta的关键设计包括：1) 选择合适的预训练小型语言模型作为基础模型，例如BERT或RoBERTa的轻量化版本；2) 使用LoRA进行微调时，选择合适的秩（rank）值，以平衡模型性能和计算成本；3) 设计平衡准确率导向的损失函数，例如Focal Loss或Class-Balanced Loss，以解决数据不平衡问题；4) 采用跨数据集训练策略时，需要仔细处理不同数据集之间的差异，例如使用领域自适应技术。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.02716/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.02716/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.02716/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Menta在多项心理健康预测任务中表现出色，与最佳非微调SLM相比，平均提升15.2%。在抑郁和压力分类任务上，Menta甚至超越了13B参数的LLM，同时模型体积缩小了3.25倍。此外，Menta成功在iPhone 15 Pro Max上实现实时部署，仅需3GB RAM，验证了其在设备端应用的可行性。

## 🎯 应用场景

Menta可应用于移动健康应用、社交媒体平台和心理健康服务机构，实现对用户心理状态的实时监测和预警。该研究有助于早期发现心理健康问题，为用户提供个性化的支持和干预，并降低医疗成本。未来，Menta可扩展到其他领域，如情感分析、舆情监控等。

## 📄 摘要（原文）

> Mental health conditions affect hundreds of millions globally, yet early detection remains limited. While large language models (LLMs) have shown promise in mental health applications, their size and computational demands hinder practical deployment. Small language models (SLMs) offer a lightweight alternative, but their use for social media--based mental health prediction remains largely underexplored. In this study, we introduce Menta, the first optimized SLM fine-tuned specifically for multi-task mental health prediction from social media data. Menta is jointly trained across six classification tasks using a LoRA-based framework, a cross-dataset strategy, and a balanced accuracy--oriented loss. Evaluated against nine state-of-the-art SLM baselines, Menta achieves an average improvement of 15.2\% across tasks covering depression, stress, and suicidality compared with the best-performing non--fine-tuned SLMs. It also achieves higher accuracy on depression and stress classification tasks compared to 13B-parameter LLMs, while being approximately 3.25x smaller. Moreover, we demonstrate real-time, on-device deployment of Menta on an iPhone 15 Pro Max, requiring only approximately 3GB RAM. Supported by a comprehensive benchmark against existing SLMs and LLMs, Menta highlights the potential for scalable, privacy-preserving mental health monitoring. Code is available at:this https URL

