---
layout: default
title: "CodeContests+: High-Quality Test Case Generation for Competitive Programming"
---

# CodeContests+: High-Quality Test Case Generation for Competitive Programming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05817" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05817v1</a>
  <a href="https://arxiv.org/pdf/2506.05817.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05817v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05817v1', 'CodeContests+: High-Quality Test Case Generation for Competitive Programming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Siyao Liu, Yang Sun, Hongyan Li, Kai Shen

**分类**: cs.SE, cs.CL

**发布日期**: 2025-06-06

**备注**: 28 pages, 7 figures

---

## 💡 一句话要点

**提出CodeContests+以解决竞争编程测试用例生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `竞争编程` `测试用例生成` `大型语言模型` `强化学习` `数据集构建`

## 📋 核心要点

1. 现有的竞争编程测试用例获取困难，影响了评估的准确性和数据集的构建。
2. 提出了一种基于大型语言模型的代理系统，能够自动生成高质量的测试用例。
3. 实验结果显示，CodeContests+在测试用例的准确性上显著高于原始数据集，尤其在真正阳性率方面有明显提升。

## 📝 摘要（中文）

竞争编程因其高推理难度和精确的正确性反馈，成为训练和评估大型语言模型（LLMs）推理能力的关键任务。然而，尽管有大量公开问题数据，测试用例往往难以获取。因此，测试用例生成是构建大规模数据集的必要任务，且其质量直接影响评估的准确性。本文介绍了一种基于LLM的代理系统，生成高质量的竞争编程问题测试用例，并在CodeContests数据集上应用，提出了改进版本CodeContests+。通过对1.72百万提交的评估，结果表明CodeContests+在准确性上显著优于CodeContests，尤其在真正阳性率（TPR）方面有显著提升。进一步的强化学习实验也证实了测试用例质量的提升对强化学习的显著优势。

## 🔬 方法详解

**问题定义**：本文旨在解决竞争编程中测试用例生成的困难，现有方法通常缺乏高质量的测试用例，导致评估结果不准确。

**核心思路**：通过构建一个基于大型语言模型的代理系统，自动生成高质量的测试用例，从而提高数据集的质量和评估的准确性。

**技术框架**：整体架构包括数据收集、测试用例生成和质量评估三个主要模块。首先收集竞争编程问题的数据，然后利用LLM生成测试用例，最后通过大量提交数据进行质量评估。

**关键创新**：最重要的创新在于引入了LLM进行测试用例生成，显著提高了生成测试用例的质量，与传统手动生成方法相比，具有更高的准确性和效率。

**关键设计**：在生成过程中，设置了特定的参数以优化生成效果，并采用了针对测试用例质量的损失函数，以确保生成的测试用例能够有效评估程序的正确性。具体的网络结构和训练策略也经过精心设计，以适应竞争编程的特点。

## 📊 实验亮点

实验结果显示，CodeContests+在测试用例的准确性上显著优于CodeContests，特别是在真正阳性率（TPR）方面提升了显著的比例。此外，通过强化学习实验验证了测试用例质量提升对模型训练的积极影响，进一步证明了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、在线编程竞赛平台和自动化测试工具。通过生成高质量的测试用例，可以帮助学生更好地理解编程问题，提高编程能力，同时为在线竞赛提供更可靠的评估标准，未来可能推动智能教育和自动化评估的发展。

## 📄 摘要（原文）

> Competitive programming, due to its high reasoning difficulty and precise correctness feedback, has become a key task for both training and evaluating the reasoning capabilities of large language models (LLMs). However, while a large amount of public problem data, such as problem statements and solutions, is available, the test cases of these problems are often difficult to obtain. Therefore, test case generation is a necessary task for building large-scale datasets, and the quality of the test cases directly determines the accuracy of the evaluation. In this paper, we introduce an LLM-based agent system that creates high-quality test cases for competitive programming problems. We apply this system to the CodeContests dataset and propose a new version with improved test cases, named CodeContests+. We evaluated the quality of test cases in CodeContestsPlus. First, we used 1.72 million submissions with pass/fail labels to examine the accuracy of these test cases in evaluation. The results indicated that CodeContests+ achieves significantly higher accuracy than CodeContests, particularly with a notably higher True Positive Rate (TPR). Subsequently, our experiments in LLM Reinforcement Learning (RL) further confirmed that improvements in test case quality yield considerable advantages for RL.

