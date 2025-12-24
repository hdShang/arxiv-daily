---
layout: default
title: "DeepMath-Creative: A Benchmark for Evaluating Mathematical Creativity of Large Language Models"
---

# DeepMath-Creative: A Benchmark for Evaluating Mathematical Creativity of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08744" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08744v1</a>
  <a href="https://arxiv.org/pdf/2505.08744.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08744v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08744v1', 'DeepMath-Creative: A Benchmark for Evaluating Mathematical Creativity of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyang Chen, Xinan Dai, Yu Du, Qian Feng, Naixu Guo, Tingshuo Gu, Yuting Gao, Yingyi Gao, Xudong Han, Xiang Jiang, Yilin Jin, Hongyi Lin, Shisheng Lin, Xiangnan Li, Yuante Li, Yixing Li, Zhentao Lai, Zilu Ma, Yingrong Peng, Jiacheng Qian, Hao-Yu Sun, Jianbo Sun, Zirui Wang, Siwei Wu, Zian Wang, Bin Xu, Jianghao Xu, Yiyang Yu, Zichuan Yang, Hongji Zha, Ruichong Zhang

**分类**: cs.AI

**发布日期**: 2025-05-13

**备注**: 14 pages, 4 figures

---

## 💡 一句话要点

**提出DeepMath-Creative基准以评估大型语言模型的数学创造力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学创造力` `大型语言模型` `DeepMath-Creative` `评估基准` `机器学习` `问题解决能力` `开源项目`

## 📋 核心要点

1. 现有的数学LLMs主要关注推理能力，创造力评估缺乏系统性和数据支持。
2. 提出DeepMath-Creative基准，系统评估LLMs在数学创造力方面的表现，涵盖多种数学领域。
3. 实验结果显示，当前模型在复杂问题上的表现不佳，主要依赖于记忆而非创造性思维。

## 📝 摘要（中文）

为提升大型语言模型（LLMs）的数学能力，DeepMath团队发起了一项开源计划，旨在开发开放的数学LLM并系统评估其数学创造力。本文是该计划的初步贡献。尽管近期数学LLM的发展主要集中在推理能力上，但对这些模型的创造性能力关注较少，评估数据集也相对匮乏。为填补这一空白，本文提出了数学创造力的评估标准，并引入了DeepMath-Creative，一个涵盖代数、几何、分析等领域的高质量基准。通过该数据集，我们对主流LLMs的创造性问题解决能力进行了系统评估。实验结果显示，即使在宽松的评分标准下，表现最佳的模型O3 Mini仅在基础本科级构造任务上达到了70%的准确率，面对更复杂的问题表现急剧下降，未能提供实质性的开放问题解决策略。这些发现表明，当前LLMs在熟悉且低难度问题上的表现可能更多源于对记忆模式的重组，而非真正的创造性洞察或新颖综合。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学创造力评估方面的不足，现有方法缺乏系统性和有效的数据集，导致对模型创造力的评估不够全面。

**核心思路**：提出DeepMath-Creative基准，通过构造多样化的数学问题，系统评估LLMs的创造性解决能力，强调对创造性思维的重视。

**技术框架**：整体架构包括数据集构建、评估标准制定和模型评估三个主要模块。数据集涵盖代数、几何、分析等领域的构造性问题，评估标准则关注核心解决方案的完整性。

**关键创新**：最重要的创新在于提出了数学创造力的评估标准，并构建了一个高质量的基准数据集，填补了现有研究的空白。与以往只关注推理能力的评估方法相比，本文更全面地考虑了创造性思维。

**关键设计**：在实验中，采用宽松的评分标准，关注核心解决方案的组成部分，忽略小的逻辑缺陷和冗余解释，确保评估的公正性和有效性。

## 📊 实验亮点

实验结果显示，最佳模型O3 Mini在基础本科级构造任务上仅达到70%的准确率，面对复杂问题时表现显著下降，未能提供有效的解决策略。这表明当前模型在创造性思维方面的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能辅导系统和数学问题生成等。通过评估和提升LLMs的数学创造力，可以为学生提供更具个性化的学习体验，并推动数学教育的创新发展。

## 📄 摘要（原文）

> To advance the mathematical proficiency of large language models (LLMs), the DeepMath team has launched an open-source initiative aimed at developing an open mathematical LLM and systematically evaluating its mathematical creativity. This paper represents the initial contribution of this initiative. While recent developments in mathematical LLMs have predominantly emphasized reasoning skills, as evidenced by benchmarks on elementary to undergraduate-level mathematical tasks, the creative capabilities of these models have received comparatively little attention, and evaluation datasets remain scarce. To address this gap, we propose an evaluation criteria for mathematical creativity and introduce DeepMath-Creative, a novel, high-quality benchmark comprising constructive problems across algebra, geometry, analysis, and other domains. We conduct a systematic evaluation of mainstream LLMs' creative problem-solving abilities using this dataset. Experimental results show that even under lenient scoring criteria -- emphasizing core solution components and disregarding minor inaccuracies, such as small logical gaps, incomplete justifications, or redundant explanations -- the best-performing model, O3 Mini, achieves merely 70% accuracy, primarily on basic undergraduate-level constructive tasks. Performance declines sharply on more complex problems, with models failing to provide substantive strategies for open problems. These findings suggest that, although current LLMs display a degree of constructive proficiency on familiar and lower-difficulty problems, such performance is likely attributable to the recombination of memorized patterns rather than authentic creative insight or novel synthesis.

