---
layout: default
title: "OmniEarth-Bench: Towards Holistic Evaluation of Earth's Six Spheres and Cross-Spheres Interactions with Multimodal Observational Earth Data"
---

# OmniEarth-Bench: Towards Holistic Evaluation of Earth's Six Spheres and Cross-Spheres Interactions with Multimodal Observational Earth Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23522" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23522v2</a>
  <a href="https://arxiv.org/pdf/2505.23522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23522v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23522v2', 'OmniEarth-Bench: Towards Holistic Evaluation of Earth\'s Six Spheres and Cross-Spheres Interactions with Multimodal Observational Earth Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengxiang Wang, Mingshuo Chen, Xuming He, Yueying Li, YiFan Zhang, Feng Liu, Zijie Guo, Zhenghao Hu, Jiong Wang, Jingyi Xu, Zhangrui Li, Fenghua Ling, Ben Fei, Weijia Li, Long Lan, Wenjing Yang, Wenlong Zhang, Lei Bai

**分类**: cs.CV, cs.LG

**发布日期**: 2025-05-29 (更新: 2025-11-04)

---

## 💡 一句话要点

**提出OmniEarth-Bench以解决地球六大圈层及其交互的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `地球科学` `评估基准` `数据推理` `专家注释` `系统性评估` `地球圈层` `交互分析`

## 📋 核心要点

1. 现有基准在地球科学多模态学习中覆盖面窄，主要集中于人类活动圈层，任务数量有限，无法全面评估地球系统。
2. 本文提出OmniEarth-Bench，系统性涵盖六大圈层及其交互，采用模块化数据推理框架和专家注释，提供丰富的评估任务。
3. 在对9种最先进的多模态学习模型进行实验时，发现它们在新基准上的表现均未达到35%的准确率，显示出认知能力的不足。

## 📝 摘要（中文）

现有的地球科学多模态学习基准在覆盖地球圈层及其交互方面存在局限，通常仅限于人类活动圈层和最多16个任务。为此，本文提出了OmniEarth-Bench，这是第一个系统性涵盖六大圈层（大气圈、岩石圈、海洋圈、冰冻圈、生物圈和人类活动圈）及其交互的多模态基准。该基准通过可扩展的模块化数据推理框架和专家参与的注释，生成了29,855个标准化的专家注释，组织成四级层次结构，涵盖109个专家评估任务。实验表明，当前最先进的多模态学习模型在该基准上表现不佳，准确率均未达到35%，揭示了地球系统认知能力的系统性差距。

## 🔬 方法详解

**问题定义**：现有的多模态学习基准在地球科学领域存在覆盖面窄、数据源单一和科学细节不足等痛点，限制了对地球六大圈层及其交互的全面评估。

**核心思路**：OmniEarth-Bench通过整合多种观测数据和专家注释，构建了一个系统化的评估框架，旨在全面覆盖地球的六大圈层及其交互，提供更丰富的评估任务。

**技术框架**：该框架采用模块化拓扑结构，包含数据推理、专家注释和任务组织等多个模块，确保数据的可扩展性和评估的系统性。

**关键创新**：OmniEarth-Bench是首个系统性涵盖所有六大圈层及其交互的多模态基准，提供了29,855个标准化的专家注释，显著提升了评估的全面性和科学性。

**关键设计**：注释数据组织为四级层次结构（圈层、场景、能力、任务），并设计了109个专家评估任务，确保了评估的科学性和多样性。实验中使用的模型和任务设置经过精心选择，以验证模型在新基准上的表现。

## 📊 实验亮点

在对9种最先进的多模态学习模型进行评估时，结果显示这些模型在OmniEarth-Bench基准上的准确率均未达到35%，揭示了当前模型在地球系统认知能力方面的系统性不足，强调了该基准的挑战性和重要性。

## 🎯 应用场景

OmniEarth-Bench的研究成果可广泛应用于地球科学、环境监测和气候变化研究等领域。通过提供全面的评估基准，研究人员可以更好地理解地球系统的复杂性，推动相关技术的发展和应用，进而为可持续发展提供科学依据。

## 📄 摘要（原文）

> Existing benchmarks for multimodal learning in Earth science offer limited, siloed coverage of Earth's spheres and their cross-sphere interactions, typically restricting evaluation to the human-activity sphere of atmosphere and to at most 16 tasks. These limitations: \textit{narrow-source heterogeneity (single/few data sources), constrained scientific granularity, and limited-sphere extensibility}. Therefore, we introduce \textbf{OmniEarth-Bench}, the first multimodal benchmark that systematically spans all six spheres: atmosphere, lithosphere, oceanosphere, cryosphere, biosphere, and human-activity sphere, and cross-spheres. Built with a scalable, modular-topology data inference framework and native multi-observation sources and expert-in-the-loop curation, OmniEarth-Bench produces 29,855 standardized, expert-curated annotations. All annotations are organized into a four-level hierarchy (Sphere, Scenario, Ability, Task), encompassing 109 expert-curated evaluation tasks. Experiments on 9 state-of-the-art MLLMs reveal that even the most advanced models struggle with our benchmarks, where none of them reach 35\% accuracy, revealing systematic gaps in Earth-system cognitive ability. The dataset and evaluation code were released at OmniEarth-Bench (https://anonymous.4open.science/r/OmniEarth-Bench-B1BD).

