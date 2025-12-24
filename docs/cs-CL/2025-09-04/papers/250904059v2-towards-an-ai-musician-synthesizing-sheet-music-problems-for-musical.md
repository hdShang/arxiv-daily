---
layout: default
title: "Towards an AI Musician: Synthesizing Sheet Music Problems for Musical Reasoning"
---

# Towards an AI Musician: Synthesizing Sheet Music Problems for Musical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04059" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04059v2</a>
  <a href="https://arxiv.org/pdf/2509.04059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04059v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04059v2', 'Towards an AI Musician: Synthesizing Sheet Music Problems for Musical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhilin Wang, Zhe Yang, Yun Luo, Yafu Li, Xiaoye Qu, Ziqian Qiao, Haoran Zhang, Runzhe Zhan, Derek F. Wong, Jizhe Zhou, Yu Cheng

**分类**: cs.CL

**发布日期**: 2025-09-04 (更新: 2025-09-26)

**备注**: 34 pages

---

## 💡 一句话要点

**提出SSMR-Bench：合成乐谱推理问题，提升AI音乐家能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `乐谱理解` `AI音乐家` `合成数据` `程序化生成` `推理基准`

## 📋 核心要点

1. 现有方法缺乏乐谱推理的评估基准和训练数据，阻碍了AI音乐家的发展。
2. 将音乐理论规则程序化，系统合成乐谱推理问题，构建SSMR-Bench基准和训练集。
3. 利用合成数据进行RLVR，模型在SSMR-Bench及人工基准上均取得显著提升。

## 📝 摘要（中文）

为了提升大型语言模型（LLMs）和多模态大型语言模型（MLLMs）理解乐谱的能力，本文提出了一种新颖的方法，旨在构建AI音乐家。当前研究缺乏乐谱推理的评估基准和训练数据。受数学的启发，本文将核心音乐理论规则（如节拍和音程）视为程序化函数，以系统地合成大量且多样化的乐谱推理问题。该方法引入了一个数据合成框架，可以生成文本和视觉模态的可验证乐谱问题，从而构建了合成乐谱推理基准（SSMR-Bench）和一个补充训练集。在SSMR-Bench上的评估结果突出了推理在乐谱理解中的关键作用，同时也指出了视觉格式乐谱理解方面存在的挑战。通过利用合成数据进行RLVR（Reinforcement Learning from Verification and Refinement），所有模型在SSMR-Bench上都表现出显著的改进。此外，它们在先前建立的人工基准（如MusicTheoryBench和MMMU的音乐子集）上也表现出显著的进步。最后，结果表明，增强的推理能力还可以促进音乐创作。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型和多模态大型语言模型在乐谱理解方面的不足。现有方法缺乏专门针对乐谱推理的评估基准和训练数据，导致模型难以有效学习和应用音乐理论知识。这限制了AI在音乐创作、分析和教育等领域的应用。

**核心思路**：论文的核心思路是将音乐理论规则（如节拍、音程等）视为程序化的函数，通过这些函数系统地生成大量多样化的乐谱推理问题。这种方法借鉴了数学中通过简单运算产生无限可验证问题的思想，从而能够低成本地创建高质量的训练和评估数据。

**技术框架**：整体框架包含数据合成、模型训练和评估三个主要阶段。数据合成阶段利用程序化的音乐理论规则生成文本和视觉模态的乐谱问题及其答案。模型训练阶段使用合成数据对LLMs或MLLMs进行训练，并采用RLVR方法进行优化。评估阶段则在SSMR-Bench以及现有的人工基准上评估模型的性能。

**关键创新**：最重要的技术创新点在于提出了基于程序化规则的乐谱数据合成方法。与传统的人工标注数据相比，该方法能够自动生成大规模、多样化且可验证的数据，有效解决了乐谱推理领域数据稀缺的问题。此外，结合RLVR方法，进一步提升了模型在乐谱理解和推理方面的能力。

**关键设计**：数据合成过程中，需要精心设计程序化的音乐理论规则，确保生成的问题具有合理性和多样性。RLVR方法中，需要设计合适的奖励函数，引导模型学习正确的推理过程。具体的参数设置和网络结构选择取决于所使用的LLMs或MLLMs，需要根据实际情况进行调整。

## 📊 实验亮点

实验结果表明，利用合成数据进行RLVR后，模型在SSMR-Bench上取得了显著的改进。此外，模型在MusicTheoryBench和MMMU的音乐子集上也表现出显著的进步，表明合成数据不仅提升了模型在特定基准上的性能，也增强了其泛化能力。具体性能提升数据未在摘要中明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于多个领域，包括：AI音乐创作，辅助作曲家进行音乐创作；音乐教育，提供个性化的乐谱学习和练习；音乐分析，自动分析乐谱并提取音乐特征；以及音乐治疗，利用AI生成的音乐进行情感调节和认知训练。该研究为构建更智能、更强大的AI音乐家奠定了基础。

## 📄 摘要（原文）

> Enhancing the ability of Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) to interpret sheet music is a crucial step toward building AI musicians. However, current research lacks both evaluation benchmarks and training data for sheet music reasoning. Inspired by mathematics, where simple operations yield infinite verifiable problems, we introduce a novel approach that treats core music theory rules, such as those governing beats and intervals, as programmatic functions to systematically synthesize a vast and diverse corpus of sheet music reasoning problems. This approach allows us to introduce a data synthesis framework that generates verifiable sheet music questions in both textual and visual modalities, leading to the Synthetic Sheet Music Reasoning Benchmark (SSMR-Bench) and a complementary training set. Evaluation results on SSMR-Bench highlight the key role reasoning plays in interpreting sheet music, while also pointing out the ongoing challenges in understanding sheet music in a visual format. By leveraging synthetic data for RLVR, all models show significant improvements on the SSMR-Bench. Additionally, they also demonstrate considerable advancements on previously established human-crafted benchmarks, such as MusicTheoryBench and the music subset of MMMU. Finally, our results show that the enhanced reasoning ability can also facilitate music composition.

