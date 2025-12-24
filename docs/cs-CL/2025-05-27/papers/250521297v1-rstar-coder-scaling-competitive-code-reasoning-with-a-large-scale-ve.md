---
layout: default
title: "rStar-Coder: Scaling Competitive Code Reasoning with a Large-Scale Verified Dataset"
---

# rStar-Coder: Scaling Competitive Code Reasoning with a Large-Scale Verified Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21297" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21297v1</a>
  <a href="https://arxiv.org/pdf/2505.21297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21297v1', 'rStar-Coder: Scaling Competitive Code Reasoning with a Large-Scale Verified Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei Liu, Li Lyna Zhang, Yi Zhu, Bingcheng Dong, Xudong Zhou, Ning Shang, Fan Yang, Mao Yang

**分类**: cs.CL

**发布日期**: 2025-05-27

**🔗 代码/项目**: [GITHUB](https://github.com/microsoft/rStar)

---

## 💡 一句话要点

**提出rStar-Coder以解决大规模代码推理数据集稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码推理` `大型语言模型` `数据集构建` `测试用例合成` `长推理解决方案`

## 📋 核心要点

1. 现有大型语言模型在代码推理方面面临高难度数据集稀缺的问题，尤其是缺乏可验证的测试用例。
2. 本文提出rStar-Coder，通过构建大规模验证数据集和引入新的测试用例合成管道，提升代码推理能力。
3. 实验结果表明，rStar-Coder在多个基准测试中表现优异，尤其在LiveCodeBench和USA Computing Olympiad上显著提高了模型的准确率。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在代码推理领域的应用，现有方法受到高难度数据集稀缺的限制，尤其是缺乏可验证的输入输出测试用例。为此，本文提出rStar-Coder，构建了一个包含418K竞赛级代码问题和580K长推理解决方案的大规模验证数据集。通过三项核心贡献，本文显著提升了LLM的代码推理能力，包括策划竞争性编程问题和解决方案、引入可靠的输入输出测试用例合成管道，以及增强高质量的长推理解决方案。实验结果显示，rStar-Coder在多个代码推理基准上表现优异，尤其在LiveCodeBench和USA Computing Olympiad上取得了显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在代码推理中面临的高难度数据集稀缺问题，现有方法缺乏可验证的输入输出测试用例，限制了模型的有效性和可靠性。

**核心思路**：通过构建一个大规模的验证数据集rStar-Coder，结合竞争性编程问题和长推理解决方案，来提升LLM的代码推理能力。设计了一个可靠的测试用例合成管道，以确保生成的测试用例的有效性和准确性。

**技术框架**：整体架构包括三个主要模块：首先，策划和合成新的可解问题；其次，采用三步法生成输入并进行相互验证以标记输出；最后，增强问题的长推理解决方案，确保其经过高质量的测试用例验证。

**关键创新**：本文的关键创新在于引入了一个有效的输入输出测试用例合成管道，能够将生成过程解耦为输入生成和输出验证两个阶段，从而提高了测试用例的质量和可靠性。

**关键设计**：在参数设置上，采用了多种难度的测试用例，并设计了相应的损失函数以优化模型的推理能力。网络结构上，结合了长推理解决方案的生成与验证，确保了最终输出的准确性和有效性。

## 📊 实验亮点

在实验中，rStar-Coder显著提升了Qwen模型的性能，Qwen2.5-7B在LiveCodeBench上的准确率从17.4%提升至57.3%，Qwen2.5-14B从23.3%提升至62.5%。在USA Computing Olympiad上，7B模型的平均pass@1准确率达到16.15%，超越了前沿的QWQ-32B模型。

## 🎯 应用场景

rStar-Coder的研究成果可广泛应用于教育、软件开发和自动化测试等领域。通过提供高质量的代码推理数据集，能够帮助开发者和研究人员更好地训练和评估大型语言模型，提升代码生成和理解的能力，推动智能编程助手的发展。

## 📄 摘要（原文）

> Advancing code reasoning in large language models (LLMs) is fundamentally limited by the scarcity of high-difficulty datasets, especially those with verifiable input-output test cases necessary for rigorous solution validation at scale. We introduce rStar-Coder, which significantly improves LLM code reasoning capabilities by constructing a large-scale, verified dataset of 418K competition-level code problems, 580K long-reasoning solutions along with rich test cases of varying difficulty. This is achieved through three core contributions: (1) we curate competitive programming code problems and oracle solutions to synthesize new, solvable problems; (2) we introduce a reliable input-output test case synthesis pipeline that decouples the generation into a three-step input generation method and a mutual verification mechanism for effective output labeling; (3) we augment problems with high-quality, test-case-verified long-reasoning solutions. Extensive experiments on Qwen models (1.5B-14B) across various code reasoning benchmarks demonstrate the superiority of rStar-Coder dataset, achieving leading performance comparable to frontier reasoning LLMs with much smaller model sizes. On LiveCodeBench, rStar-Coder improves Qwen2.5-7B from 17.4% to an impressive 57.3%, and Qwen2.5-14B from 23.3% to 62.5%, surpassing o3-mini (low) by3.1%. On the more challenging USA Computing Olympiad, our 7B model achieves an average pass@1 accuracy of 16.15%, outperforming the frontier-level QWQ-32B. Code and the dataset will be released at https://github.com/microsoft/rStar.

