---
layout: default
title: Evaluating Large Language Models in Scientific Discovery
---

# Evaluating Large Language Models in Scientific Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15567" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15567v1</a>
  <a href="https://arxiv.org/pdf/2512.15567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15567v1" onclick="toggleFavorite(this, '2512.15567v1', 'Evaluating Large Language Models in Scientific Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhangde Song, Jieyu Lu, Yuanqi Du, Botao Yu, Thomas M. Pruyn, Yue Huang, Kehan Guo, Xiuzhe Luo, Yuanhao Qu, Yi Qu, Yinkai Wang, Haorui Wang, Jeff Guo, Jingru Gan, Parshin Shojaee, Di Luo, Andres M Bran, Gen Li, Qiyuan Zhao, Shao-Xiong Lennon Luo, Yuxuan Zhang, Xiang Zou, Wanru Zhao, Yifan F. Zhang, Wucheng Zhang, Shunan Zheng, Saiyang Zhang, Sartaaj Takrim Khan, Mahyar Rajabi-Kochi, Samantha Paradi-Maropakis, Tony Baltoiu, Fengyu Xie, Tianyang Chen, Kexin Huang, Weiliang Luo, Meijing Fang, Xin Yang, Lixue Cheng, Jiajun He, Soha Hassoun, Xiangliang Zhang, Wei Wang, Chandan K. Reddy, Chao Zhang, Zhiling Zheng, Mengdi Wang, Le Cong, Carla P. Gomes, Chang-Yu Hsieh, Aditya Nandy, Philippe Schwaller, Heather J. Kulik, Haojun Jia, Huan Sun, Seyed Mohamad Moosavi, Chenru Duan

**分类**: cs.AI, cond-mat.mtrl-sci, cs.LG, physics.chem-ph

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出科学发现评估框架SDE，用于评估大语言模型在科学研究中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `科学发现` `评估框架` `场景化评估` `迭代推理`

## 📋 核心要点

1. 现有科学基准测试侧重于去语境化的知识，忽略了科学发现中重要的迭代推理和假设生成。
2. 论文提出科学发现评估框架（SDE），通过场景化的研究项目来评估LLMs在科学领域的推理能力。
3. 实验表明，现有LLMs在SDE框架下的表现与通用科学基准存在差距，且模型规模提升收益递减。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地应用于科学研究，但现有的科学基准测试主要考察去语境化的知识，忽略了驱动科学发现的迭代推理、假设生成和观察解释。本文提出了一个基于场景的基准测试，用于评估LLMs在生物学、化学、材料学和物理学等领域的表现。领域专家定义了真实的研究项目，并将其分解为模块化的研究场景，从中抽取经过审核的问题。该框架在两个层面上评估模型：（i）场景相关项目的问答准确性；（ii）项目层面的表现，模型必须提出可验证的假设，设计模拟或实验，并解释结果。将这种两阶段科学发现评估（SDE）框架应用于最先进的LLMs，揭示了相对于通用科学基准的一致性能差距，模型规模和推理能力的提升带来的收益递减，以及不同提供商的顶级模型之间存在的系统性弱点。研究场景中性能的巨大差异导致了科学发现项目中表现最佳模型的选择变化，表明目前所有LLMs距离通用的科学“超智能”还很遥远。然而，LLMs已经在各种科学发现项目中展现出潜力，包括组成场景得分较低的情况，突出了引导探索和意外发现的作用。该SDE框架为LLMs的发现相关评估提供了一个可复现的基准，并为推动其向科学发现发展指明了实际路径。

## 🔬 方法详解

**问题定义**：现有的大语言模型评估方法，特别是针对科学领域的评估，往往侧重于模型对孤立知识点的记忆和检索能力，而忽略了科学研究中至关重要的迭代推理、假设生成、实验设计和结果解释等能力。现有的科学基准测试无法有效评估LLMs在真实科研场景下的表现，阻碍了LLMs在科学发现领域的应用。

**核心思路**：本文的核心思路是构建一个更贴近真实科研流程的评估框架，即科学发现评估（SDE）框架。该框架通过模拟真实的科研项目，将复杂的科研任务分解为一系列模块化的研究场景，并设计相应的评估指标，从而更全面、更准确地评估LLMs在科学发现中的能力。这种场景化的评估方式能够更好地反映LLMs在实际科研中的应用潜力。

**技术框架**：SDE框架包含以下几个主要阶段：
1. **研究项目定义**：领域专家根据自身研究兴趣，定义具有实际意义的科研项目。
2. **场景分解**：将科研项目分解为一系列模块化的研究场景，每个场景对应一个具体的科研任务。
3. **问题生成与审核**：针对每个研究场景，生成一系列经过专家审核的问题，用于评估LLMs在该场景下的表现。
4. **模型评估**：使用LLMs回答场景相关的问题，并评估其在问题层面的准确性和项目层面的整体表现。
5. **结果分析**：分析LLMs在不同研究场景和项目中的表现，识别其优势和不足。

**关键创新**：SDE框架的关键创新在于其场景化的评估方式。与传统的基于知识点的评估方法不同，SDE框架将LLMs置于真实的科研场景中，要求其完成一系列与科研相关的任务，从而更全面地评估其在科学发现中的能力。此外，SDE框架还引入了项目层面的评估指标，用于评估LLMs在完成整个科研项目中的表现。

**关键设计**：SDE框架的关键设计包括：
1. **场景选择**：选择具有代表性的科研场景，覆盖生物学、化学、材料学和物理学等多个领域。
2. **问题设计**：设计具有挑战性的问题，要求LLMs进行推理、假设生成和结果解释。
3. **评估指标**：采用问题层面的准确率和项目层面的整体表现作为评估指标，全面评估LLMs的能力。

## 📊 实验亮点

实验结果表明，现有最先进的LLMs在SDE框架下的表现与通用科学基准存在显著差距，表明LLMs在真实科研场景下的推理能力仍有待提高。此外，实验还发现，模型规模的提升带来的收益递减，且不同提供商的顶级模型之间存在系统性弱点。尽管如此，LLMs在某些科研项目中仍展现出潜力，即使在组成场景得分较低的情况下，也可能取得较好的整体表现。

## 🎯 应用场景

该研究成果可用于评估和改进大语言模型在科学研究领域的应用能力，推动AI在科学发现中的应用。潜在应用领域包括新材料发现、药物研发、生物学研究等。通过SDE框架，可以更有效地指导LLMs的开发，使其更好地服务于科学研究，加速科学发现的进程。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly applied to scientific research, yet prevailing science benchmarks probe decontextualized knowledge and overlook the iterative reasoning, hypothesis generation, and observation interpretation that drive scientific discovery. We introduce a scenario-grounded benchmark that evaluates LLMs across biology, chemistry, materials, and physics, where domain experts define research projects of genuine interest and decompose them into modular research scenarios from which vetted questions are sampled. The framework assesses models at two levels: (i) question-level accuracy on scenario-tied items and (ii) project-level performance, where models must propose testable hypotheses, design simulations or experiments, and interpret results. Applying this two-phase scientific discovery evaluation (SDE) framework to state-of-the-art LLMs reveals a consistent performance gap relative to general science benchmarks, diminishing return of scaling up model sizes and reasoning, and systematic weaknesses shared across top-tier models from different providers. Large performance variation in research scenarios leads to changing choices of the best performing model on scientific discovery projects evaluated, suggesting all current LLMs are distant to general scientific "superintelligence". Nevertheless, LLMs already demonstrate promise in a great variety of scientific discovery projects, including cases where constituent scenario scores are low, highlighting the role of guided exploration and serendipity in discovery. This SDE framework offers a reproducible benchmark for discovery-relevant evaluation of LLMs and charts practical paths to advance their development toward scientific discovery.

