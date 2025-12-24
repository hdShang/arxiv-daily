---
layout: default
title: "AttriLens-Mol: Attribute Guided Reinforcement Learning for Molecular Property Prediction with Large Language Models"
---

# AttriLens-Mol: Attribute Guided Reinforcement Learning for Molecular Property Prediction with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04748" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04748v2</a>
  <a href="https://arxiv.org/pdf/2508.04748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04748v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04748v2', 'AttriLens-Mol: Attribute Guided Reinforcement Learning for Molecular Property Prediction with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan Lin, Long Chen, Yile Wang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-06 (更新: 2025-09-28)

**备注**: 9 pages

**🔗 代码/项目**: [GITHUB](https://github.com/szu-tera/AttriLens-Mol)

---

## 💡 一句话要点

**提出AttriLens-Mol以解决分子属性预测中的推理效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子属性预测` `强化学习` `大型语言模型` `属性引导` `可解释性`

## 📋 核心要点

1. 现有方法在分子属性预测中依赖人工设计的提示，导致推理过程冗长且缺乏相关性。
2. AttriLens-Mol通过引入格式奖励、计数奖励和合理性奖励，优化了模型的推理过程，提升了预测效果。
3. 实验表明，使用AttriLens-Mol训练的模型在多个数据集上性能显著提升，超越了多种基线模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在分子属性预测任务中展现出潜力，但通常依赖人工设计的提示和思维链模板。尽管最近的深度推理模型如DeepSeek-R1采用强化学习进行扩展的推理过程，但其推理往往冗长且缺乏相关性。我们提出了AttriLens-Mol，一个基于属性引导的强化学习框架，用于利用LLMs进行分子属性预测。该方法通过格式奖励、计数奖励和合理性奖励来引导模型推理，显著提升了预测效果。实验结果表明，使用AttriLens-Mol训练的模型在多个数据集上表现优异，超越了现有的监督微调模型和先进模型，且提取的属性在可解释性决策树模型中表现更佳。我们已在https://github.com/szu-tera/AttriLens-Mol发布代码。

## 🔬 方法详解

**问题定义**：本论文旨在解决分子属性预测中推理效率低下的问题，现有方法往往依赖人工提示，导致推理过程冗长且缺乏相关性。

**核心思路**：AttriLens-Mol通过引入属性引导的强化学习框架，利用格式奖励、计数奖励和合理性奖励来优化模型的推理过程，从而提升分子属性的预测效果。

**技术框架**：该框架主要包括三个模块：格式奖励模块、计数奖励模块和合理性奖励模块。格式奖励鼓励基于属性的结构化输出，计数奖励避免枚举无关属性，而合理性奖励则通过高级LLMs和RDKit验证生成属性的相关性。

**关键创新**：AttriLens-Mol的核心创新在于通过强化学习引导模型推理，显著提升了模型对相关分子属性的识别能力，与传统方法相比，能够更有效地进行属性预测。

**关键设计**：在设计中，格式奖励和计数奖励的具体参数设置经过调优，以确保模型输出的相关性和结构化，同时合理性奖励利用了先进的LLMs和RDKit工具进行属性验证。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，使用AttriLens-Mol训练的7B规模模型在4,000个样本上显著提升了性能，取得了与监督微调模型（如Mol-Instructions、ChemDFM等）和先进模型（如GPT-3.5、GPT-4o等）相当或更好的结果，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括药物发现、材料科学和化学合成等。通过提升分子属性预测的准确性和效率，AttriLens-Mol能够为新材料的设计和药物的开发提供更为可靠的支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown promise in assisting molecular property prediction tasks but often rely on human-crafted prompts and chain-of-thought templates. While recent advanced large reasoning models like DeepSeek-R1 employ reinforcement learning for an extended ``thinking'' process, their reasoning can be verbose and lack relevance. We introduce AttriLens-Mol, an attribute-guided reinforcement learning framework for molecular property prediction with LLMs. AttriLens-Mol steers the model's reasoning by using: (1) a format reward encouraging attribute-based structured output, (2) a count reward to avoid enumerating irrelevant attributes, and (3) a rationality reward using advanced LLMs and RDKit to verify the relatedness of the generated attributes. This approach implicitly elicits the model's inherent knowledge of relevant molecular attributes during reasoning, enables making predictions for the molecular property more effectively. Experiments on both in-distribution and out-of-distribution datasets show that, training both 7B-size R1-Distilled-Qwen2.5 and R1-Distilled-LLaMA3.1 models on 4,000 samples with our proposed AttriLens-Mol method significantly boosts the performance, getting comparable or better results than supervised fine-tuning models (Mol-Instructions, ChemDFM, etc.) and advanced models (GPT-3.5, GPT-4o, DeepSeek-V3, DeepSeek-R1, etc.). Further, our extracted attributes for the target property, when used as features for an interpretable decision tree model, yield superior performance compared to attributes generated by prompting LLMs. This shows that AttriLens-Mol effectively elicits more relevant and predictive molecular attributes, leading to enhanced interpretability and performance for property prediction. We release the code in https://github.com/szu-tera/AttriLens-Mol.

