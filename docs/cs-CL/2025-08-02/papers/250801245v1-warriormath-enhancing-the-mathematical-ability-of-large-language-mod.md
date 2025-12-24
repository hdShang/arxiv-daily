---
layout: default
title: "WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework"
---

# WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01245" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01245v1</a>
  <a href="https://arxiv.org/pdf/2508.01245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01245v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01245v1', 'WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Chen, Minghua He, Fangkai Yang, Pu Zhao, Lu Wang, Yu Kang, Yifei Dong, Yuefeng Zhan, Hao Sun, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang

**分类**: cs.CL

**发布日期**: 2025-08-02

---

## 💡 一句话要点

**提出WarriorMath框架以提升大语言模型的数学能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `数学能力` `缺陷感知` `数据合成` `渐进学习` `智能教育` `自动化求解`

## 📋 核心要点

1. 现有方法在增强LLMs数学能力时，未能有效识别和针对模型的特定失败模式，导致性能提升有限。
2. 本文提出WarriorMath框架，通过专家LLMs协作生成高质量训练数据，并采用渐进式训练策略，针对模型弱点进行优化。
3. 实验结果显示，WarriorMath在六个数学基准测试中平均提升12.57%，显著优于现有强基线，展示了其有效性。

## 📝 摘要（中文）

大语言模型（LLMs）在解决数学问题方面表现优异，但其性能常受限于高质量、多样化训练数据的可用性。现有方法主要通过重述或难度进阶来增强数据集，但忽视了LLMs的特定失败模式，导致生成的合成问题往往是模型已能解决的，性能提升有限。为此，本文提出了WarriorMath，一个缺陷感知框架，集成了针对性的数据合成和渐进式训练。在合成阶段，多个专家LLMs协作生成、评估和改进问题，识别基础LLMs无法解决的问题，并通过专家反馈进行迭代改进，生成高质量的缺陷感知训练数据。在训练阶段，提出了渐进学习框架，利用逐渐增加难度的数据对模型进行微调。实验结果表明，WarriorMath在六个数学基准测试中平均超越强基线12.57%，设立了新的最先进水平。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在数学问题求解中的性能瓶颈，现有方法未能有效识别模型的失败模式，导致生成的合成问题往往是模型已能解决的，提升效果有限。

**核心思路**：论文提出的WarriorMath框架通过缺陷感知的方式，结合多专家LLMs的协作生成和渐进式训练，针对模型的具体弱点进行优化，从而提升其数学能力。

**技术框架**：WarriorMath框架分为两个主要阶段：数据合成阶段和训练阶段。在数据合成阶段，多个专家LLMs协作生成和评估数学问题，识别基础LLMs无法解决的问题，并通过反馈进行迭代改进；在训练阶段，采用渐进学习策略，逐步微调模型，使用难度逐渐增加的数据。

**关键创新**：最重要的技术创新在于缺陷感知的数据合成方法，通过专家LLMs的协作生成高质量训练数据，显著提升了模型在数学问题上的求解能力。这与现有方法的单一数据增强策略形成鲜明对比。

**关键设计**：在数据合成过程中，采用了多种专家LLMs进行问题生成与评估，确保生成的问题具有挑战性且能有效针对模型的弱点；在训练过程中，设计了渐进式学习策略，使模型能够逐步适应更复杂的问题。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，WarriorMath在六个数学基准测试中平均提升12.57%，超越了现有强基线，设立了新的最先进水平，验证了缺陷感知框架在数学能力提升中的有效性。

## 🎯 应用场景

WarriorMath框架的潜在应用领域包括教育技术、智能辅导系统和自动化数学问题求解工具。通过提升大语言模型的数学能力，该研究可为学生提供更精准的学习支持，并推动智能教育的发展，未来可能在各类数学相关应用中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) excel in solving mathematical problems, yet their performance is often limited by the availability of high-quality, diverse training data. Existing methods focus on augmenting datasets through rephrasing or difficulty progression but overlook the specific failure modes of LLMs. This results in synthetic questions that the model can already solve, providing minimal performance gains. To address this, we propose WarriorMath, a defect-aware framework for mathematical problem solving that integrates both targeted data synthesis and progressive training. In the synthesis stage, we employ multiple expert LLMs in a collaborative process to generate, critique, and refine problems. Questions that base LLMs fail to solve are identified and iteratively improved through expert-level feedback, producing high-quality, defect-aware training data. In the training stage, we introduce a progressive learning framework that iteratively fine-tunes the model using increasingly challenging data tailored to its weaknesses. Experiments on six mathematical benchmarks show that WarriorMath outperforms strong baselines by 12.57% on average, setting a new state-of-the-art. Our results demonstrate the effectiveness of a defect-aware, multi-expert framework for improving mathematical ability.

