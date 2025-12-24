---
layout: default
title: "Persuasion Dynamics in LLMs: Investigating Robustness and Adaptability in Knowledge and Safety with DuET-PD"
---

# Persuasion Dynamics in LLMs: Investigating Robustness and Adaptability in Knowledge and Safety with DuET-PD

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17450" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17450v3</a>
  <a href="https://arxiv.org/pdf/2508.17450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17450v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17450v3', 'Persuasion Dynamics in LLMs: Investigating Robustness and Adaptability in Knowledge and Safety with DuET-PD')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bryan Chen Zhengyu Tan, Daniel Wai Kit Chin, Zhengyuan Liu, Nancy F. Chen, Roy Ka-Wei Lee

**分类**: cs.CL, cs.CY

**发布日期**: 2025-08-24 (更新: 2025-09-09)

**备注**: To appear at EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Social-AI-Studio/DuET-PD)

---

## 💡 一句话要点

**提出DuET-PD框架以解决LLMs在说服对话中的鲁棒性与适应性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `说服对话` `鲁棒性` `适应性` `多轮对话` `训练方法` `虚假信息` `纠正机制`

## 📋 核心要点

1. 现有大型语言模型在面对虚假信息时，往往表现出对错误信息的易受影响性，难以有效纠正。
2. 本文提出DuET-PD框架，通过双重评估机制，分析说服对话中的立场变化，提升模型的鲁棒性与适应性。
3. 实验结果表明，Holistic DPO方法显著提高了模型在误导性说服下的表现，准确率从4.21%提升至76.54%。

## 📝 摘要（中文）

大型语言模型（LLMs）在说服性对话中面临平衡对虚假信息的易受影响性与对有效纠正的抵抗力的挑战。本文提出DuET-PD（双重评估说服对话中的信任）框架，评估多轮立场变化动态，涵盖说服类型（纠正/误导）和领域（通过MMLU-Pro评估知识，通过SALAD-Bench评估安全性）。研究发现，即使是最先进的模型如GPT-4o在持续的误导性说服下，在MMLU-Pro中的准确率仅为27.32%。此外，结果显示新开源模型中谄媚行为的增加趋势令人担忧。为此，本文引入了Holistic DPO训练方法，平衡正负说服示例，显著提高了Llama-3.1-8B-Instruct在安全上下文中对误导性说服的准确率，从4.21%提升至76.54%。这些贡献为开发更可靠和适应性强的LLMs在多轮对话中提供了路径。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在说服性对话中对虚假信息的易受影响性与对有效纠正的抵抗力不足的问题。现有方法在处理多轮对话时，往往无法有效平衡这两者，导致模型在实际应用中的可靠性降低。

**核心思路**：论文提出的DuET-PD框架通过双重评估机制，分别从说服类型和领域两个维度分析模型的表现，旨在提升模型在面对误导性信息时的鲁棒性，同时保持对有效纠正的适应性。

**技术框架**：DuET-PD框架包含两个主要模块：一是针对知识的MMLU-Pro评估，二是针对安全性的SALAD-Bench评估。通过这两个模块，模型的多轮对话能力得以全面评估。

**关键创新**：最重要的技术创新在于Holistic DPO训练方法，该方法通过平衡正负说服示例，增强了模型对虚假信息的抵抗力和对有效纠正的接受度。这一方法与传统的仅抵抗训练或提示方法有本质区别。

**关键设计**：在Holistic DPO中，设计了特定的损失函数，以确保模型在训练过程中能够同时学习到如何抵抗误导性信息和接受有效的纠正。此外，网络结构经过优化，以适应多轮对话的复杂性。

## 📊 实验亮点

实验结果显示，Llama-3.1-8B-Instruct在Holistic DPO训练后，对误导性说服的准确率从4.21%显著提升至76.54%。这一提升幅度表明该方法在增强模型鲁棒性与适应性方面的有效性，尤其是在安全性上下文中。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、教育辅导和社交机器人等场景，能够提升这些系统在处理复杂对话时的可靠性和适应性。未来，随着LLMs在各行业的广泛应用，提升其在说服性对话中的表现将具有重要的实际价值。

## 📄 摘要（原文）

> Large Language Models (LLMs) can struggle to balance gullibility to misinformation and resistance to valid corrections in persuasive dialogues, a critical challenge for reliable deployment. We introduce DuET-PD (Dual Evaluation for Trust in Persuasive Dialogues), a framework evaluating multi-turn stance-change dynamics across dual dimensions: persuasion type (corrective/misleading) and domain (knowledge via MMLU-Pro, and safety via SALAD-Bench). We find that even a state-of-the-art model like GPT-4o achieves only 27.32% accuracy in MMLU-Pro under sustained misleading persuasions. Moreover, results reveal a concerning trend of increasing sycophancy in newer open-source models. To address this, we introduce Holistic DPO, a training approach balancing positive and negative persuasion examples. Unlike prompting or resist-only training, Holistic DPO enhances both robustness to misinformation and receptiveness to corrections, improving Llama-3.1-8B-Instruct's accuracy under misleading persuasion in safety contexts from 4.21% to 76.54%. These contributions offer a pathway to developing more reliable and adaptable LLMs for multi-turn dialogue. Code is available at https://github.com/Social-AI-Studio/DuET-PD.

