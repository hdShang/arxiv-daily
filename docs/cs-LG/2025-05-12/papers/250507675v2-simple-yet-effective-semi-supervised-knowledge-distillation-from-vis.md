---
layout: default
title: Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization
---

# Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07675" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07675v2</a>
  <a href="https://arxiv.org/pdf/2505.07675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07675v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07675v2', 'Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seongjae Kang, Dong Bok Lee, Hyungjoon Jang, Sung Ju Hwang

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-05-12 (更新: 2025-09-30)

**备注**: 38 pages, 17 figures, preprint

**🔗 代码/项目**: [GITHUB](https://github.com/erjui/DHO)

---

## 💡 一句话要点

**提出双头优化方法以解决知识蒸馏中的梯度冲突问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `半监督学习` `知识蒸馏` `视觉-语言模型` `双头优化` `特征学习` `模型泛化` `计算机视觉` `自然语言处理`

## 📋 核心要点

1. 现有的知识蒸馏方法在监督损失与蒸馏损失之间存在梯度冲突，影响了模型性能。
2. 本文提出双头优化（DHO）方法，通过引入双重预测头来解决梯度冲突问题，从而提升特征学习效果。
3. 在15个数据集上的实验表明，DHO方法在性能上超越了传统的知识蒸馏基线，且在多个任务中表现优异。

## 📝 摘要（中文）

半监督学习（SSL）通过利用未标记数据来应对数据稀缺问题。近年来，视觉-语言模型（VLMs）在大量图像-文本对上进行预训练，展现出卓越的零样本和少样本性能，超越了传统的SSL方法。为有效利用VLM的强大泛化能力，本文提出了双头优化（DHO）方法，旨在解决监督损失与蒸馏损失之间的梯度冲突。DHO通过为每个信号引入双重预测头，显著改善了特征学习效果，且在计算开销和测试时超参数调优方面具有优势。实验结果表明，DHO在15个数据集上均优于传统KD基线，且在ImageNet半监督学习和跨ImageNet变体的外部泛化上达到了新的最优性能。

## 🔬 方法详解

**问题定义**：本文旨在解决知识蒸馏过程中监督损失与蒸馏损失之间的梯度冲突问题。现有方法在处理未标记数据时，常常无法有效利用VLM的泛化能力，导致性能下降。

**核心思路**：提出双头优化（DHO）方法，通过为每个信号引入双重预测头，分别处理监督和蒸馏信号，从而避免梯度冲突，提升特征学习效果。

**技术框架**：DHO的整体架构包括两个主要模块：一个用于监督学习的预测头，另一个用于知识蒸馏的预测头。模型在训练过程中同时优化这两个头，确保各自信号的独立性。

**关键创新**：DHO的核心创新在于引入双重预测头设计，解决了传统单头蒸馏方法中存在的梯度冲突问题。这一设计使得模型在特征学习上表现更为优越。

**关键设计**：DHO在损失函数设计上采用了独立的监督损失和蒸馏损失，并在网络结构上实现了双头架构。该方法在计算开销上保持了低成本，同时支持测试时的超参数调优，无需重新训练。

## 📊 实验亮点

实验结果显示，DHO在15个数据集上均优于传统的知识蒸馏基线，且在ImageNet半监督学习任务中，DHO方法的性能甚至超过了较大的教师模型，展示了其在小模型训练中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理及其交叉领域，尤其是在数据稀缺的场景下。通过有效利用未标记数据，DHO方法能够提升模型的泛化能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Semi-supervised learning (SSL) has emerged as a practical solution for addressing data scarcity challenges by leveraging unlabeled data. Recently, vision-language models (VLMs), pre-trained on massive image-text pairs, have demonstrated remarkable zero-/few-shot performance that often surpasses SSL approaches due to their exceptional generalization capabilities. This gap motivates us to question: how can we effectively harness the powerful generalization capabilities of VLMs into task-specific models? Knowledge distillation (KD) offers a natural framework for transferring VLM capabilities, but we identify that it suffers from gradient conflicts between supervised and distillation losses. To address this challenge, we propose Dual-Head Optimization (DHO), which introduces dual prediction heads for each distinct signal. We observe that DHO resolves gradient conflicts, enabling improved feature learning compared to single-head KD baselines, with practical benefits of minimal computational overhead and test-time hyperparameter tuning without retraining. Extensive experiments across 15 datasets show that DHO consistently outperforms KD baselines, often outperforming teacher models with smaller student models. DHO also achieves new state-of-the-art performance on both in-distribution ImageNet semi-supervised learning and out-of-distribution generalization across ImageNet variants. We publicly release our code and model checkpoints to facilitate future research at https://github.com/erjui/DHO.

