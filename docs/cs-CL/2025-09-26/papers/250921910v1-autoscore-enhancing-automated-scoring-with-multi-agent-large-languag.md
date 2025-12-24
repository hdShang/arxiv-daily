---
layout: default
title: "AutoSCORE: Enhancing Automated Scoring with Multi-Agent Large Language Models via Structured Component Recognition"
---

# AutoSCORE: Enhancing Automated Scoring with Multi-Agent Large Language Models via Structured Component Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21910" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21910v1</a>
  <a href="https://arxiv.org/pdf/2509.21910.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21910v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21910v1', 'AutoSCORE: Enhancing Automated Scoring with Multi-Agent Large Language Models via Structured Component Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yun Wang, Zhaojun Ding, Xuansheng Wu, Siyue Sun, Ninghao Liu, Xiaoming Zhai

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

**备注**: 9 pages, 2 figures

---

## 💡 一句话要点

**提出AutoSCORE以解决自动评分中的准确性和可解释性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动评分` `大型语言模型` `教育评估` `多代理系统` `结构化组件识别` `评分标准一致性` `可解释性` `机器学习`

## 📋 核心要点

1. 现有的自动评分方法在准确性、可解释性和与评分标准的一致性方面存在显著不足，限制了其在实际评估中的应用。
2. 本文提出的AutoSCORE框架通过结构化组件识别和多代理设计，确保评分过程更符合人类评分逻辑，从而提升评分的准确性和可解释性。
3. 实验结果显示，AutoSCORE在多个基准数据集上相较于单代理基线显著提高了评分准确性和人机一致性，尤其在复杂的多维评分标准上表现尤为突出。

## 📝 摘要（中文）

自动评分在教育中扮演着重要角色，能够减少对人工评分的依赖，实现对学生作业的可扩展和即时评估。尽管大型语言模型（LLMs）在此任务中展现出强大潜力，但作为端到端评分工具的应用面临准确性低、提示敏感性、可解释性有限和评分标准不一致等挑战。为了解决这些问题，本文提出了AutoSCORE，一个通过结构化组件识别增强自动评分的多代理LLM框架。AutoSCORE通过两个代理，首先从学生回答中提取与评分标准相关的组件，并将其编码为结构化表示，随后用于最终评分。这一设计确保模型推理遵循类似人类的评分过程，从而提高可解释性和鲁棒性。实验结果表明，AutoSCORE在多个基准数据集上显著提升了评分准确性和人机一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动评分方法在准确性、可解释性和与评分标准一致性方面的不足，特别是在复杂评分标准下的表现不佳。

**核心思路**：AutoSCORE通过引入多代理设计，首先提取与评分标准相关的组件，并将其结构化，从而使评分过程更符合人类的评分逻辑。

**技术框架**：AutoSCORE框架包含两个主要模块：评分标准组件提取代理和评分代理。前者负责从学生的回答中提取相关组件，后者则基于这些组件进行最终评分。

**关键创新**：AutoSCORE的核心创新在于通过结构化组件识别与多代理设计相结合，显著提升了自动评分的准确性和可解释性，这与传统的单一代理评分方法形成了鲜明对比。

**关键设计**：在设计中，采用了特定的损失函数来优化评分准确性，并通过对不同规模的LLM（如GPT-4o和LLaMA-3.1系列）进行实验，验证了框架的有效性。

## 📊 实验亮点

实验结果表明，AutoSCORE在四个基准数据集上相较于单代理基线显著提高了评分准确性和人机一致性，具体表现为QWK和相关性指标的提升，以及MAE和RMSE等误差指标的降低，尤其在复杂的多维评分标准上，较小的LLM模型获得了显著的相对增益。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、在线学习平台和自动化考试系统。通过提高自动评分的准确性和可解释性，AutoSCORE能够为教育工作者提供更可靠的评估工具，进而提升教学质量和学习效果。未来，随着教育技术的不断发展，该框架有望在更广泛的评估场景中得到应用。

## 📄 摘要（原文）

> Automated scoring plays a crucial role in education by reducing the reliance on human raters, offering scalable and immediate evaluation of student work. While large language models (LLMs) have shown strong potential in this task, their use as end-to-end raters faces challenges such as low accuracy, prompt sensitivity, limited interpretability, and rubric misalignment. These issues hinder the implementation of LLM-based automated scoring in assessment practice. To address the limitations, we propose AutoSCORE, a multi-agent LLM framework enhancing automated scoring via rubric-aligned Structured COmponent REcognition. With two agents, AutoSCORE first extracts rubric-relevant components from student responses and encodes them into a structured representation (i.e., Scoring Rubric Component Extraction Agent), which is then used to assign final scores (i.e., Scoring Agent). This design ensures that model reasoning follows a human-like grading process, enhancing interpretability and robustness. We evaluate AutoSCORE on four benchmark datasets from the ASAP benchmark, using both proprietary and open-source LLMs (GPT-4o, LLaMA-3.1-8B, and LLaMA-3.1-70B). Across diverse tasks and rubrics, AutoSCORE consistently improves scoring accuracy, human-machine agreement (QWK, correlations), and error metrics (MAE, RMSE) compared to single-agent baselines, with particularly strong benefits on complex, multi-dimensional rubrics, and especially large relative gains on smaller LLMs. These results demonstrate that structured component recognition combined with multi-agent design offers a scalable, reliable, and interpretable solution for automated scoring.

